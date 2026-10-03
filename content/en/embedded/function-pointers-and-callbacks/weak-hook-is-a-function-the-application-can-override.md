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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-weak-attribute
    title: "GCC: Common Function Attributes – weak"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "GCC current documentation"
    applicability: "Describes GNU weak attribute and override support on supported ELF/a.out toolchains; this is a compiler extension, not an ISO C guarantee."
---

## Short answer

**A weak hook** is a function with a weak symbol that an application can override with a strong implementation on a toolchain supporting that linker semantics.[^gcc-weak-attribute]

On supported ELF or a.out targets, a GCC declaration with `__attribute__((weak))` emits a weak symbol; a strong definition of the same symbol can override it at link time.[^gcc-weak-attribute]

This is a GNU/toolchain-specific mechanism, not an ISO C property. It is convenient for startup defaults; runtime multiple instances usually need explicit callback registration with context.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
