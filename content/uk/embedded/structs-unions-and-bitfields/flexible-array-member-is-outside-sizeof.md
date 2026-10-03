---
id: emb-structs-0052
title: "Чому `sizeof(struct with flexible array)` не дорівнює повному packet size?"
description: "Бо flexible array member не має compile-time розміру і не входить у sizeof."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
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
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**Бо flexible array member не має фіксованої довжини й не додає елементи до `sizeof` структури.**

`sizeof(struct Packet)` повертає розмір структури з урахуванням можливого padding, але без елементів `data[]`. Реальний розмір треба рахувати як `sizeof(struct Packet) + payload_len * sizeof data[0]`.

Правило: flexible array member описує layout prefix, а не володіє storage автоматично.[^iso-c-n1570]

## Detailed explanation

Flexible array member – останній член структури, записаний як масив без зазначеної довжини, наприклад `uint8_t data[]`. Його призначення – описати змінну кількість елементів, що зберігаються безпосередньо після фіксованої частини структури. За правилами C такий член не враховується як звичайний масив фіксованого розміру в `sizeof`; результат для структури може містити padding наприкінці.[^iso-c-n1570]

Розмір потрібного блока обчислюють за кількістю елементів і їхнім розміром: `sizeof(struct Packet) + count * sizeof data[0]`. Не слід автоматично писати `sizeof(struct Packet) + count`, якщо елемент не є однобайтовим. Також перевіряй переповнення при множенні та додаванні і переконайся, що виділення пам’яті успішне до доступу до payload.[^iso-c-n1570]

Приклад розрахунку для `uint8_t data[]` із 20 байтами payload: основа – `sizeof(struct Packet)`, а потім додаються 20 елементів по одному байту. Якщо перед payload структура має padding, воно вже входить у `sizeof(struct Packet)`; фактичний offset члена може мати специфічні вимоги розміщення, тому формат серіалізації не варто виводити лише з `sizeof` без перевірки ABI.[^iso-c-n1570]

FAM не виділяє пам’ять і не зберігає довжину самостійно. Код, який читає пакет із зовнішнього джерела, має перевірити заявлену довжину та межі буфера перед індексацією. Типова помилка – виділити тільки `sizeof(struct Packet)`, а потім записати payload у `data[]`; це вихід за межі виділеного об’єкта.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
