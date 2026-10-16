---
id: emb-volconst-0050
title: "Trap: can you pass a `const uint8_t *` to a function expecting `uint8_t *`?"
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

<span class="warn">Without a compiler diagnostic this is not allowed; a cast does not make writes legal for an actually const object.</span>

A `const uint8_t *` argument passed where `uint8_t *` is required violates C's type constraint and requires a diagnostic. Casting away the qualifier and writing has undefined behavior if the original object was actually defined `const`; otherwise the write may be permitted, but the API hides intent.[^iso-c-n1570]

Separate the API: input buffer as `const uint8_t *`, output buffer as `uint8_t *`. Do not strip the qualifier without checking whether the original object is modifiable.[^iso-c-n1570]

## Detailed explanation

TODO
