# Contributing

Use Docker Compose for all Node tooling. Install dependencies with `docker compose run --rm web npm ci`; no host Node/npm installation is required.

Keep changes focused on this website. The Tydal application and the future publishing client are separate projects.

## Before a pull request

```sh
docker compose run --rm web npm run format
docker compose run --rm web npm run build
```

For visual changes, inspect the affected pages at desktop and mobile widths and check keyboard navigation. Include screenshots when they help explain the change.

Use semantic HTML, readable contrast, meaningful alternative text and reduced-motion support. Add client-side JavaScript only for an interaction that needs it.

Keep content in English and distinguish available product behavior from planned features. Preserve the supplied brand identity. Avoid committing generated output, local credentials or private reference material.

Dependency changes must include the updated `package-lock.json`. Explain the reason for a new runtime dependency in the pull request.
