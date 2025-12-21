# Tag Helpers

This is a source-derived catalog of the Razor tag helpers that are directly useful for theme development.

## Shape rendering

### `<shape>`
- Purpose: Render any shape by type name with optional props and caching metadata.
- Attributes:
  - `type` (optional): shape type. If omitted, uses tag name.
  - `prop-*`: passes additional shape properties; values keep original type.
  - Any other attributes become shape properties (string).
  - `id`, `alternate`, `wrapper`, `display-type` map to shape metadata.
  - `cache-id`, `cache-context`, `cache-tag`, `cache-fixed-duration`, `cache-sliding-duration`.
- Example:
```cshtml
<shape type="Card" prop-title="Hello" class="hero" cache-id="card-1" />
```

### `<metadata>`
- Purpose: Set shape metadata inside a shape tag.
- Attributes:
  - `display-type` (sets metadata display type).
- Example:
```cshtml
<shape type="Card">
  <metadata display-type="Summary" />
</shape>
```

### `<add-alternate name="...">`, `<remove-alternate name="...">`, `<clear-alternates>`
- Purpose: Manage shape alternates.
- Location: inside a shape tag; alternates and clears require `<metadata>` as parent.
- Example:
```cshtml
<shape type="Card">
  <metadata>
    <add-alternate name="Card__Featured" />
    <remove-alternate name="Card__Old" />
    <clear-alternates />
  </metadata>
</shape>
```

### `<add-wrapper name="...">`, `<remove-wrapper name="...">`, `<clear-wrappers>`
- Purpose: Manage shape wrappers.
- Location: inside a shape tag; wrappers and clears require `<metadata>` as parent.
- Example:
```cshtml
<shape type="Card">
  <metadata>
    <add-wrapper name="Card_Wrapper" />
  </metadata>
</shape>
```

### `<add-class name="...">`, `<remove-class name="...">`, `<clear-classes>`
- Purpose: Manage `shape.Classes`.
- Location: inside a shape tag.
- Example:
```cshtml
<shape type="Card">
  <add-class name="featured" />
</shape>
```

### `<add-property name="...">`
- Purpose: Adds a property to the current shape; value can come from inner content or a `value` attribute.
- Location: inside a shape tag.
- Attributes:
  - `name` (required)
  - `value` (optional)
- Example:
```cshtml
<shape type="Card">
  <add-property name="Intro">Short intro text</add-property>
</shape>
```

### `<zone name="..." position="...">`
- Purpose: Add child content to a layout zone.
- Attributes:
  - `name` (required)
  - `position` (optional)
- Example:
```cshtml
<zone name="Header" position="1">...</zone>
```

## Content helpers

### `<contentitem>`
- Purpose: Render a `ContentItem` shape.
- Attributes: same as `<shape>`, plus `prop-*` etc.
- Example:
```cshtml
<contentitem content-item="@Model.ContentItem" display-type="Summary" />
```

### `<a display-for="...">`, `<a edit-for="...">`, `<a admin-for="...">`, `<a remove-for="...">`, `<a create-for="...">`
- Purpose: Generate links for content items.
- Attributes:
  - `display-for`, `edit-for`, `admin-for`, `remove-for`, `create-for` (each expects a `ContentItem`).
  - `asp-route-*` adds route values.
- Example:
```cshtml
<a display-for="@Model.ContentItem" class="btn" asp-route-returnUrl="@Context.Request.Path" />
```

## Menus

### `<menu>`
- Purpose: Render a menu shape.
- Attributes: same as `<shape>`, plus `prop-*` etc.
- Example:
```cshtml
<menu prop-name="main" />
```

## User and validation helpers

### `<user-display-name user-name="...">`
- Purpose: Render a user display name shape with caching hints.
- Attributes:
  - `user-name`
  - inherits `<shape>` attributes and cache metadata.
- Example:
```cshtml
<user-display-name user-name="@user.UserName" />
```

### `asp-validation-class-for`
- Purpose: Adds `has-validation-error is-invalid` to any element when the specified model field has errors.
- Attribute:
  - `asp-validation-class-for="Model.Property"`
- Example:
```cshtml
<div asp-validation-class-for="Model.Email">...</div>
```

### `<input asp-is-disabled="true">`
- Purpose: Adds `disabled="disabled"` when `asp-is-disabled` is true.
- Attribute:
  - `asp-is-disabled` (bool)
