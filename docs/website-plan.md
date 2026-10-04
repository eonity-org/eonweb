# Website scope

## Purpose

Introduce TYDAL to developers and early adopters, explain the Semantic Asset Platform model, show applications and connect visitors to code and documentation.

## Brand

- TYDAL: product and main visual identity.
- Eonity.org: confirmed public website.
- Eonity: umbrella, credited in About and the footer.
- Main message: **Control your knowledge flow.**
- Category: **Semantic Asset Platform**.
- Product definition: **TYDAL is the typed Digital Asset Layer.**
- Supporting explanation: **The semantic layer between your files and your AI.**

## Naming and terminology

Use **FullFrame** as one word, with capital F in both parts, in all website copy. Keep `fullframe` lowercase in URLs and repository identifiers. This is the agreed brand spelling; upstream README prose may still use the older two-word form.

The founder defines **DAL** as **Digital Asset Layer**. **TY** connects TYDAL to the TY / Eonity product family. Use “TYDAL” in running text and preserve the supplied logo; “TYDAL — the typed Digital Asset Layer” explains the name.

“Control your knowledge flow” remains the main headline. “Semantic Asset Platform” describes the product category, while “Digital Asset Layer” explains its architectural role: digital assets → TYDAL → people, applications and AI.

In more detail, the TYDAL repository is the core and Vaults are contextual views of selected resources with access rules. Resources retain their canonical source across Vaults and delivery channels. “Layer” refers to the whole platform's role; it does not relocate the core into Vaults.

DAM provides useful category context. Explain the added value through structure, semantic discovery, AI enrichment and programmatic access. Keep RDF/linked-data evolution and future automation in future technical material until their implementation and availability are verified. Aity / Ask AI describes conversational access; MCP connects external AI tools and agents.

“Typed” means schemas define resource fields, validation and search behavior. Keep the headline, category and definition at distinct levels; do not stack developer slogans in the hero.

## Public source and documentation

Verified 2026-09-24: the product repository is https://github.com/eonity-org/tydal and TYDAL is licensed under Apache-2.0. Product links point directly there; website source/edit links continue to point to eonity-org/eonweb. Developer pages introduce each topic and link to maintained product guides rather than duplicating installation commands. The screenshot gallery remains planned until actual product images are available.

## Page plan

### Current direction — 2026-09-29

Keep eonity.org as TYDAL's product and developer home. Explain the whole platform before individual clients. FullFrame is the first standalone open-source client product and a concrete integration case study, linked from Applications and the developer guides. Its case study explains what TYDAL provides, what the client adds, and how the same model supports other content and applications. It does not need a separate top-level product navigation item.

Reserve tydalia.com for a future demonstrator covering multiple running client experiences. Revisit it when there are contrasting uses to show alongside photography. This update makes no domain changes and does not turn Eonity's homepage into a product-family directory.

### Content areas

- Hero architecture: the TYDAL repository is the core; resources, schemas and enrichment belong there. Vaults are contextual views feeding experiences for people, applications and AI agents. Keep deeper architecture details for future developer documentation.
- Home: promise, illustrative Vault model, key benefits, applications and developer entry points.
- Platform: resources, schemas, collections, Vaults, enrichment and publishing.
- Applications: FullFrame as a client case study, AI/MCP connections and a build-your-own path.
- Developers: architecture and links to maintained setup/API/MCP documentation.
- Open source: repositories, license, contribution and project maturity.
- About: Eonity relationship and project purpose.

Some destinations may begin as homepage sections.

## Link behavior

External HTTP(S) links open in a new tab with `rel="noopener noreferrer"` and an “Opens in a new tab” title. Internal links and section anchors stay in the current tab. Astro templates declare this explicitly; the Markdown pipeline applies it automatically to content pages and developer guides.

## Visual direction

Predominantly light surfaces with the October 2026 sRGB TYDAL master as the colour source: dark blue `#0A5475` (“ty”) for primary actions and the developer section, blue `#287C9C` (“dal”) for accents and links, `#1A5D7D` for secondary text, and light blue `#5295B3` for decorative connectors and borders. Derive backgrounds and dark-section colours from this palette. The light blue is decorative only: its 3.33:1 contrast against white is insufficient for small text. The accent has 4.72:1 contrast against white; darken it by 12% for small accent text on tinted surfaces, and use the darker secondary-text blue for body descriptions. Use the supplied transparent complete masters for wordmarks and the simplified monochrome Ty variant for the small favicon; preserve their artwork and embedded sRGB profiles. Keep the header white and visible while scrolling, with section-link offsets that follow its actual height. Use strong typography, clear diagrams and real product imagery when available. Respect reduced motion and support small screens.

## Technical boundary

Use Astro, TypeScript, custom CSS and local content/assets. Run development, installation and builds only in the dedicated Docker Compose service; no host Node installation. React is optional for a demonstration that needs it. Do not integrate the separately planned TYDAL publishing client, MCP authoring, visual page editor or DBE workflow into this website release.

## License

The website source is licensed under Apache-2.0.

## Deployment destination

Confirmed public domain: **https://eonity.org**, superseding the earlier tydalia.com plan. Keep TYDAL as the product name and Eonity as the umbrella identity. The existing Tydalia X account remains the social destination.

For GitHub Pages, publish the generated `dist/` artifact through GitHub Actions and configure `eonity.org` in the repository Pages settings. Verify the domain, configure apex DNS records for GitHub Pages and point the `www` CNAME to `eonity-org.github.io`, and enable HTTPS. Domain selection alone does not configure DNS or publish the site.

## Subsequent updates

The website is published through `.github/workflows/pages.yml`. Verify public source/documentation/demo destinations, add actual captures when available, and check responsive and keyboard behavior for changed pages. Keep the TYDAL product model central as client examples grow.
