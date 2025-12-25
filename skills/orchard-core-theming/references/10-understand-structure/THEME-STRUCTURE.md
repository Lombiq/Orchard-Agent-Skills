# Theme Structure

Understanding the theme structure helps you locate templates and confirm inheritance.

## Views and rendering, Razor vs Liquid
- Site theme views usually live under the theme's `Views/`.
- Admin UI views live in module `Views/` or the active admin theme.
- If multiple themes exist, confirm which you need to work with, unless specifically asked by the user.
- View files are either `.cshtml` or `.liquid`. Determine this for the active theme and use the matching guidance. If none are present, check the base theme or ask the user.
- Razor guidance: `30-razor/INDEX.md`; Liquid guidance: `40-liquid/INDEX.md`.
- Prefer shapes over MVC partials for UI composition.
- `Views/Layout.cshtml` is treated as the site layout automatically; do not set `Layout = null` inside it.

## _ViewImports for Razor themes
If a theme uses Razor, `_ViewImports.cshtml` should exist with at least:
- `@inherits OrchardCore.DisplayManagement.Razor.RazorPage<TModel>`
If it's missing, it can be a typical build error. Read `CREATE-THEME.md` to verify what should be present.

## Manifest file, Theme inheritance (base theme)
- Theme manifest lives in `Manifest.cs` defining metadata for the theme.
- Look for a `Theme` attribute with metadata like `Name`, `Description`, and `BaseTheme`.
- `BaseTheme` indicates theme inheritance; child themes can override base theme templates.
- Base themes supply views/resources that the child theme inherits.
- Override base theme views in the child theme rather than editing the base theme unless explicitly requested.
