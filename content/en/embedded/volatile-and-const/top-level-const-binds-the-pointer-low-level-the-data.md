---
id: emb-volconst-0040
title: "What are top-level and low-level `const` in a pointer type?"
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

**Top-level `const` qualifies the pointer object itself; low-level `const` qualifies the pointed-to data.**

In `int * const p`, the top-level const means `p` cannot be reassigned. In `const int *p`, the low-level const means `*p` cannot be modified through `p`. For an API, low-level const matters more because it describes what the function does with the caller's data.

Rule: `const` after `*` qualifies the pointer, while `const` before the base type qualifies the pointed-to data.[^iso-c-n1570]

## Detailed explanation

TODO
