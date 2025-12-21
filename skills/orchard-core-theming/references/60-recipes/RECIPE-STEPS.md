# Recipe Steps Catalog

This is a practical catalog of built-in recipe steps and their expected shape.
Use it to assemble setup recipes or content imports quickly.
Note: step names appear in different casing across recipes. Prefer the canonical names shown in this file.

## Most common steps (real projects)
These are the steps that show up most often in real Orchard Core solutions.
Use these as the default "first examples" when building or reading recipes.

### `feature`
- Enables/disables features.
- Example:
```json
{ "name": "feature", "enable": [ "OrchardCore.Contents", "OrchardCore.Media" ] }
```
- Feature IDs: see `FEATURE-CATALOG.md`.

### `content`
- Imports content items as full `ContentItem` JSON.
- Example (minimal):
```json
{
  "name": "content",
  "data": [
    {
      "ContentType": "Page",
      "DisplayText": "Home",
      "TitlePart": { "Title": "Home" }
    }
  ]
}
```
- Cross-reference: `40-content-model/CONTENT-ITEMS.md`, `40-content-model/FIELDS.md`.

### `ContentDefinition`
- Adds/updates content types and parts (merge behavior).
- Example (type + part):
```json
{
  "name": "ContentDefinition",
  "ContentTypes": [
    {
      "Name": "Page",
      "DisplayName": "Page",
      "Settings": { "ContentTypeSettings": { "Creatable": true } },
      "ContentTypePartDefinitionRecords": [
        { "PartName": "TitlePart", "Name": "TitlePart" }
      ]
    }
  ],
  "ContentParts": [
    {
      "Name": "PageBody",
      "Settings": { "ContentPartSettings": { "Attachable": true } },
      "ContentPartFieldDefinitionRecords": [
        {
          "FieldName": "Body",
          "Name": "HtmlBody",
          "Settings": { "ContentPartFieldSettings": { "DisplayName": "Body" } }
        }
      ]
    }
  ]
}
```
- Cross-reference: `40-content-model/CONTENT-DEFINITIONS.md`.

### `settings`
- Updates site settings (known keys + module settings).
- Example:
```json
{
  "name": "settings",
  "HomeRoute": { "Area": "OrchardCore.Contents", "Action": "Display", "ContentItemId": "..." },
  "RegistrationSettings": { "UsersCanRegister": true }
}
```

### `recipes`
- Executes other recipes (like composition).
- Example:
```json
{
  "name": "recipes",
  "Values": [ { "executionid": "MyApp", "name": "My.Setup.Content" } ]
}
```

### `media`
- Imports media from package files into the media library.
- Example:
```json
{
  "name": "media",
  "Files": [
    { "SourcePath": "Recipes/Media/logo.svg", "TargetPath": "branding/logo.svg" }
  ]
}
```

### `roles`
- Creates/updates roles.
- Example:
```json
{
  "name": "Roles",
  "Roles": [
    { "Name": "Editor", "Permissions": [ "EditContent" ], "PermissionBehavior": "Add" }
  ]
}
```

### `themes`
- Sets site/admin themes.
- Example:
```json
{ "name": "themes", "site": "MyTheme", "admin": "TheAdmin" }
```

### `layers`
- Defines layer rules (used with widgets and LayerMetadata on content items).
- Example:
```json
{
  "name": "layers",
  "Layers": [
    { "Name": "Homepage", "LayerRule": { "Conditions": [ { "$type": "OrchardCore.Rules.Models.UrlCondition, OrchardCore.Rules", "Value": "/" } ] } }
  ]
}
```

### `custom-settings`
- Imports custom settings content items (often from modules).
- Example:
```json
{
  "name": "custom-settings",
  "MyModuleSettings": {
    "ContentType": "MyModuleSettings",
    "DisplayText": "",
    "MySettingsPart": { "Enabled": true }
  }
}
```
- Cross-reference: `40-content-model/CONTENT-ITEMS.md`.

