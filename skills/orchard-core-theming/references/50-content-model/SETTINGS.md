# Definition Settings

This file documents the settings objects used inside content definitions.
Settings appear under the `Settings` property in `ContentDefinition.json`.
Prefer using `CONTENT-DEFINITIONS-EXTRACTOR.md` to pull the exact settings slice you need.

## Shared settings

### ContentTypeSettings
- `Creatable`
- `Listable`
- `Draftable`
- `Versionable`
- `Stereotype`
- `Securable`
- `Description`

### ContentPartSettings
- `Attachable`
- `Reusable`
- `DisplayName`
- `Description`
- `DefaultPosition`

### ContentTypePartSettings
- `DisplayName`
- `Description`
- `Position`
- `DisplayMode`
- `Editor`

### ContentPartFieldSettings
- `DisplayName`
- `Description`
- `Editor`
- `DisplayMode`
- `Position`

### FieldSettings (base)
- `Hint`
- `Required`

## Part-specific settings (common)

### TitlePartSettings
- `Options` (`Editable`, `GeneratedDisabled`, `GeneratedHidden`, `EditableRequired`)
- `Pattern`
- `RenderTitle`
- `Placeholder`

### AutoroutePartSettings
- `AllowCustomPath`
- `Pattern`
- `ShowHomepageOption`
- `AllowUpdatePath`
- `AllowDisabled`
- `AllowRouteContainedItems`
- `ManageContainedItemRoutes`
- `AllowAbsolutePath`

### AliasPartSettings
- `Pattern`
- `Options` (`Editable`, `GeneratedDisabled`)

### HtmlBodyPartSettings
- `SanitizeHtml`

### MarkdownBodyPartSettings
- `SanitizeHtml`

### ListPartSettings
- `PageSize`
- `ContainedContentTypes`
- `EnableOrdering`
- `ShowHeader`

### WidgetsListPartSettings
- `Zones`

### BagPartSettings
- `ContainedContentTypes`
- `ContainedStereotypes`
- `DisplayType`
- `CollapseContainedItems`

### FlowPartSettings
- `ContainedContentTypes`
- `CollapseContainedItems`
- `DefaultAlignment`

### CommonPartSettings
- `DisplayDateEditor`
- `DisplayOwnerEditor`

### AuditTrailPartSettings
- `ShowCommentInput`

### PreviewPartSettings
- `Pattern`

### HtmlMenuItemPartSettings
- `SanitizeHtml`

### SeoMetaPartSettings
- `DisplayKeywords`
- `DisplayCustomMetaTags`
- `DisplayOpenGraph`
- `DisplayTwitter`
- `DisplayGoogleSchema`

### FacebookPluginPartSettings
- `Liquid`

## Field-specific settings
See `FIELDS.md` for each field type's settings and editor settings.
