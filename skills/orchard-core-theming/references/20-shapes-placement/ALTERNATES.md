# Shape Alternates

Shape alternates are the template name candidates that Orchard Core tries in order.
They let you target a specific content type, display type, part, field, or zone without changing drivers.

## Naming rules (high level)
- `__` separates alternate segments; filenames replace `__` with `-`.
- Display types are inserted with `_DisplayType` between the base shape and the alternate segments.
- Display modes append `_Display` to the shape type for parts/fields that support display modes.
- Part and field "differentiators" use `-` inside the alternate segment (e.g., `Blog-MyField`).

## Content item alternates
- `Content__ContentType`
- `Content_DisplayType__ContentType`
- `Content__Alias__Alias`
- `Content_DisplayType__Alias__Alias`
- `Content__Slug__Slug`
- `Content_DisplayType__Slug__Slug`

Filename mapping examples:
- `Content__Article` -> `Content-Article.cshtml`
- `Content_Summary__Article` -> `Content-Article.Summary.cshtml`

## Stereotype alternates (general pattern)
- Use the stereotype value as the base shape name.
- Example: `Section` -> `Section__ContentType` -> `Section-ContentType.cshtml`.
- Example: `Block` -> `Block__ContentType` -> `Block-ContentType.cshtml`.

## Widget alternates (stereotype)
- `Widget__ContentType`
- `Widget_DisplayType__ContentType`
- `Widget__Alias__Alias`
- `Widget_DisplayType__Alias__Alias`
- `Widget__Slug__Slug`
- `Widget_DisplayType__Slug__Slug`

## Section alternates (stereotype example)
- `Section__ContentType`
- `Section_DisplayType__ContentType`

## Part alternates (common patterns)
- `[ShapeType]` (often the part type name)
- `[ShapeType]_[DisplayType]`
- `[ContentType]_[DisplayType]__[PartType]`
- `[ContentType]_[DisplayType]__[PartName]`
- `[ContentType]_[DisplayType]__[PartType]__[ShapeType]`
- `[ContentType]_[DisplayType]__[PartName]__[ShapeType]`

Display mode variants (for parts with display modes):
- `[ShapeType]_[DisplayType]__[DisplayMode]_Display`
- `[ContentType]_[DisplayType]__[PartType]__[DisplayMode]_Display`
- `[ContentType]_[DisplayType]__[PartName]__[DisplayMode]_Display`

## Field alternates (common patterns)
- `[ShapeType]_[DisplayType]` (field type with display type)
- `[PartType]__[FieldName]`
- `[ContentType]__[PartName]__[FieldName]`
- `[ContentType]__[FieldType]`
- `[FieldType]__[ShapeType]`
- `[PartType]__[FieldName]__[ShapeType]`
- `[ContentType]__[PartName]__[FieldName]__[ShapeType]`
- `[ContentType]__[FieldType]__[ShapeType]`

Field display mode variants require `_Display` on the shape type and a full differentiator.

## Zone alternates
- `Zone__ZoneName` (e.g., `Zone__Footer` -> `Zone-Footer.cshtml`)

## User alternates
- `UserDisplayName_DisplayType`
- `UserDisplayName_DisplayType__UserName` (when available)

## Practical tips
- Use `console_log` or the Razor `ConsoleLog` helper to inspect a shape’s alternates list.
- When changing shape type or display type in Liquid/Razor, clear alternates first.
- Most-specific alternates win; keep templates targeted to avoid surprising overrides.
