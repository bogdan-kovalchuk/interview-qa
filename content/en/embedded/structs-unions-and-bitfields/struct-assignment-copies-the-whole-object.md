---
id: emb-structs-0039
title: "How do assignment and `memcpy` differ for structs?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Structure assignment copies every struct member value**, but does not guarantee preservation of padding bytes.

`memcpy` copies the object representation byte by byte, including padding. The C standard allows padding bytes to take unspecified values when a struct value is stored, so assignment and `memcpy` do not promise the same in-memory representation.

Use assignment to copy a struct in C. For wire or storage serialization, encode fields explicitly instead of relying on padding or compiler-specific layout.[^iso-c-n1570]

## Detailed explanation

TODO
