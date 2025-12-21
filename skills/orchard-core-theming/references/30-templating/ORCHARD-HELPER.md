# IOrchardHelper Extensions (Razor)

Quick catalog of useful `IOrchardHelper` extension methods in Razor views.

## Content queries (OrchardCore.Contents.Core)
- `GetContentItemIdByHandleAsync(handle)`
- `GetContentItemByHandleAsync(handle, VersionOptions option = null)`
- `GetContentItemByIdAsync(id, VersionOptions option = null)`
- `GetContentItemsByIdAsync(ids, VersionOptions option = null)`
- `GetContentItemByVersionIdAsync(versionId)`
- `QueryContentItemsAsync(Func<IQuery<ContentItem, ContentItemIndex>, IQuery<ContentItem>> query)`
- `GetRecentContentItemsByContentTypeAsync(contentType, max = 10)`

## Display helpers (OrchardCore.ContentManagement.Display/Razor)
- `DisplayAsync(ContentItem, displayType = "", groupId = "", IUpdateModel updater = null)` (on `IOrchardDisplayHelper`, which implements `IOrchardHelper`).
- `ConsoleLog(object content)` (logs JSON to browser console; no-op in production/null content).
- `LiquidToHtmlAsync(string liquid, object model = null)` - render a Liquid string to HTML from Razor (e.g., for HtmlField content).

## Culture helpers (OrchardCore.DisplayManagement/Extensions)
- `CultureDir()` -> `"rtl"` or `"ltr"`
- `IsRightToLeft()` -> bool
- `CultureName()` -> culture name (e.g., `en-US`)

## Localization (OrchardCore.ContentLocalization.Abstractions)
- `GetContentCultureAsync(ContentItem)` -> `CultureInfo`

## Users (OrchardCore.Users.Core/Razor)
- `GetUserByIdAsync(userId)`
- `GetUsersByIdsAsync(userIds)`

## CSS helpers (wrappers/classes)
- Content wrappers (OrchardCore.ContentManagement.Display/Razor):
  - `GetPartWrapperClasses(ContentTypePartDefinition, params string[] extra)`
  - `GetFieldWrapperClasses(ContentPartFieldDefinition, params string[] extra)`
- Theme/admin CSS helpers (OrchardCore.DisplayManagement/Html):
  - `GetLimitedWidthWrapperClasses(...)`
  - `GetLimitedWidthClasses(...)`
  - `GetStartClasses(...)`
  - `GetEndClasses(...)` (+ overload with offset)
  - `GetLabelClasses(bool inputRequired = false, params string[] extra)`
  - `GetWrapperClasses(...)`
  - `GetOffsetClasses(...)`
  - `GetThemeOptions()` -> `TheAdminThemeOptions`

## Media/CDN and sanitization
- `ResourceUrl(resourcePath, bool? appendVersion = null)` (OrchardCore.ResourceManagement.Core) - maps `~/` to app base, applies CDN and versioning.
- `SanitizeHtml(string html)` (OrchardCore.Infrastructure) - returns sanitized HTML.

## Tips
- Add `@inject IOrchardHelper Orchard` (or use the built-in `Orchard` property in Razor views) to access these.
- For shape rendering in Razor, prefer the `<shape>` tag helper for ad-hoc shapes and `DisplayAsync` for content items.
