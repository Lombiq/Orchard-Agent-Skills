# Resources

How to register and require scripts/styles via Orchard Core's resource manager.

## Define resources
- Create a class implementing `IResourceManifestProvider` in a module or theme.
- Example:
```csharp
using OrchardCore.ResourceManagement;
public class ResourceManifest : IResourceManifestProvider
{
    public void BuildManifests(IResourceManifestBuilder builder)
    {
        var manifest = builder.Add();
        manifest
            .DefineStyle("MyTheme")
            .SetUrl("~/MyTheme/styles/site.min.css", "~/MyTheme/styles/site.css")
            .SetVersion("1.0")
            .SetDependencies("bootstrap");

        manifest
            .DefineScript("MyTheme")
            .SetUrl("~/MyTheme/scripts/site.min.js", "~/MyTheme/scripts/site.js")
            .SetDependencies("jquery");
    }
}
```

## Require resources in Razor
- From manifest: `<style asp-name="MyTheme" at="Foot"></style>` or `<script asp-name="MyTheme" at="Foot"></script>`.
- Direct file: `<style asp-src="~/MyTheme/styles/extra.css" at="Head"></style>`.
- `at="Head"` or `at="Foot"` controls rendering location.
- Use `depends-on` to ensure order: `<style asp-name="MyTheme" depends-on="bootstrap"></style>`.

## Built-in Orchard Core resources (from `OrchardCore.Resources`)
- Common style/script names you can require without adding CDNs yourself:
  - `bootstrap` (CSS/JS), `bootstrap-theme`, `bootstrap-rtl`
  - `font-awesome` (multiple versions defined)
  - `jQuery`, `jQuery-ui`
  - `trumbowyg`, `trumbowyg-plugins`
  - `codemirror` (plus addons like `codemirror-addon-display-fullscreen`, `codemirror-addon-hint-show-hint`, theme `monokai`)
  - `bootstrap-select`, `nouislider`, `vue-multiselect`
  - Media indexers and other module-specific resources may be available when features are enabled.
- Prefer using these names in `asp-name`/`depends-on` instead of adding CDN links manually.

## Require resources in Liquid
- Use the same tag helpers inside Liquid templates via Razor-rendered shapes, or emit `<style asp-name="...">`/`<script asp-name="...">` tags in Razor shapes that wrap Liquid content.
- For simple cases in Liquid, link static assets directly with `href` filter: `<link rel="stylesheet" href="{{ '~/MyTheme/styles/site.css' | href }}">`.

## Tips
- Keep resource names stable; use versioning to bust caches.
- Prefer manifest resources so dependencies are tracked and deduplicated.
- Use `at="Head"` for critical CSS/JS; default to `FootScript` for scripts.
- For quick theme prototyping, you can use the Tailwind Play CDN by adding
  `<script src="https://cdn.tailwindcss.com"></script>` in the theme `Layout` head.
  Prefer a build pipeline for production.
