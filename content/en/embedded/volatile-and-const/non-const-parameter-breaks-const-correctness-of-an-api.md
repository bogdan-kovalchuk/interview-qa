---
id: emb-volconst-0028
title: "Trap: what is wrong with this API?"
description: "The API loses const-correctness; a read-only buffer parameter should be const uint8t so callers can pass const data safely."
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
void uart_send(uint8_t *data, size_t len);
const uint8_t msg[] = { 0x55, 0xAA };
uart_send(msg, 2);
```

## Short answer

<span class="warn">The API loses const-correctness.</span>

If `uart_send` only reads the buffer, the parameter must be `const uint8_t *data`. Otherwise the caller cannot safely pass a `const` buffer from Flash/`.rodata`, and casting away const hides a potential write into read-only memory.

Fix: declare read-only input parameters as `const T *`. This is also a typical MISRA Rule 8.13 requirement.[^embeddedinterviewlab]

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
