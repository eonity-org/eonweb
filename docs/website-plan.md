# Website scope

## Purpose

Introduce Tydal to developers and early adopters, explain the Semantic Asset Platform model, show applications and connect visitors to code and documentation.

## Brand

- Tydal: product and main visual identity.
- Eonity.org: confirmed public website.
- Eonity: umbrella, credited in About and the footer.
- Main message: **Control your knowledge flow.**
- Category: **Semantic Asset Platform**.
- Product definition: **Tydal is the typed Digital Asset Layer.**
- Supporting explanation: **The semantic layer between your files and your AI.**

## Naming and terminology

The founder defines **DAL** as **Digital Asset Layer**. **TY** connects TYDAL to the TY / Eonity product family. Use “Tydal” in running text and preserve the supplied logo; “TYDAL — the typed Digital Asset Layer” explains the name.

“Control your knowledge flow” remains the main headline. “Semantic Asset Platform” describes the product category, while “Digital Asset Layer” explains its architectural role: digital assets → Tydal → people, applications and AI.

In more detail, the Tydal repository is the core and Vaults are contextual views of selected resources with access rules. Resources retain their canonical source across Vaults and delivery channels. “Layer” refers to the whole platform's role; it does not relocate the core into Vaults.

DAM provides useful category context. Explain the added value through structure, semantic discovery, AI enrichment and programmatic access. Keep RDF/linked-data evolution and future automation in future technical material until their implementation and availability are verified. Aity / Ask AI describes conversational access; MCP connects external AI tools and agents.

“Typed” means schemas define resource fields, validation and search behavior. Keep the headline, category and definition at distinct levels; do not stack developer slogans in the hero.

## Public source and documentation

Verified 2026-09-24: the product repository is https://github.com/eonity-org/tydal and Tydal is licensed under Apache-2.0. Product links point directly there; website source/edit links continue to point to eonity-org/eonweb. Developer pages introduce each topic and link to maintained product guides rather than duplicating installation commands. The screenshot gallery remains planned until actual product images are available.

## Page plan

- Hero architecture: the Tydal repository is the core; resources, schemas and enrichment belong there. Vaults are contextual views feeding experiences for people, applications and AI agents. Keep deeper architecture details for future developer documentation.
- Home: promise, illustrative Vault model, key benefits, applications and developer entry points.
- Platform: resources, schemas, collections, Vaults, enrichment and publishing.
- Applications: Full Frame, AI/MCP connections and other confirmed examples.
- Developers: architecture and links to maintained setup/API/MCP documentation.
- Open source: repositories, license, contribution and project maturity.
- About: Eonity relationship and project purpose.

Some destinations may begin as homepage sections.

## Link behavior

External HTTP(S) links open in a new tab with `rel="noopener noreferrer"` and an “Opens in a new tab” title. Internal links and section anchors stay in the current tab. Astro templates declare this explicitly; the Markdown pipeline applies it automatically to content pages and developer guides.

## Visual direction

Predominantly light surfaces with Eonity blue (`#005275`, sampled from the September 2026 logos) for primary actions and the developer section, slate blue (`#52738C`) for secondary text and accents, and blue-grey (`#8694A1`) for connectors and borders. Derive backgrounds, greys and dark-section colors from these three colors. Keep small text in the darker blues for readable contrast. Avoid green and teal UI colors. Use the supplied transparent 200px-high logos; preserve their artwork. Keep the header white and visible while scrolling, with section-link offsets that follow its actual height. Use strong typography, clear diagrams and real product imagery when available. Respect reduced motion and support small screens.

## Technical boundary

Use Astro, TypeScript, custom CSS and local content/assets. Run development, installation and builds only in the dedicated Docker Compose service; no host Node installation. React is optional for a demonstration that needs it. Do not integrate the separately planned Tydal publishing client, MCP authoring, visual page editor or DBE workflow into this website release.

## License

The website source is licensed under Apache-2.0.

## Deployment destination

Confirmed public domain: **https://eonity.org**, superseding the earlier tydalia.com plan. Keep Tydal as the product name and Eonity as the umbrella identity. The existing Tydalia X account remains the social destination.

For GitHub Pages, publish the generated `dist/` artifact through GitHub Actions and configure `eonity.org` in the repository Pages settings. Verify the domain, configure apex DNS records for GitHub Pages and point the `www` CNAME to `eonity-org.github.io`, and enable HTTPS. Domain selection alone does not configure DNS or publish the site.

## Before public launch

Verify public source/documentation/demo destinations, replace any illustrative product representations where real screenshots are needed, check responsive and keyboard behavior, and configure the chosen static hosting provider.
