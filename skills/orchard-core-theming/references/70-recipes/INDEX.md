# Recipes

Purpose: Author, validate, and reuse recipes for setup, definitions, and content import.

Files:
- `RECIPE-STEPS.md` - step groups and common first steps.
- `RECIPE-STEPS-CORE.md` - `feature`, `themes`, `settings`, and `recipes` steps.
- `RECIPE-STEPS-DEFINITIONS.md` - `ContentDefinition`, `ReplaceContentDefinition`, `DeleteContentDefinition`.
- `RECIPE-STEPS-CONTENT-MEDIA.md` - `content`, `media`, and `MediaProfiles` steps.
- `RECIPE-STEPS-SEARCH.md` - `Queries`, Lucene (index/reset/rebuild), Elastic (index/reset/rebuild), Azure AI Search, index profile steps.
- `RECIPE-STEPS-SECURITY.md` - `Roles`, `Users`, custom user settings, OpenID/external auth, social providers.
- `RECIPE-STEPS-MISC.md` - `Layers`, `Placements`, `AdminMenu`, `Sitemaps`, `UrlRewriting`, `custom-settings`, tenants.
- `RECIPE-STEPS-TEMPLATES-WORKFLOWS.md` - `Templates`, `AdminTemplates`, `ShortcodeTemplates`, `WorkflowType`.
- `RECIPE-CONTENT.md` - content import structure, fields/parts, references, definitions vs items, Flow/Bag examples.
- `RECIPE-COMMANDS.md` - command step shape, known commands, discovery, and when to use vs `Users`.
- `RECIPE-EXAMPLES.md` - ready-to-copy examples.
- `RECIPE-EXAMPLES-SETUP.md` - minimal setup recipe and a page example with Summary/Autoroute settings.
- `RECIPE-EXAMPLES-CONTENT.md` - content package example with FlowPart and BagPart.
- `FEATURE-CATALOG.md` - common feature IDs (full list in `FEATURE-CATALOG-ALL.md`).
- `FEATURE-CATALOG-ALL.md` - full feature ID list.
- `BASE-RECIPES.md` - base setup recipes (Blank, Headless) and when to reuse.

## Where recipes live
- `*/Recipes/*.recipe.json`: reusable recipes in modules/themes.
- `*/Migrations/*.recipe.json`: recipes used by data migrations.
- `HostProject/Recipes/`: optional, common location for setup recipes.

## Top-level schema
```json
{
  "name": "My.Recipe.Name",
  "displayName": "My Recipe",
  "description": "What this recipe does",
  "author": "Org",
  "website": "https://example.com",
  "version": "1.0",
  "issetuprecipe": true,
  "tags": [ "setup", "content" ],
  "variables": {
    "homeId": "[js:uuid()]"
  },
  "steps": [
    { "name": "feature", "enable": [ "OrchardCore.Contents" ] }
  ]
}
```

## Recipe helpers (inline values)
- `js`: execute JavaScript expressions (for example, `"[js:uuid()]"`).
- `file`: load file contents (for example, `"[file:text('Snippets/page.liquid')]"`).
- `env`: read environment variables (for example, `"[env:MY_VAR]"`).
- `appsettings`: read configuration values (for example, `"[appsettings:OrchardCore:SiteName]"`).
- `localization`: read localized strings (for example, `"[localization:WelcomeTitle]"`).
- `base64`, `html`, `gzip`: decode content.

## Execution and composition
- Use the `recipes` step to include other recipes by `name`.
- Order matters; definitions and settings should usually come before content.
- Setup recipes (`issetuprecipe: true`) are available during tenant setup and AutoSetup.
