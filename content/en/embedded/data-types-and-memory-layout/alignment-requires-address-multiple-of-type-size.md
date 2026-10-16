---
id: emb-dtypes-0012
title: "What is alignment, and how does it affect data access?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Alignment is an implementation-defined address requirement for an object of a given type; it is not necessarily equal to the type's size. In C, `_Alignof(T)` reports the alignment requirement for type `T`.

Accessing an improperly aligned address may be slower or disallowed, depending on the processor, instruction, and memory region; not every core handles it the same way.[^iso-c-n1570]

## Detailed explanation

TODO