### `AdminMenu`
- Creates/updates admin menu structure.
- Example:
```json
{
  "name": "AdminMenu",
  "data": [
    {
      "Name": "Admin menus",
      "MenuItems": [
        { "$type": "OrchardCore.AdminMenu.AdminNodes.LinkAdminNode, OrchardCore.AdminMenu", "LinkText": "Docs", "LinkUrl": "/Admin/Docs" }
      ]
    }
  ]
}
```

### `WorkflowType`
- Imports workflow definitions.
- Example:
```json
{
  "name": "WorkflowType",
  "data": [ { "Name": "My Workflow", "IsEnabled": true, "Activities": [], "Transitions": [] } ]
}
```

### Search index steps (if used)
- Elasticsearch and Lucene index steps appear in some solutions.
- Examples:
```json
{ "name": "ElasticIndexSettings", "Indices": [ { "Search": { "IndexLatest": true } } ] }
{ "name": "elastic-index-rebuild", "includeAll": true }
```

## Core setup steps

### `feature`
- Enables/disables features.
- Shape:
```json
{ "name": "feature", "enable": [ "Feature.Id" ], "disable": [ "Feature.Id" ] }
```

### `themes`
- Sets site and admin theme IDs.
- Shape:
```json
{ "name": "themes", "site": "MyTheme", "admin": "TheAdmin" }
```

### `settings`
- Updates site settings (known keys + custom properties).
- Site settings keys (built-in `SiteSettings`):
  - `SiteName` (string)
  - `BaseUrl` (string)
  - `Calendar` (string)
  - `PageTitleFormat` (string)
  - `PageSize`, `MaxPageSize`, `MaxPagedCount` (ints)
  - `TimeZoneId` (string)
  - `ResourceDebugMode` (`FromConfiguration` | `Enabled` | `Disabled`)
  - `AppendVersion` (bool)
  - `UseCdn` (bool), `CdnBaseUrl` (string)
  - `HomeRoute` (route dictionary: `Area`, `Controller`/`Action` or `ContentItemId`)
  - `SuperUser` (string)
  - `CacheMode` (`FromConfiguration` | `Enabled` | `DebugEnabled` | `Disabled`)
- Any additional properties are stored in `site.Properties` and can be module-specific settings.
- Example:
```json
{
  "name": "settings",
  "SiteName": "Site",
  "TimeZoneId": "UTC",
  "ResourceDebugMode": "FromConfiguration",
  "HomeRoute": { "Area": "OrchardCore.Contents", "Action": "Display", "ContentItemId": "..." }
}
```

### `recipes`
- Executes other recipes by name.
- Shape:
```json
{ "name": "recipes", "Values": [ { "executionid": "MyApp", "name": "My.Recipe.Name" } ] }
```

## Definitions

### `ContentDefinition`
- Adds or updates content types/parts (merge style).
- Shape:
```json
{ "name": "ContentDefinition", "ContentTypes": [ ... ], "ContentParts": [ ... ] }
```
- Use `ContentTypeSettings` for type-level flags (Creatable, Draftable, Listable, Stereotype).
- Attach parts via `ContentTypePartDefinitionRecords`; add fields inside `ContentPartFieldDefinitionRecords`.
- Part/field settings mirror `ContentDefinitions.json` (see `40-content-model/CONTENT-DEFINITIONS.md`).

### `ReplaceContentDefinition`
- Replaces content definitions (delete then recreate).
- Shape:
```json
{ "name": "ReplaceContentDefinition", "ContentTypes": [ ... ], "ContentParts": [ ... ] }
```

### `DeleteContentDefinition`
- Deletes content types/parts by name.
- Shape:
```json
{ "name": "DeleteContentDefinition", "ContentTypes": [ "Type" ], "ContentParts": [ "Part" ] }
```

## Content and media

### `content`
- Imports content items.
- Shape:
```json
{ "name": "content", "data": [ { "ContentType": "Page", ... } ] }
```
- Tips:
  - Ensure content types/parts/fields exist before import (see `ContentDefinition`).
  - Use variables for IDs referenced across steps.
  - For Flow/Bag/List items, include embedded content items with their parts/fields.

