---
title: Screenshots and walkthroughs
description: Visual guides to the interface and common development workflows.
section: Reference
order: 40
status: ready
---

Real captures from a local instance with demonstration content: TYDAL v1.2.0 and FullFrame v0.2.0, taken on 3 and 4 October 2026. Select an image to open it at full size.

## Schemes and uploads

[![TYDAL’s Schemes & Indexes page: four schemes (Multimedia, Documents and General Collection, and Photo Exhibition), each with its field count, how many collections use it and which organizations it is offered to, above four search indexes available to all organizations.](/developers/screenshots/schemes-and-indexes.webp)](/developers/screenshots/schemes-and-indexes.webp)

_Schemes and search indexes. A scheme is the field contract a collection follows; an index is where its documents are stored for search._

[![TYDAL’s new-resources wizard after uploading two photographs: a choice between Interactive review and Auto, with Auto selected to accept AI-suggested names, descriptions and tags, cluster tags, and name the new workspace.](/developers/screenshots/upload-wizard.webp)](/developers/screenshots/upload-wizard.webp)

_The upload wizard. Review AI suggestions one resource at a time, or let them be applied automatically to the batch._

## Vaults

[![The Capabilities dialog for the Pike and Shot Vault: read tiers for chunk text, binaries and answering questions, the file roles that get addresses or feed chunks, and the write methods the Vault accepts, each following its purpose preset.](/developers/screenshots/vault-capabilities.webp)](/developers/screenshots/vault-capabilities.webp)

_A Vault’s capabilities. Its purpose sets a preset; each read tier, file role and write method can override it for this Vault only._

[![The Sharing & reach dialog for the Pike and Shot Vault: state Public, its Vault hash, human and machine URLs, time-limited signed links, and an optional base URL for a Vault domain.](/developers/screenshots/vault-sharing-and-reach.webp)](/developers/screenshots/vault-sharing-and-reach.webp)

_Sharing and reach: whether the Vault is disabled, private or public, and the addresses people and applications use. The addresses point at the local instance the capture was taken on._

## Publishing an exhibition in FullFrame

The curator’s side of [FullFrame](/developers/fullframe/), from setup to a live exhibition, shown with Drift, a demo exhibition.

[![FullFrame’s studio for Drift in setup: stage Preparing, private to the curator and invited people, with 6 photographs connected to TYDAL, a private exhibition, no jury yet, and step 1, Submissions, below.](/developers/screenshots/studio-setup.webp)](/developers/screenshots/studio-setup.webp)

_1. Setup. The stage, the photographs connected from TYDAL, the exhibition’s visibility and the jury._

[![Step 2 in FullFrame’s studio, Photographs: an upload box and the six photographs in the exhibition, from “Last Breath of Air” to “Touchdown, Three Ways” by Clara Venn, each with Edit and Remove.](/developers/screenshots/studio-photographs.webp)](/developers/screenshots/studio-photographs.webp)

_2. Photographs. Uploads go straight into the exhibition’s Vault in TYDAL, with the details the curator gives them._

[![Step 4 in FullFrame’s studio, Choose and publish: the six parachuting photographs in a grid and a Choose photographs button.](/developers/screenshots/studio-choose-and-publish.webp)](/developers/screenshots/studio-choose-and-publish.webp)

_3. Choose and publish. The curator writes the exhibition’s texts and selects the photographs, then picks a style and publishes._

[![FullFrame’s appearance settings: Mosaic and Wall chosen as the views visitors can open, Mosaic as the default, the Blue palette selected from five, and a live preview of the exhibition in the Mosaic view.](/developers/screenshots/studio-views-and-palette.webp)](/developers/screenshots/studio-views-and-palette.webp)

_4. Appearance. Which views visitors can open, the default view and the palette, with a live preview._

[![FullFrame’s studio after publishing Drift: stage Live, “Your exhibition is live.”, 6 photographs selected, exhibition Published, no jury, and buttons to visit or close the exhibition.](/images/drift-studio-live.webp)](/images/drift-studio-live.webp)

_5. Live. Publishing activates the selection and opens the Vault; Close exhibition makes it private again._

## Workflow walkthroughs

[Watch Claude curate Drift](/#see-it-work): it reads the exhibition through its Vault, proposes titles and descriptions, and writes them back through the organization’s MCP server after asking permission. FullFrame then shows the new titles without any export or upload.
