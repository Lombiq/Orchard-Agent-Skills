# Liquid Filters

This is a source-derived catalog of Liquid filters commonly used for Orchard Core theme work.

**Core formatting and utilities**
- `t`: localize a string with optional parameters. Example: `{{ "Hello {0}" | t: user.Name }}`
- `html_class`: converts text to a CSS class (e.g., spaces -> dashes). Example: `{{ "My Title" | html_class }}`
- `json`: serialize to JSON; pass `true` to indent. Example: `{{ Model | json: true }}`
- `jsonparse`: parse JSON into a Liquid object/array. Example: `{% assign obj = my_json | jsonparse %}`

**Dates and times**
- `local`: convert a date/time to local timezone; accepts `"now"`/`"today"`. Example: `{{ "now" | local }}`
- `utc`: convert a date/time to UTC; accepts `"now"`/`"today"`. Example: `{{ Model.PublishedUtc | utc }}`

**Strings and templating**
- `slugify`: slugifies text. Example: `{{ Model.Title | slugify }}`
- `liquid`: renders a Liquid string template; first argument is an optional model. Example: `{{ "{{ user.Name }}" | liquid: Model }}`

**Shapes**
- `shape_new`: create a shape; named args become shape properties. Example: `{% assign s = "Card" | shape_new: title: "Hi" %}`
- `shape_render`: renders a shape to HTML. Example: `{{ s | shape_render }}`
- `shape_stringify`: renders a shape to a string (not HTML-encoded). Example: `{{ s | shape_stringify }}`
- `shape_properties`: set shape properties from named args. Example: `{{ s | shape_properties: title: "Hi" }}`

**Resources and URLs**
- `href`: convert a virtual path to an app-relative URL. Example: `{{ "~/css/site.css" | href }}`
- `absolute_url`: convert a URL to absolute. Example: `{{ "~/about" | absolute_url }}`
- `append_version`: append file version to a URL. Example: `{{ "~/css/site.css" | append_version }}`
- `resource_url`: prefix a CDN base URL if configured. Example: `{{ "~/css/site.css" | resource_url }}`

**HTML safety**
- `sanitize_html`: sanitize HTML content. Example: `{{ Model.Html | sanitize_html }}`
- `supported_cultures`: returns supported cultures (obsolete). Example: `{% assign cultures = "" | supported_cultures %}`

**Content**
- `display_url`: get display URL for a content item or id. Example: `{{ Model.ContentItem | display_url }}`
- `shape_build_display`: build a display shape for a content item. Example: `{{ Model.ContentItem | shape_build_display: "Summary" | shape_render }}`
- `content_item_id`: load content item(s) by id(s). Example: `{{ "42" | content_item_id }}`
- `full_text`: get full-text segments for indexing/search. Example: `{{ Model.ContentItem | full_text }}`

**Lists**
- `list_items`: get contained items for a list content item (or id). Example: `{{ Model.ListItem | list_items }}`
- `list_count`: get count of items in a list content item (or id). Example: `{{ Model.ListItem | list_count }}`
- `container`: get the list container of a contained item. Example: `{{ Model.ContentItem | container }}`

**Media**
- `asset_url`: resolve a media path to a public URL. Example: `{{ "/media/hero.jpg" | asset_url }}`
- `resize_url`: build a resized image URL. Example: `{{ "/media/hero.jpg" | resize_url: width: 800, mode: "crop" }}`.
  Use a media profile with named args: `{{ "/media/hero.jpg" | resize_url: profile: "site-default" }}`

**Localization**
- `localization_set`: get localized item(s) for a set; optional culture arg. Example: `{{ Model.LocalizationSet | localization_set: "fr-FR" }}`
- `switch_culture_url`: build a URL that switches to the given culture. Example: `{{ "fr-FR" | switch_culture_url }}`

**Queries**
- `query`: execute a query with parameters. Example: `{{ Query | query: category: "news" }}`

**Taxonomies**
- `taxonomy_terms`: resolve term items from a taxonomy field. Example: `{{ Model.TaxonomyField | taxonomy_terms }}`
- `inherited_terms`: get term hierarchy for a term in a taxonomy. Example: `{{ Term | inherited_terms: TaxonomyId }}`

**Users and permissions**
- `users_by_id`: load user(s) by user id(s). Example: `{{ "user-id" | users_by_id }}`
- `has_permission`: check current user permission. Example: `{{ User | has_permission: "ViewContent" }}`
- `is_in_role`: check current user role. Example: `{{ User | is_in_role: "Administrator" }}`
- `user_email`: get email for current user or a user. Example: `{{ User | user_email }}`

**Markdown and shortcodes**
- `markdownify`: convert markdown to HTML. Example: `{{ Model.Body | markdownify }}`
- `shortcode`: process shortcodes in text. Example: `{{ Model.Body | shortcode }}`

**Workflows**
- `signal_url`: build a workflow signal URL. Example: `{{ "MySignal" | signal_url }}`

**Debug**
- `console_log`: outputs a `<script>console.log(...)` in non-production. Example: `{{ Model | console_log }}`
