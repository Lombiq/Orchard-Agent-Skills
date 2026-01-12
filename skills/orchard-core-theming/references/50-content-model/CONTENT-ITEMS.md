# Content Items

## Structure
- Content item graph
- Content type, parts, fields

## Core properties (ContentItem)
- `ContentItemId`, `ContentItemVersionId`
- `ContentType`
- `Published`, `Latest`
- `CreatedUtc`, `ModifiedUtc`, `PublishedUtc`
- `Owner`, `Author`
- `DisplayText`
- `Id` (database document id), `Number` (version number) may be present in some contexts.
- Use `DisplayText` for rendering; `TitlePart.Title` is for editor UX/back-compat and should not be used as a rendering fallback.

## Content JSON access
- `ContentItem.Content` is a dynamic JSON object.
- Parts are stored under `ContentItem.Content.<PartName>`.
- Fields are stored under `ContentItem.Content.<PartName>.<FieldName>`.
- Field values live in a field-specific property (see `FIELDS.md`).
- In Razor, avoid explicit casts like `(string)` on dynamic field values; inline the expression or call `.ToString()`/`Convert.ToString()` when you need a string.
- Avoid `Model?.ContentItem?.Content` null chains in shape templates; use null checks only at the field/property level when data can be missing (e.g., `MediaField.Paths`).

## Template conventions
- Content item templates (e.g., `Content-Article.cshtml` or `Widget-MyType.liquid`) typically expose:
  - `Model.ContentItem`: the underlying content item.
  - `Model.Content`: a zone containing rendered parts and fields.
  - Other local zones like `Model.Header` or `Model.Footer`.
- When a task requires direct part/field access, avoid relying solely on `Model.Content` and inspect parts directly.

## Content definitions (optional)
- If `ContentDefinition.json` exists under `App_Data/Sites/<TenantName>/`, it describes content types, parts, and fields.
- Prefer the extractor (`CONTENT-DEFINITIONS-EXTRACTOR.md`) to infer the shape of `ContentItem.Content` when overriding templates,
  including when definitions live in SQLite.

## Sample content items from SQLite
When actual values are needed (e.g., to confirm field data or build recipe samples), use
`CONTENT-ITEMS-EXTRACTOR.md` to pull items from `OrchardCore.db`.

