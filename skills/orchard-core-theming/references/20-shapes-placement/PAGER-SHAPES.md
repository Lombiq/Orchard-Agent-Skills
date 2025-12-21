# Pager Shapes and Rendering

Pager rendering in Orchard Core (Navigation module) and how to override/customize.

## Shapes involved (C#-created via `[Shape]`)
- `Pager`: main pager shape built from child shapes (not just a view).
- `Pager_Links`: builds/aggregates link shapes for standard pager.
- Sub-shapes: `Pager_Gap`, `Pager_First`, `Pager_Previous`, `Pager_Next`, `Pager_Last`, `Pager_CurrentPage` (all morph to `Pager_Link`).
- `Pager_Link`: morphs to `ActionLink` (Razor view) to render `<a>`.
- `Pager_Gap`: renders a disabled link.
- `PagerSlim`: two-link pager; uses `Pager_Previous`/`Pager_Next`.

## Properties (common)
- Core: `Page`, `PageSize`, `TotalItemCount`, `Quantity`, `PagerId`, `ShowNext`, text labels (`FirstText`, `PreviousText`, `NextText`, `LastText`, `GapText`).
- Shape base: `TagName`, `Attributes`, `Classes`.
- List inherited (for link items): `ItemTagName`, `ItemClasses`, `ItemAttributes`, `FirstClass`, `LastClass`.
- Slim-specific: `PreviousClass`, `NextClass`, `PreviousText`, `NextText`, `UrlParams`.

## Shape-building flow (from `PagerShapesTableProvider`/`PagerShapes`)
- `Pager`/`PagerSlim` are created with default `ItemClasses`/`ItemAttributes`. Alternates added per `PagerId` (`Pager__{id}`).
- `Pager_Links` builds the list:
  - Computes page count; if < 2 pages, morphs pager to `List` and renders children directly.
  - Creates `Pager_First`, `Pager_Previous`, optional `Pager_Gap`, per-page items (`Pager_CurrentPage` or `Pager_Link`), optional trailing gap, `Pager_Next`, `Pager_Last`.
  - Adds `rel` attributes (`next`/`prev`/`no-follow`) as needed.
  - Sets `shape.Metadata.Type = "List"`; children render via list/item rendering.
- Sub-shapes (`Pager_First`, `Pager_Previous`, `Pager_CurrentPage`, `Pager_Next`, `Pager_Last`, `Pager_Gap`) all:
  - Clear alternates, set `Metadata.Type = "Pager_Link"` (except `Pager_Link` sets to `ActionLink`), then render.
  - `Pager_CurrentPage` adds `active` class to parent tag; `Pager_Gap` adds `disabled`.
- `Pager_Link` morphs to `ActionLink` (Razor `ActionLink` shape renders `<a>` with `href` unless disabled).
- Alternates per `PagerId` are added for all shapes (`Pager__id`, `Pager_First__id`, etc.).

## Alternates
- `Pager` alternates by `PagerId`: `Pager__{Id}`, `Pager_Previous__{Id}`, etc.
- You can add your own in code or via placement.

## Customization approaches
- Override `Pager.cshtml` / `Pager.liquid` in your theme to change wrapper/markup.
- Override sub-shapes (e.g., `Pager_Link.cshtml`, `Pager_Previous.cshtml`, `Pager_CurrentPage.cshtml`) for link-level markup.
- For `PagerSlim`, override `Pager_Previous`/`Pager_Next`.
- Use `shape_pager` (Liquid) or configure the pager shape in Razor controller/view to set classes/attributes/texts.

## Override examples (Razor)
- Minimal `Views/Pager.cshtml` (forces C# shape pipeline to run `Pager_Links`):
  ```cshtml
  @{
      Model.Metadata.Alternates.Clear();
      Model.Metadata.Type = "Pager_Links";
  }
  @await DisplayAsync(Model)
  ```
- `Views/Pager.cshtml` with wrapper/Bootstrap classes:
  ```cshtml
  TagBuilder tag = Tag(Model, "ul");
  tag.AddCssClass("pagination");
  foreach (var item in Model) { tag.InnerHtml.AppendHtml(await DisplayAsync(item)); }
  <nav aria-label="Pager">@tag</nav>
  ```
- `Views/Pager_Link.cshtml` (bootstrap-style link items):
  ```cshtml
  @*
    Model has Attributes (href, rel, etc.), Classes, and Value.
    Add active/disabled classes if set on parent tags.
  *@
  var li = Tag(Model, "li");
  li.AddCssClass("page-item");
  if (Model.Tag?.HasCssClass("disabled") == true) { li.AddCssClass("disabled"); }
  if (Model.Tag?.HasCssClass("active") == true) { li.AddCssClass("active"); }

  var a = Tag(Model, "a");
  a.AddCssClass("page-link");
  foreach (var attr in Model.Attributes) { a.Attributes[attr.Key] = attr.Value?.ToString(); }
  a.InnerHtml.AppendHtml(CoerceHtmlString(Model.Value));

  li.InnerHtml.AppendHtml(a);
  @li
  ```
- `Views/Pager_Previous.cshtml` (optional custom glyph/text):
  ```cshtml
  Model.Value = Html.Raw("&laquo;");
  Model.Metadata.Type = "Pager_Link";
  @await DisplayAsync(Model)
  ```
- Example glyph-based overrides (from a working theme):
  - `Pager_First`: set `Model.Metadata.Type = "Pager_Link"`, `Model.Value` to `««` (Font Awesome icons), add `title`, set `RouteValues["action"]="Index"`; then `@await DisplayAsync(Model)`.
  - `Pager_Last`: same pattern with `»»`.
  - `Pager_Next`: set `Model.Value` to `»`, add `title`, `Model.Metadata.Type = "Pager_Link"`.
  - `Pager_Previous`: set `Model.Value` to `«`, add `title`, set `Model.RouteValues["action"]="Index"` when `pageNum` is null; `Model.Metadata.Type = "Pager_Link"`.

Use `PagerId` alternates (`Pager__Blog`) to scope overrides to a specific pager instance if needed.

## Liquid helpers (from docs)
- `shape_pager Model.Pager attributes: "{\"rel\": \"no-follow\"}"` to adjust attributes.
- Alternates with `PagerId` can target specific pagers (e.g., `Pager-Blog.cshtml`).

## Tips
- Pager is just a specialized navigation/list; overriding the navigation templates changes pager rendering too.
- Use `PagerId` to scope overrides to a specific pager instance to avoid global impact.
- When adding attributes (e.g., `rel="nofollow"`), set them on `Pager` or `Pager_Link` via shape properties or `shape_pager`.
