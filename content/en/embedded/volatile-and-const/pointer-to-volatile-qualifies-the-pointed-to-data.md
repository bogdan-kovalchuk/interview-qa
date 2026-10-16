---
id: emb-volconst-0009
title: "What does the declaration `volatile uint32_t *p` mean?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`p` is a pointer to volatile `uint32_t`**.

The pointer `p` itself can be changed: it can point to a different address. But every `*p` must be a real volatile access to the object. This is the normal form for accessing a hardware register when the address may be chosen at runtime.

Reading rule: start from the name `p`: `p` is pointer to volatile `uint32_t`.[^iso-c-n1570]

## Detailed explanation

TODO
