# Shape Build Workflow (Checklist)

Use this to build/override a shape safely (e.g., `TextAndImage` section).

## 1) Identify content type and tenant
- If `ContentDefinition.json` exists: find the tenant folder under `App_Data/Sites/<TenantName>/` that matches the active theme/site.
- Locate the content type and note:
- `Stereotype` (Widget, Section, etc.) - drives base shape name.
  - Parts attached, and fields on those parts.
  - Field types and settings (see `40-content-model/FIELDS.md`).

## 2) Determine template name
- Base on stereotype:
  - Use the stereotype value as the prefix (e.g., `Widget` -> `Widget-<ContentType>`, `Section` -> `Section-<ContentType>`, `Block` -> `Block-<ContentType>`).
  - Default content -> `Content-<ContentType>`
- Add display type if needed: `Content-<Type>.Summary.cshtml` (or `.liquid`).
- Alternates patterns: see `20-shapes-placement/ALTERNATES.md`.
- If unsure, check `ContentDefinition.json` for `ContentTypeSettings.Stereotype` before creating the template.

## 3) Map fields to properties
- Use the field type to know the value property (see `40-content-model/FIELDS.md`):
  - `TextField.Text`
  - `MediaField.Paths[]` and `MediaTexts[]`
  - etc.
- Access pattern in Razor: `Model.ContentItem.Content.<Part>.<Field>.<Property>`.
- For fields on the type itself, the part name equals the type name.

## 4) Render helpers (Razor/Liquid)
- These are examples; for other field types use `40-content-model/FIELDS.md` and the tag/helper catalogs.
- Media (Razor, MediaField first path):
  ```cshtml
  @{
      var imgPath = (string)(Model.ContentItem.Content.PartName.Image.Paths?[0]);
  }
  <img asset-src="@imgPath" asp-append-version="true" alt="">
  ```
- Media (Liquid):
  ```liquid
  {% assign img = Model.ContentItem.Content.PartName.Image.Paths[0] %}
  <img src="{{ img | asset_url | resize_url: width: 1200 }}" alt="">
  ```
- Text field (Razor): `@Model.ContentItem.Content.PartName.Text.Text`
- Text field (Liquid): `{{ Model.ContentItem.Content.PartName.Text.Text }}`
- Other fields: see `40-content-model/FIELDS.md` for the property to use (e.g., NumericField.Value, BooleanField.Value, LinkField.Url/Text/Target, TaxonomyField.TermContentItemIds, ContentPickerField.ContentItemIds, etc.).
- Use `<shape>` or `shape_render` to embed other shapes if needed.
- Helper catalogs:
  - Tag helpers: `30-templating/TAG-HELPERS.md`
  - Liquid tags/filters: `30-templating/LIQUID-TAGS.md`, `30-templating/LIQUID-FILTERS.md`
  - Orchard helper extensions: `30-templating/ORCHARD-HELPER.md`
- Editor-aware rendering:
- Check `40-content-model/FIELDS.md` for editor options that affect data shape (notably TextField editors like `IconPicker` -> Font Awesome class; `PredefinedList` -> selected option value). HtmlField renders `Html` regardless of editor flavor.

- When overriding a content item template and you just want a wrapper, prefer `@await DisplayAsync(Model.Content)` and let parts (including BagPart) render with their own templates.
- Override `BagPart` only when you need custom item-level markup (e.g., FAQ accordion).

## 5) Placement and differentiator
- If scoping to a specific instance/part, use placement with `differentiator` (see `PLACEMENT.md`).
- For Section/Widget stereotypes, alternates often suffice without placement changes.

## 6) Validate (manual checks)
- Optional debugging when values look wrong/missing:
  - Liquid: `{{ Model.Metadata.Alternates | json | console_log }}` and `{{ Model.ContentItem | json | console_log }}` to the browser console.
  - Razor: temporarily render a `<pre>` with `Model.Metadata.Type`, `Model.Metadata.Alternates`, or `System.Text.Json.JsonSerializer.Serialize(Model.ContentItem)`.
  - Remove these snippets after verifying to keep output clean.
- Verify the target display types you care about (`Detail`, `Summary`, etc.).

