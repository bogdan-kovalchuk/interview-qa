---
id: emb-dtypes-0108
title: "Як безпечно парсити binary protocol frame без невалідного type punning і проблем alignment?"
description: "Перевірити довжину frame, потім читати кожне поле з uint8_t буфера через memcpy або byte shifts. Для multi-byte полів явно застосувати le16toh/ntohs. Не кастити wire-format buffer у struct."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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
---

## Short answer

Перевірити довжину frame, потім читати кожне поле з `uint8_t` буфера через `memcpy` або byte shifts. Для multi-byte полів явно застосувати `le16toh`/`ntohs` або власну конверсію. <span class="warn">Не кастити wire-format buffer у struct</span>, якщо layout, packing, alignment і endianness не зафіксовані та не перевірені.[^iso-c-n1570]

## Detailed explanation

Безпечний parser трактує frame як форматовану послідовність байтів, а не як готовий C-об’єкт. Він спершу перевіряє загальну довжину та межі кожного поля, перш ніж обчислювати адресу або читати значення. Це важливо для пошкоджених і навмисно коротких пакетів: доступ за межами буфера є окремою помилкою незалежно від того, чи правильно описано структуру.[^iso-c-n1570]

Далі кожне поле декодується за правилами протоколу. Для однобайтового поля достатньо зчитати байт; для multi-byte числа треба знати його endianness і зібрати значення відповідно. `memcpy` у локальну змінну допомагає уникнути невирівняного typed load, але сама по собі не міняє порядок байтів і не виправляє довжину. Якщо використовують `ntohs` чи `le16toh`, перевіряють, що функція доступна на цільовій платформі й відповідає byte order протоколу.[^iso-c-n1570]

Приклад: протокол задає 16-бітне little-endian поле за offset `2`. Після перевірки `length >= 4` значення можна отримати як молодший байт плюс старший байт, помножений на 256. Такий код не залежить від вирівнювання буфера, padding у структурі чи endianness CPU. Для полів із signed значеннями, float або бітовими прапорцями треба додатково дотримуватися визначеного протоколом кодування.

Cast на `struct*` виглядає привабливо, бо створює прямий доступ через імена полів. Проте він не підтверджує, що offset членів збігаються зі специфікацією, що буфер вирівняний або що об’єкт відповідного типу існує. `packed` може прибрати padding у певному compiler ABI, але лишає залежність від розширення компілятора та не виконує конверсій значень.[^iso-c-n1570]

**Типові помилки:**
- Читати поле до перевірки його повної довжини.
- Застосувати host-to-network conversion до поля, яке вже little-endian.
- Виправити alignment через `packed`, але залишити неперевіреними layout та byte order.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
