# Recipe Steps - Content Definitions

Steps that add, replace, or delete content type/part/field definitions.

## `ContentDefinition`
- Adds or updates content types/parts (merge style).
- Shape:
```json
{ "name": "ContentDefinition", "ContentTypes": [ ... ], "ContentParts": [ ... ] }
```
- Use `ContentTypeSettings` for type-level flags (Creatable, Draftable, Listable, Stereotype).
- Attach parts via `ContentTypePartDefinitionRecords`; add fields inside `ContentPartFieldDefinitionRecords`.
- Part/field settings mirror `ContentDefinition.json` (see `40-content-model/CONTENT-DEFINITIONS.md`); use the extractor for existing definitions.

## `ReplaceContentDefinition`
- Replaces content definitions (delete then recreate).
- Shape:
```json
{ "name": "ReplaceContentDefinition", "ContentTypes": [ ... ], "ContentParts": [ ... ] }
```

## `DeleteContentDefinition`
- Deletes content types/parts by name.
- Shape:
```json
{ "name": "DeleteContentDefinition", "ContentTypes": [ "Type" ], "ContentParts": [ "Part" ] }
```