### `media`
- Imports media from file, base64, or URL.
- Shape:
```json
{ "name": "media", "Files": [ { "TargetPath": "img/logo.png", "SourcePath": "../wwwroot/img/logo.png" } ] }
```
- `SourcePath` is relative to the recipe file; include files in `Recipes/Media/` beside the recipe.

### `MediaProfiles`
- Creates/updates media profiles.
- Shape:
```json
{ "name": "MediaProfiles", "MediaProfiles": { "MyProfile": { ... } } }
```

## Layers and placements

### `Layers`
- Defines display layers with rules.
- Shape:
```json
{ "name": "Layers", "Layers": [ { "Name": "Homepage", "Rule": "isHomepage()" } ] }
```

### `Placements`
- Updates placement rules.
- Shape:
```json
{ "name": "Placements", "Placements": { "TextField": [ { "place": "Content:1" } ] } }
```

## Queries and search

### `Queries`
- Defines queries (Lucene/SQL/etc).
- Shape:
```json
{ "name": "Queries", "Queries": [ { "Name": "Recent", "Source": "Lucene", ... } ] }
```

### `lucene-index`
- Creates/updates Lucene indexes.
- Shape:
```json
{ "name": "lucene-index", "Indices": [ { "Search": { ... } } ] }
```

### `lucene-index-reset` / `lucene-index-rebuild`
- Reset or rebuild specific Lucene indexes.
- Shape:
```json
{ "name": "lucene-index-reset", "Indices": [ "Search" ] }
{ "name": "lucene-index-rebuild", "Indices": [ "Search" ] }
```

### `ElasticIndexSettings`
- Creates/updates Elasticsearch indexes.
- Shape:
```json
{ "name": "ElasticIndexSettings", "Indices": [ { "Search": { ... } } ] }
```

### `elastic-index-reset` / `elastic-index-rebuild`
- Reset or rebuild Elasticsearch indexes.

### `CreateOrUpdateIndexProfile`
- Creates/updates index profiles across providers.
- Shape:
```json
{ "name": "CreateOrUpdateIndexProfile", "Indexes": [ { "Name": "Search", "ProviderName": "Lucene", ... } ] }
```

### `ResetIndex` / `RebuildIndex`
- Reset/rebuild index profiles by name or include all.
- Shape:
```json
{ "name": "ResetIndex", "IncludeAll": true }
{ "name": "RebuildIndex", "IndexNames": [ "Search" ] }
```

### Azure AI Search
- `azureai-index-create`, `azureai-index-reset`, `azureai-index-rebuild`
- Used to manage Azure AI Search indexes.

## Security and identity

### `Roles`
- Creates/updates roles and permissions.
- Shape:
```json
{ "name": "Roles", "Roles": [ { "Name": "Editor", "Permissions": [ "EditContent" ], "PermissionBehavior": "Add" } ] }
```

### `Users`
- Creates/updates users.
- Shape:
```json
{ "name": "Users", "Users": [ { "UserId": "...", "UserName": "...", "RoleNames": [ "Editor" ] } ] }
```

### `custom-user-settings`
- Updates per-user custom settings content items.

## Templates and workflows

### `Templates`
- Creates/updates Liquid templates.
- Shape:
```json
{ "name": "Templates", "Templates": { "Content__Page": { "Content": "..." } } }
```

### `AdminTemplates`
- Creates/updates admin templates.

### `ShortcodeTemplates`
- Creates/updates shortcode templates.

### `WorkflowType`
- Creates/updates workflow definitions.

## Other common steps

### `AdminMenu`
- Creates/updates admin menu structure.

### `Sitemaps`
- Creates/updates sitemaps.

### `UrlRewriting`
- Creates/updates URL rewrite rules.

### `custom-settings`
- Updates custom settings content items stored in the site settings bag.

### OpenID and external auth
- `OpenIdApplication`, `OpenIdScope`, `OpenIdClientSettings`, `OpenIdServerSettings`, `OpenIdValidationSettings`
- `AzureADSettings`, `MicrosoftAccountSettings`, `GitHubAuthenticationSettings`, `FacebookLoginSettings`

### Social providers
- `FacebookCoreSettings`, `TwitterSettings`

### Tenants
- `FeatureProfiles` for tenant feature profile definitions.
