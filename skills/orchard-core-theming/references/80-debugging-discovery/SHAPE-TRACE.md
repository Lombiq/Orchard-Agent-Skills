# Shape Tracing

Fast ways to learn which shape is rendering and which alternates are available.

## Quick trace in Liquid
- Temporarily log metadata: `{{ Model.Metadata | json | console_log }}`.
- Log alternates: `{{ Model.Metadata.Alternates | json | console_log }}`.
- Remove logging after discovery to avoid noisy output.

## Quick trace in Razor
- Inspect type/alternates:
```csharp
@{
    var meta = Model.Metadata;
    <text>Type: @meta.Type</text>
    foreach (var alt in meta.Alternates) { <text>Alt: @alt</text> }
}
```
- Serialize the model in development only if needed:
```csharp
@* for debugging only *@
@System.Text.Json.JsonSerializer.Serialize(Model)
```

## Content item JSON
- If a content item object is available, the ContentItem.Content can be treated as a JSON object, render it in Liquid or Razor when needed.

## Placement and selection hints
- Placement uses shape type + differentiator; confirm differentiator value by logging `Model.Metadata.Differentiator`.
- Enable detailed logs for `OrchardCore.DisplayManagement` in development to see template binding choices.

## Cleanup
- Remove debug code and reduce logging once you know the target shape/alternate.
