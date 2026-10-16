---
id: emb-structs-0040
title: "Trap: why is `memcmp(&a, &b, sizeof a)` a bad way to compare structs?"
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

<span class="warn">Because padding bytes may differ even when all fields are equal.</span> Padding is not part of member values, and the C standard allows it to take unspecified values when a struct value is stored. `memcmp` compares raw bytes, so it may find different representations in structs whose fields have equal values.

Defence: compare fields explicitly or normalize the serialization format. Do not expose padding bytes in security-sensitive output.[^iso-c-n1570]

## Detailed explanation

TODO
