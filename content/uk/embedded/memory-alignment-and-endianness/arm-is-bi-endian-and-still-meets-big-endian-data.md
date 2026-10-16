---
id: emb-align-0013
title: "Trap: чому не можна казати «endianness не важлива на ARM, бо там завжди little-endian»?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-library-endianness
    title: "Selection of Arm C and C++ library variants based on build options"
    url: https://developer.arm.com/documentation/dui0475/latest/the-arm-c-and-c---libraries/c-and-c---runtime-libraries/selection-of-arm-c-and-c---library-variants-based-on-build-options
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

<span class="warn">Екосистема Arm охоплює little-endian і big-endian конфігурації, а зовнішній формат даних може мати інший порядок, ніж процесор.</span>

Конкретний мікроконтролер, однак, має певний реалізований і налаштований порядок байтів. Internet network byte order є big-endian, але payload польових шин і формати файлів дотримуються власних специфікацій; наприклад, CAN transport сам собою не задає єдиного універсального порядку цілих чисел у payload.

Захист: називай обидві сторони межі – host order цільової платформи та визначений порядок зовнішнього формату – і конвертуй лише там, де це потрібно.[^embeddedinterviewlab]

## Detailed explanation

«Arm» позначає сімейство архітектур, а не одну фіксовану конфігурацію плати. Toolchain і runtime library мають окремі little-endian та big-endian варіанти,[^arm-library-endianness] тоді як обрані MCU, reset-конфігурація, ABI і toolchain визначають фактичний порядок конкретного firmware image. Тому ні «Arm завжди little-endian», ні «кожен Arm-чип може перемикатися під час виконання» не є безпечним твердженням.

Порядок байтів на інтерфейсі – незалежний контракт. POSIX визначає network byte order із найстаршим octet першим і надає host/network перетворення.[^posix-byte-order] Це обґрунтовує твердження про IP networking API, але не тезу, що кожен протокол є big-endian. Register map периферії, CAN application payload, послідовність Modbus-регістрів, binary file або власний packet можуть задавати інший порядок чи окремо визначати порядок байтів, слів і бітів.

Перетворення потрібне лише для багатобайтових полів, зовнішній порядок яких відрізняється від host representation. Однобайтовим полям byte-order conversion не потрібне. Явні shifts і masks – один із переносних способів декодування; матеріал LearnCpp про bitwise operations пояснює ці операції.[^learncpp-bitwise]

### Симптом

Firmware працює на little-endian платі розробника, але читає переставлені lengths, timestamps або значення регістрів, коли дані надходять з іншої реалізації чи інтерфейсу.

### Чому це стається

Код сприймає локальне object representation як representation протоколу. Також він підміняє специфікації конкретного пристрою і протоколу широкими ярликами на кшталт «Arm» або «network».

### Як цього уникнути

Документуй порядок байтів для кожного багатобайтового поля, застосовуй іменовані encode/decode helpers на межі та тестуй їх фіксованими байтовими векторами. Використовуй `htonl`/`ntohl` лише там, де потрібним контрактом є POSIX network order; в інших випадках реалізуй формат, названий у специфікації пристрою чи протоколу. Дорожня карта aCode є корисним додатковим орієнтиром для подальшого вивчення C і C++.[^acode-cpp-next]
