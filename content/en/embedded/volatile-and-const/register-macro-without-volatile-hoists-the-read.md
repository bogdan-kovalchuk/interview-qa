---
id: emb-volconst-0007
title: "Trap: what is wrong with this polling code?"
description: "The hardware register access is missing volatile, so the compiler can cache the first read and polling may hang."
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

## Question code

```c
#define UART_SR (*( uint32_t *)0x40011000)

while ((UART_SR & 0x20) == 0) { }
```

## Short answer

<span class="warn">The hardware register access is missing `volatile`.</span>

`UART_SR` dereferences a plain `uint32_t *`, so the compiler can cache the first read value of the status register and never re-read the peripheral. In a release build, polling may hang or see stale state.

Mitigation: `#define UART_SR (*(volatile uint32_t *)0x40011000u)`. In vendor headers, every register field in a struct overlay must be volatile-qualified.[^embeddedinterviewlab]

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
