---
id: emb-cppfound-0053
title: "Що поверне `sizeof(\"hello\")` vs `sizeof(char*)` на 32-bit?"
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

`sizeof("hello")` -> **6**: рядковий літерал – масив `{'h','e','l','l','o','\0'}`, і `sizeof` повертає розмір масиву включно з null-terminator.

`sizeof(char*)` -> **4**: розмір вказівника = розрядність платформи.

Важливо: `sizeof("hello")` не decay-ується до вказівника (sizeof – одне з трьох виключень array decay), тому отримуємо розмір масиву.[^embeddedinterviewlab]

## Detailed explanation

TODO
