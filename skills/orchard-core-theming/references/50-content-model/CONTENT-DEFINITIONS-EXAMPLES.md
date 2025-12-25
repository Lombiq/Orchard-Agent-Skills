# Content Definition Examples

Large reference examples. Load only when you need working JSON patterns.

## Examples from a real tenant (anonymized)
- Page with FlowPart and Autoroute:
```json
{
  "Name": "Page",
  "Settings": { "ContentTypeSettings": { "Creatable": true, "Listable": true, "Draftable": true, "Versionable": true, "Securable": true } },
  "ContentTypePartDefinitionRecords": [
    { "PartName": "TitlePart", "Name": "TitlePart", "Settings": { "ContentTypePartSettings": { "Position": "0" } } },
    {
      "PartName": "AutoroutePart",
      "Name": "AutoroutePart",
      "Settings": {
        "ContentTypePartSettings": { "Position": "1" },
        "AutoroutePartSettings": { "AllowCustomPath": true, "Pattern": "{{ ContentItem.DisplayText | slugify }}", "ShowHomepageOption": true }
      }
    },
    { "PartName": "FlowPart", "Name": "FlowPart", "Settings": { "ContentTypePartSettings": { "Position": "2" } } }
  ]
}
```
- Widget with FlowPart:
```json
{
  "Name": "ContainerWidget",
  "Settings": { "ContentTypeSettings": { "Stereotype": "Widget", "Securable": true } },
  "ContentTypePartDefinitionRecords": [
    { "PartName": "TitlePart", "Name": "TitlePart", "Settings": { "ContentTypePartSettings": { "Position": "0" } } },
    { "PartName": "FlowPart", "Name": "FlowPart", "Settings": { "ContentTypePartSettings": { "Position": "1" } } }
  ]
}
```
- Form widget with TitlePart, FormElementPart, FormPart, FlowPart:
```json
{
  "Name": "Form",
  "Settings": { "ContentTypeSettings": { "Stereotype": "Widget" } },
  "ContentTypePartDefinitionRecords": [
    { "PartName": "TitlePart", "Name": "TitlePart", "Settings": { "TitlePartSettings": { "RenderTitle": false }, "ContentTypePartSettings": { "Position": "0" } } },
    { "PartName": "FormElementPart", "Name": "FormElementPart", "Settings": { "ContentTypePartSettings": { "Position": "1" } } },
    { "PartName": "FormPart", "Name": "FormPart", "Settings": {} },
    { "PartName": "FlowPart", "Name": "FlowPart", "Settings": {} }
  ]
}
```
- Part with fields (ContentPicker, Text fields):
```json
{
  "Name": "ContentItemWidget",
  "ContentPartFieldDefinitionRecords": [
    {
      "FieldName": "ContentPickerField",
      "Name": "ContentToDisplay",
      "Settings": {
        "ContentPartFieldSettings": { "DisplayName": "Content to display" },
        "ContentPickerFieldSettings": { "Multiple": true, "DisplayAllContentTypes": true, "TitlePattern": "{{ Model.ContentItem | display_text }}" }
      }
    },
    { "FieldName": "TextField", "Name": "DisplayType", "Settings": { "ContentPartFieldSettings": { "DisplayName": "Display type" } } },
    { "FieldName": "TextField", "Name": "GroupId", "Settings": { "ContentPartFieldSettings": { "DisplayName": "Group ID" } } }
  ]
}
```

## Example: Case Study type (with editors)
```json
{
  "ContentTypeDefinitionRecords": [
    {
      "Name": "CaseStudy",
      "DisplayName": "Case Study",
      "Settings": {
        "ContentTypeSettings": {
          "Creatable": true,
          "Listable": true,
          "Draftable": true,
          "Versionable": true,
          "Securable": true
        }
      },
      "ContentTypePartDefinitionRecords": [
        {
          "PartName": "TitlePart",
          "Name": "TitlePart",
          "Settings": { "ContentTypePartSettings": { "Position": "0" } }
        },
        {
          "PartName": "AutoroutePart",
          "Name": "AutoroutePart",
          "Settings": {
            "ContentTypePartSettings": { "Position": "1" },
            "AutoroutePartSettings": {
              "AllowCustomPath": true,
              "AllowUpdatePath": true,
              "Pattern": "{{ ContentItem.DisplayText | slugify }}"
            }
          }
        },
        { "PartName": "CaseStudy", "Name": "CaseStudy", "Settings": { "ContentTypePartSettings": { "Position": "2" } } }
      ]
    }
  ],
  "ContentPartDefinitionRecords": [
    {
      "Name": "CaseStudy",
      "ContentPartFieldDefinitionRecords": [
        {
          "FieldName": "HtmlField",
          "Name": "Body",
          "Settings": {
            "ContentPartFieldSettings": { "DisplayName": "Body", "Editor": "Trumbowyg", "Position": "0" },
            "HtmlFieldSettings": { "SanitizeHtml": true },
            "HtmlFieldTrumbowygEditorSettings": {
              "Options": "{ \"autogrow\": true, \"removeformatPasted\": true, \"btns\": [[\"viewHTML\"],[\"undo\",\"redo\"],[\"formatting\"],[\"strong\",\"em\",\"del\"],[\"fontsize\"],[\"link\"],[\"align\"],[\"unorderedList\",\"orderedList\"],[\"removeformat\"]], \"btnsDef\": { \"align\": { \"dropdown\": [\"justifyLeft\",\"justifyCenter\",\"justifyRight\",\"justifyFull\"], \"ico\": \"justifyLeft\" } } }",
              "InsertMediaWithUrl": false
            }
          }
        },
        {
          "FieldName": "UserPickerField",
          "Name": "Owner",
          "Settings": {
            "ContentPartFieldSettings": { "DisplayName": "Owner", "Position": "1" },
            "UserPickerFieldSettings": { "Multiple": false, "DisplayAllUsers": true, "DisplayedRoles": [] }
          }
        },
        {
          "FieldName": "TaxonomyField",
          "Name": "Tags",
          "Settings": {
            "ContentPartFieldSettings": { "DisplayName": "Tags", "Editor": "Tags", "Position": "2" },
            "TaxonomyFieldSettings": { "TaxonomyContentItemId": "<replace-with-taxonomy-id>", "LeavesOnly": false, "Unique": false, "Open": true, "DisplayAllNodes": true, "Required": false },
            "TaxonomyFieldTagsEditorSettings": { "Open": true }
          }
        }
      ]
    }
  ]
}
```
