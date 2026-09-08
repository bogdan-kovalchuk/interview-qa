---
id: emb-align-0015
title: "Що повертає `htonl()` на big-endian хості?"
description: "На відповідному стандарту big-endian host функція htonl повертає те саме числове значення, бо host і network order збігаються."
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
  - source_id: posix-htonl
    title: "htonl, htons, ntohl, ntohs"
    url: https://pubs.opengroup.org/onlinepubs/000095399/functions/htonl.html
    accessed: 2026-09-08
    kind: spec
    version: "The Open Group Base Specifications Issue 6"
    applicability: "Нормативна специфікація POSIX для перетворень host-to-network і network-to-host."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення переставляння байтів, потрібного за іншого host order."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткова українська дорожня карта; не є нормативним джерелом щодо htonl."
---

## Short answer

**Те саме числове значення – host order уже відповідає network order.**

На big-endian host реалізація може зробити `htonl` identity macro або function. На little-endian host вона зазвичай переставляє байти. Caller має використовувати `htonl` на мережевій межі в обох випадках, не перевіряючи платформу самостійно.

Правило: ніколи не роби byte swap «вручну за умовою платформи», якщо є `hton*`/`ntoh*`.[^embeddedinterviewlab]

## Detailed explanation

POSIX визначає `htonl` як перетворення з host byte order у network byte order, а не як безумовний byte swap.[^posix-htonl] Отже, якщо host уже зберігає 32-бітне значення в тому самому порядку з найстаршим octet першим, перетворений результат має те саме числове значення і representation.

Ця різниця важлива, бо правило «завжди переставляй» помилкове. Самописний безумовний swap працює на little-endian host, але псує значення на big-endian host. І навпаки, пропуск `htonl` через те, що поточна платформа little-endian, відправляє host representation замість network representation.

Залишай перетворення на межі інтерфейсу:

- викликай `htonl`, формуючи 32-бітне поле, визначене в network order;
- копіюй отримані байти в message, не покладаючись на layout структури;
- копіюй отримані байти в належно вирівняний 32-бітний об'єкт і викликай `ntohl` перед використанням значення.

Функція охоплює одне 32-бітне unsigned integer. Вона не конвертує 64-бітні значення, floating-point objects, масиви чи цілу структуру, і її не слід застосовувати двічі до того самого поля. Іншим форматам потрібні helpers, що реалізують визначений ними порядок.

Bitwise operations пояснюють переставляння, яке реалізація може застосувати на host із невідповідним порядком,[^learncpp-bitwise] а дорожня карта aCode є додатковим орієнтиром для ширшого вивчення C і C++.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->
