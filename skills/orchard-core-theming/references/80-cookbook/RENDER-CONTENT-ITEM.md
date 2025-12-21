# Render a Content Item

Quick paths; for full workflow see `20-shapes-placement/SHAPE-WORKFLOW.md`.

## Liquid
- By ID:
```liquid
{{ Content.ContentItemId["<id>"] | shape_build_display: "Detail" | shape_render }}
```
- From current model:
```liquid
{{ Model.ContentItem | shape_build_display: "Summary" | shape_render }}
```

## Razor
```csharp
@using OrchardCore.ContentManagement.Display
@inject IContentItemDisplayManager DisplayManager
@{
    var shape = await DisplayManager.BuildDisplayAsync(Model.ContentItem, "Detail");
}
@await DisplayAsync(shape)
```

- Pick the display type (`Detail`, `Summary`, or custom).
- Ensure definitions exist (see `40-content-model/CONTENT-DEFINITIONS.md`).

See also: `40-content-model/CONTENT-ITEMS.md`, `40-content-model/FIELDS.md`, `40-content-model/PARTS.md`, `40-content-model/CONTAINERS.md`.
