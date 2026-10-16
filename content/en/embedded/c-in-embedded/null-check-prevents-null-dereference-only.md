---
id: emb-cppfound-0035
title: "Trap: `int *p = NULL; if(p) *p = 5;` vs `int *p = NULL; *p = 5;` – is the first safe?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**The first is safe**. `if(p)` ≡ `if(p != NULL)` – a check before dereferencing. If `p == NULL` -> the condition is false, `*p` is not executed.

<span class="warn">The second is undefined behavior</span>: `*p = 5` when `p == NULL` -> HardFault on Cortex-M.

However: a NULL check does not protect against a dangling pointer or a wild pointer – they are non-null but invalid; a NULL check is necessary but not sufficient for safety.[^embeddedinterviewlab]

## Detailed explanation

TODO
