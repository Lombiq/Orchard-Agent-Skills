#!/usr/bin/env python3
import argparse
import json
import os
import sqlite3
import sys


ORDER_COLUMNS = {
    "modified": "i.ModifiedUtc",
    "published": "i.PublishedUtc",
    "created": "i.CreatedUtc",
    "display-text": "i.DisplayText",
}

OUTPUT_MODES = ("extract", "content-step")


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


def _resolve_db_path(source_path, sqlite_db_path):
    if source_path:
        if os.path.isdir(source_path):
            db_path = os.path.join(source_path, "OrchardCore.db")
            if os.path.isfile(db_path):
                return db_path
        elif os.path.isfile(source_path):
            if source_path.lower().endswith(".db"):
                return source_path

    if sqlite_db_path:
        return sqlite_db_path

    raise FileNotFoundError(
        "Could not locate OrchardCore.db. Provide --source (tenant folder or db path) "
        "or --sqlite-db."
    )


def _format_json(data):
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def _json_block(data):
    return "```json\n" + json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n```\n"


def _format_markdown(source, filters, items):
    lines = [f"# Content Item Extract\n\nSource: {source}\n\n"]
    lines.append("## Filters\n")
    lines.append(_json_block(filters))

    if not items:
        lines.append("## Items (0)\n\nNo items matched the filters.\n")
        return "".join(lines)

    lines.append(f"## Items ({len(items)})\n")
    for item in items:
        index = item["index"]
        title = index.get("DisplayText") or "(no display text)"
        lines.append(f"### {title} ({index.get('ContentType')})\n")
        lines.append("Index:\n")
        lines.append(_json_block(index))
        lines.append("Document:\n")
        lines.append(_json_block(item["document"]))
    return "".join(lines)


def _apply_like(field, value):
    return f"%{value}%" if value else value


def _query_items(db_path, args):
    filters = []
    params = []

    content_types = _split_values(args.content_type)
    content_item_ids = _split_values(args.content_item_id)
    content_item_version_ids = _split_values(args.content_item_version_id)

    if content_types:
        placeholders = ",".join("?" for _ in content_types)
        filters.append(f"i.ContentType IN ({placeholders})")
        params.extend(content_types)
    if content_item_ids:
        placeholders = ",".join("?" for _ in content_item_ids)
        filters.append(f"i.ContentItemId IN ({placeholders})")
        params.extend(content_item_ids)
    if content_item_version_ids:
        placeholders = ",".join("?" for _ in content_item_version_ids)
        filters.append(f"i.ContentItemVersionId IN ({placeholders})")
        params.extend(content_item_version_ids)
    if args.display_text:
        filters.append("i.DisplayText LIKE ?")
        params.append(_apply_like("DisplayText", args.display_text))
    if args.owner:
        filters.append("i.Owner = ?")
        params.append(args.owner)
    if args.author:
        filters.append("i.Author = ?")
        params.append(args.author)

    if args.latest:
        filters.append("i.Latest = 1")
    if args.published:
        filters.append("i.Published = 1")

    if not args.any_version and not args.latest and not args.published:
        if content_types or content_item_ids or content_item_version_ids:
            filters.append("i.Latest = 1")

    if not filters:
        raise ValueError(
            "Specify at least one filter (e.g., --content-type, --content-item-id) "
            "to avoid dumping the full index."
        )

    order_column = ORDER_COLUMNS[args.order_by]
    direction = "ASC" if args.order_direction == "asc" else "DESC"

    query = (
        "SELECT i.ContentItemId, i.ContentItemVersionId, i.ContentType, i.DisplayText, "
        "i.Latest, i.Published, i.CreatedUtc, i.ModifiedUtc, i.PublishedUtc, "
        "i.Owner, i.Author, d.Content "
        "FROM ContentItemIndex i "
        "JOIN Document d ON d.Id = i.DocumentId "
        f"WHERE {' AND '.join(filters)} "
        f"ORDER BY {order_column} {direction} "
        "LIMIT ?"
    )
    params.append(args.limit)

    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query, params).fetchall()

    items = []
    for row in rows:
        document = json.loads(row["Content"])
        index = {
            "ContentItemId": row["ContentItemId"],
            "ContentItemVersionId": row["ContentItemVersionId"],
            "ContentType": row["ContentType"],
            "DisplayText": row["DisplayText"],
            "Latest": row["Latest"],
            "Published": row["Published"],
            "CreatedUtc": row["CreatedUtc"],
            "ModifiedUtc": row["ModifiedUtc"],
            "PublishedUtc": row["PublishedUtc"],
            "Owner": row["Owner"],
            "Author": row["Author"],
        }
        items.append({"index": index, "document": document})

    filter_info = {
        "content_type": content_types,
        "content_item_id": content_item_ids,
        "content_item_version_id": content_item_version_ids,
        "display_text_contains": args.display_text,
        "owner": args.owner,
        "author": args.author,
        "latest": args.latest,
        "published": args.published,
        "any_version": args.any_version,
        "order_by": args.order_by,
        "order_direction": args.order_direction,
        "limit": args.limit,
    }

    return filter_info, items


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract content items from OrchardCore.db using ContentItemIndex filters."
        )
    )
    parser.add_argument(
        "--source",
        help="Path to tenant folder or OrchardCore.db.",
    )
    parser.add_argument(
        "--sqlite-db",
        help="Path to OrchardCore.db.",
    )
    parser.add_argument(
        "--content-type",
        action="append",
        default=[],
        help="Content type name (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--content-item-id",
        action="append",
        default=[],
        help="Content item ID (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--content-item-version-id",
        action="append",
        default=[],
        help="Content item version ID (repeatable or comma-separated).",
    )
    parser.add_argument(
        "--display-text",
        help="DisplayText contains value (uses SQL LIKE).",
    )
    parser.add_argument("--owner", help="Owner user name (exact match).")
    parser.add_argument("--author", help="Author user name (exact match).")
    parser.add_argument(
        "--latest",
        action="store_true",
        help="Filter to latest versions only.",
    )
    parser.add_argument(
        "--published",
        action="store_true",
        help="Filter to published versions only.",
    )
    parser.add_argument(
        "--any-version",
        action="store_true",
        help="Disable default Latest filter when using IDs or content type.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Maximum number of items to return (default: 5).",
    )
    parser.add_argument(
        "--order-by",
        choices=sorted(ORDER_COLUMNS.keys()),
        default="modified",
        help="Sort order (default: modified).",
    )
    parser.add_argument(
        "--order-direction",
        choices=("asc", "desc"),
        default="desc",
        help="Sort direction (default: desc).",
    )
    parser.add_argument(
        "--format",
        choices=("json", "md"),
        default="md",
        help="Output format (default: md).",
    )
    parser.add_argument(
        "--output",
        choices=OUTPUT_MODES,
        default="extract",
        help="Output mode (default: extract). Use content-step for recipe export.",
    )
    parser.add_argument("--out", help="Output path (default: stdout).")

    args = parser.parse_args()
    if not args.source and not args.sqlite_db:
        parser.error("Specify --source or --sqlite-db.")
    if args.limit <= 0:
        parser.error("--limit must be greater than 0.")

    if (
        args.output == "content-step"
        and not args.published
        and not args.latest
        and not args.any_version
    ):
        args.published = True

    db_path = _resolve_db_path(args.source, args.sqlite_db)
    filter_info, items = _query_items(db_path, args)

    if args.output == "content-step":
        output = {"name": "content", "data": [item["document"] for item in items]}
        formatted = _format_json(output)
    else:
        output = {
            "source": f"{db_path} (sqlite)",
            "filters": filter_info,
            "items": items,
        }
        formatted = _format_json(output) if args.format == "json" else _format_markdown(
            output["source"], filter_info, items
        )
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(formatted)
    else:
        sys.stdout.write(formatted)


if __name__ == "__main__":
    main()
