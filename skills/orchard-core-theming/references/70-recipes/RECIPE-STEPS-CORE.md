# Recipe Steps - Core Setup

Core steps used in most setup recipes.

## `feature`
- Enables/disables features.
- Shape:
```json
{ "name": "feature", "enable": [ "Feature.Id" ], "disable": [ "Feature.Id" ] }
```

## `themes`
- Sets site and admin theme IDs.
- Shape:
```json
{ "name": "themes", "site": "MyTheme", "admin": "TheAdmin" }
```

## `settings`
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

## `recipes`
- Executes other recipes by name.
- Shape:
```json
{ "name": "recipes", "Values": [ { "executionid": "MyApp", "name": "My.Recipe.Name" } ] }
```
