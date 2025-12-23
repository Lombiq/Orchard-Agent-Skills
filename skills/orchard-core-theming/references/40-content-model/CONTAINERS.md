# Containers: BagPart, FlowPart, ListPart

How Orchard Core stores and renders contained items.

## BagPart
- Data: embeds items under `ContentItem.Content.<PartName>.ContentItems` (array of full `ContentItem` objects).
- Shape: `BagPart` with a differentiator matching the part name.
- Render (Liquid):
```liquid
{% for item in Model.ContentItems %}
  {{ item | shape_build_display: "Detail" | shape_render }}
{% endfor %}
```
- Render (Razor):
```csharp
@using OrchardCore.ContentManagement.Display
@inject IContentItemDisplayManager DisplayManager
@foreach (var item in Model.ContentItems)
{
    var shape = await DisplayManager.BuildDisplayAsync(item, "Detail");
    @await DisplayAsync(shape);
}
```
- Placement differentiator: the part name (e.g., `ContentPart` rules use `BagPartName`).
- If a content type just needs a wrapper (Page with sections), render `@await DisplayAsync(Model.Content)` in the content template and let the default BagPart render; override `BagPart` only for custom item-level markup.

## FlowPart
- Data: `ContentItem.Content.<PartName>.Widgets` with `FlowMetadata` (Alignment, Size).
- Shape: `FlowPart` renders widgets in order; widgets are just content items.
- Custom rendering:
  - Access `Model.Widgets` (already shapes in display mode) or rebuild like BagPart.
  - Use `FlowMetadata.Size` to apply grid classes if the base theme uses them.
  - To change layout rules globally, override the `FlowPart` shape.
 - Typical usage: FlowPart is meant for Widget stereotypes. It is usually rendered as part of
   `@await DisplayAsync(Model.Content)`; manual rendering is rare compared to BagPart.

## ListPart and ContainedPart
- ListPart stores no items; items live as regular content items with `ContainedPart`.
- `ContainedPart` properties: `ListContentItemId`, `ListContentType`, `Order`.
- The `ListPart` display shape usually queries contained items and renders them as a list.
- Custom rendering:
  - Override `ListPart` shape to change listing markup.
  - Use placement on `ListPart` (`differentiator` is the part name) to move/hide.
  - If you need direct access to contained items, query by `ContainedPart.ListContentItemId`.

## Quick placement patterns
- Bag/Flow/List part shapes: `BagPart`, `FlowPart`, `ListPart` (add display type suffix as needed).
- Differentiator is the part name: target with placement `differentiator: "<PartName>"`.
- Widget/contained item alternates still follow content-type rules (see `20-shapes-placement/ALTERNATES.md`).
