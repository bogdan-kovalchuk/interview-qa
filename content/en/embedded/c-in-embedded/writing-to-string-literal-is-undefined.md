---
id: emb-cppfound-0011
title: "Trap: what happens?"
description: "A string literal lives in read-only memory so modifying it is undefined behavior causing a segfault or HardFault; use a character array instead so the compiler copies the string into writable memory."
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
    applicability: "Origin of the question and answer; answer not independently verified."
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
char *s = "hello";
s[0] = 'H';
```

## Short answer

The string literal `"hello"` is stored in **.rodata** (Flash/read-only). `s` points to this read-only region.

Writing `s[0] = 'H'` -> <span class="warn">undefined behavior</span>: on a PC – segfault, on an MCU – HardFault (if MPU protects Flash) or a silent write into Flash (which won't work).

Correct: `char arr[] = "hello";` – the compiler copies the string into a writable array (stack or .data). Then `arr[0] = 'H'` is legal.[^embeddedinterviewlab]

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
