---
id: emb-volconst-0057
title: "Trap: are `const volatile uint32_t *` and `volatile const uint32_t *` the same?"
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

**Yes, `const volatile uint32_t *` and `volatile const uint32_t *` have the same type.**

Both types mean pointer to const volatile `uint32_t`. The data behind the pointer cannot be written through this lvalue, but reads must be volatile. The important thing is not to confuse this with `const volatile uint32_t * const`, where the extra `const` after `*` protects the pointer itself.

Rule: the order of cv-qualifiers at one type level does not change their meaning; what matters is which level of the pointer chain they apply to.[^iso-c-n1570]

## Detailed explanation

TODO
