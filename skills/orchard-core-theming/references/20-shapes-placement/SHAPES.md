# Shapes Overview

## What is a shape
- A shape is a renderable object with metadata and properties (often dynamic).
- Shapes are rendered via templates (Razor or Liquid) and resolved using alternates.

## When to create shapes
- Prefer shapes over MVC partials for UI composition and theming.
- Shapes can be invoked from other shapes using the `<shape>` tag helper (Razor) or `shape_render`/`shape` tags (Liquid).

## Determining the shape model
- If the view model is unclear, find where the shape is created or invoked to see which properties are passed.
- If that fails, treat it as a Content Item shape (see `40-content-model/CONTENT-ITEMS.md`) or ask for the expected model.

## Shape lifecycle (high level)
- Creation -> metadata/alternates -> placement -> rendering.

## Finding shape data
- Inspect the driver/tag helper/Liquid invocation that created the shape to see what properties are set.
- If unsure, log `Model.Metadata.Alternates` and `Model` (Liquid `| console_log`, Razor serialize in dev) to learn the model.
- Content item shapes usually expose `ContentItem`, `ContentItem.Content`, and the part/field being rendered; see `40-content-model/CONTENT-ITEMS.md`.
