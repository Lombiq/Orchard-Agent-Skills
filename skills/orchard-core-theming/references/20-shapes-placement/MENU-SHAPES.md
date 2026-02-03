# Menu Shapes and Rendering

How Orchard Core renders menus and how to override or hand-render them.

## Feature dependency
- Enable `OrchardCore.Menu` for menu content types and shapes.

## Shapes involved
- `Menu`: root shape for a menu.
- `MenuItem`: one per menu item (recursive).
- `MenuItemLink`: the link portion of a menu item.
- Metadata/alternates (from `MenuShapes.cs`):
  - Level alternates: `MenuItem__level__{n}`, `MenuItemLink__level__{n}`.
  - By content type: `MenuItem__<ContentType>`, `MenuItemLink__<ContentType>`, with level variants.
  - By menu name (differentiator): `MenuItem__<MenuName>`, `MenuItem__<MenuName>__level__{n}`, and combined with content type; same for `MenuItemLink`.

## Default rendering patterns
- Built-in shape drivers create `MenuItem` and `MenuItemLink` shapes per item; child items recurse.
- Permissions: `MenuItemPermissionPart` can hide items from users lacking permissions.
- Menu item kinds (content types with stereotype `MenuItem`):
  - `LinkMenuItem` (LinkMenuItemPart: Url/Target)
  - `HtmlMenuItem` (HtmlMenuItemPart: Html)
  - `ContentMenuItem` (ContentMenuItemPart: selected content item)
  - Nested items are stored via `MenuItemsListPart.MenuItems`.

## Tag helpers (Razor)
- `<menu>` tag helper: `<menu alias="alias:main-menu" cache-id="main-menu" cache-tag="alias:main-menu" cache-context="user.roles" />`
  - Parameters: `alias` (e.g., `alias:main-menu`), caching attributes (`cache-id`, `cache-tag`, `cache-context`, `cache-fixed-duration`), `cache-expires-after`, etc.
- Use the tag helper to get default rendering, then override shapes if you need different markup.

## Rendering manually (Liquid or Razor)
- Liquid: load by alias and build shapes:
```liquid
{% assign menu = "alias:main-menu" | menu %}
{{ menu | shape_render }}
```
- Liquid (content item access for in-place rendering):
```liquid
{% assign menu_item = Content["alias:main-menu"] %}
{% assign menu_items = menu_item.Content.MenuItemsListPart.MenuItems %}
{% for item in menu_items %}
  {{ item.DisplayText }}
{% endfor %}
```
- Razor: inject `IShapeFactory` or use `New` to build:
```cshtml
@inject OrchardCore.DisplayManagement.IShapeFactory ShapeFactory
@{
    var menu = await ShapeFactory.New.Menu(Alias: "alias:main-menu");
}
@await DisplayAsync(menu)
```
- To fully custom render, iterate items:
  - Liquid: `menu.MenuItems` is a list of content items (with parts like LinkMenuItemPart, HtmlMenuItemPart, ContentMenuItemPart, MenuItemsListPart for children).
  - Razor: iterate `Model.MenuItems` (from Menu shape) or `ContentItem.As<MenuItemsListPart>().MenuItems`.

## Overriding templates
- Place overrides in the active theme:
  - `Views/Menu.liquid` or `Views/Menu.cshtml`
  - `Views/MenuItem.liquid` / `Views/MenuItemLink.liquid` (use alternates for menu name/level/content type to target specific cases).
- Use alternates for per-menu or per-level styling:
  - `MenuItem__MainMenu`, `MenuItem__MainMenu__level__2`
  - `MenuItemLink__LinkMenuItem`, `MenuItemLink__MainMenu__level__1`

## Built-in templates (Razor, simplified)
- `Menu.cshtml`:
  ```cshtml
  TagBuilder tag = Tag(Model, "ul");
  tag.AddCssClass("list-group");
  foreach (var item in Model.Items) { tag.InnerHtml.AppendHtml(await DisplayAsync(item)); }
  <nav>@tag</nav>
  ```
- `MenuItem.cshtml`:
  ```cshtml
  TagBuilder tag = Tag(Model, "li");
  tag.InnerHtml.AppendHtml(await DisplayAsAsync(Model, "MenuItemLink"));
  if ((bool)Model.HasItems) {
      tag.InnerHtml.AppendHtml("<ul>");
      foreach (var item in Model.Items) { tag.InnerHtml.AppendHtml(await DisplayAsync(item)); }
      tag.InnerHtml.AppendHtml("</ul>");
  }
  @tag
  ```
- `MenuItemLink` (base):
  ```cshtml
  <a href="@(Model.Href ?? "#")" target="@(!string.IsNullOrEmpty(Model.Target) ? Model.Target : "_self")">@Model.Text</a>
  ```
- `MenuItemLink-LinkMenuItem.cshtml` (LinkMenuItemPart):
  ```cshtml
  var part = Model.ContentItem.As<LinkMenuItemPart>();
  var url = part.Url.StartsWith('/') ? "~" + part.Url : part.Url;
  url = url.StartsWith("~/") ? Url.Content(part.Url) : url;
  if (!string.IsNullOrEmpty(part.Target)) tag.Attributes["target"] = part.Target;
  tag.Attributes["href"] = url;
  tag.InnerHtml.Append(Model.ContentItem.DisplayText);
  ```
- `MenuItemLink-HtmlMenuItem.cshtml` (HtmlMenuItemPart):
  ```cshtml
  var part = Model.ContentItem.As<HtmlMenuItemPart>();
  var url = part.Url.StartsWith('/') ? "~" + part.Url : part.Url;
  url = url.StartsWith("~/") ? Url.Content(part.Url) : url;
  tag.Attributes["href"] = url;
  if (!string.IsNullOrEmpty(part.Target)) tag.Attributes["target"] = part.Target;
  tag.InnerHtml.AppendHtml(Html.Raw(part.Html));
  ```
- `MenuItemLink-ContentMenuItem.cshtml` (ContentMenuItemPart):
  ```cshtml
  var part = Model.ContentItem.As<ContentMenuItemPart>();
  string id = part.ContentItem.Content.ContentMenuItemPart.SelectedContentItem.ContentItemIds[0];
  var routeValues = new RouteValueDictionary(AutorouteOptions.Value.GlobalRouteValues);
  routeValues[AutorouteOptions.Value.ContentItemIdKey] = id;
  tag.Attributes["href"] = Url.RouteUrl(routeValues);
  tag.InnerHtml.Append(Model.ContentItem.DisplayText);
  ```

## Useful models/properties (per menu item)
- `ContentItem` with parts:
  - `LinkMenuItemPart`: `Url`, `Target`
  - `HtmlMenuItemPart`: `Html`
  - `ContentMenuItemPart`: `SelectedContentItem.ContentItemIds[]`
  - `MenuItemsListPart`: `MenuItems` (children)
  - `MenuItemPermissionPart`: permission data (hide if unauthorized)
- For display, the `MenuItem` shape includes the content item and computed alternates; `MenuItemLink` focuses on the link rendering.
- Use `ContentItem.DisplayText` for link labels; avoid `TitlePart.Title` in front-end rendering since it's admin UX metadata and not reliable for content handling.

## Tips
- Start with the tag helper for default behavior; override `MenuItem` / `MenuItemLink` for custom markup.
- Use level and menu-name alternates to target specific menu instances without affecting others.
- When hand-rendering, respect `MenuItemPermissionPart` if present (check permissions) to avoid showing unauthorized links.
