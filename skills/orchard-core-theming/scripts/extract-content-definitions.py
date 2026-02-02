#!/usr/bin/env python3
import argparse
import json
import os
import sqlite3
import sys
from collections import deque # codespell:ignore

TYPE_REFERENCE_KEYS = {
    "AllowedContentTypes",
    "ContainedContentTypes",
    "ContentTypes",
    "DisplayedContentTypes",
}

STEREOTYPE_REFERENCE_KEYS = {
    "ContainedStereotypes",
    "DisplayedStereotypes",
    "Stereotypes",
}

CONTENT_DEFINITION_DOC_TYPE = (
    "OrchardCore.ContentManagement.Metadata.Records.ContentDefinitionRecord, "
    "OrchardCore.ContentManagement.Abstractions"
)


def _split_values(values):
    result = []
    for value in values:
        if not value:
            continue
        for item in value.split(","):
            item = item.strip()
            if item:
                result.append(item)
    return result


def _coerce_strings(value):
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str) and item.strip()]
    if isinstance(value, str) and value.strip():
        return [value]
    return []


def _extract_references(obj):
    refs = {"content_types": set(), "stereotypes": set()}

    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in TYPE_REFERENCE_KEYS:
                    refs["content_types"].update(_coerce_strings(child))
                elif key in STEREOTYPE_REFERENCE_KEYS:
                    refs["stereotypes"].update(_coerce_strings(child))
                walk(child)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(obj)
    return refs


def _sorted_refs(refs):
    return {
        "content_types": sorted(refs["content_types"]),
        "stereotypes": sorted(refs["stereotypes"]),
    }


def _load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _load_from_sqlite(db_path):
    if not os.path.isfile(db_path):
        raise FileNotFoundError(f"SQLite database not found: {db_path}")

    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute(
            "SELECT Content FROM Document WHERE Type = ? ORDER BY Id DESC LIMIT 1",
            (CONTENT_DEFINITION_DOC_TYPE,),
        )
        row = cursor.fetchone()
        if not row:
            raise ValueError(
                "ContentDefinition record not found in Document table for Type "
                f"'{CONTENT_DEFINITION_DOC_TYPE}'."
            )
        return json.loads(row["Content"])


def _resolve_source(source_path, sqlite_db_path):
    if source_path:
        if os.path.isdir(source_path):
            json_path = os.path.join(source_path, "ContentDefinition.json")
            if os.path.isfile(json_path):
                return _load_json(json_path), f"{json_path}"
            db_path = os.path.join(source_path, "OrchardCore.db")
            if os.path.isfile(db_path):
                return _load_from_sqlite(db_path), f"{db_path} (sqlite)"
        else:
            if os.path.isfile(source_path):
                if source_path.lower().endswith(".db"):
                    return _load_from_sqlite(source_path), f"{source_path} (sqlite)"
                return _load_json(source_path), f"{source_path}"

            parent = os.path.dirname(source_path)
            db_path = os.path.join(parent, "OrchardCore.db")
            if os.path.basename(source_path).lower() == "contentdefinition.json":
                if os.path.isfile(db_path):
                    return _load_from_sqlite(db_path), f"{db_path} (sqlite)"

    if sqlite_db_path:
        return _load_from_sqlite(sqlite_db_path), f"{sqlite_db_path} (sqlite)"

    raise FileNotFoundError(
        "Could not locate ContentDefinition.json or OrchardCore.db. "
        "Provide --source (file or tenant folder) or --sqlite-db."
    )


def _build_part_definition_view(part_record):
    if not part_record:
        return None

    fields = []
    for field in part_record.get("ContentPartFieldDefinitionRecords", []):
        field_settings = field.get("Settings", {}) or {}
        field_refs = _extract_references(field_settings)
        fields.append(
            {
                "name": field.get("Name"),
                "field_type": field.get("FieldName"),
                "settings": field_settings,
                "references": _sorted_refs(field_refs),
            }
        )

    part_settings = part_record.get("Settings", {}) or {}
    part_refs = _extract_references(part_settings)
    part_view = {
        "name": part_record.get("Name"),
        "settings": part_settings,
        "references": _sorted_refs(part_refs),
        "fields": fields,
    }
    return part_view


