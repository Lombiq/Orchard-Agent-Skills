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
- When you need direct field access on contained items in Liquid, use `item.PartName.Field` (no `.Content` prefix).
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
 - FlowPart adds widget classes. These are the exact class patterns:
   - `widget`
   - `widget-<contenttype>` (content type HTML-classified, ex: `widget-input`)
   - `widget-align-left`, `widget-align-center`, `widget-align-right`, `widget-align-justify`, `widget-align-inherit`
   - `widget-size-25`, `widget-size-33`, `widget-size-50`, `widget-size-66`, `widget-size-75`, `widget-size-100`
   - Sizes are integers and can be any value, but FlowPart UI usually sets the above defaults.
   - If you override widget templates, render `Model.Classes` on the wrapper or you lose sizing/alignment metadata.

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
