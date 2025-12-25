# Glossary

## Content model
- Content item: A single document of a content type, versioned and localizable, often with its own URL.
- Content item version: One version of a content item (draft, published, or past).
- Content type: The definition of parts and fields that make up a content item (like a class for items).
- Content part: A reusable unit of content or behavior attached to content types.
- Content field: A named piece of data attached to a content type or part; multiple fields of the same kind can exist.
- Display type: Rendering context for a content element (e.g., `Detail`, `Summary`, `SummaryAdmin`).
- Stereotype: A classification used by modules to decide which content types they operate on (e.g., Menu, Widget).
- Bag: A collection of content items embedded in a parent content item.
- List: A list of content items referenced by a parent container.
- Flow: A page layout that contains widgets (typically via FlowPart).
- Widget: A content item with the `Widget` stereotype, rendered in a zone and layer.
- Tenant: An independent subsite with its own URL and configuration.

## Theming
- Theme: A module with views and assets that define site display; can include a setup recipe.
- Shape: A renderable object with metadata (type, alternates, differentiator) and properties, rendered by a template.
- Template: A Razor or Liquid file that renders a shape or display type.
- Alternate: A more specific template name Orchard tries when rendering a shape (e.g., `Content__Article`).
- Placement: Rules in `placement.json` that control where and how a shape renders, including alternates and wrappers.
- Zone: A layout region (e.g., Footer) where shapes render.
- Layer: A display condition that determines when something renders (e.g., `isHomepage()`).
- Assets: Theme static files under `wwwroot`; in admin, this refers to the Media library.
- Resource: A registered script/style library with versioning and optional minified/CDN urls.
- Liquid: A template language used in themes and templates as an alternative to Razor.
- Razor: The `.cshtml` view engine used for templates.

## Recipes and setup
- Recipe: A JSON file with steps that configure or import data.
- Setup recipe: A recipe executed during setup (e.g., set theme, define types, import data).
- Recipe step: One named step within a recipe.
