# eonweb

The website of **Eonity** and its open-source tools, published at **https://eonity.org**.

> Structure and meaning for people and AI.

Eonity builds tools that give AI a clear scope to work in while people stay in the loop:

- **[TYDAL](https://github.com/eonity-org/tydal)**, the typed Digital Asset Layer, with [FullFrame](https://github.com/eonity-org/fullframe) as its first client (`/tydal/`).
- **[TYKERF](https://github.com/eonity-org/tykerf)**, web pages edited one named block at a time (`/tykerf/`).
- **Tyset**, structured desktop publishing, coming soon (shown as a card on the home page).

This repository contains the website only. The products are separate repositories, each licensed under Apache-2.0.

## Status

Published at eonity.org through GitHub Pages. The home page introduces Eonity and its tools; each product has its own page, and About explains Eonity's approach. The TYDAL developer guides stay at `/developers/`, and the user guides at `/guides/` cover TYDAL, FullFrame and TYKERF. The diagrams on the home, TYDAL and TYKERF pages are concept illustrations, not live connections.

The products shown on the home page come from `src/data/products.ts`: a new product is one entry there plus its page under `src/pages/<id>/`. The project's social account is [@eonity_org on X](https://x.com/eonity_org).

## Stack

- Astro with static output
- TypeScript
- Custom CSS, with Manrope (variable) self-hosted through `@fontsource-variable/manrope`, the typeface the TYDAL app and FullFrame also use
- Local Markdown, data and assets
- React islands only if an interactive demonstration needs them; React is not installed yet

The website is independent of TYDAL at build time and runtime. Integrating a future content-publishing client is outside the current scope.

## Requirements

Docker with Docker Compose (for example, OrbStack). **Do not install Node.js or npm on the host.** All Node tooling runs in the dedicated `eonweb` container using `node:22-slim`, independently of TYDAL's containers.

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
public/brand/      Supplied TYDAL and Eonity logos
public/images/     Optimized product screenshots and the MCP walkthrough video
public/developers/screenshots/  Screenshot gallery images for /developers/screenshots/
src/components/    Reusable presentation components
src/data/          Local structured content
src/layouts/       Shared page layouts
src/pages/         Website routes and Markdown pages
src/styles/        Shared CSS
```

Empty directories appear as the corresponding source is added; Git does not track empty folders.

## Developer documentation

The Markdown-based developer space is at `/developers/`. Edit pages in `src/content/developers/`; navigation, topic cards and page tables of contents are generated automatically. Guides introduce setup, configuration, integrations and troubleshooting and link to maintained documentation in the TYDAL repository. The screenshot gallery shows real captures of TYDAL and FullFrame's studio. See [the authoring guide](docs/developer-documentation.md) for page metadata and screenshot conventions.

## Content and design

The main product name is **TYDAL**, written in capitals in all running text; the lowercase “tydal” appears only in the logo. The website is published at eonity.org; Eonity is the umbrella attribution. The design is predominantly light, based on Eonity blue (`#005275`, sampled from the September 2026 logos) and slate blue (`#52738C`), with blue-grey (`#8694A1`) connectors and borders, pale blue surfaces and a limited dark blue section. Preserve the supplied logo artwork.

Screenshots on the home page and the FullFrame guide are real product captures from `TYDAL/WEBSITE_SHOTS/`, cropped and converted to WebP (each well under 250 KB), with alt text describing what they show. `public/og-image.png` (1200 × 630) is the social preview image; `robots.txt`, `favicon.ico` and the generated `sitemap.xml` sit beside it.

The brand assets use the October 2026 sRGB exports from `LOGOS/NEW_LOGOS`: the complete TYDAL master (315 × 140), complete Eonity master (405 × 140), and simplified monochrome Ty symbol (64 × 64). TYDAL appears in the header and footer; the Ty symbol is the favicon. The header stays white and remains visible while scrolling. Anchor offsets follow its height, including when navigation wraps on mobile. Backgrounds, greys and dark-section colors are tints and shades of the brand colors defined in `src/styles/global.css`.

Write content in English. Prefer working examples and verified product capabilities. Keep repository and demo links centralized as they become available. Do not present illustrative diagrams as live product screenshots.

See [the website plan](docs/website-plan.md) and [contribution notes](CONTRIBUTING.md).

## Configuration and deployment

`astro.config.mjs` sets the canonical site to `https://eonity.org` and uses static output. No environment variables are required by the initial website.

CI uses the same Docker Compose service to install dependencies, check formatting and run Astro/TypeScript checks and a production build. The separate `pages.yml` workflow builds and deploys `dist/` to GitHub Pages on pushes to `main` or manual dispatch.

Keep credentials in local environment files or CI secrets. Generated output, caches and local environment files are excluded by `.gitignore`.

## License

Licensed under the [Apache License 2.0](LICENSE). The license does not grant rights to the TYDAL or Eonity names and trademarks.
