# Content Parts

This catalog lists built-in Orchard Core content parts and their stored properties.
Parts with no properties are still useful for behaviors, routing, or display, but do not
add fields to `ContentItem.Content`.

## Core content parts

### TitlePart
- Properties: `Title` (string)
- Often mirrored into `ContentItem.DisplayText`.

### AutoroutePart
- Properties: `Path`, `SetHomepage` (bool), `Disabled` (bool), `RouteContainedItems` (bool), `Absolute` (bool)

### AliasPart
- Properties: `Alias` (string)

### HtmlBodyPart
- Properties: `Html` (string)

### MarkdownBodyPart
- Properties: `Markdown` (string)

### LiquidPart
- Properties: `Liquid` (string)

### CommonPart
- No stored properties (uses `ContentItem` metadata like `CreatedUtc`, `Owner`, etc.).

### PreviewPart
- No stored properties (used for preview pipeline).

### ArchiveLaterPart
- Properties: `ScheduledArchiveUtc` (DateTime?)

### PublishLaterPart
- Properties: `ScheduledPublishUtc` (DateTime?)

### AuditTrailPart
- Properties: `Comment` (string), `ShowComment` (bool)

## Lists and flows

### ListPart
- No stored properties (list behavior; items are in index/query).

### ContainedPart
- Properties: `ListContentItemId`, `ListContentType`, `Order`

### BagPart
- Properties: `ContentItems` (array of embedded content items)

### FlowPart
- Properties: `Widgets` (array of flow widgets/content items)

## Widgets and menus

### WidgetsListPart
- No stored properties (controls widget placement in zones).

### MenuPart
- No stored properties (menu container).

### MenuItemsListPart
- Properties: `MenuItems` (array of menu item content items)

### MenuItemPermissionPart
- Properties: `PermissionNames` (string[])

### LinkMenuItemPart
- Properties: `Url`, `Target`

### HtmlMenuItemPart
- Properties: `Url`, `Target`, `Html`

### ContentMenuItemPart
- Properties: `CheckContentPermissions` (bool)

## Forms

### FormPart
- Properties: `Action`, `Method`, `WorkflowTypeId`, `EncType`,
  `EnableAntiForgeryToken`, `SaveFormLocation`

### FormElementPart
- Properties: `Id`

### FormInputElementPart
- Properties: `Name`

### FormInputElementVisibilityPart
- Properties: `Groups`, `Action`

### FormElementLabelPart
- Properties: `Option`, `Label`

### FormElementValidationPart
- Properties: `For`

### InputPart
- Properties: `Type`, `DefaultValue`, `Placeholder`

### TextAreaPart
- Properties: `DefaultValue`, `Placeholder`, `Rows`

### SelectPart
- Properties: `Options`, `DefaultValue`, `Editor`, `Text`, `Value`

### LabelPart
- Properties: `For`

### ButtonPart
- Properties: `Text`, `Type`

### ValidationPart
- Properties: `For`

### ValidationSummaryPart
- Properties: `ModelOnly` (bool)

### ReCaptchaPart
- No stored properties (runtime behavior only).

## Taxonomies

### TaxonomyPart
- Properties: `TermContentType`, `Terms` (JSON array of embedded terms)
- Routing tip: add `AutoroutePart` to the taxonomy content item (`RouteContainedItems: true`) and to the term content type (e.g., Tag) so each term gets its own URL (use `AutoroutePart.Path` on terms like `strategy`).

### TermPart
- Properties: `TaxonomyContentItemId`

## Search and localization

### SearchFormPart
- Properties: `IndexName`, `Placeholder`

### LocalizationPart
- Properties: `LocalizationSet`, `Culture`

## SEO and sitemaps

### SeoMetaPart
- Properties:
  - `PageTitle`, `Render`, `MetaDescription`, `MetaKeywords`, `Canonical`,
    `MetaRobots`, `CustomMetaTags`, `DefaultSocialImage`,
    `OpenGraphImage`, `OpenGraphType`, `OpenGraphTitle`, `OpenGraphDescription`,
    `TwitterImage`, `TwitterTitle`, `TwitterDescription`, `TwitterCard`,
    `TwitterCreator`, `TwitterSite`, `GoogleSchema`

### SitemapPart
- Properties: `OverrideSitemapConfig`, `ChangeFrequency`, `Priority`, `Exclude`

## Miscellaneous

### DashboardPart
- Properties: `Position`, `Width`, `Height`

### FacebookPluginPart
- Properties: `Liquid` (string)

### UserNotificationPreferencesPart
- Properties: `Methods`, `Optout`
