---
id: emb-dtypes-0040
title: "What does `sizeof(void*)` return on a 32-bit versus a 64-bit platform?"
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

Common ABIs use 4-byte `sizeof(void*)` on 32-bit systems and 8 bytes on 64-bit systems, but the C standard does not derive pointer size from an architecture label.[^iso-c-n1570] A platform's address model affects pointer representation, while the implementation determines the exact value. Check `sizeof` with the target toolchain and do not hard-code a size in portable code.[^iso-c-n1570]

## Detailed explanation

TODO
