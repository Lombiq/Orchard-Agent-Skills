# Solution Structure

This section captures where to find the core pieces of a typical Orchard Core solution.
Keep it generic and use it as a checklist for discovery in any repo.

## Repository layout (typical)
- `src/`: application code.
  - `src/Modules/`: Orchard Core modules.
  - `src/Themes/`: Orchard Core themes.
  - `src/Libraries/`: shared libraries that are not Orchard Core extensions.
  - `src/Utilities/`: optional utilities or support projects.
- `test/`: automated tests and UI testing projects.
- `tools/`: repo tooling (analyzers, scripts, build helpers).
- `node_modules/`: JS tooling dependencies (if front-end tooling is used).

## Host web project (the running app)
Look for the primary `*.Web` project under `src/`. Typical contents:
- `appsettings*.json`: environment settings and Orchard configuration.
- `Program.cs`: application startup.
- `wwwroot/`: static assets, but typically not used, because assets comes from the themes and modules.
- `App_Data/`: tenant data, logs, and runtime state, see below.
- `NLog.config` (or other logging config).

## App_Data for understanding the state of the app and tenants after setup
- `App_Data/logs/`: logs, useful for debugging runtime errors, help the user with providing errors found here when needed.
- `App_Data/tenants.json`: tenant registry; keys are tenant names with values like `TenantId`, `VersionId`, `RequestUrlPrefix`, `State`.
- `App_Data/Sites/<TenantName>/`: tenant-specific storage.
  - `appsettings.json`: per-tenant settings.
  - `Media/`: media files for local development environments.
  - `DataProtection-Keys/`: data protection keys.
  - SQLite database files (e.g., `OrchardCore.db`) when using file-based providers.
  - optional `ContentDefinition.json` when definitions are stored to file, use this to understand the active content types on the tenant before doing work with content items

## Auto-setup when user wants to skip the setup screen
In `appsettings.Development.json` (or other environment files), check:
```
OrchardCore:OrchardCore_AutoSetup:Tenants[]
```
Each tenant typically includes:
- `ShellName`
- `SiteName`
- `SiteTimeZone`
- `AdminUsername`, `AdminEmail`, `AdminPassword`
- `DatabaseProvider`, `DatabaseConnectionString`, `DatabaseTablePrefix`
- `RecipeName`
- optional `RequestUrlHost`, `RequestUrlPrefix`, `FeatureProfile`

## Recipes
Recipes convey data, configuration, content items, content types either during setup or when needed. Recipes can be located in:
- `HostProject/Recipes/` (common but not required).
- `ModuleOrTheme/Recipes/` (custom or sample recipes)
- `ModuleOrTheme/Migrations/Recipes/`
- Test projects may also include recipes for automation.
Built outputs may contain `bin/.../Migrations/Recipes` folders; ignore these for source edits.

## Content definitions (optional file storage)
If present, `ContentDefinition.json` provides the content type/part/field definitions
for a tenant and is useful for understanding ContentItem shape data.

