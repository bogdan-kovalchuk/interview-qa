---
id: py-site-9002
title: Why must internal links include the project base path?
description: A fixture for production link and resolver verification.
track: python
section: fundamentals
level: junior
type: concept
tags: [site-spike, base-path]
status: published
updated: 2026-09-03
content_revision: 1
anki:
  export: true
sources:
  - title: Astro configuration reference
    url: https://docs.astro.build/en/reference/configuration-reference/
    accessed: 2026-09-03
    kind: official
---

## Short answer

A GitHub Pages project site is served below the repository name, so root-relative project links need the `/interview-qa/` prefix.

## Detailed explanation

The production build applies the configured base path to Starlight assets and navigation. The mirror materializes question links with the same prefix.

## Sources

Generated from frontmatter for the spike.
