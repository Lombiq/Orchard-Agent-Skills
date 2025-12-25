# Feature Catalog (Orchard Core feature IDs)

Feature IDs to use in recipes (`feature` step) or module enables. Module = feature name unless additional `[Feature]` attributes are defined.

## Commonly used (setup/themes/content)
- `OrchardCore.Setup`
- `OrchardCore.Themes`
- `OrchardCore.Contents`
- `OrchardCore.ContentTypes`
- `OrchardCore.ContentFields`
- `OrchardCore.Flows`
- `OrchardCore.Lists`
- `OrchardCore.Media`
- `OrchardCore.Navigation` (menus)
- `OrchardCore.Layers` (widgets on rules)
- `OrchardCore.Localization` (+ `OrchardCore.ContentLocalization`)
- `OrchardCore.Taxonomies`
- `OrchardCore.Sitemaps`
- `OrchardCore.Shortcodes`
- `OrchardCore.Queries` (core) + provider (e.g., `OrchardCore.Queries.Sql`, `OrchardCore.Search.Lucene`)
- `OrchardCore.Resources` (resource management)
- `OrchardCore.Html`, `OrchardCore.Markdown`
- `OrchardCore.Title`, `OrchardCore.Alias`, `OrchardCore.Autoroute`
- `OrchardCore.Users`, `OrchardCore.Roles` (Users base feature is implicit with security packages)
- `OrchardCore.Admin`, `OrchardCore.AdminMenu`
- `OrchardCore.Seo`
- `OrchardCore.Tenants` (multi-tenant scenarios)
- `OrchardCore.Deployment` (export/import plans)
- `OrchardCore.Workflows` (+ `OrchardCore.Workflows.Http`)

## Full list
- See `FEATURE-CATALOG-ALL.md`.
