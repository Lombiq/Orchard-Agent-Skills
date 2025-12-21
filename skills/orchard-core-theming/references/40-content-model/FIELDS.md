# Fields

## Access pattern
Fields are stored under their parent part:
```
ContentItem.Content.<PartName>.<FieldName>.<FieldProperty>
```
If a field is attached directly to the content type (not via a named part),
the part name equals the content type.

## Shared settings
All field settings derive from `FieldSettings`:
- `Hint`
- `Required`

## Field types (built-in)

### BooleanField
- Value: `Value` (bool)
- Settings: `BooleanFieldSettings` (`Label`, `DefaultValue`)
- Example:
```
ContentItem.Content.MyPart.Featured.Value
```

### TextField
- Value: `Text` (string)
- Settings: `TextFieldSettings` (`DefaultValue`, `Type`, `Pattern`, `Placeholder`)
  - `Type`: `Editable`, `GeneratedDisabled`, `GeneratedHidden`
- Editor options (affects data and display expectations):
  - Standard: plain text input; `Text` holds the string.
  - `TextArea`: multiline input; `Text` holds the string.
  - `PredefinedList`: `TextFieldPredefinedListEditorSettings` (`Options`, `Editor`, `DefaultValue`); `Text` is the selected option value.
  - `IconPicker`: `Text` is typically a Font Awesome class (e.g., `fas fa-home`) to use in `<i class="...">`.
  - `Color`: `Text` is a color string (e.g., `#ffffff`).
  - `Email`, `Tel`, `Url`: specialized inputs; `Text` is the email/phone/url.
  - `Header`: header-style input; `Text` is the heading; see display mode below.
  - `CodeMirror`: code editor; `Text` is the code; uses CodeMirror UI.
  - `Monaco`: code editor; `Text` is the code; `TextFieldMonacoEditorSettings` (`Options`).
- Display modes:
  - `TextFieldHeaderDisplaySettings` (`Level`) for header display mode (e.g., template alternate `TextField-Header.Display`).
- Example:
```
ContentItem.Content.MyPart.Title.Text
```

### HtmlField
- Value: `Html` (string)
- Settings: `HtmlFieldSettings` (`SanitizeHtml`)
- Editor options:
  - Standard: simple HTML textarea.
  - `Trumbowyg` (`HtmlFieldTrumbowygEditorSettings`):
    - `Options` (JSON string passed to Trumbowyg).
    - `InsertMediaWithUrl` (bool).
    - Lean toolbar example (less bloat, keeps `removeformatPasted`):
      ```json
      {
        "autogrow": true,
        "removeformatPasted": true,
        "btns": [
          ["viewHTML"],
          ["undo","redo"],
          ["formatting"],
          ["strong","em","del"],
          ["fontsize"],
          ["link"],
          ["align"],
          ["unorderedList","orderedList"],
          ["removeformat"]
        ],
        "btnsDef": {
          "align": {
            "dropdown": ["justifyLeft","justifyCenter","justifyRight","justifyFull"],
            "ico": "justifyLeft"
          }
        }
      }
      ```
  - `Monaco` (`HtmlFieldMonacoEditorSettings`): `Options`.
- Example:
```
ContentItem.Content.MyPart.Body.Html
```

### NumericField
- Value: `Value` (decimal?)
- Settings: `NumericFieldSettings` (`Scale`, `Minimum`, `Maximum`, `Placeholder`, `DefaultValue`)
- Example:
```
ContentItem.Content.MyPart.Price.Value
```

### DateField
- Value: `Value` (DateTime?)
- Settings: `DateFieldSettings` (inherits base only)
- Example:
```
ContentItem.Content.MyPart.PublishDate.Value
```

### DateTimeField
- Value: `Value` (DateTime?)
- Settings: `DateTimeFieldSettings` (inherits base only)
- Example:
```
ContentItem.Content.MyPart.EventTime.Value
```

