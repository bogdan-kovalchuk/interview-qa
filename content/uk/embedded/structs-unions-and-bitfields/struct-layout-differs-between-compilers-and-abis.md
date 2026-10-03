---
id: emb-structs-0053
title: "Trap: чи можна порівнювати layout C struct між різними компіляторами без перевірки?"
description: "Ні: ABI, alignment, packing pragmas і bit-field rules можуть відрізнятися."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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

<span class="warn">Ні: ABI, alignment, packing pragmas і bit-field rules можуть відрізнятися.</span>

Навіть однаковий source може мати інші offsets або розмір на іншій архітектурі. Для host tool + MCU firmware це частий баг: PC tool пише binary file за своїм struct layout, firmware читає за іншим.

Захист: external binary formats описуй у байтах, не в C structs. Додай version, length, endian і static/runtime checks.[^iso-c-n1570]

## Detailed explanation

Не можна без перевірки вважати, що C `struct` має однаковий бінарний layout у різних компіляторах або ABI. Реалізація визначає багато деталей представлення типів, alignment і padding; правила bit-field також залишають окремі рішення реалізації. Тому однакова декларація не є переносним описом зовнішнього wire format.[^iso-c-n1570]

Компілятор може вставити padding між членами або в кінці структури, щоб задовольнити alignment. Інша архітектура може мати інший розмір типів чи вимоги вирівнювання, а compiler options або packing pragmas змінюють розкладку в межах конкретного toolchain. Для bit-field можуть відрізнятися одиниця зберігання, порядок розміщення бітів та перетин меж одиниць; переносна програма не має підстав припускати один універсальний порядок.[^iso-c-n1570]

Типовий прояв – PC tool записує `struct` напряму у файл, а MCU читає ті самі байти у власну структуру. Offset поля може не збігтися, тому довжина інтерпретується як прапорець або padding стає частиною даних. Навіть якщо зараз розміри збігаються, зміна компілятора, прапорців чи цілі може зламати сумісність без зміни вихідного коду.[^iso-c-n1570]

**Як уникнути помилки:**

- Описуй протокол явними байтами, endian та offset-ами, а не memory image `struct`.
- Серіалізуй і парсь поля явно, перевіряючи довжину та версію повідомлення.
- Якщо внутрішній ABI контракт усе ж потрібен, фіксуй компілятор і прапорці та перевіряй `sizeof`, `offsetof` і layout assertions для кожної цілі.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
