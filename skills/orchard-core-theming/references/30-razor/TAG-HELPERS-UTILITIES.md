# Tag Helpers - Utilities

Helpers for user display, validation, date/time, and other utilities.

## `<user-display-name user-name="...">`
- Purpose: Render a user display name shape with caching hints.
- Attributes:
  - `user-name`
  - inherits `<shape>` attributes and cache metadata.
- Example:
```cshtml
<user-display-name user-name="@user.UserName" />
```

## `asp-validation-class-for`
- Purpose: Adds `has-validation-error is-invalid` to any element when the specified model field has errors.
- Attribute:
  - `asp-validation-class-for="Model.Property"`
- Example:
```cshtml
<div asp-validation-class-for="Model.Email">...</div>
```

## `<input asp-is-disabled="true">`
- Purpose: Adds `disabled="disabled"` when `asp-is-disabled` is true.
- Attribute:
  - `asp-is-disabled` (bool)
- Example:
```cshtml
<input asp-for="Model.Name" asp-is-disabled="true" />
```

## `<datetime utc="..." format="...">`
- Purpose: Render a `DateTime` shape.
- Attributes:
  - `utc` (DateTime?)
  - `format` (string)
- Example:
```cshtml
<datetime utc="@Model.PublishedUtc" format="g" />
```

## `<timespan utc="..." origin="...">`
- Purpose: Render a `TimeSpan` shape relative to `origin`.
- Attributes:
  - `utc` (DateTime?)
  - `origin` (DateTime?)
- Example:
```cshtml
<timespan utc="@Model.PublishedUtc" origin="@DateTime.UtcNow" />
```

## `<captcha language="..." onload="...">`
- Purpose: Render a ReCaptcha shape.
- Attributes:
  - `language` (ISO code)
  - `onload` (callback)
- Example:
```cshtml
<captcha language="en" onload="onCaptchaLoaded" />
```
