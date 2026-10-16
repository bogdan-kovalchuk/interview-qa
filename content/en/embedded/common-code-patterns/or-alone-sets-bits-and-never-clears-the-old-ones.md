---
id: emb-patterns-0034
title: "Trap: why is `reg |= (value << SHIFT)` without clearing the mask a bug?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">OR only sets bits but does not clear old ones</span> – if the field already had a value, the new one is layered on top.

For example, the old field is `0b110`, we write `0b001` via `|=` -> we get `0b111`, not `0b001`.

Defense: first `reg &= ~MASK;`, then `reg |= (value << SHIFT) & MASK;` – a full read-modify-write when the datasheet permits this access.[^iso-c-n1570]

## Detailed explanation

TODO
