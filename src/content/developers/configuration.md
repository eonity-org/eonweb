---
title: Configuration
description: Environment settings, services and configuration examples for your installation.
section: Build and configure
order: 20
status: ready
---

## Services and environment

The [deployment guide](https://github.com/eonity-org/tydal/blob/main/DEPLOYMENT.md) covers environment variables, database and queue services, search, storage and production setup. Use the templates and instructions from the version of Tydal you are running.

## Schemas and search

Schemas define resource metadata fields, validation, forms and search behavior. Start with the [schema field contract](https://github.com/eonity-org/tydal/blob/main/docs/architecture/SCHEMA_FIELDS.md) for supported field definitions and how they affect indexing and filters.

## AI providers

Server-side enrichment uses configurable language and vision providers; embeddings are configured separately for semantic search. Enrichment produces suggestions for review or configured automatic approval. It is optional: the documented default leaves language-model enrichment disabled until enabled by the operator.

The [AI surfaces guide](https://github.com/eonity-org/tydal/blob/main/docs/architecture/AI_SURFACES.md) explains provider configuration and the distinction between enrichment and external AI clients connected through MCP.

## Vault access

Each Vault defines the resources, content and operations it exposes. Read the [Vault specification](https://github.com/eonity-org/tydal/blob/main/docs/architecture/VAULT_SYSTEM.md) for purposes, access policies and addressing, and [Vault write methods](https://github.com/eonity-org/tydal/blob/main/docs/architecture/VAULT_WRITE_METHODS.md) for supported writes.