def _build_type_view(type_record, parts_by_name, relationship):
    parts = []
    type_refs = {"content_types": set(), "stereotypes": set()}

    for type_part in type_record.get("ContentTypePartDefinitionRecords", []):
        part_settings = type_part.get("Settings", {}) or {}
        part_refs = _extract_references(part_settings)
        for key in type_refs:
            type_refs[key].update(part_refs[key])

        part_definition = parts_by_name.get(type_part.get("PartName"))
        part_def_view = _build_part_definition_view(part_definition)
        if part_def_view:
            for key in type_refs:
                type_refs[key].update(part_def_view["references"][key])

        parts.append(
            {
                "part_name": type_part.get("PartName"),
                "name": type_part.get("Name"),
                "settings": part_settings,
                "references": _sorted_refs(part_refs),
                "part_definition": part_def_view,
            }
        )

    return {
        "name": type_record.get("Name"),
        "display_name": type_record.get("DisplayName"),
        "relationship": relationship,
        "settings": type_record.get("Settings", {}) or {},
        "references": _sorted_refs(type_refs),
        "parts": parts,
    }


def _collect_type_references(type_record, parts_by_name):
    refs = {"content_types": set(), "stereotypes": set()}
    for type_part in type_record.get("ContentTypePartDefinitionRecords", []):
        part_settings = type_part.get("Settings", {}) or {}
        part_refs = _extract_references(part_settings)
        for key in refs:
            refs[key].update(part_refs[key])

        part_definition = parts_by_name.get(type_part.get("PartName"))
        if not part_definition:
            continue
        part_view = _build_part_definition_view(part_definition)
        if not part_view:
            continue
        for key in refs:
            refs[key].update(part_view["references"][key])
    return refs


def _expand_related(type_names, types_by_name, types_by_stereotype, parts_by_name, depth):
    related = {name: "selected" for name in type_names}
    queue = deque((name, 0) for name in type_names) # codespell:ignore

    while queue:
        name, level = queue.popleft()
        if level >= depth:
            continue
        type_record = types_by_name.get(name)
        if not type_record:
            continue

        refs = _collect_type_references(type_record, parts_by_name)
        next_names = set(refs["content_types"])
        for stereotype in refs["stereotypes"]:
            next_names.update(types_by_stereotype.get(stereotype, []))

        for next_name in sorted(next_names):
            if next_name not in related:
                related[next_name] = "related"
                queue.append((next_name, level + 1))

    return related


