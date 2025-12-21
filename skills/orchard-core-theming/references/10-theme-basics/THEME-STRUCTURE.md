# Theme Structure

## Standard layout (typical Orchard Core solution)
- `src/Modules/`: Orchard Core modules.
- `src/Themes/`: Orchard Core themes.
- `src/Libraries/`: shared libraries that are not Orchard Core extensions.

## Views and rendering
- Site theme views usually live under the theme's `Views/`.
- Admin UI views live in module `Views/` or the active admin theme.
- If multiple themes exist, confirm which is active before adding views.
- View files are either `.cshtml` or `.liquid`. Follow existing view type; if none, default to Liquid.
- Razor guidance: `30-razor/INDEX.md`; Liquid guidance: `31-liquid/INDEX.md`.
- Prefer shapes over MVC partials for UI composition.
- To customize admin branding or inject admin-only CSS, override `Views/AdminBranding.cshtml` in an admin theme (BaseTheme `TheAdmin`).
  The default Orchard Core markup is:
  ```cshtml
  @inject IOptions<AdminOptions> AdminOptions
  <zone name="HeadMeta">
      <link href="@Url.Content("~/OrchardCore.Admin/favicon.ico")" type="image/x-icon" rel="shortcut icon" />
  </zone>
  <a class="ta-navbar-brand navbar-brand" href="@Url.Content("~/" + AdminOptions.Value.AdminUrlPrefix)">
      <div class="d-flex align-items-center">
          <img src="@Url.Content("~/OrchardCore.Admin/logo.png")" alt="@Site.SiteName" class="pe-2" />
          <span>@Site.SiteName</span>
      </div>
  </a>
  ```
- `Views/Layout.cshtml` is treated as the site layout automatically; do not set `Layout = null` inside it.

## _ViewImports for Razor themes
If a theme uses Razor, ensure `_ViewImports.cshtml` exists with:
- `@inherits OrchardCore.DisplayManagement.Razor.RazorPage<TModel>`
- `@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers`
- `@addTagHelper *, OrchardCore.DisplayManagement`
- `@addTagHelper *, OrchardCore.ResourceManagement`
- `@addTagHelper *, OrchardCore.Contents`

## Theme inheritance (base theme)
- Check the theme manifest for `BaseTheme`.
- Base themes supply views/resources that the child theme inherits.
- Override base theme views in the child theme rather than editing the base theme unless explicitly requested.
