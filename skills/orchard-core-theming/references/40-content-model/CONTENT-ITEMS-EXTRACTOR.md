# Content Items Extractor (SQLite)

Use this to inspect real content items when the definition alone is not enough (e.g., confirm
actual field values, shape data, or sample items for recipes).

Script: `scripts/extract-content-items.py`

## Common scenarios
- **Understand sample items for a type** (e.g., `BlogPost`, `Page`, `Section` widgets).
- **Confirm real field values or JSON shape** when templates are unclear.
- **Pull latest/published items** to prepare recipe seeds.
- **Find items by display text** when the content item ID is unknown.

## Quick usage
Latest items for a content type (default limit 5):
```bash
python scripts/extract-content-items.py \
  --source <tenant-folder|OrchardCore.db> \
  --content-type BlogPost \
  --latest \
  --format md
```

Published pages for a recipe seed:
```bash
python scripts/extract-content-items.py \
  --source <tenant-folder|OrchardCore.db> \
  --content-type Page \
  --published \
  --limit 10 \
  --format json
```

Content step for a recipe (defaults to published items):
```bash
python scripts/extract-content-items.py \
  --source <tenant-folder|OrchardCore.db> \
  --content-type SectionPage \
  --output content-step \
  --format json
```

Find a specific item by display text:
```bash
python scripts/extract-content-items.py \
  --source <tenant-folder|OrchardCore.db> \
  --display-text "About" \
  --latest \
  --format md
```

Fetch by content item ID:
```bash
python scripts/extract-content-items.py \
  --source <tenant-folder|OrchardCore.db> \
  --content-item-id <ContentItemId> \
  --format json
```

## Notes
- Requires at least one filter to avoid dumping the full index.
- If `--latest`/`--published` are omitted and you filter by type or IDs, it defaults to `Latest = 1`.
- `--output content-step` defaults to `Published = 1` unless you set `--latest` or `--any-version`.
- Omit `--out` to write to stdout (preferred to avoid creating files tracked by git).
