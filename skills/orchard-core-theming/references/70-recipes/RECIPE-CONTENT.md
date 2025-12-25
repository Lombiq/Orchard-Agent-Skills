# Recipe Content Import

Use the `content` step to import content items as JSON.
Each item is a full `ContentItem` record, including parts and fields.

## Basic structure
```json
{
  "name": "content",
  "data": [
    {
      "ContentItemId": "[js:uuid()]",
      "ContentItemVersionId": "[js:uuid()]",
      "ContentType": "Page",
      "DisplayText": "Home",
      "Published": true,
      "Latest": true,
      "CreatedUtc": "2024-01-01T00:00:00Z",
      "ModifiedUtc": "2024-01-01T00:00:00Z",
      "PublishedUtc": "2024-01-01T00:00:00Z",
      "Owner": "admin",
      "Author": "admin",

      "TitlePart": { "Title": "Home" },
      "AutoroutePart": {
        "Path": "home",
        "SetHomepage": true,
        "Disabled": false,
        "RouteContainedItems": false,
        "Absolute": false
      },
      "HtmlBodyPart": {
        "Html": "<p>Welcome</p>"
      }
    }
  ]
}
```
Notes:
- Some recipes use `Data` instead of `data`. Prefer lowercase `data` for consistency.
- The properties under each part match the part/field models in the content model docs.

## Fields and parts
- Use the exact part name as the property name (e.g., `TitlePart`).
- Fields live under their part:
```
<PartName>.<FieldName>.<FieldProperty>
```
- Field properties are in `50-content-model/FIELDS.md` (e.g., `TextField.Text`, `NumericField.Value`).
- Part properties are in `50-content-model/PARTS.md`.

## Referencing other content items
Use variables and IDs when content items reference each other:
```json
{
  "variables": { "pageId": "[js:uuid()]" },
  "steps": [
    {
      "name": "content",
      "data": [
        {
          "ContentItemId": "[js:variables('pageId')]",
          "ContentType": "Page",
          "TitlePart": { "Title": "Example" }
        },
        {
          "ContentType": "Landing",
          "MyPickerField": { "ContentItemIds": [ "[js:variables('pageId')]" ] }
        }
      ]
    }
  ]
}
```

## Content definitions vs content items
- `ContentDefinition` defines the shape of types and parts.
- `content` imports actual items and uses that definition.
- Ensure definitions exist before importing items.
- Cross-reference: `50-content-model/CONTENT-DEFINITIONS.md`.

## FlowPart and BagPart examples
- FlowPart embeds widgets under `FlowPart.Widgets[]` with `FlowMetadata`:
```json
{
  "FlowPart": {
    "Widgets": [
      {
        "ContentItemId": "widget0001",
        "ContentType": "HtmlWidget",
        "TitlePart": { "Title": "Intro" },
        "HtmlBodyPart": { "Html": "<p>Hello</p>" },
        "FlowMetadata": { "Alignment": "Justify", "Size": 100 }
      }
    ]
  }
}
```
- BagPart embeds items under `BagPart.ContentItems[]`:
```json
{
  "BagPart": {
    "ContentItems": [
      {
        "ContentItemId": "faqitem1",
        "ContentType": "FaqItem",
        "TitlePart": { "Title": "Q1" },
        "MarkdownBodyPart": { "Markdown": "Answer." }
      }
    ]
  }
}
```
- Ensure contained item definitions exist and match the parts/fields you populate.
