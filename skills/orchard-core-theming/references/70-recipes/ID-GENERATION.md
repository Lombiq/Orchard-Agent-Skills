# Orchard ID Generation

Use this when you need stable `ContentItemId` values in recipes (autoroutes, aliases, and
cross-item references).

Script: `scripts/generate-orchard-ids.py`

## Why this matters
Orchard Core generates IDs using a 26-character base32 alphabet:
`0123456789abcdefghjkmnpqrstvwxyz`

Do not invent IDs with the full `a-z0-9` alphabet; Orchard intentionally excludes
`i`, `l`, `o`, and `u`.

## Quick usage
Generate one ID:
```bash
python scripts/generate-orchard-ids.py
```

Generate multiple IDs:
```bash
python scripts/generate-orchard-ids.py --count 5
```

## Notes
- Use generated IDs for `ContentItemId` when you need stability across environments.
- Keep `ContentItemVersionId` as `[js:uuid()]` unless you need deterministic versions.
