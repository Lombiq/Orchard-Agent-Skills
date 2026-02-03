# Tag Helpers - Shapes and Zones

Tag helpers used to render and customize shapes.

## `<shape>`
- Purpose: Render any shape by type name with optional props and caching metadata.
- Attributes:
  - `type` (optional): shape type. If omitted, uses tag name. Use the internal shape type, not the file name.
    File name mapping: `-` -> `__`, `.` -> `_`. E.g. `Component-Header.cshtml` renders with
    `type="Component__Header"` and `Content-Page.Summary.cshtml` renders with `type="Content_Summary__Page"`.
  - `prop-*`: passes additional shape properties; values keep original type.
  - Any other attributes become shape properties (string).
  - `id`, `alternate`, `wrapper`, `display-type` map to shape metadata.
  - `cache-id`, `cache-context`, `cache-tag`, `cache-fixed-duration`, `cache-sliding-duration`.
- Example:
```cshtml
<shape type="Card" prop-title="Hello" class="hero" cache-id="card-1" />
```

## `<metadata>`
- Purpose: Set shape metadata inside a shape tag.
- Attributes:
  - `display-type` (sets metadata display type).
- Example:
```cshtml
<shape type="Card">
  <metadata display-type="Summary" />
</shape>
```

## `<add-alternate name="...">`, `<remove-alternate name="...">`, `<clear-alternates>`
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

## `<add-wrapper name="...">`, `<remove-wrapper name="...">`, `<clear-wrappers>`
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

## `<add-class name="...">`, `<remove-class name="...">`, `<clear-classes>`
- Purpose: Manage `shape.Classes`.
- Location: inside a shape tag.
- Example:
```cshtml
<shape type="Card">
  <add-class name="featured" />
</shape>
```

## `<add-property name="...">`
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

## `<zone name="..." position="...">`
- Purpose: Add child content to a layout zone.
- Attributes:
  - `name` (required)
  - `position` (optional)
- Example:
```cshtml
<zone name="Header" position="1">...</zone>
```
