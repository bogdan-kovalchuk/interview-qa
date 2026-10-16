---
id: emb-cppfound-0070
title: "What do `strlen(s)` and `sizeof(s)` return for `char s[20] = \"hello\"`?"
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

`strlen(s)` -> **5**: counts characters up to '\0' (not including it) – a runtime function.

`sizeof(s)` -> **20**: the array size declared at compile time – the entire buffer, regardless of content. A compile-time operation.

The string "hello" occupies 6 bytes (`h,e,l,l,o,\0`), the remaining 14 bytes are zeros (due to `= "hello"` array initialization); `sizeof(s)/sizeof(s[0]) = 20/1 = 20` – the buffer capacity.[^embeddedinterviewlab]

## Detailed explanation

TODO
