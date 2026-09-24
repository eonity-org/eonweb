---
title: API and integrations
description: Reference material for repository APIs, Vault interfaces and MCP connections.
section: Build and configure
order: 30
status: ready
---

## Build an application

The management API works with resources, collections and workspaces. Vault interfaces expose selected content with the context and access rules of a particular Vault.

Use the [OpenAPI specification](https://github.com/eonity-org/tydal/blob/main/backend/docs/openapi.yaml) for management endpoints and the [Vault specification](https://github.com/eonity-org/tydal/blob/main/docs/architecture/VAULT_SYSTEM.md) for Vault addressing and operations. The [TypeScript SDK](https://github.com/eonity-org/tydal/blob/main/client/README.md) provides application clients for both management and Vault consumption.

## Choose an AI connection

### Enrichment inside Tydal

Tydal can propose descriptions, tags and other metadata using configured AI providers. Suggestions go through review or configured automatic approval. See [AI surfaces](https://github.com/eonity-org/tydal/blob/main/docs/architecture/AI_SURFACES.md) for the enrichment pipeline and provider choices.

### Organization MCP

Use [Organization MCP](https://github.com/eonity-org/tydal/blob/main/org-mcp/README.md) when an agent needs to manage resources, upload files, update metadata or curate workspaces. Its access follows the organization token and granted permissions; authorized writes apply final values directly.

### Vault MCP

Use [Vault MCP](https://github.com/eonity-org/tydal/blob/main/vault-mcp/README.md) to connect an external AI client to one curated context. It is read-only by default. A write key enables supported operations exposed by the Vault's purpose, such as ingesting derived content into an AI Vault.

Read the [AI client connection guide](https://github.com/eonity-org/tydal/blob/main/docs/CONNECTING_MCP_CLIENTS.md) for supported local MCP clients and configuration. The supplied servers use local stdio connections; check the guide for your client's transport requirements.

## Authentication and capabilities

Management clients and organization MCP use organization-scoped API credentials. Vault access depends on its policy: public access, Vault keys or supported signed links. A Vault connection does not grant organization-wide management access. Follow the authentication examples in the relevant API, SDK or MCP guide.
