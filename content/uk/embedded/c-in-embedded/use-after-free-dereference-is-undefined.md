---
id: emb-cppfound-0046
title: "Trap: що не так?"
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

## Question code

```c
free(ptr);
if(*ptr == 0)
```

## Short answer

<span class="warn">Use-after-free – undefined behavior.</span> Після `free(ptr)` блок пам'яті повертається heap manager-у і може бути одразу перевикористаний.

Читання `*ptr` -> UB: може повернути 0, старе значення або нове значення від іншого malloc. У реальному коді – джерело security vulnerabilities (type confusion, heap exploitation).

Правило: після `free` завжди: `ptr = NULL;`; `if(ptr != NULL && *ptr == 0)` – тоді безпечно.[^embeddedinterviewlab]

## Detailed explanation

TODO
