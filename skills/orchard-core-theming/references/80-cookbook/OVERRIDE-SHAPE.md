# Override a Shape

## Steps
1) Identify the shape type and alternates in use (`70-debugging-discovery/SHAPE-TRACE.md`).
2) Choose the most specific alternate (`20-shapes-placement/ALTERNATES.md`).
3) Create the template in the active theme (Razor: `Views/<ShapeName>.cshtml` using `-` for `__`; Liquid: `Views/<ShapeName>.liquid`).
4) If targeting a content type/part/field, add placement to scope the override (`20-shapes-placement/PLACEMENT.md`).
5) Verify by reloading and checking alternates again. For end-to-end shape steps see `20-shapes-placement/SHAPE-WORKFLOW.md`.

## Source refs
- Alternates: `20-shapes-placement/ALTERNATES.md`
- Placement: `20-shapes-placement/PLACEMENT.md`
