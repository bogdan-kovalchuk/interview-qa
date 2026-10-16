---
id: emb-align-0032
title: "How do you correctly send data between two different MCUs?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Define an explicit wire format and serialize field by field with explicit byte order.**

The format defines fields, widths, byte order, signedness, versioning, and length checks. Do not send a struct as raw bytes across different ABIs: padding, alignment, and type representations can differ. `htonl`/`htons` cover 32- and 16-bit values in network byte order; they are not general encoders.[^iso-c-n1570]

An explicit specification and matching encoders/decoders remove dependence on a particular struct layout; portability still depends on the types and rules the format defines.[^iso-c-n1570]

## Detailed explanation

TODO
