---
id: emb-cppfound-0035
title: "Trap: `int *p = NULL; if(p) *p = 5;` vs `int *p = NULL; *p = 5;` – чи безпечний перший?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Перший – безпечний**. `if(p)` ≡ `if(p != NULL)` – перевірка перед розіменуванням. Якщо `p == NULL` -> умова false, `*p` не виконується.

<span class="warn">Другий – undefined behavior (UB)</span>: `*p = 5` при `p == NULL` -> HardFault на Cortex-M.

Але: перевірка NULL не захищає від dangling pointer або wild pointer – вони ненульові, але невалідні; NULL-check – необхідна, але недостатня умова безпеки.[^embeddedinterviewlab]

## Detailed explanation

TODO
