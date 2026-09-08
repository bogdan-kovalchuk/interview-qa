---
id: emb-align-0014
title: "Чому network byte order – це big-endian і як з ним працювати?"
description: "POSIX network byte order є big-endian і надає htonl, ntohl, htons та ntohs для перетворення."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Визначає network byte order і модель перетворення мережевих даних."
  - source_id: posix-htonl
    title: "htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Нормативна специфікація POSIX для 16- і 32-бітних функцій перетворення host/network."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення явного перетворення байтів."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткова українська дорожня карта; не є нормативним джерелом щодо network byte order."
---

## Short answer

**POSIX network byte order є big-endian: найстарший octet передається першим.**

POSIX (Portable Operating System Interface) дає конвертери host vs network: 

```c
uint32_t net = htonl(host);
uint32_t host_again = ntohl(net);
```

Для 16-бітних – `htons`/`ntohs`.

Правило: конвертуй поля, API або протокол яких визначає network byte order; не припускай, що його використовує кожен wire-протокол.[^embeddedinterviewlab]

## Detailed explanation

Network byte order дає системам зв'язку одне представлення незалежно від їхнього host order. POSIX визначає його з найстаршим octet першим і рекомендує передавати байтові дані безпосередньо, а для 16- і 32-бітних цілих даних виконувати host/network conversion.[^posix-byte-order]

Пари функцій мають визначений напрямок і симетричне застосування:

- `htonl` перетворює 32-бітне unsigned-значення з host order у network order, а `ntohl` повертає його назад.
- `htons` і `ntohs` виконують відповідну операцію для 16-бітних unsigned-значень.[^posix-htonl]

На little-endian host реалізація зазвичай змінює byte representation. На big-endian host, порядок якого вже відповідає network order, це може бути identity operation. Application code має викликати функцію в обох випадках, адже інтерфейс документує намір і зберігає переносність коду.

Ці функції не серіалізують цілу C-структуру. Структура може містити padding, а widths чи layout її членів можуть відрізнятися між ABI. Перетворюй кожне визначене integer field, а потім копіюй його байти до message buffer або з нього, не створюючи невирівняний типізований вказівник. Також інший протокол може явно вибрати little-endian або визначити складніший layout; його власна специфікація має пріоритет.

Огляд bitwise operations на LearnCpp допомагає зрозуміти, що обчислює byte-order conversion,[^learncpp-bitwise] а дорожня карта aCode є додатковим орієнтиром для ширшого вивчення C і C++.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->
