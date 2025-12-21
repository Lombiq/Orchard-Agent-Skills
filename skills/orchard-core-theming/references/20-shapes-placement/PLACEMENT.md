# Placement

Placement controls where shapes render, whether they render, and which alternates/wrappers apply.
Themes and modules can supply `placement.json` at their root.

## File location and format
- File name: `placement.json` at the root of a theme or module.
- JSON object: keys are shape types; values are arrays of placement rules.

Example skeleton:
```json
{
  "TextField": [
    { "place": "Content:1", "displayType": "Detail" }
  ]
}
```

## Filters (rule matching)
- `displayType`: `Detail`, `Summary`, `SummaryAdmin`, etc.
- `differentiator`: used to target a specific part/field instance.
- `contentType`: single or array, supports `*` wildcard prefixes.
- `contentPart`: single or array.
- `path`: single or array of request paths.

## Placement info
- `place`: target zone/position. `-` hides the shape. `/ZoneName` moves to a layout zone.
- `alternates`: list of alternates to add.
- `wrappers`: list of wrapper shapes.
- `shape`: replace shape type.

## Placement precedence
1) Startup project (acts like a super-theme)
2) Active theme (front-end or admin depending on request)
3) Modules (dependency order)

## Differentiators
Differentiators uniquely identify shapes that share the same type.
Common patterns:
- Part shapes: `[PartName]` or `[PartName]-[ShapeType]`
- Field shapes: `[PartName]-[FieldName]` or `[PartName]-[FieldName]-[ShapeType]`

## Field display modes (strict rules)
If a field uses a display mode, the shape type changes and the differentiator must include it:
- Shape type: `TextField_Display` (example)
- Differentiator: `[PartType]-[FieldName]-[FieldType]_Display__[DisplayMode]`

Example:
```json
{
  "TextField_Display": [
    {
      "place": "Content:1",
      "differentiator": "Blog-MyField-TextField_Display__Header"
    }
  ]
}
```

## Editor grouping (tabs/cards/columns)
Editor shapes can be grouped using modifiers in `place`:
- Tabs: `#`
- Cards: `%`
- Columns: `|`
- Group position: `;` (e.g., `#Media;0`)
- Column width: `_` (e.g., `|Content_9;1`)

Example:
```json
{
  "MediaField_Edit": [
    { "place": "Parts:0#Media;0", "contentType": [ "Article" ] }
  ],
  "HtmlField_Edit": [
    { "place": "Parts:0#Content;1", "contentType": [ "Article" ] }
  ]
}
```

## Dynamic parts (no driver)
Dynamic parts render with `ContentPart` shape and use the part name as differentiator.
For non-detail displays, use `ContentPart_Summary` (or the display type suffix).

Example:
```json
{
  "ContentPart": [
    { "place": "MyGalleryZone", "differentiator": "GalleryPart" }
  ],
  "ContentPart_Summary": [
    { "place": "MyGalleryZone", "differentiator": "GalleryPart" }
  ]
}
```
