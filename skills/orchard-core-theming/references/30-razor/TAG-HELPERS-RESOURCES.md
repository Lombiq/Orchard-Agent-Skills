# Tag Helpers - Resources and Metadata

Tag helpers for scripts, styles, and head metadata.

## `<script ...>` and `<style ...>`
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

## `<resources type="...">`
- Purpose: Render all registered resources of a given type.
- Attributes:
  - `type` (enum; e.g., `HeadLink`, `HeadScript`, `FootScript`, `Stylesheet`, `Meta`)
- Example:
```cshtml
<resources type="Stylesheet"></resources>
```

## `<meta asp-name="..." content="...">`, `<meta asp-property="..." content="...">`
- Purpose: Register meta entries.
- Attributes:
  - `asp-name` or `asp-property`
  - `content`, `http-equiv`, `charset`, `separator`
- Example:
```cshtml
<meta asp-name="description" content="..." />
```

## `<link asp-src="...">`
- Purpose: Register a link resource.
- Attributes:
  - `asp-src`, `asp-append-version`
  - `rel`, `title`, `type`, `condition`
- Example:
```cshtml
<link asp-src="~/MyTheme/icons/favicon.ico" rel="icon" />
```
