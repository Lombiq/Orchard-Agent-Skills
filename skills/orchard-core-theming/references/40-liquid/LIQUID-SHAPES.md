# Liquid Shape Tags

## Build and render shapes
- Tag: `{% shape type: "Card", title: "Hello" %}` creates and renders a shape immediately.
- Filters:
  - `shape_build_display`: build a display shape for a content item.
  - `shape_build_editor`: build an editor shape for a content item.
  - `shape_render`: render a built shape.
- Example (content item already available):
```liquid
{% assign display = Model.ContentItem | shape_build_display: "Detail" %}
{{ display | shape_render }}
```

## Render content items by ID
```liquid
{{ Content.ContentItemId["<id>"] | shape_build_display: "Summary" | shape_render }}
```

## Render content items by handle/alias
```liquid
{% assign menu = Content["alias:main-menu"] %}
{{ menu | shape_build_display: "Summary" | shape_render }}
```

## Zone content
- `{% zone "Header", position: "1" %}...{% endzone %}` pushes content into a zone/section.
- Use `render_section` in the layout to output the zone.

## Shape metadata helpers
- `{% shape_add_alternates shape, "Alt1 Alt2" %}`
- `{% shape_clear_alternates shape %}`
- `{% shape_add_wrappers shape, "Wrapper1" %}`
- `{% shape_type shape, "MyType" %}`

See `40-liquid/LIQUID-TAGS.md` for the full tag list and `20-shapes-placement/ALTERNATES.md` for naming patterns.

