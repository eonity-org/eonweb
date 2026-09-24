---
layout: ../layouts/ContentLayout.astro
title: Content with a context.
description: Tydal is the typed Digital Asset Layer for organizing, understanding, finding and delivering digital assets.
label: About Tydal
---

Tydal is an open-source Semantic Asset Platform. It combines digital asset management with configurable schemas, semantic search, AI enrichment and programmatic access, making content usable by people, applications and AI systems.

## The typed Digital Asset Layer

The **DAL** in **TYDAL** stands for **Digital Asset Layer**. The **TY** prefix connects it to the broader TY / Eonity product family.

“Layer” describes Tydal’s role between digital assets and the people, applications and AI systems that use them. It brings together structure, metadata, relationships and AI enrichment to help organize, understand, find and deliver those assets.

**Typed** means schemas define resource fields, validation and search behavior. The same structure guides forms, filters and indexing.

Digital assets extend beyond images, audio and video. Documents, datasets, Markdown, source code and combinations of these files can all be resources in Tydal. A learning resource, for example, might bring together a lesson, illustrations and supporting data. Its schema defines how those parts are described, processed and indexed.

## The model

**The Tydal repository** is the core: it holds and organizes your resources, their files and their semantic structure.

**Resources** are the fundamental objects in the repository. A resource can contain a single file, several related components, or a canonical asset with supporting files and representations. Metadata and relationships describe the resource as a whole.

**Collections and schemas** define how different kinds of resources are described, validated, processed and indexed. Schemas specify metadata fields, file roles and indexing rules, so the structure fits the content.

**Workspaces** let you curate selections of resources for a task or a project. Vaults can expose those selections to their intended audiences.

**Vaults** are contextual views of selected resources, with their own presentation and access rules. The source stays in the repository and can serve multiple Vaults without duplicating the underlying asset. Vault interfaces support delivery, search and permitted AI interactions.

**Experiences** make use of those Vaults: exhibitions, knowledge spaces, AI connections and applications built through the API.

## Find resources by meaning

Tydal combines metadata filters and full-text search with embeddings and vector similarity. This helps people find relevant resources even when their query uses different words from the original content. Relationships provide another route to related material.

Schemas define structure and meaning; embeddings provide signals for retrieval. Indexing rules determine which information contributes to search and how it is represented.

## AI for enrichment and exploration

AI enrichment can suggest descriptions, tags, classifications and other metadata. Suggestions can be reviewed before they are applied, with configurable approval rules for batch workflows.

**Ask AI** provides conversational access to resources in context. **Organization MCP** lets authorized agents manage resources and curate workspaces. **Vault MCP** connects an external AI client to one Vault: read-only by default, with supported write operations enabled through a write key. See [API and integrations](/developers/api-and-integrations/) to choose a connection.

## Build on the layer

The management API works with the repository's resources, collections and workspaces. Vault interfaces expose selected content to consuming applications. This supports galleries, knowledge spaces, learning tools and AI clients built around the same canonical resources.

Resources can be delivered through different Vault links and CDN configurations. The event model records resource operations to support auditing and provenance.

## An Eonity project

Eonity is an umbrella for open-source work in education, content and data management. Tydal is its foundation for bringing structure and meaning to digital assets.

The project is built for developers and early adopters. Tydal is available under the [Apache License 2.0](https://github.com/eonity-org/tydal/blob/main/LICENSE). Services, support, implementation and hosted capabilities can support its development.

## Build with us

Explore the [Tydal repository](https://github.com/eonity-org/tydal), read the [contribution guide](https://github.com/eonity-org/tydal/blob/main/docs/CONTRIBUTING.md), and follow [Tydalia on X](https://x.com/_tydalia) for the project’s development.
