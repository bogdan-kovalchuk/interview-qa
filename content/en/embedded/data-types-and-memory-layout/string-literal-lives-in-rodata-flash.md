---
id: emb-dtypes-0035
title: "Where does the string literal `\"Hello, World!\"` live in an embedded program's memory?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

In a typical embedded build, a string literal often resides in a read-only section such as `.rodata` mapped to Flash, but this depends on the toolchain and linker script rather than being guaranteed by C.

The same string is used only once (deduplication is compiler-dependent).

<span class="warn">Separate object</span>: `char arr[] = "hello";` creates a modifiable array containing a copy of the characters; an automatic local array is usually on the stack, while a static array is in writable static storage. Check the target build's map file.[^iso-c-n1570]

## Detailed explanation

TODO
