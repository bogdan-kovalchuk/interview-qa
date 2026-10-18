---
id: emb-cppfound-0070
title: "Що поверне `strlen(s)` і `sizeof(s)` якщо `char s[20] = \"hello\"`?"
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

`strlen(s)` -> **5**: рахує символи до '\0' (не включаючи) – runtime функція.

`sizeof(s)` -> **20**: розмір масиву оголошений при компіляції – весь буфер, незалежно від вмісту. Compile-time операція.

Рядок "hello" займає 6 байт (`h,e,l,l,o,\0`), решта 14 байт – нулі (через `= "hello"` ініціалізацію масиву); `sizeof(s)/sizeof(s[0]) = 20/1 = 20` – ємність буфера.[^embeddedinterviewlab]

## Detailed explanation

TODO
