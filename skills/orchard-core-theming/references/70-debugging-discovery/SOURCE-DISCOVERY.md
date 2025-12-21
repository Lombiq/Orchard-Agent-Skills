# Source Discovery

Use ripgrep to find definitions quickly in the Orchard Core source.

## What to search
- Display drivers for shapes: look for `DisplayDriver` implementations.
- Shape attributes and templates: search for `ShapeAttribute`.
- Recipe steps: `IRecipeStepHandler` and `RecipeStep` classes.
- Liquid filters/tags: `ILiquidFilter` / `ILiquidTag`.
- Tag helpers: `TagHelper` classes in modules and themes.

## Suggested `rg` queries
- `rg \"DisplayDriver\" src/OrchardCore.*`
- `rg \"ShapeAttribute\" src/OrchardCore.*`
- `rg \"class .*RecipeStep\" src/OrchardCore.*`
- `rg \"ILiquidFilter\" src/OrchardCore.*`
- `rg \"TagHelper\" src/OrchardCore.*`
- `rg \"ResourceManifest\" src/OrchardCore.*` (find resource registrations)
