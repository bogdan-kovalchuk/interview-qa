---
id: emb-align-0013
title: "Trap: чому не можна казати «endianness не важлива на ARM, бо там завжди little-endian»?"
description: "Arm-системи й зовнішні формати можуть мати різний порядок байтів, тому код має спиратися на специфікації конкретної платформи та інтерфейсу."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: arm-library-endianness
    title: "Selection of Arm C and C++ library variants based on build options"
    url: https://developer.arm.com/documentation/dui0475/latest/the-arm-c-and-c---libraries/c-and-c---runtime-libraries/selection-of-arm-c-and-c---library-variants-based-on-build-options
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Документація Arm показує, що вибір бібліотеки розрізняє little-endian і big-endian варіанти збірки."
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Визначає big-endian network byte order для мережевих типів і перетворень POSIX."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення явного виділення та складання байтів."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткова українська дорожня карта; не є нормативним джерелом щодо Arm або порядку байтів протоколу."
---

## Short answer

<span class="warn">Екосистема Arm охоплює little-endian і big-endian конфігурації, а зовнішній формат даних може мати інший порядок, ніж процесор.</span>

Конкретний мікроконтролер, однак, має певний реалізований і налаштований порядок байтів. Internet network byte order є big-endian, але payload польових шин і формати файлів дотримуються власних специфікацій; наприклад, CAN transport сам собою не задає єдиного універсального порядку цілих чисел у payload.

Захист: називай обидві сторони межі – host order цільової платформи та визначений порядок зовнішнього формату – і конвертуй лише там, де це потрібно.[^embeddedinterviewlab]

## Detailed explanation

«Arm» позначає сімейство архітектур, а не одну фіксовану конфігурацію плати. Toolchain і runtime library мають окремі little-endian та big-endian варіанти,[^arm-library-endianness] тоді як обрані MCU, reset-конфігурація, ABI і toolchain визначають фактичний порядок конкретного firmware image. Тому ні «Arm завжди little-endian», ні «кожен Arm-чип може перемикатися під час виконання» не є безпечним твердженням.

Порядок байтів на інтерфейсі – незалежний контракт. POSIX визначає network byte order із найстаршим octet першим і надає host/network перетворення.[^posix-byte-order] Це обґрунтовує твердження про IP networking API, але не тезу, що кожен протокол є big-endian. Register map периферії, CAN application payload, послідовність Modbus-регістрів, binary file або власний packet можуть задавати інший порядок чи окремо визначати порядок байтів, слів і бітів.

Перетворення потрібне лише для багатобайтових полів, зовнішній порядок яких відрізняється від host representation. Однобайтовим полям byte-order conversion не потрібне. Явні shifts і masks – один із переносних способів декодування; матеріал LearnCpp про bitwise operations пояснює ці операції.[^learncpp-bitwise]

## Symptom

Firmware працює на little-endian платі розробника, але читає переставлені lengths, timestamps або значення регістрів, коли дані надходять з іншої реалізації чи інтерфейсу.

## Why it happens

Код сприймає локальне object representation як representation протоколу. Також він підміняє специфікації конкретного пристрою і протоколу широкими ярликами на кшталт «Arm» або «network».

## How to avoid

Документуй порядок байтів для кожного багатобайтового поля, застосовуй іменовані encode/decode helpers на межі та тестуй їх фіксованими байтовими векторами. Використовуй `htonl`/`ntohl` лише там, де потрібним контрактом є POSIX network order; в інших випадках реалізуй формат, названий у специфікації пристрою чи протоколу. Дорожня карта aCode є корисним додатковим орієнтиром для подальшого вивчення C і C++.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->
