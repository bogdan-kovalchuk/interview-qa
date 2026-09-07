---
id: emb-volconst-0030
title: "Trap: what is unsafe about `char *p = \"OK\"; p[0] = 'N';`?"
description: "Writing to a string literal has undefined behavior."
track: embedded
section: volatile-and-const
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

<span class="warn">Writing to a string literal has undefined behavior.</span>

In C, a string literal often resides in a read-only region such as `.rodata` in Flash. Historically, C allows assigning a literal to `char *` with a warning on some compilers, but modifying the object through that pointer is semantically forbidden and can cause a HardFault on an MCU.

Protection: use `const char *p = "OK";` or a mutable array: `char p[] = "OK";`.[^embeddedinterviewlab]

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
