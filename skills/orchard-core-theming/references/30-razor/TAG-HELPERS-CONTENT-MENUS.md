# Tag Helpers - Content and Menus

Tag helpers for content item rendering and menus.

## `<contentitem>`
- Purpose: Render a `ContentItem` shape.
- Attributes: same as `<shape>`, plus `prop-*` etc.
- Example:
```cshtml
<contentitem content-item="@Model.ContentItem" display-type="Summary" />
```

## `<a display-for="...">`, `<a edit-for="...">`, `<a admin-for="...">`, `<a remove-for="...">`, `<a create-for="...">`
- Purpose: Generate links for content items.
- Attributes:
  - `display-for`, `edit-for`, `admin-for`, `remove-for`, `create-for` (each expects a `ContentItem`).
  - `asp-route-*` adds route values.
- Example:
```cshtml
<a display-for="@Model.ContentItem" class="btn" asp-route-returnUrl="@Context.Request.Path" />
```

## `<menu>`
- Purpose: Render a menu shape.
- Attributes: same as `<shape>`, plus `prop-*` etc.
- Example:
```cshtml
<menu prop-name="main" />
```
