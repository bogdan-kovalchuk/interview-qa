---
id: emb-macros-0031
title: "Trap: why can `inline` without `static` produce a linker error in C?"
description: "In C99+ a bare inline function provides only an inline definition and creates no external symbol for the linker."
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

In C99+, a function declared as just `inline` (without `static`/`extern`) provides only an inline definition; it <span class="warn">does not create an external symbol</span>.

If the compiler decides at some point not to inline and makes a regular call, the linker will not find an external definition -> `undefined reference`.

Protection: in a header write `static inline` – each translation unit (TU) gets its own definition, and no linkage problem arises. (In C++ the semantics of `inline` are different and safer.)[^embeddedinterviewlab]

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
