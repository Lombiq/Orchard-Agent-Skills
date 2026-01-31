# Liquid Tags

This is a source-derived catalog of Liquid tags commonly used for Orchard Core theme work.
Liquid tag arguments are typically snake_case (e.g., `append_version`, `cache_id`).

**Layout and sections**
- `{% layout "LayoutName" %}`: set the view layout. Example: `{% layout "Layout" %}`
- `{% render_body %}`: render the main `Content` zone.
- `{% render_section "ZoneName", required: true %}`: render a zone by name. Example: `{% render_section "Header" %}`
- `{% page_title "Segment", position: "0", separator: " - " %}`: render full page title.
- `{% page_title_add_segment "Segment", position: "0" %}`: add a title segment only.
- `{% antiforgerytoken %}`: render a hidden anti-forgery input.

**Shapes (rendering)**
- `{% shape type: "Card", title: "Hi" %}`: render a shape; extra args become properties. Use the internal shape type,
  not the file name. File name mapping: `-` -> `__`, `.` -> `_`. E.g. `Component-Header.cshtml` renders as
  `Component__Header` and `Content-Page.Summary.cshtml` renders as `Content_Summary__Page`.
- `{% contentitem content_item: Model.ContentItem %}`: render a content item shape.
- `{% zone "Header", position: "1" %}...{% endzone %}`: add content to a zone.

**Shapes (metadata and manipulation)**
- `{% shape_add_alternates shape, "Alt1 Alt2" %}`: add alternates.
- `{% shape_clear_alternates shape %}`: clear alternates.
- `{% shape_add_wrappers shape, "Wrapper1 Wrapper2" %}`: add wrappers.
- `{% shape_clear_wrappers shape %}`: clear wrappers.
- `{% shape_add_classes shape, "class1 class2" %}`: add CSS classes.
- `{% shape_clear_classes shape %}`: clear classes.
- `{% shape_add_attributes shape, data_id: "42" %}`: add HTML attributes (underscores become dashes).
- `{% shape_clear_attributes shape %}`: clear attributes.
- `{% shape_type shape, "MyType" %}`: set shape type.
- `{% shape_display_type shape, "Summary" %}`: set display type.
- `{% shape_position shape, "1" %}`: set position.
- `{% shape_tab shape, "Content" %}`: set editor tab.
- `{% shape_cache shape, cache_id: "id", cache_tag: "tag", cache_context: "ctx" %}`: set cache metadata.
- `{% shape_add_properties shape, title: "Hi" %}`: set properties.
- `{% shape_remove_property shape, "Title" %}`: remove a property.
- `{% shape_remove_item shape, "MyItem" %}`: remove an item from a `Shape`.
- `{% shape_pager shape, classes: "a b", item_classes: "x y" %}`: customize pager properties.

**Anchors and tag helpers**
- `{% a action: "Index", controller: "Home" %}Home{% enda %}`: route-based anchor.
- `{% a route: "MyRoute", route_id: "42" %}Link{% enda %}`: route-name anchor with `route_*`.
- `{% form method: "post", asp_action: "Save" %}...{% endform %}`: call a Razor tag helper for `<form>`.
- `{% helper "input", asp_for: "Model.Name", class: "form-control" %}`: call any tag helper.
- `{% block "textarea", asp_for: "Model.Body" %}...{% endblock %}`: tag helpers with block content.

**Resources**
- `{% script name: "bootstrap", at: "Foot" %}`: require a script resource.
- `{% script src: "~/theme/app.js", append_version: true %}`: include a script URL.
- `{% scriptblock name: "app", at: "Foot" %}...{% endscriptblock %}`: inline script block.
- `{% style name: "site", at: "Head" %}`: require a style resource.
- `{% style src: "~/theme/site.css", append_version: true %}`: include a style URL.
- `{% styleblock name: "site", at: "Head" %}...{% endstyleblock %}`: inline style block.
- `{% meta name: "description", content: "..." %}`: register meta tags.
- `{% link src: "~/favicon.ico", rel: "icon" %}`: register link tags.
- `{% resources type: "Stylesheet" %}`: render registered resources.

**Caching**
- `{% cache "id", vary_by: "culture", dependencies: "contentitem:123", expires_after: "00:01:00" %}...{% endcache %}`
- `{% cache_dependency "contentitem:123" %}`: add cache dependency inside a cache scope.
- `{% cache_expires_on "2024-01-01T00:00:00Z" %}`: set absolute expiration.
- `{% cache_expires_after "00:05:00" %}`: set absolute duration.
- `{% cache_expires_sliding "00:00:30" %}`: set sliding expiration.

**HttpContext items**
- `{% httpcontext_add_items key: value, another: 1 %}`: add items to `HttpContext.Items`.
- `{% httpcontext_remove_items "key" %}`: remove an item by key.
