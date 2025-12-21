# Tag Helpers - Media

Tag helpers for media library paths and image resizing.

## `<img asset-src="...">`
- Purpose: Resolve a media library path to a public URL.
- Attributes:
  - `asset-src` (media path)
  - `asp-append-version` (bool)
- Example:
```cshtml
<img asset-src="/media/hero.jpg" asp-append-version="true" />
```

## `<a asset-href="...">`
- Purpose: Resolve a media library path to a public URL.
- Attributes:
  - `asset-href` (media path)
  - `asp-append-version` (bool)
- Example:
```cshtml
<a asset-href="/media/file.pdf">Download</a>
```

## `<img img-width="..." img-height="..." img-resize-mode="..." img-quality="..." img-format="..." img-profile="..." img-anchor="..." img-bgcolor="...">`
- Purpose: Apply image resizing to an existing `src`.
- Attributes (prefix `img-`):
  - `img-width`, `img-height`, `img-resize-mode`, `img-quality`
  - `img-format`, `img-profile`, `img-anchor`, `img-bgcolor`
- Example:
```cshtml
<img src="/media/hero.jpg" img-width="800" img-resize-mode="Crop" />
```
