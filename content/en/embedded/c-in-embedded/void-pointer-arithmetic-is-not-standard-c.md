---
id: emb-cppfound-0025
title: "Is this legal in standard C?"
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
void *p = malloc(10);
p++;
```

## Short answer

<span class="warn">NO, this is not valid standard C</span> (constraint violation). The standard forbids pointer arithmetic on `void*` – the element size is unknown (sizeof(void) is undefined), so the compiler must issue a diagnostic.

GCC allows it as an extension: it treats `sizeof(void) = 1`, so `p++` -> +1 byte. With `-pedantic-errors`: an error.

Correct approach: before arithmetic, cast to a concrete type: `uint8_t *bp = (uint8_t*)p; bp++;`[^embeddedinterviewlab]

## Detailed explanation

TODO
