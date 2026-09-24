---
title: Getting started
description: Prepare a development environment and run your first Tydal instance.
section: Start here
order: 10
status: ready
---

## Run your own instance

Tydal includes a Laravel API, a React frontend and backing services for storage, processing and search. The [deployment guide](https://github.com/eonity-org/tydal/blob/main/DEPLOYMENT.md) is the maintained reference for prerequisites and installation, including development on Docker-only hosts and production deployment.

Follow its sequence: install, configure your environment, start the services, then seed the instance. Choose the documented setup that matches your environment; optional AI providers and MCP connections can be configured afterward.

## Understand your first resource

A resource can represent one file or several related files. Collection schemas define its structure, workspaces curate selections, and Vaults make those selections available with their own context and access rules.

Before importing content, read [the resource model](https://github.com/eonity-org/tydal/blob/main/docs/architecture/RESOURCE_MODEL.md). For provisioning and ingestion commands, use the [CLI guide](https://github.com/eonity-org/tydal/blob/main/docs/CLI.md).

## Connect to an existing instance

If you already have access to a running Tydal instance, you can connect an AI client without deploying another instance. Read [Connecting an AI Client](https://github.com/eonity-org/tydal/blob/main/docs/CONNECTING_MCP_CLIENTS.md) and choose the appropriate scope in [API and integrations](/developers/api-and-integrations/).
