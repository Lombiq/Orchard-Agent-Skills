# Forms widgets (OrchardCore.Forms)

Purpose: implement and override Form widgets in themes and recipes without breaking FlowPart layout
or losing form metadata.

## Source of truth (Orchard Core)
- Module: `src/OrchardCore.Modules/OrchardCore.Forms`
- Feature id: `OrchardCore.Forms` (Manifest.cs). Depends on `OrchardCore.Widgets` and `OrchardCore.Flows`.
- Content types (Migrations.cs): `Form`, `Input`, `TextArea`, `Select`, `Button`, `Label`,
  `ValidationSummary`, `Validation` (all Stereotype: `Widget`).
- Default display templates:
  - `Views/Form.Wrapper.cshtml` (form wrapper, renders `<form>` + child content)
  - `Views/Items/InputPart.cshtml`, `SelectPart.cshtml`, `TextAreaPart.cshtml`
  - `Views/Items/ButtonPart.cshtml`
  - `Views/Items/FormElementLabelPart.cshtml`
  - `Views/Items/FormElementValidationPart.cshtml`
  - `Views/Items/ValidationSummaryPart.cshtml`

## Recipe checklist
- Enable the feature in setup recipe:
  - `OrchardCore.Forms` (also pulls Widgets/Flows dependencies).
- Add a `Form` widget to the page/container (BagPart or FlowPart).
  - BagPart: include `Form` in `ContainedContentTypes`.
- The Form widget contains a `FlowPart` with child form element widgets.
- Use `FlowMetadata` on each widget for size/alignment.
  - Alignment is `FlowAlignment` (Left/Center/Right/Justify/Inherit) serialized as numbers.
  - Export from admin to capture correct numeric values.

## Rendering strategy (Liquid)
- Override the widget templates for form elements:
  - `Views/Widget__Form.liquid`
  - `Views/Widget__Input.liquid`
  - `Views/Widget__Select.liquid`
  - `Views/Widget__TextArea.liquid`
  - `Views/Widget__Button.liquid`
  - `Views/Widget__ValidationSummary.liquid` (if needed)
- Label and validation are separate parts. Render them explicitly in the widget templates:
  - `Model.Content.FormElementLabelPart`
  - `Model.Content.FormElementValidationPart`
  - `Model.Content.InputPart` / `SelectPart` / `TextAreaPart` / `ButtonPart`

Example pattern (Input widget):
```liquid
{% assign widget_classes = Model.Classes | join: " " | strip %}

<div class="form-field{% if widget_classes != blank %} {{ widget_classes }}{% endif %}">
  {% if Model.Content.FormElementLabelPart %}
    {{ Model.Content.FormElementLabelPart | shape_render }}
  {% endif %}
  {% if Model.Content.InputPart %}
    {{ Model.Content.InputPart | shape_render }}
  {% endif %}
  {% if Model.Content.FormElementValidationPart %}
    {{ Model.Content.FormElementValidationPart | shape_render }}
  {% endif %}
</div>
```

## Keep FlowPart logic intact
- `FlowPart` adds classes and runs authorization checks per widget.
- If you override `Widget__Form`, do NOT loop `FlowPart.Widgets` manually.
  Render the content zone instead so FlowPart can do its work:
```liquid
{% assign widget_classes = Model.Classes | join: " " | strip %}
{% if widget_classes != blank %}
  <div class="{{ widget_classes }}">
    {{ Model.Content | shape_render }}
  </div>
{% else %}
  {{ Model.Content | shape_render }}
{% endif %}
```

## FlowPart classes and layout
- `OrchardCore.Flows/Views/FlowPart.cshtml` adds sizing/alignment classes to each widget shape.
- See `50-content-model/CONTAINERS.md` for the exact class list and size variants to style.
- Always apply `Model.Classes` on widget wrappers to preserve sizing/alignment metadata.
- The FlowPart wrapper renders `<section class="flow">`. Style `.flow` and the widget classes
  to get the desired grid or flex layout.

## Form wrapper override
- `FormContentDisplayDriver` adds wrapper `Form_Wrapper__{ContentType}` for display type Detail.
- Default wrapper (`Form.Wrapper.cshtml`) builds the `<form>` element and anti-forgery token.
- If you override it, keep `FormPart` fields (`Action`, `Method`, `EncType`,
  `EnableAntiForgeryToken`, `SaveFormLocation`) and render child content.

## Content type collisions
- OrchardCore.Forms defines a widget content type named `Button`.
- Avoid naming your own content type `Button`; rename it (for example, `ActionButton`).
