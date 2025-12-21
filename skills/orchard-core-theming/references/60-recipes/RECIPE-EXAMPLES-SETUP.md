# Recipe Examples - Setup

Use these as starting points for setup recipes.

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
