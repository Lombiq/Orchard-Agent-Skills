# Static Files

## Where to place assets
- Themes: `Themes/<ThemeName>/wwwroot/` (e.g., `~/MyTheme/styles/site.css`).
- Modules: `Modules/<ModuleName>/wwwroot/` (e.g., `~/MyModule/js/widget.js`).
- Keep build outputs (bundles/minified files) here so tag helpers can find them.

## Referencing assets
- Razor: `<link rel="stylesheet" href="~/MyTheme/styles/site.css" asp-append-version="true" />`
- Liquid: `<link rel="stylesheet" href="{{ '~/MyTheme/styles/site.css' | href }}">`
- Use `asp-append-version="true"` for cache-busting when hashes are available.

## Tips
- Keep CDN overrides in the manifest (see `RESOURCES.md`) while shipping local fallbacks in `wwwroot`.
- Ensure static files are included in the project file or build pipeline if using custom SDK settings.
