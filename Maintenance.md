# Maintenance Guide

Purpose: keep `skills/orchard-core-theming` aligned with the latest Orchard Core source. Use this when a new Orchard Core version is released.

## Step-by-step update workflow

1. Choose the target Orchard Core version (tag).
   - Determine the new tag in `D:\Repos\OrchardCore`.
   - If no baseline version is recorded, use the last tag used in the previous update commit or pick the prior stable tag as the baseline for diffing.

2. Prepare a clean Orchard Core snapshot.
   - Use a worktree or a new branch so you do not disturb local changes.
   - Example (PowerShell):
     ```powershell
     cd D:\Repos\OrchardCore
     git fetch --tags
     git worktree add ..\OrchardCore-vX.Y.Z vX.Y.Z
     ```

3. Scan for changes that affect theming and recipes.
   - Compare the baseline tag to the new tag:
     ```powershell
     cd D:\Repos\OrchardCore
     git diff <old-tag>..<new-tag> -- src/OrchardCore.*
     ```
   - Use this diff to target which reference files need updates first.

4. Update Razor references (`skills/orchard-core-theming/references/30-razor/`).
   - Tag helpers: scan for new or changed tag helpers in source and update `TAG-HELPERS-*.md`.
     ```powershell
     rg "TagHelper" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Tag helper names and attributes are usually on classes with `HtmlTargetElement` and public properties. Add/remove entries to match the current source.
   - IOrchardHelper: scan for extension methods and update `ORCHARD-HELPER.md`.
     ```powershell
     rg "IOrchardHelper" D:\Repos\OrchardCore\src -g "*.cs"
     ```

5. Update Liquid references (`skills/orchard-core-theming/references/40-liquid/`).
   - Liquid tags: scan for `ILiquidTag` implementations and update `LIQUID-TAGS.md`.
     ```powershell
     rg "ILiquidTag" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Liquid filters: scan for `ILiquidFilter` implementations and update `LIQUID-FILTERS.md`.
     ```powershell
     rg "ILiquidFilter" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - If the Liquid base syntax changes, update `LIQUID.md` accordingly.

6. Update shapes and placement (`skills/orchard-core-theming/references/20-shapes-placement/`).
   - Scan for shape drivers and shape attributes to spot new shape types or renamed alternates.
     ```powershell
     rg "ShapeAttribute" D:\Repos\OrchardCore\src -g "*.cs"
     rg "DisplayDriver" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Review module views and templates in `src/OrchardCore.*` for shape type changes and update `SHAPES.md`, `ALTERNATES.md`, `PLACEMENT.md`, and `SHAPE-WORKFLOW.md`.
   - Menu and pager shapes: check `OrchardCore.Menu` and `OrchardCore.Navigation` modules for shape types and update `MENU-SHAPES.md` and `PAGER-SHAPES.md`.

7. Update content model references (`skills/orchard-core-theming/references/50-content-model/`).
   - Content parts: scan for classes deriving from `ContentPart` and update `PARTS.md`.
     ```powershell
     rg "class .*Part\\s*:\\s*ContentPart" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Content fields: scan for classes deriving from `ContentField` and update `FIELDS.md`.
     ```powershell
     rg "class .*Field\\s*:\\s*ContentField" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Settings objects: scan for `*Settings` types used by parts/fields and update `SETTINGS.md`.
     ```powershell
     rg "class .*Settings" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Containers: verify Flow/Bag/List parts in source and update `CONTAINERS.md` if behaviors or properties changed.

8. Update assets and resources (`skills/orchard-core-theming/references/60-assets-resources/`).
   - Scan for `ResourceManifest` usage to validate built-in resources and update `RESOURCES.md`.
     ```powershell
     rg "ResourceManifest" D:\Repos\OrchardCore\src -g "*.cs"
     ```

9. Update recipes (`skills/orchard-core-theming/references/70-recipes/`).
   - Recipe steps: scan for step handlers and update `RECIPE-STEPS*.md`.
     ```powershell
     rg "RecipeStep" D:\Repos\OrchardCore\src -g "*.cs"
     rg "IRecipeStepHandler" D:\Repos\OrchardCore\src -g "*.cs"
     ```
   - Base recipes: review `src/OrchardCore.Themes/TheAdmin/Recipes/*.recipe.json` and update `BASE-RECIPES.md`.
   - Feature catalog: re-scan `Manifest.cs` files for features and update `FEATURE-CATALOG.md` and `FEATURE-CATALOG-ALL.md`.
     ```powershell
     rg "Feature\\(" D:\Repos\OrchardCore\src -g "Manifest.cs"
     ```
   - Re-validate recipe examples and step names in `RECIPE-EXAMPLES-*.md` and `RECIPE-CONTENT.md`.

10. Update debugging and discovery (`skills/orchard-core-theming/references/80-debugging-discovery/`).
    - Confirm shape tracing and logging guidance still matches the current features and logging categories.
    - Update `SOURCE-DISCOVERY.md` if new search patterns or interfaces are introduced.

11. Update glossary (`skills/orchard-core-theming/references/90-glossary/`).
    - Add or update glossary terms if new concepts appear in source or docs.

12. Keep navigation and maps accurate.
    - If you add or move reference files, update `skills/orchard-core-theming/references/TASK-MAP.md`.
    - Update `skills/orchard-core-theming/references/INDEX.md` to reflect any new files or sections.

13. Final consistency pass.
    - Verify that all file references resolve and stay one level deep from `SKILL.md`.
    - Preserve existing content unless a change is deliberate and documented in the update commit message.
    - Keep files ASCII-only unless the file already uses Unicode and it is required.

## Notes

- If the Orchard Core repo includes breaking changes between the two tags, prioritize updating reference files that are derived directly from source (`30-razor/`, `40-liquid/`, `70-recipes/`, `50-content-model/`).
- If new workflows are added, make sure the task map points directly to leaf reference files.
