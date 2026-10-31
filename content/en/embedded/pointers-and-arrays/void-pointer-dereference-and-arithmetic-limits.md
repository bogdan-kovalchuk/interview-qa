---
id: emb-cppfound-0014
title: "What is void* and what limitations does this pointer type have?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

**void*** – a type-erased pointer: it can hold the address of an object of any type without an explicit cast.

Limitations:
- <span class="warn">Cannot be dereferenced</span> without a cast: `*p` – compilation error;
- <span class="warn">Cannot undergo arithmetic</span> without a cast (C standard). GCC allows it as an extension (element size = 1 byte).

Uses: `malloc`/`free`, `memcpy`/`memset`, generic callbacks, `qsort`. In embedded: generic ISR handler tables.[^embeddedinterviewlab]

## Detailed explanation

TODO
