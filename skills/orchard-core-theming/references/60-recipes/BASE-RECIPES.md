# Base Setup Recipes (Orchard Core)

Canonical setup recipes shipped with Orchard Core that can be referenced or mimicked.

## Blank (full CMS skeleton)
- File: `src/OrchardCore.Themes/TheAdmin/Recipes/blank.recipe.json`
- Purpose: Blank CMS-ready site with admin, content management, media, flows, lists, templates, widgets, etc.
- Key features enabled:
  - SaaS/admin: `OrchardCore.HomeRoute`, `OrchardCore.Admin`, `OrchardCore.Diagnostics`, `OrchardCore.DynamicCache`, `OrchardCore.Features`, `OrchardCore.Navigation`, `OrchardCore.Recipes`, `OrchardCore.Resources`, `OrchardCore.Roles`, `OrchardCore.Security`, `OrchardCore.Settings`, `OrchardCore.Themes`, `OrchardCore.Users`
  - Content: `OrchardCore.Alias`, `OrchardCore.Autoroute`, `OrchardCore.Html`, `OrchardCore.ContentFields`, `OrchardCore.ContentPreview`, `OrchardCore.Contents`, `OrchardCore.ContentTypes`, `OrchardCore.CustomSettings`, `OrchardCore.Deployment`, `OrchardCore.Deployment.Remote`, `OrchardCore.Flows`, `OrchardCore.Indexing`, `OrchardCore.Layers`, `OrchardCore.Lists`, `OrchardCore.Markdown`, `OrchardCore.Media`, `OrchardCore.Menu`, `OrchardCore.Queries`, `OrchardCore.Shortcodes.Templates`, `OrchardCore.Title`, `OrchardCore.Templates`, `OrchardCore.Widgets`
  - Theme: `TheAdmin` as admin theme; site theme left empty.
- Roles scaffolded: Moderator, Editor, Author, Contributor (no permissions assigned by default).

## Headless (API-first)
- File: `src/OrchardCore.Themes/TheAdmin/Recipes/headless.recipe.json`
- Purpose: Headless CMS with GraphQL and OpenID enabled; admin home route.
- Key features enabled:
  - SaaS/admin: same core set as Blank (minus DynamicCache), plus GraphQL and OpenID server/validation.
  - Content: similar to Blank (HTML/Markdown/Flows/Lists/Media/Queries/Widgets), plus `OrchardCore.Apis.GraphQL`.
  - OpenID: `OrchardCore.OpenId`, `OrchardCore.OpenId.Management`, `OrchardCore.OpenId.Server`, `OrchardCore.OpenId.Validation`.
  - Theme: `TheAdmin` as admin theme; site theme left empty.
- Roles: Moderator, Editor, Author, Contributor, and `Authenticated` with `ViewContent`, `ExecuteGraphQL`, `ExecuteApiAll`.
- Settings: HomeRoute set to Admin dashboard.

## When to reuse
- Use Blank as a "full CMS scaffold" for most sites; copy feature list or reference it in your setup recipe.
- Use Headless when API/GraphQL/OpenID are required; copy its features/roles and home route.
- Both are setup recipes (`issetuprecipe: true`); you can reference them via the `recipes` step or copy their feature blocks into your own setup recipe.
- Example (reference Blank directly from TheAdmin):
  ```json
  {
    "name": "recipes",
    "Values": [
      { "executionid": "TheAdmin", "name": "Blank" }
    ]
  }
  ```
- `executionid` must match the extension containing the recipe.
- If you want to keep composition local (host project), create a wrapper recipe in your project that references `TheAdmin` and then reference the wrapper by your project name.
