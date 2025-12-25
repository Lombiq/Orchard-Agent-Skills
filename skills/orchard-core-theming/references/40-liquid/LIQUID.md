# Liquid Basics

## Syntax quick ref
- Output: `{{ value }}`; statements: `{% ... %}`.
- Variables: `assign`, `capture`, `increment`, `decrement`.
- Flow: `if/unless`, `case/when`, `for` with `limit/offset/reverse`, `break/continue`.
- Strings/arrays/objects follow Shopify Liquid semantics plus Orchard filters/tags.

## Orchard-specific tips
- Use `href`/`img_tag`/`asset_url` filters to resolve paths.
- Build and render shapes: `shape_build_display`, `shape_build_editor`, `shape_render`.
- Access content items in scope: `Model.ContentItem`, `Content.ContentItemId["id"]`, or values passed in the shape's model.
- Localization: `| t` filter.

## Safety and debugging
- Avoid heavy logic in templates; push logic to drivers when possible.
- Debug quickly with `| console_log` or `| json` in development.

## Related files
- Tags: `40-liquid/LIQUID-TAGS.md`
- Filters: `40-liquid/LIQUID-FILTERS.md`
- Shape helpers: `40-liquid/LIQUID-SHAPES.md`

