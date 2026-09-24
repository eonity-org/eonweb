# Maintaining the developer space

The public developer space lives at `/developers/`. It uses local Markdown files and Astro's built-in content collections; no external CMS or database is required.

## Add or edit a page

Create a `.md` file in `src/content/developers/`, or edit an existing one. Use this frontmatter:

```yaml
---
title: Storage configuration
description: Configure storage for your installation.
section: Build and configure
order: 25
status: planned
---
```

The file `storage.md` becomes `/developers/storage/`; `configuration/storage.md` becomes `/developers/configuration/storage/`. `index.md` is the landing page. Use lowercase, hyphen-separated filenames and unique paths.

`section` groups pages in the sidebar. `order` controls page ordering and the order in which groups first appear. The sidebar and landing-page cards update automatically. Set `status: ready` once the page has verified content; `planned` (the default) displays a coming-soon notice. Both statuses are public, so keep unpublished or private material outside this directory.

The title supplies the H1. Start the body with `##` headings; H2 and H3 headings automatically populate the table of contents. Markdown supports links, lists, fenced code blocks with syntax highlighting, tables, blockquotes and images. Use public URL paths for internal links, for example `[Configuration](/developers/configuration/)`.

## Add screenshots

Place screenshots under `public/developers/screenshots/` and reference them using an absolute URL:

```md
![Resource details showing metadata fields](/developers/screenshots/resource-details.png)

_Resource details — Tydal version X, captured YYYY-MM-DD._
```

Use actual product captures with descriptive alt text, captions and version context. Remove credentials and personal data before publishing. The screenshot placeholder page intentionally contains no fabricated interface images.

## Validate and publish

Run `docker compose run --rm web npm run build`. Preview the affected pages at desktop and mobile widths. Content changes become public when the static site is rebuilt and deployed.
