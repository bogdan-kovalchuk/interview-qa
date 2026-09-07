---
id: emb-macros-0035
title: "Trap: how can a macro break apparently unrelated code in another file?"
description: "A macro has no scope and replaces every occurrence of its identifier in all subsequent lines and included files."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

<span class="warn">A macro has no scope</span> – after `#define` it replaces every occurrence of the identifier in all subsequent lines and included files.

Classic case: `#define max(a,b) ...` in a header breaks `std::max`, the field `obj.max`, or a local variable `max` in any code that includes that header (a typical pain with `min`/`max` in Windows headers).

Protection: for macros use UPPER_CASE names with a project prefix; avoid names that look like ordinary identifiers; use `#undef` when needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
