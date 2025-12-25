# Recipe Steps - Queries and Search

Steps for queries and search index configuration.

## `Queries`
- Defines queries (Lucene/SQL/etc).
- Shape:
```json
{ "name": "Queries", "Queries": [ { "Name": "Recent", "Source": "Lucene", ... } ] }
```

## `lucene-index`
- Creates/updates Lucene indexes.
- Shape:
```json
{ "name": "lucene-index", "Indices": [ { "Search": { ... } } ] }
```

## `lucene-index-reset` / `lucene-index-rebuild`
- Reset or rebuild specific Lucene indexes.
- Shape:
```json
{ "name": "lucene-index-reset", "Indices": [ "Search" ] }
{ "name": "lucene-index-rebuild", "Indices": [ "Search" ] }
```

## `ElasticIndexSettings`
- Creates/updates Elasticsearch indexes.
- Shape:
```json
{ "name": "ElasticIndexSettings", "Indices": [ { "Search": { ... } } ] }
```

## `elastic-index-reset` / `elastic-index-rebuild`
- Reset or rebuild Elasticsearch indexes.

## `CreateOrUpdateIndexProfile`
- Creates/updates index profiles across providers.
- Shape:
```json
{ "name": "CreateOrUpdateIndexProfile", "Indexes": [ { "Name": "Search", "ProviderName": "Lucene", ... } ] }
```

## `ResetIndex` / `RebuildIndex`
- Reset/rebuild index profiles by name or include all.
- Shape:
```json
{ "name": "ResetIndex", "IncludeAll": true }
{ "name": "RebuildIndex", "IndexNames": [ "Search" ] }
```

## Azure AI Search
- `azureai-index-create`, `azureai-index-reset`, `azureai-index-rebuild`
- Used to manage Azure AI Search indexes.
