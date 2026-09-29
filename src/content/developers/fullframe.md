---
title: 'FullFrame: a client built on Tydal'
description: How a photography application uses Tydal for resources, Vault access and publishing while keeping its own presentation and workflows.
section: Build and configure
order: 35
status: ready
---

FullFrame is Tydal's first standalone open-source client product. It turns a gallery Vault into a photography exhibition, adding visitor views, a curator studio and an optional jury. It demonstrates how an application can build on Tydal's resource platform.

Tydal also supports documents, datasets, code and composite resources. Photography is one use of the same model: structure resources with schemas, curate them in workspaces and expose them through Vaults for people, applications and AI agents. Start with [the Tydal model](/about/#the-model) for the broader picture.

## What belongs to each product

| Tydal provides                                        | FullFrame adds                                      |
| ----------------------------------------------------- | --------------------------------------------------- |
| Photograph resources, files and metadata              | Mosaic, Gallery and Wall visitor views              |
| Schemas, collections and workspace membership         | Exhibition details, appearance and curator workflow |
| Vault access, previews and permitted write operations | Jury invitations, scores and private notes          |
| The resource projection used for publication          | The curator's selection and local scoring records   |

Tydal remains the repository of record for the photographs. FullFrame stores its exhibition settings and jury records separately. An exhibition does not create another independently managed copy of the photographs.

## How the connection works

An administrator prepares a gallery Vault in Tydal. In FullFrame's studio, the curator connects its shared URL and the required Vault keys. FullFrame resolves the address and uses Vault-scoped hashes to refer to the photographs.

The FullFrame server uses the [TypeScript SDK](https://github.com/eonity-org/tydal/blob/main/client/README.md) to read the Vault and invoke permitted writes. Credentials stay on the server. Curator sign-in is a separate connection to Tydal's identity endpoint; exhibition content and publication use the Vault boundary.

With the appropriate permissions, the workflow is:

1. **Prepare:** add photographs and their details during setup. Tydal stores them in the Vault's configured collection and workspace.
2. **Curate:** choose the appearance and select photographs. An optional jury can inform that selection.
3. **Publish:** FullFrame submits the selected hashes with `activate`, then makes the gallery public with `open`.
4. **Revise:** `close` makes the Vault private and restores its pre-selection projection. Photographs remain in Tydal, and the curator can adjust the selection before publishing again.

These are supported operations on one Vault, authorized by its write key. The application does not need an organization-wide management token to publish an exhibition. See [Vault write methods](https://github.com/eonity-org/tydal/blob/main/docs/architecture/VAULT_WRITE_METHODS.md) for the detailed contract.

## Apply the pattern to your own client

Start with the resources your application needs and the context a Vault should expose. Read the Vault's metadata to discover its available capabilities, use its resource addresses, and request only the write permissions the workflow requires.

Your client supplies its own interface and domain-specific workflows. Tydal supplies the resource structure and controlled access. A document knowledge space or an AI connection can use that foundation with different content and capabilities. The bundled [Gallery](https://github.com/eonity-org/tydal/blob/main/vaults/gallery/README.md), [knowledge graph](https://github.com/eonity-org/tydal/blob/main/vaults/obsidian/README.md) and [AI chat](https://github.com/eonity-org/tydal/blob/main/vaults/aity/README.md) clients provide other examples; the Gallery renderer is separate from FullFrame's curator and jury application.

Continue with [API and integrations](/developers/api-and-integrations/) to choose your connection.

## Explore or run FullFrame

FullFrame is available under [Apache-2.0](https://github.com/eonity-org/fullframe/blob/main/LICENSE). Running it requires a reachable Tydal instance and a configured gallery Vault.

- [Source and application overview](https://github.com/eonity-org/fullframe)
- [FullFrame deployment guide](https://github.com/eonity-org/fullframe/blob/main/DEPLOY.md)
- [Prepare an exhibition in Tydal](https://github.com/eonity-org/tydal/blob/main/docs/CLI.md#photo-exhibitions-full-frame)
- [Curator and jury guide](https://github.com/eonity-org/fullframe/blob/main/docs/GUIDE.md)

If you are starting with the platform, use [Getting started with Tydal](/developers/getting-started/) first. Setup commands remain in the product repositories so they can evolve with the code.
