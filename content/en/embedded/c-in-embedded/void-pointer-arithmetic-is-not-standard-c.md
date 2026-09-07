---
id: emb-cppfound-0025
title: "Is this legal in standard C?"
description: "Pointer arithmetic on void is a constraint violation in standard C because sizeof(void) is undefined; cast to a concrete type first."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Question code

```c
void *p = malloc(10);
p++;
```

## Short answer

<span class="warn">NO, this is not valid standard C</span> (constraint violation). The standard forbids pointer arithmetic on `void*` – the element size is unknown (sizeof(void) is undefined), so the compiler must issue a diagnostic.

GCC allows it as an extension: it treats `sizeof(void) = 1`, so `p++` -> +1 byte. With `-pedantic-errors`: an error.

Correct approach: before arithmetic, cast to a concrete type: `uint8_t *bp = (uint8_t*)p; bp++;`[^embeddedinterviewlab]

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
