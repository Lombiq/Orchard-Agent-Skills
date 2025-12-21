# Recipe Examples (Ready-to-Copy)

Use these as starting points for setup and content packages. Adjust names/IDs as needed.

## Minimal setup recipe (single tenant)
```json
{
  "name": "My.Setup",
  "displayName": "My Site Setup",
  "issetuprecipe": true,
  "variables": {
    "homeId": "[js:uuid()]",
    "articleId": "[js:uuid()]",
    "imageId": "[js:uuid()]"
  },
  "steps": [
    { "name": "feature", "enable": [ "OrchardCore.Setup", "OrchardCore.Themes", "OrchardCore.Contents", "OrchardCore.ContentTypes", "OrchardCore.Flows", "OrchardCore.Media" ] },
    { "name": "themes", "site": "MyTheme", "admin": "TheAdmin" },
    {
      "name": "settings",
      "SiteName": "My Orchard Site",
      "TimeZoneId": "UTC",
      "ResourceDebugMode": "FromConfiguration",
      "AppendVersion": true,
      "HomeRoute": { "Area": "OrchardCore.Contents", "Action": "Display", "ContentItemId": "[js:variables('homeId')]" }
    },
    {
      "name": "ContentDefinition",
      "ContentTypes": [
        {
          "Name": "Page",
          "DisplayName": "Page",
          "Settings": { "ContentTypeSettings": { "Creatable": true, "Listable": true, "Draftable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "TitlePart", "Name": "TitlePart" },
            { "PartName": "AutoroutePart", "Name": "AutoroutePart", "Settings": { "AutoroutePartSettings": { "AllowCustomPath": true } } },
            { "PartName": "HtmlBodyPart", "Name": "HtmlBodyPart" }
          ]
        }
      ]
    },
    {
      "name": "content",
      "data": [
        {
          "ContentItemId": "[js:variables('homeId')]",
          "ContentType": "Page",
          "DisplayText": "Home",
          "Published": true,
          "Latest": true,
          "TitlePart": { "Title": "Home" },
          "AutoroutePart": { "Path": "home", "SetHomepage": true },
          "HtmlBodyPart": { "Html": "<p>Welcome to Orchard Core.</p>" }
        },
        {
          "ContentItemId": "[js:variables('articleId')]",
          "ContentType": "Page",
          "DisplayText": "Article",
          "Published": true,
          "Latest": true,
          "TitlePart": { "Title": "Article" },
          "AutoroutePart": { "Path": "article" },
          "HtmlBodyPart": { "Html": "<p>Example content.</p><p><img src=\"{{ '~/media/uploads/hero.jpg' | href }}\" alt=\"Hero\"></p>" }
        }
      ]
    },
    {
      "name": "media",
      "Files": [
        { "SourcePath": "Recipes/Media/hero.jpg", "TargetPath": "uploads/hero.jpg" }
      ]
    },
    {
      "name": "Roles",
      "Roles": [
        { "Name": "Editor", "Description": "Site editor", "Permissions": [ "EditContent", "PublishContent" ] }
      ]
    }
  ]
}
```
Notes:
- `SourcePath` is relative to the recipe file location; include media files in a `Recipes/Media/` folder next to the recipe.
- Ensure the `ContentDefinition` matches the parts/fields you use in `content`.
- `HomeRoute` must reference a content item ID present in the same recipe.

## Page with Summary HtmlField and full Autoroute options
```json
{
  "steps": [
    {
      "name": "ContentDefinition",
      "ContentTypes": [
        {
          "Name": "Page",
          "DisplayName": "Page",
          "Settings": { "ContentTypeSettings": { "Creatable": true, "Listable": true, "Draftable": true } },
          "ContentTypePartDefinitionRecords": [
            { "PartName": "TitlePart", "Name": "TitlePart" },
            {
              "PartName": "AutoroutePart",
              "Name": "AutoroutePart",
              "Settings": {
                "AutoroutePartSettings": {
                  "AllowCustomPath": true,
                  "Pattern": "{{ ContentItem.DisplayText | slugify }}",
                  "ShowHomepageOption": true,
                  "AllowUpdatePath": true,
                  "AllowDisabled": true,
                  "AllowRouteContainedItems": true,
                  "ManageContainedItemRoutes": true,
                  "AllowAbsolutePath": true
                }
              }
            },
            { "PartName": "Page", "Name": "Page" }
          ]
        }
      ],
      "ContentParts": [
        {
          "Name": "Page",
          "ContentPartFieldDefinitionRecords": [
            {
              "FieldName": "HtmlField",
              "Name": "Summary",
              "Settings": {
                "ContentPartFieldSettings": { "DisplayName": "Summary", "Editor": "Trumbowyg" },
                "HtmlFieldSettings": { "SanitizeHtml": true },
                "HtmlFieldTrumbowygEditorSettings": {
                  "Options": "{ \"autogrow\": true, \"removeformatPasted\": true, \"btns\": [[\"viewHTML\"],[\"undo\",\"redo\"],[\"formatting\"],[\"strong\",\"em\",\"del\"],[\"fontsize\"],[\"link\"],[\"align\"],[\"unorderedList\",\"orderedList\"],[\"removeformat\"]], \"btnsDef\": { \"align\": { \"dropdown\": [\"justifyLeft\",\"justifyCenter\",\"justifyRight\",\"justifyFull\"], \"ico\": \"justifyLeft\" } } }"
                }
              }
            }
          ]
        }
      ]
    },
    {
      "name": "content",
      "data": [
        {
          "ContentType": "Page",
          "DisplayText": "Home",
          "Published": true,
          "Latest": true,
          "TitlePart": { "Title": "Home" },
          "AutoroutePart": { "Path": "home", "SetHomepage": true },
          "Page": { "Summary": { "Html": "<p>Summary text.</p>" } }
        }
      ]
    }
  ]
}
```

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