def _format_json(data):
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def _json_block(data):
    return "```json\n" + json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n```\n"


def _format_markdown(data):
    lines = []
    source = data.get("source")
    if source:
        lines.append(f"# Content Definition Extract\n\nSource: {source}\n")

    if data.get("types"):
        lines.append("## Content Types\n")
        for type_view in data["types"]:
            lines.append(f"### {type_view['name']} ({type_view['relationship']})\n")
            if type_view.get("display_name"):
                lines.append(f"DisplayName: {type_view['display_name']}\n\n")
            if type_view.get("settings"):
                lines.append("Settings:\n")
                lines.append(_json_block(type_view["settings"]))
            if type_view.get("references"):
                refs = type_view["references"]
                if refs["content_types"] or refs["stereotypes"]:
                    lines.append("References:\n")
                    lines.append(_json_block(refs))
            if type_view.get("parts"):
                lines.append("Parts:\n")
                for part in type_view["parts"]:
                    lines.append(f"- Part: {part['part_name']} (instance: {part['name']})\n")
                    if part.get("settings"):
                        lines.append("  Settings:\n")
                        lines.append(_indent_block(_json_block(part["settings"]), 2))
                    if part.get("references"):
                        refs = part["references"]
                        if refs["content_types"] or refs["stereotypes"]:
                            lines.append("  References:\n")
                            lines.append(_indent_block(_json_block(refs), 2))
                    part_def = part.get("part_definition")
                    if part_def:
                        lines.append(f"  Part definition: {part_def['name']}\n")
                        if part_def.get("settings"):
                            lines.append("  Part settings:\n")
                            lines.append(_indent_block(_json_block(part_def["settings"]), 2))
                        if part_def.get("fields"):
                            lines.append("  Fields:\n")
                            for field in part_def["fields"]:
                                lines.append(
                                    f"  - Field: {field['name']} ({field['field_type']})\n"
                                )
                                if field.get("settings"):
                                    lines.append("    Settings:\n")
                                    lines.append(
                                        _indent_block(_json_block(field["settings"]), 4)
                                    )
                                if field.get("references"):
                                    refs = field["references"]
                                    if refs["content_types"] or refs["stereotypes"]:
                                        lines.append("    References:\n")
                                        lines.append(
                                            _indent_block(_json_block(refs), 4)
                                        )
            lines.append("\n")

    if data.get("parts"):
        lines.append("## Content Parts\n")
        for part in data["parts"]:
            lines.append(f"### {part['name']}\n")
            if part.get("settings"):
                lines.append("Settings:\n")
                lines.append(_json_block(part["settings"]))
            if part.get("references"):
                refs = part["references"]
                if refs["content_types"] or refs["stereotypes"]:
                    lines.append("References:\n")
                    lines.append(_json_block(refs))
            if part.get("fields"):
                lines.append("Fields:\n")
                for field in part["fields"]:
                    lines.append(f"- Field: {field['name']} ({field['field_type']})\n")
                    if field.get("settings"):
                        lines.append("  Settings:\n")
                        lines.append(_indent_block(_json_block(field["settings"]), 2))
                    if field.get("references"):
                        refs = field["references"]
                        if refs["content_types"] or refs["stereotypes"]:
                            lines.append("  References:\n")
                            lines.append(_indent_block(_json_block(refs), 2))
            lines.append("\n")

    return "".join(lines)


def _indent_block(text, spaces):
    pad = " " * spaces
    return "".join(pad + line if line.strip() else line for line in text.splitlines(True))


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract content definitions and related content types from ContentDefinition.json "
            "or OrchardCore.db."
        )
    )
    parser.add_argument(
        "--source",
        help="Path to ContentDefinition.json, OrchardCore.db, or tenant folder.",
    )
    parser.add_argument(
        "--sqlite-db",
        help="Path to OrchardCore.db (Document table fallback).",
    )
    parser.add_argument(
        "--type",
        dest="types",
        action="append",
        default=[],
        help="Content type name (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--part",
        dest="parts",
        action="append",
        default=[],
        help="Content part name (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Include all content types (ignores --type filtering).",
    )
    parser.add_argument(
        "--include-related",
        action="store_true",
        help="Include related types referenced by container/field settings.",
    )
    parser.add_argument(
        "--related-depth",
        type=int,
        default=1,
        help="Depth for related-type expansion (default: 1).",
    )
    parser.add_argument(
        "--format",
        choices=("json", "md"),
        default="md",
        help="Output format (default: md).",
    )
    parser.add_argument("--out", help="Output path (default: stdout).")

    args = parser.parse_args()
    if not args.source and not args.sqlite_db:
        parser.error("Specify --source or --sqlite-db.")
    selected_types = _split_values(args.types)
    selected_parts = _split_values(args.parts)

    if not args.all and not selected_types and not selected_parts:
        parser.error("Specify --type, --part, or --all.")

    data, source_label = _resolve_source(args.source, args.sqlite_db)
    type_records = data.get("ContentTypeDefinitionRecords", [])
    part_records = data.get("ContentPartDefinitionRecords", [])
    types_by_name = {record.get("Name"): record for record in type_records}
    parts_by_name = {record.get("Name"): record for record in part_records}

    types_by_stereotype = {}
    for record in type_records:
        settings = record.get("Settings", {}) or {}
        type_settings = settings.get("ContentTypeSettings", {}) or {}
        stereotype = type_settings.get("Stereotype")
        if stereotype:
            types_by_stereotype.setdefault(stereotype, set()).add(record.get("Name"))

    output = {"source": source_label}

    types_output = []
    if args.all:
        type_names = [record.get("Name") for record in type_records if record.get("Name")]
        relationships = {name: "selected" for name in type_names}
    elif args.include_related and selected_types:
        relationships = _expand_related(
            selected_types,
            types_by_name,
            types_by_stereotype,
            parts_by_name,
            max(args.related_depth, 0),
        )
    else:
        relationships = {name: "selected" for name in selected_types}

    for name in sorted(relationships):
        type_record = types_by_name.get(name)
        if not type_record:
            continue
        types_output.append(
            _build_type_view(type_record, parts_by_name, relationships[name])
        )

    if types_output:
        output["types"] = types_output

    parts_output = []
    for name in sorted(set(selected_parts)):
        part_record = parts_by_name.get(name)
        if not part_record:
            continue
        parts_output.append(_build_part_definition_view(part_record))

    if parts_output:
        output["parts"] = parts_output

    formatted = _format_json(output) if args.format == "json" else _format_markdown(output)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(formatted)
    else:
        sys.stdout.write(formatted)


if __name__ == "__main__":
    main()
