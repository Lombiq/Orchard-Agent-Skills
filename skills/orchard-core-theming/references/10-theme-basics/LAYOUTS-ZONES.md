# Layouts and Zones

How the layout template exposes zones/sections that placement can target.

## Layout template (Razor)
- The active theme's `Views/Layout.cshtml` controls the page shell.
- Common sections/zones: `HeadMeta`, `Header`, `Messages`, `Content` (via `RenderBodyAsync()`), `Footer`, plus any theme-specific ones.
- Render zones/sections with `@await RenderSectionAsync("<Zone>", required: false)`; the `Content` body is rendered by `@await RenderBodyAsync()`.
- Placement `place` values (e.g., `Content:1`, `/Footer`) must match zones/sections rendered in the layout.

## Layout template (Liquid)
- `Views/Layout.liquid` uses sections with the Liquid equivalents (follow the active theme's layout for exact syntax).
- Common sections mirror Razor layouts (`HeadMeta`, `Header`, `Messages`, `Content`, `Footer`).

## Adding or changing zones
- Add a new zone/section in the layout, then target it from `placement.json` with `place: "/MyZone"` or `place: "MyZone:0"`.
- If you move the main content zone name, update placement rules accordingly.

## Where to confirm in source
- Check the active theme's layout file first (child themes can override base theme layouts).
- Reference layouts from OrchardCore themes (`TheTheme`, `TheAdmin`, etc.) for working patterns.
