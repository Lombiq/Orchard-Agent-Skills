# Layouts and Zones

How the layout template exposes zones/sections that placement can target.

## Layout template global zones
- The active theme's layout (`Views/Layout.cshtml` for Razor or `Views/Layout.liquid` for Liquid) controls the page shell. If it's missing and a base theme is set, the base theme layout is applied.
- Common zones: `HeadMeta`, `Header`, `Messages`, `Content`, `Footer`, plus any theme-specific ones.
- Razor: render sections with `@await RenderSectionAsync("<Zone>", required: false)`; render the main body with `@await RenderBodyAsync()`.
- Placement `place` values (e.g., `Content:1`, `/Footer`) must match zones rendered in the layout. See `20-shapes-placement/PLACEMENT.md` for details.
- The `<zone>` Razor tag helper or `{% zone %}` Liquid tag can also place ad-hoc shapes into zones. See `30-razor/TAG-HELPERS-SHAPES.md` or `31-liquid/LIQUID-TAGS.md` if needed.

## Where to confirm in source
- Check the active theme's layout file first (child themes can override base theme layouts).
- If a base theme is set and the layout is not overridden, use the base theme layout to confirm zones.

## Content item shape local zones
- When overriding content item shapes (e.g., `Content-Page.cshtml`, `Widget-Hero.Summary.liquid`), local zones are available on the dynamic view model.
- Render them with `@await DisplayAsync(Model.Content)` (Razor) or `{{ Model.Content | shape_render }}` (Liquid).
- These contain pre-rendered part/field shapes you can override individually.
- Use these only when needed; see `20-shapes-placement/SHAPE-WORKFLOW.md` to decide.
- Common local zones: `Model.Header`, `Model.Metadata`, `Model.Content`, `Model.Footer`.
