---
id: emb-macros-0049
title: "How does `inline` affect code size in embedded?"
description: "Inline removes call overhead but duplicates the function body at every call site, which can bloat flash on larger functions."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Inline removes call overhead but duplicates the function body at every call site.**

For tiny functions this often reduces code (the call is more expensive than the body). For larger or frequently called ones, it <span class="warn">bloats flash and pressures the I-cache</span>, sometimes slowing the system down.

Rule: `inline` small helpers; keep large functions as regular ones and trust the optimizer. On limited flash, weigh `-Os` against the actual map file.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
