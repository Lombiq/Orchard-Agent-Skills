# Recipe Examples - Content Packages

Use these as starting points for content packages.

## Content package with FlowPart and BagPart
```json
{
  "name": "My.ContentPackage",
  "displayName": "Sample Content Package",
  "steps": [
    {
      "name": "ContentDefinition",
      "ContentTypes": [
        {
          "Name": "LandingPage",
          "DisplayName": "Landing Page",
          "Settings": { "ContentTypeSettings": { "Creatable": true, "Listable": true, "Draftable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "TitlePart", "Name": "TitlePart" },
            { "PartName": "AutoroutePart", "Name": "AutoroutePart" },
            { "PartName": "FlowPart", "Name": "FlowPart" }
          ]
        },
        {
          "Name": "CalloutWidget",
          "DisplayName": "Callout Widget",
          "Settings": { "ContentTypeSettings": { "Stereotype": "Widget", "Creatable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "TitlePart", "Name": "TitlePart" },
            { "PartName": "HtmlBodyPart", "Name": "HtmlBodyPart" }
          ]
        },
        {
          "Name": "FaqList",
          "DisplayName": "FAQ List",
          "Settings": { "ContentTypeSettings": { "Creatable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "BagPart", "Name": "BagPart", "Settings": { "BagPartSettings": { "ContainedContentTypes": [ "FaqItem" ] } } }
          ]
        },
        {
          "Name": "FaqItem",
          "DisplayName": "FAQ Item",
          "Settings": { "ContentTypeSettings": { "Creatable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "TitlePart", "Name": "TitlePart" },
            { "PartName": "MarkdownBodyPart", "Name": "MarkdownBodyPart" }
          ]
        }
      ]
    },
    {
      "name": "content",
      "data": [
        {
          "ContentItemId": "landing000000000000000000000001",
          "ContentType": "LandingPage",
          "DisplayText": "Landing",
          "Published": true,
          "Latest": true,
          "TitlePart": { "Title": "Landing" },
          "AutoroutePart": { "Path": "landing" },
          "FlowPart": {
            "Widgets": [
              {
                "ContentItemId": "callout00000000000000000000001",
                "ContentType": "CalloutWidget",
                "DisplayText": "Callout",
                "Latest": true,
                "Published": true,
                "TitlePart": { "Title": "Callout" },
                "HtmlBodyPart": { "Html": "<h3>Callout</h3><p>Details.</p>" },
                "FlowMetadata": { "Alignment": "Justify", "Size": 100 }
              }
            ]
          }
        },
        {
          "ContentItemId": "faqlist0000000000000000000001",
          "ContentType": "FaqList",
          "DisplayText": "FAQs",
          "Published": true,
          "Latest": true,
          "BagPart": {
            "ContentItems": [
              {
                "ContentItemId": "faqitem000000000000000000001",
                "ContentType": "FaqItem",
                "DisplayText": "Question 1",
                "Published": true,
                "Latest": true,
                "TitlePart": { "Title": "What is this?" },
                "MarkdownBodyPart": { "Markdown": "Sample answer." }
              }
            ]
          }
        }
      ]
    }
  ]
}
```
Notes:
- `FlowPart.Widgets` items carry `FlowMetadata` for layout hints (Alignment, Size).
- `BagPart.ContentItems` embeds contained items directly; they must match definitions (here `FaqItem`).
- Use deterministic IDs in content packages when other items reference them.
