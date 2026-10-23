---
layout: ../layouts/ContentLayout.astro
title: Structure and meaning for people and AI.
description: Eonity builds open-source tools that give AI a clear scope to work in, so people and AI can work on the same content together, with people in the loop.
label: About Eonity
updated: 2026-10-23
---

AI can do real work on content: describe a collection, build a page, lay out a document. It does that work best when it knows what it is working on and where its work ends. Eonity's tools make both explicit.

## Structure and meaning

Every Eonity tool starts from structure. In **TYDAL**, schemas define what a resource is, how it is described and how it is found. In **TYKERF**, a web page is a tree of named blocks. In **Tyset**, a document's text flows through the frames of master pages, and every format comes from a catalog.

Structure gives content a meaning that people and AI can both read. When a person and an AI point at the same named thing, they can talk about it, change it and check the result.

## A scope for the AI

Each tool gives the AI a defined area to work in and the moves it may make there:

| Tool       | Content        | The AI's scope          | Its moves                         |
| ---------- | -------------- | ----------------------- | --------------------------------- |
| **TYDAL**  | Digital assets | A Vault                 | Read, search and propose metadata |
| **TYKERF** | Web pages      | A block of a page       | Split, move, resize and rewrite   |
| **Tyset**  | Documents      | A section of a document | Write, format and restructure     |

The tools offer these moves through MCP, so Claude and other AI clients get the same scoped tools the products use themselves.

## People in the loop

The AI proposes; people decide. TYDAL's AI suggestions can be reviewed before they are applied. Every TYKERF move is validated before it changes the page, and every change can be undone step by step. The same principle will guide Tyset.

## The tools

- **[TYDAL](/tydal/)**, the typed Digital Asset Layer, organizes, enriches and shares digital resources through Vaults. Read [About TYDAL](/tydal/about/) for its model. [FullFrame](/developers/fullframe/), a photography exhibition client, is built on it.
- **[TYKERF](/tykerf/)** makes complex web pages understandable and editable, and lets AI change one clearly scoped block at a time.
- **Tyset** brings the same approach to desktop publishing. It is a document editor in which text flows through the frames of master pages and the AI writes and edits one section at a time. It arrives in the coming weeks.

The **TY** in their names comes from Eoni**ty** and marks them as one family.

## Open source

Eonity's tools are open source under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). The code lives in the [eonity-org organization on GitHub](https://github.com/eonity-org). They are built for developers and early adopters; services, support, implementation and hosted capabilities can support their development.

## Get in touch

Follow [Eonity on X](https://x.com/eonity_org) for the projects' development, or write to [develop@eonity.org](mailto:develop@eonity.org).
