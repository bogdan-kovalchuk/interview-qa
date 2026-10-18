---
id: emb-cppfound-0061
title: "Trap: що не так?"
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

## Question code

```c
int *p = malloc(sizeof(int)*10);
free(p);
printf("%d", p[0]);
```

## Short answer

<span class="warn">Use-after-free – undefined behavior.</span> Після `free(p)` пам'ять повернута heap manager-у і може бути негайно перевикористана (наприклад, наступним `malloc`).

`p[0]` після `free`: може повернути 0 (heap manager записав туди metadata), старе значення, або crash. У security контексті: джерело use-after-free exploits.

Захист: `free(p); p = NULL;`, потім `if(p != NULL)` перед доступом.[^embeddedinterviewlab]

## Detailed explanation

TODO
