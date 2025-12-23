# Content Definition Extractor

Use this by default instead of reading `ContentDefinition.json` directly. It returns a focused slice for a content type or part,
including container-related types (Bag/Flow/List, content pickers, stereotypes).

Script: `scripts/extract-content-definitions.py`

## Quick usage
Extract a type and its related container types (Markdown, stdout):
```bash
python scripts/extract-content-definitions.py \
  --source <ContentDefinition.json> \
  --type Page \
  --include-related \
  --format md
```

Extract a type as JSON (machine-friendly, stdout):
```bash
python scripts/extract-content-definitions.py \
  --source <ContentDefinition.json> \
  --type Page \
  --format json
```

Extract a reusable part definition (optional; type output already embeds attached part definitions):
```bash
python scripts/extract-content-definitions.py \
  --source <ContentDefinition.json> \
  --part BlogPost \
  --format md
```

## Related-type expansion
`--include-related` pulls in types referenced by settings keys like:
- `ContainedContentTypes` (Bag/Flow/List)
- `DisplayedContentTypes` (ContentPicker)
- `ContainedStereotypes` / `DisplayedStereotypes` / `Stereotypes`

Use `--related-depth 2` if related types themselves contain nested containers.

## Notes
- The script reads `ContentDefinition.json` directly. For SQLite-backed tenants, export or extract the JSON first.
- Use `--all` only when you truly need the full set; it can be large.
- Omit `--out` to write to stdout (preferred to avoid creating files tracked by git).
- First extract the type without `--include-related` to see attached parts. If it only has FlowPart
  and you are not overriding FlowPart, skip `--include-related` because widget types are usually
  not rendered directly.