- Example:
```cshtml
<input asp-for="Model.Name" asp-is-disabled="true" />
```

## Date/time helpers

### `<datetime utc="..." format="...">`
- Purpose: Render a `DateTime` shape.
- Attributes:
  - `utc` (DateTime?)
  - `format` (string)
- Example:
```cshtml
<datetime utc="@Model.PublishedUtc" format="g" />
```

### `<timespan utc="..." origin="...">`
- Purpose: Render a `TimeSpan` shape relative to `origin`.
- Attributes:
  - `utc` (DateTime?)
  - `origin` (DateTime?)
- Example:
```cshtml
<timespan utc="@Model.PublishedUtc" origin="@DateTime.UtcNow" />
```

## Resources and assets

### `<script ...>` and `<style ...>`
- Purpose: Register or inline scripts/styles with resource management.
- Key attributes:
  - `asp-name`, `asp-src`, `at`, `asp-append-version`
  - `cdn-src`, `debug-src`, `debug-cdn-src`
  - `use-cdn`, `condition`, `culture`, `debug`, `depends-on`, `version`
- Notes:
  - `at` can be `Head`, `Foot`, or `Inline`.
- Example:
```cshtml
<script asp-name="bootstrap" at="Foot"></script>
<style asp-src="~/MyTheme/site.css" at="Head" asp-append-version="true"></style>
```

### `<resources type="...">`
- Purpose: Render all registered resources of a given type.
- Attributes:
  - `type` (enum; e.g., `HeadLink`, `HeadScript`, `FootScript`, `Stylesheet`, `Meta`)
- Example:
```cshtml
<resources type="Stylesheet"></resources>
```

### `<meta asp-name="..." content="...">`, `<meta asp-property="..." content="...">`
- Purpose: Register meta entries.
- Attributes:
  - `asp-name` or `asp-property`
  - `content`, `http-equiv`, `charset`, `separator`
- Example:
```cshtml
<meta asp-name="description" content="..." />
```

### `<link asp-src="...">`
- Purpose: Register a link resource.
- Attributes:
  - `asp-src`, `asp-append-version`
  - `rel`, `title`, `type`, `condition`
- Example:
```cshtml
<link asp-src="~/MyTheme/icons/favicon.ico" rel="icon" />
```

## Media

### `<img asset-src="...">`
- Purpose: Resolve a media library path to a public URL.
- Attributes:
  - `asset-src` (media path)
  - `asp-append-version` (bool)
- Example:
```cshtml
<img asset-src="/media/hero.jpg" asp-append-version="true" />
```

### `<a asset-href="...">`
- Purpose: Resolve a media library path to a public URL.
- Attributes:
  - `asset-href` (media path)
  - `asp-append-version` (bool)
- Example:
```cshtml
<a asset-href="/media/file.pdf">Download</a>
```

### `<img img-width="..." img-height="..." img-resize-mode="..." img-quality="..." img-format="..." img-profile="..." img-anchor="..." img-bgcolor="...">`
- Purpose: Apply image resizing to an existing `src`.
- Attributes (prefix `img-`):
  - `img-width`, `img-height`, `img-resize-mode`, `img-quality`
  - `img-format`, `img-profile`, `img-anchor`, `img-bgcolor`
- Example:
```cshtml
<img src="/media/hero.jpg" img-width="800" img-resize-mode="Crop" />
```

## Caching

### `<dynamic-cache cache-id="...">`
- Purpose: Cache rendered output with dynamic invalidation.
- Attributes:
  - `cache-id` (required)
  - `vary-by`, `dependencies`
  - `expires-on`, `expires-after`, `expires-sliding`
  - `enabled` (bool)
- Example:
```cshtml
<dynamic-cache cache-id="home-hero" vary-by="culture">
  ...
</dynamic-cache>
```

### `<cache-dependency dependency="...">`
- Purpose: Add a cache dependency inside a cache scope.
- Example:
```cshtml
<cache-dependency dependency="contentitem:123" />
```

## Miscellaneous

### `<captcha language="..." onload="...">`
- Purpose: Render a ReCaptcha shape.
- Attributes:
  - `language` (ISO code)
  - `onload` (callback)
- Example:
```cshtml
<captcha language="en" onload="onCaptchaLoaded" />
```
