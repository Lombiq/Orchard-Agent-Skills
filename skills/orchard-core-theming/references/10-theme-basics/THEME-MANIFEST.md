# Theme Manifest

## Manifest file
- Theme manifest lives in `Manifest.cs`.
- Look for a `Theme` attribute with metadata like `Name`, `Description`, and `BaseTheme`.
- `BaseTheme` indicates theme inheritance; child themes can override base theme templates.
- Admin themes are tagged with `Tags = new[] { "admin" }` and typically set `BaseTheme = "TheAdmin"`.
