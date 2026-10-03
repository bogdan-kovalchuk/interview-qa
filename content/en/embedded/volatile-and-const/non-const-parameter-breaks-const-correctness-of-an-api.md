---
id: emb-volconst-0028
title: "Trap: what is wrong with this API?"
description: "A read-only buffer parameter should be const-qualified so the API can accept const data safely."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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
---

## Question code

```c
void uart_send(uint8_t *data, size_t len);
const uint8_t msg[] = { 0x55, 0xAA };
uart_send(msg, 2);
```

## Short answer

<span class="warn">The API loses const-correctness.</span>

If `uart_send` only reads the buffer, declare its parameter as `const uint8_t *data`. Otherwise passing a `const` buffer causes a pointer type incompatibility; explicitly casting away `const` does not make a write valid and can hide a bug.

Declare read-only input parameters as `const T *` so the signature matches the function's behavior.[^iso-c-n1570]

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
