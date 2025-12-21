# Add Scripts/Styles to a Section

## Steps
1) Define the resource in a manifest or use a static file path (see `50-assets-resources/RESOURCES.md` and `50-assets-resources/STATIC-FILES.md`).
2) Require it in the correct location:
   - Razor: `<style asp-name="MyTheme" at="Head"></style>` or `<script asp-name="MyTheme" at="Foot"></script>`.
   - Direct file: `<style asp-src="~/MyTheme/styles/extra.css" at="Head"></style>`.
3) If only needed for a specific shape or page, add the tag helper inside that shape/template.
4) Verify the resource renders once (resource manager dedupes by name).

## Source refs
- Resource manager: `50-assets-resources/RESOURCES.md`
- Tag helpers: `30-razor/TAG-HELPERS-RESOURCES.md`

