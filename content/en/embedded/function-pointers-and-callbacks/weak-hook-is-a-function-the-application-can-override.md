---
id: emb-fnptr-0052
title: "What is a weak callback hook in embedded firmware?"
description: "A weak hook is a weak function that the application can override with a strong implementation."
track: embedded
section: function-pointers-and-callbacks
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

**A weak hook** is a weak function that the application can override with a strong implementation.

Startup files often have `void SysTick_Handler(void) __attribute__((weak));` or weak default handlers. If user code defines a function with the same name, the linker picks the user implementation.

Rule: weak hooks are simple for startup and board support, but for runtime multiple instances explicit callback registration is better.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
