# Recipe Steps - Content and Media

Steps that import content items and media assets.

## `content`
- Imports content items.
- Shape:
```json
{ "name": "content", "data": [ { "ContentType": "Page", ... } ] }
```
- Tips:
  - Ensure content types/parts/fields exist before import (see `ContentDefinition`).
  - Use variables for IDs referenced across steps.
  - For Flow/Bag/List items, include embedded content items with their parts/fields.

## `media`
- Imports media from file, base64, or URL.
- Shape:
```json
{ "name": "media", "Files": [ { "TargetPath": "img/logo.png", "SourcePath": "../wwwroot/img/logo.png" } ] }
```
- `SourcePath` is relative to the recipe file; include files in `Recipes/Media/` beside the recipe.

## `MediaProfiles`
- Creates/updates media profiles.
- Shape:
```json
{ "name": "MediaProfiles", "MediaProfiles": { "MyProfile": { ... } } }
```