### TimeField
- Value: `Value` (TimeSpan?)
- Settings: `TimeFieldSettings` (`Step`)
- Example:
```
ContentItem.Content.MyPart.OpeningTime.Value
```

### MultiTextField
- Value: `Values` (string[])
- Settings: `MultiTextFieldSettings` (`Options[]` with `Name`, `Value`, `Default`)
- Editor options:
  - Standard: free text entries into `Values`.
  - `CheckboxList`: renders options as checkboxes; selected option values stored in `Values`.
  - `Picker`: renders a picker UI; selected option values stored in `Values`.
- Example:
```
ContentItem.Content.MyPart.Tags.Values
```

### LinkField
- Values: `Url`, `Text`, `Target`
- Settings: `LinkFieldSettings` (`HintLinkText`, `LinkTextMode`, `UrlPlaceholder`,
  `TextPlaceholder`, `DefaultUrl`, `DefaultText`, `DefaultTarget`)
  - `LinkTextMode`: `Optional`, `Required`, `Static`, `Url`
- Example:
```
ContentItem.Content.MyPart.CTA.Url
ContentItem.Content.MyPart.CTA.Text
```

### ContentPickerField
- Values: `ContentItemIds` (string[])
- Settings: `ContentPickerFieldSettings`
  - `Multiple`, `DisplayAllContentTypes`, `DisplayedContentTypes`,
    `DisplayedStereotypes`, `Placeholder`, `TitlePattern`
- Example:
```
ContentItem.Content.MyPart.Related.ContentItemIds
```

### LocalizationSetContentPickerField
- Values: `LocalizationSets` (string[])
- Settings: `LocalizationSetContentPickerFieldSettings` (`Multiple`, `DisplayedContentTypes`)
- Example:
```
ContentItem.Content.MyPart.RelatedLocalization.LocalizationSets
```

### UserPickerField
- Values: `UserIds` (string[])
- Settings: `UserPickerFieldSettings` (`Multiple`, `DisplayAllUsers`, `DisplayedRoles`, `Placeholder`)
- Example:
```
ContentItem.Content.MyPart.Authors.UserIds
```

### YoutubeField
- Values: `RawAddress`, `EmbeddedAddress`
- Settings: `YoutubeFieldSettings` (`Label`, `Width`, `Height`, `Placeholder`)
- Example:
```
ContentItem.Content.MyPart.Video.EmbeddedAddress
```

### MediaField
- Values: `Paths` (string[]), `MediaTexts` (string[])
- Settings: `MediaFieldSettings` (`Multiple`, `AllowMediaText`, `AllowAnchors`, `AllowedExtensions`)
- Example:
```
ContentItem.Content.MyPart.Image.Paths
```

### TaxonomyField
- Values: `TaxonomyContentItemId`, `TermContentItemIds` (string[])
- Settings: `TaxonomyFieldSettings` (`TaxonomyContentItemId`, `Unique`, `LeavesOnly`, `Open`, `Placeholder`)
- Editor settings: `TaxonomyFieldTagsEditorSettings` (`Open`)
- Example:
```
ContentItem.Content.MyPart.Categories.TermContentItemIds
```
- Getting taxonomy/terms:
  - Razor: `var taxonomy = await Orchard.GetContentItemByIdAsync(field.TaxonomyContentItemId);`
  - The taxonomy tree is embedded under `taxonomy.Content.TaxonomyPart.Terms` as term content items (not separately stored in the DB).
  - Selected term IDs are in `TermContentItemIds` (string[]). Match them against the embedded terms tree (e.g., recursive filter where `ContentItemId` is in `TermContentItemIds`).
  - Liquid: assign the taxonomy content item from the ID (`{% assign tax = Content.ContentItemId[field.TaxonomyContentItemId] %}`), then iterate `tax.Content.TaxonomyPart.Terms` and filter by `TermContentItemIds` to get selected terms.
