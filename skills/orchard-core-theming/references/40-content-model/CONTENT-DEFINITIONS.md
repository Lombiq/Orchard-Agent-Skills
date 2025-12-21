# Content Definitions

`ContentDefinition.json` is a tenant-scoped snapshot of content type, part, and field definitions.
It lives under `App_Data/Sites/<TenantName>/` when file storage is enabled.

## Top-level structure
- `ContentTypeDefinitionRecords`: all content types and the parts attached to them.
- `ContentPartDefinitionRecords`: reusable part definitions and their fields.
- `Identifier`: internal identifier for the definitions document.

## Content type records
Each `ContentTypeDefinitionRecord` includes:
- `Name`, `DisplayName`
- `Settings`: usually includes `ContentTypeSettings` (Creatable, Draftable, Stereotype, etc.).
- `ContentTypePartDefinitionRecords`: attached parts and their settings.

Each `ContentTypePartDefinitionRecord` includes:
- `PartName`: the part's technical name.
- `Name`: the part instance name (often same as `PartName`).
- `Settings`: usually includes `ContentTypePartSettings` plus part-specific settings.

## Part records
Each `ContentPartDefinitionRecord` includes:
- `Name`
- `Settings`: usually includes `ContentPartSettings`.
- `ContentPartFieldDefinitionRecords`: fields attached to this part.

Each `ContentPartFieldDefinitionRecord` includes:
- `FieldName`: field type (e.g., `TextField`).
- `Name`: field instance name.
- `Settings`: includes `ContentPartFieldSettings` plus field-specific settings.

## Field and part settings
- Shared settings:
  - `ContentTypeSettings`, `ContentPartSettings`, `ContentTypePartSettings`, `ContentPartFieldSettings`.
- Field-specific settings:
  - Stored under `<FieldType>Settings` plus optional editor-specific settings.
- Part-specific settings:
  - Stored under `<PartType>Settings` or similar.
- For type-scoped parts used only as a field container (e.g., part name matches the content type),
  omit `ContentPartSettings.Attachable` unless you want it to show as a reusable part.

## Access pattern from ContentItem
The JSON structure maps directly to `ContentItem.Content`:
```
ContentItem.Content.<PartName>.<FieldName>.<FieldProperty>
```
Example:
```
ContentItem.Content.BlogPost.Summary.Html
```

### Fields on the content type itself
If a field is attached directly to the content type (not via a named part),
it is stored on a part named exactly like the content type:
```
ContentItem.Content.<ContentType>.<FieldName>.<FieldProperty>
```

## How to use this file
- Identify which parts and fields exist for a type.
- Read settings to know editor/display behavior and validation.
- Use the field type to determine which property holds the value (see `FIELDS.md`).
Examples: see `CONTENT-DEFINITIONS-EXAMPLES.md`.

## Editing tips (JSON)
- Types live under `ContentTypes`, parts under `ContentParts`. Attach parts via `ContentTypePartDefinitionRecords`.
- Stereotypes matter for shape names (e.g., `"Stereotype": "Widget"` -> `Widget-<Type>`; `"Stereotype": "MenuItem"` for menu items).
- Set editors/display modes via field settings:
  - TextField example with IconPicker:
    ```json
    {
      "FieldName": "TextField",
      "Name": "Icon",
      "Settings": {
        "ContentPartFieldSettings": { "DisplayName": "Icon", "Editor": "IconPicker" },
        "TextFieldSettings": { "Hint": "Pick an icon" }
      }
    }
    ```
  - HtmlField with Trumbowyg (lean toolbar):
    ```json
    {
      "FieldName": "HtmlField",
      "Name": "Body",
      "Settings": {
        "ContentPartFieldSettings": { "DisplayName": "Body", "Editor": "Trumbowyg" },
        "HtmlFieldSettings": { "SanitizeHtml": true },
        "HtmlFieldTrumbowygEditorSettings": {
          "Options": "{ \"autogrow\": true, \"removeformatPasted\": true, \"btns\": [[\"viewHTML\"],[\"undo\",\"redo\"],[\"formatting\"],[\"strong\",\"em\",\"del\"],[\"fontsize\"],[\"link\"],[\"align\"],[\"unorderedList\",\"orderedList\"],[\"removeformat\"]], \"btnsDef\": { \"align\": { \"dropdown\": [\"justifyLeft\",\"justifyCenter\",\"justifyRight\",\"justifyFull\"], \"ico\": \"justifyLeft\" } } }"
        }
      }
    }
    ```
- Keep `Position` strings ordered if present; they control editor tab order.
- For fields directly on the type, use the type name as the part name in `ContentPartFieldDefinitionRecords`.


