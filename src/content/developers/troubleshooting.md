---
title: Troubleshooting
description: Known issues, diagnostic steps and verified solutions.
section: Reference
order: 50
status: ready
---

## Installation and service issues

Start with the common issues and operational commands in the [deployment guide](https://github.com/eonity-org/tydal/blob/main/DEPLOYMENT.md). Check the guide for your installation mode and the services involved in the failing operation.

## AI and processing

For enrichment that does not run, check the configured feature flags, provider settings and queue worker against the [AI surfaces guide](https://github.com/eonity-org/tydal/blob/main/docs/architecture/AI_SURFACES.md). Enrichment and embeddings have separate configuration; an external MCP client also has its own model configuration.

## MCP and Vault access

Use [Connecting an AI Client](https://github.com/eonity-org/tydal/blob/main/docs/CONNECTING_MCP_CLIENTS.md) for client setup. For unavailable content or operations, compare the connected Vault's policy and credentials with the [Vault MCP guide](https://github.com/eonity-org/tydal/blob/main/vault-mcp/README.md). Write tools require a write key and a supported operation.

## Report a problem

Follow the [contribution guide](https://github.com/eonity-org/tydal/blob/main/docs/CONTRIBUTING.md) when opening an issue. Include the version, setup, reproduction steps, expected behavior and relevant diagnostic output without credentials. Report security vulnerabilities through the [security policy](https://github.com/eonity-org/tydal/blob/main/docs/SECURITY.md).
