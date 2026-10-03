---
id: emb-dtypes-0113
title: "Що таке little-endian і big-endian, і де це проявляється в embedded-системах?"
description: "Endianness визначає порядок байтів багатобайтового числа в пам’яті; в embedded це важливо для протоколів, периферії, образів Flash і налагодження."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: python-struct-byte-order
    title: "Python 3 struct module: byte order, size, and alignment"
    url: https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
    accessed: 2026-10-04
    kind: official
    version: "3"
    applicability: "Описує little-endian і big-endian у форматах серіалізації та застерігає не покладатися на native byte order під час обміну даними; не визначає порядок бітів конкретної периферії."
---

## Short answer

**Endianness** визначає порядок байтів багатобайтового числа в пам’яті: little-endian кладе молодший байт за нижчою адресою, big-endian – старший. В embedded це важливо під час обміну binary protocols, читання peripheral FIFOs, роботи з flash images і перегляду пам’яті в debugger; мережевий byte order зазвичай задають явно, незалежно від CPU.[^python-struct-byte-order] Порядок передавання бітів у SPI/I2C кадрі визначає периферійний протокол і це окрема властивість від byte order багатобайтового значення в пам’яті.[^iso-c-n1570]

## Detailed explanation

Endianness – це порядок байтів, яким багатобайтове значення розміщується в пам’яті або кодується в послідовність байтів. У little-endian молодший байт має нижчу адресу; у big-endian нижчу адресу має старший байт. Наприклад, `0x12345678` у пам’яті little-endian має байти `78 56 34 12`, а big-endian – `12 34 56 78`. Це не змінює числове значення, але змінює його подання як байтів.[^python-struct-byte-order]

Це розрізнення потрібне, коли firmware інтерпретує буфер із UART, читає байти з peripheral FIFO або розбирає запис у Flash: пристрій-відправник і код-одержувач мають погодити порядок байтів. Не можна просто привести адресу буфера до `uint32_t *` і вважати, що результат відповідає протоколу: окрім byte order, таке читання може мати проблеми з alignment та допустимим доступом до типізованого об’єкта. Надійніше явно зібрати значення з байтів або застосувати функцію перетворення з чітко заданим wire format.[^iso-c-n1570]

Порядок байтів у RAM – не те саме, що порядок передавання бітів у SPI чи I2C. Контролер SPI може передавати старший або молодший біт першим згідно з налаштуванням, а I2C визначає порядок бітів у байті; ці правила задає конкретний протокол/периферія. Їх потрібно звіряти з документацією контролера та специфікацією протоколу, і з них не можна вивести endianness CPU з одного осцилографічного кадру.[^iso-c-n1570]

**Приклад:** якщо протокол передає `0x1234` старшим байтом першим, байти буфера будуть `12 34` навіть на little-endian MCU. Код має скласти значення як `(b[0] << 8) | b[1]`, а не залежати від native layout процесора.[^python-struct-byte-order]

**Типова помилка:** вважати, що little-endian означає передачу молодшого біта першим. Endianness описує порядок байтів багатобайтового значення, а bit order і framing належать до протоколу. Так само не слід припускати, що всі MCU мають однаковий native byte order або що файл/пакет збереже його: формат обміну має задати порядок явно.[^python-struct-byte-order]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
