# Tag Helpers - Caching

Tag helpers for dynamic caching and cache dependencies.

## `<dynamic-cache cache-id="...">`
- Purpose: Cache rendered output with dynamic invalidation.
- Attributes:
  - `cache-id` (required)
  - `vary-by`, `dependencies`
  - `expires-on`, `expires-after`, `expires-sliding`
  - `enabled` (bool)
- Example:
```cshtml
<dynamic-cache cache-id="home-hero" vary-by="culture">
  ...
</dynamic-cache>
```

## `<cache-dependency dependency="...">`
- Purpose: Add a cache dependency inside a cache scope.
- Example:
```cshtml
<cache-dependency dependency="contentitem:123" />
```
