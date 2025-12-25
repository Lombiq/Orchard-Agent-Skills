# Recipe Steps - Other Common Steps

Other steps that do not fit the main categories.

## `Layers`
- Defines display layers with rules.
- Shape:
```json
{ "name": "Layers", "Layers": [ { "Name": "Homepage", "Rule": "isHomepage()" } ] }
```

## `Placements`
- Updates placement rules.
- Shape:
```json
{ "name": "Placements", "Placements": { "TextField": [ { "place": "Content:1" } ] } }
```

## `AdminMenu`
- Creates/updates admin menu structure.

## `Sitemaps`
- Creates/updates sitemaps.

## `UrlRewriting`
- Creates/updates URL rewrite rules.

## `custom-settings`
- Updates custom settings content items stored in the site settings bag.
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
- Cross-reference: `50-content-model/CONTENT-ITEMS.md`.

## Tenants
- `FeatureProfiles` for tenant feature profile definitions.
