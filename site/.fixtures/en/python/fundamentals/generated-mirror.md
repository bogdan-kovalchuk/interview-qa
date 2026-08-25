---
id: py-site-9001
title: How does the generated content mirror work?
description: A fixture that proves Starlight consumes generated Markdown.
track: python
section: fundamentals
level: junior
type: concept
tags: [site-spike, mirror]
status: published
updated: 2026-09-03
content_revision: 1
anki:
  export: true
sources:
  - title: Astro Starlight documentation
    url: https://starlight.astro.build/
    accessed: 2026-09-03
    kind: official
---

## Short answer

The Python tool copies source Markdown into Starlight's standard docs collection and adds computed routing metadata.

## Detailed explanation

Starlight reads only the generated mirror through `docsLoader`. The source tree remains independent of Astro.

## Follow-up

- [How are base-path links kept valid?](qid:py-site-9002)

## Sources

Generated from frontmatter for the spike.
