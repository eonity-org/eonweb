# eonweb

The product website for **Tydal**, the open-source typed Digital Asset Layer developed under **Eonity**. Semantic Asset Platform describes its product category.

The [Tydal product repository](https://github.com/eonity-org/tydal) is public and licensed under Apache-2.0.

> Control your knowledge flow.

The planned public home is **https://eonity.org**. This repository contains the website only. It does not contain the Tydal backend or the separately planned MCP publishing client.

## Status

Initial website development. The initial homepage concept, About page, supplied brand assets and repository tooling are in place. The homepage Vault diagram is an interactive concept illustration, not a live Tydal connection. Public deployment is not configured.

## Stack

- Astro with static output
- TypeScript
- Custom CSS
- Local Markdown, data and assets
- React islands only if an interactive demonstration needs them; React is not installed yet

The website is independent of Tydal at build time and runtime. Integrating a future content-publishing client is outside the current scope.

## Requirements

Docker with Docker Compose (for example, OrbStack). **Do not install Node.js or npm on the host.** All Node tooling runs in the dedicated `eonweb` container using `node:22-slim`, independently of Tydal's containers.

## Local development

From the repository directory:

```sh
docker compose run --rm web npm ci
docker compose up -d web
```

Open **http://127.0.0.1:4321**. Follow the server output with `docker compose logs -f web`.

Source files are mounted from the repository. Dependencies and the npm cache live in named Docker volumes. The development port is bound only to the local host.

Stop the server with:

```sh
docker compose down
```

## Commands

| Command                                            | Purpose                                       |
| -------------------------------------------------- | --------------------------------------------- |
| `docker compose up -d web`                         | Start the local development server            |
| `docker compose run --rm web npm run check`        | Check Astro and TypeScript files              |
| `docker compose run --rm web npm run build`        | Check and generate the static site in `dist/` |
| `docker compose run --rm web npm run format`       | Format source and documentation               |
| `docker compose run --rm web npm run format:check` | Check formatting without changing files       |

To preview the production build, stop the development server first and run:

```sh
docker compose down
docker compose run --rm --service-ports web npm run preview -- --host 0.0.0.0
```

Commit `package-lock.json` so contributors and CI use the same dependency versions. Install or update dependencies inside the container, for example `docker compose run --rm web npm install some-package`. Use `npm ci` inside Docker for a clean installation.

## Project structure

```text
.github/workflows/  Continuous integration
public/brand/      Supplied Tydal and Eonity logos
src/components/    Reusable presentation components
src/data/          Local structured content
src/layouts/       Shared page layouts
src/pages/         Website routes and Markdown pages
src/styles/        Shared CSS
```

Empty directories appear as the corresponding source is added; Git does not track empty folders.

## Developer documentation

The Markdown-based developer space is at `/developers/`. Edit pages in `src/content/developers/`; navigation, topic cards and page tables of contents are generated automatically. Guides introduce setup, configuration, integrations and troubleshooting and link to maintained documentation in the Tydal repository. The screenshot gallery remains marked **Coming soon**. See [the authoring guide](docs/developer-documentation.md) for page metadata and screenshot conventions.

## Content and design

The main product name is **Tydal**. The website is published at eonity.org; Eonity is the umbrella attribution. The design is predominantly light, based on Eonity blue (`#005275`, sampled from the September 2026 logos) and slate blue (`#52738C`), with blue-grey (`#8694A1`) connectors and borders, pale blue surfaces and a limited dark blue section. Preserve the supplied logo artwork.

The brand assets use the supplied transparent 200px-high PNGs: Tydal (450 × 200), Eonity (578 × 200) and the Ty symbol (200 × 200). Tydal appears in the header and footer; the Ty symbol is the favicon. The header stays white and remains visible while scrolling. Anchor offsets follow its height, including when navigation wraps on mobile. Backgrounds, greys and dark-section colors are tints and shades of the three brand colors defined in `src/styles/global.css`.

Write content in English. Prefer working examples and verified product capabilities. Keep repository and demo links centralized as they become available. Do not present illustrative diagrams as live product screenshots.

See [the website plan](docs/website-plan.md) and [contribution notes](CONTRIBUTING.md).

## Configuration and deployment

`astro.config.mjs` sets the canonical site to `https://eonity.org` and uses static output. No environment variables are required by the initial website.

CI uses the same Docker Compose service to install dependencies, check formatting and run Astro/TypeScript checks and a production build. It does not deploy. The `dist/` directory can be served by a static host; a provider and deployment workflow will be selected separately.

Keep credentials in local environment files or CI secrets. Generated output, caches and local environment files are excluded by `.gitignore`.

## License

Licensed under the [Apache License 2.0](LICENSE). The license does not grant rights to the Tydal or Eonity names and trademarks.
