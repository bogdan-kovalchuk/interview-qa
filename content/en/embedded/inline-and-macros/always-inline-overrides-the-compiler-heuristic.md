---
id: emb-macros-0032
title: "What does `__attribute__((always_inline))` do and when is it needed?"
description: "Forces the compiler to inline a function even when its heuristics would choose a regular call."
track: embedded
section: inline-and-macros
level: junior
type: concept
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

**Forces the compiler to inline a function** even when its heuristics would choose a regular call (usually used together with `inline`).

In embedded this is needed for tiny register-access wrappers, latency-critical sections, or when a call in a hot path/ISR (interrupt service routine) is unacceptable. The opposite is `__attribute__((noinline))`.

Rule: `inline` is a hint the compiler can ignore; `always_inline` is a directive. Do not overuse: code bloat hurts I-cache and flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
