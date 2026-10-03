---
id: emb-structs-0020
title: "Що таке bit-field у C struct?"
description: "Bit-field дозволяє оголосити поле структури з кількістю бітів, наприклад unsigned mode : 3;."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Bit-field** – це член структури або union із явно заданою шириною в бітах, наприклад `unsigned int mode : 3;`.[^iso-c-n1570]

Реалізація розміщує bit-fields у storage unit; порядок бітів і поведінка поля, що не вміщується в поточну одиницю, є implementation-defined. Типи bit-field обмежені стандартом або конкретною реалізацією. Це може бути зручно для компактних flags, але ризиковано для hardware register layout і wire format.[^iso-c-n1570]

Для hardware/protocol layout покладайся на bit-fields лише тоді, коли формат і ABI конкретного компілятора документовані та перевірені.[^iso-c-n1570]

## Detailed explanation

Bit-field – це член `struct` або `union`, якому в оголошенні задають ширину після двокрапки. Наприклад, `unsigned int mode : 3;` описує unsigned поле шириною три біти; число після двокрапки має бути цілим constant expression і не може перевищувати ширину відповідного типу.[^iso-c-n1570]

Компілятор виділяє для bit-fields addressable storage unit і, якщо в ньому є місце, може розмістити сусідні поля в суміжних бітах. C не задає єдиний порядок бітів усередині такої одиниці, її alignment або однакову поведінку поля, яке перетинає межу одиниці. Це implementation-defined властивості, тому дві реалізації можуть створити різний memory layout для того самого оголошення.[^iso-c-n1570]

Bit-fields допомагають описати набір невеликих прапорців або станів у внутрішній структурі. Водночас вони не гарантують сумісний формат байтів для периферійного регістра чи мережевого пакета. Для таких форматів потрібні правила конкретного MCU, ABI та compiler, а часто надійніше явно збирати й розбирати значення масками та зсувами.

**Типові помилки:**

- припускати, що перший оголошений bit-field завжди відповідає молодшим бітам;
- вважати, що `sizeof` структури дорівнює сумі ширин полів;
- переносити layout bit-fields між компіляторами без перевірки ABI.

Наприклад, три поля шириною по одному біту можуть бути сусідніми в одному storage unit, але стандарт не обіцяє конкретних номерів фізичних бітів. Перевіряй layout документацією компілятора та тестом для цільової платформи; не трактуй саме оголошення як переносний протокол обміну.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
