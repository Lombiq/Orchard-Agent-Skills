# Shape Alternates

Shape alternates are the template name candidates that Orchard Core tries in order.
They let you target a specific content type, display type, part, field, or zone without changing drivers.

## Naming rules (high level)
- `__` separates alternate segments; filenames use `-` in place of `__` (both work, but `-` is standard).
- A single `_` in shape type maps to `.` in file names.
- Display types are inserted with `_DisplayType` between the base shape and the alternate segments.
- Display modes append `_Display` to the shape type for parts/fields that support display modes.
- Part and field "differentiators" use `-` inside the alternate segment (e.g., `Blog-MyField`).
-
  Shape type ↔ file name examples:
  - `Component__Header` -> `Component-Header.cshtml`
  - `Content_Summary__Page` -> `Content-Page.Summary.cshtml`

## Content item alternates
- `Content__[ContentType]` - content item shape for a specific content type.
- `Content_[DisplayType]__[ContentType]` - display-type-specific override (e.g., Summary).
- `Content__Alias__[Alias]`
- `Content_[DisplayType]__Alias__[Alias]`
- `Content__Slug__[Slug]`
- `Content_[DisplayType]__Slug__[Slug]`

Filename mapping examples:
- `Content__Article` -> `Content-Article.cshtml` (or same with .liquid)
- `Content_Summary__Article` -> `Content-Article.Summary.cshtml` (or same with .liquid)

## Stereotype alternates for content items
- A content type might have a stereotype set. If you are unsure, use the extractor (`50-content-model/CONTENT-DEFINITIONS-EXTRACTOR.md`) or fall back to `Content`. Use the stereotype value as the base shape name instead of `Content`.
- Example: `Section` -> `Section__[ContentType]` -> `Section-Hero.cshtml`.
- Example: `Block` -> `Block__[ContentType]` -> `Block-TextAndImage.cshtml`.
- Example: `Widget` -> `Widget__[ContentType]` -> `Widget-Image.cshtml`.
- Same alternates apply; replace `Content` with the stereotype.

## Part alternates if granular overrides are required
- `[ShapeType]` (often the part type name)
- `[ShapeType]_[DisplayType]`
- `[ContentType]_[DisplayType]__[PartType]`
- `[ContentType]_[DisplayType]__[PartName]`
- `[ContentType]_[DisplayType]__[PartType]__[ShapeType]`
- `[ContentType]_[DisplayType]__[PartName]__[ShapeType]`
- If a custom part only has fields, a field override may be enough.

Display mode variants (for parts with display modes):
- `[ShapeType]_[DisplayType]__[DisplayMode]_Display`
- `[ContentType]_[DisplayType]__[PartType]__[DisplayMode]_Display`
- `[ContentType]_[DisplayType]__[PartName]__[DisplayMode]_Display`

## Taxonomy term alternates
- Term landing pages render the `TermPart` shape for the term content type.
- Alternate name: `<TermContentType>__TermPart` (file example: `Tag-TermPart.liquid` or `Tag__TermPart.liquid`).
- Use `Model.ContentItems` for the related content list and `Model.Pager` for paging (use `shape_pager` and `shape_render`).
- For the term header/body, override the term content item with `Content__<TermContentType>` (e.g., `Content__Tag.liquid`).

## Field alternates if granular overrides are required
- `[ShapeType]` (often the field type name)
- `[ShapeType]_[DisplayType]` (field type with display type)
- `[PartType]__[FieldName]`
- `[ContentType]__[PartName]__[FieldName]`
- `[ContentType]__[FieldType]`
- `[FieldType]__[ShapeType]`
- `[PartType]__[FieldName]__[ShapeType]`
- `[ContentType]__[PartName]__[FieldName]__[ShapeType]`
- `[ContentType]__[FieldType]__[ShapeType]`

Field display mode variants require `_Display` on the shape type and a full differentiator.

## Zone alternates (wrap or override a zone)
- `Zone__ZoneName` (e.g., `Zone__Footer` -> `Zone-Footer.cshtml`)

## User alternates
- `UserDisplayName_DisplayType`
- `UserDisplayName_DisplayType__UserName` (when available)

## Practical tips
- Use `console_log` or the Razor `ConsoleLog` helper to inspect a shape's alternates list.
- When changing shape type or display type in Liquid/Razor, clear alternates first.
- Most-specific alternates win; keep templates targeted to avoid surprising overrides.
