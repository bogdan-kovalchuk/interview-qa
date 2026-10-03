---
id: emb-structs-0028
title: "Trap: чи portable порядок bit-field-ів у пам’яті?"
description: "Ні: порядок allocation bit-field-ів у storage unit implementation-defined."
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

<span class="warn">Ні: порядок allocation bit-field-ів у storage unit implementation-defined.</span>

Один компілятор може розміщувати перше поле в least significant bits, інший або інший ABI може поводитися інакше. Endianness також не дає простого portable правила для bit-field layout у bytes.

Захист: не використовуй bit-fields як wire format між різними compiler/targets. Для protocol bits використовуй masks/shifts над integer, отриманим із явно розпарсених bytes.[^iso-c-n1570]

## Detailed explanation

Порядок, у якому C bit-fields займають біти allocation unit, є implementation-defined, тому порядок оголошень не визначає переносно позиції бітів у пам’яті від молодшого до старшого.[^iso-c-n1570]

Наприклад, у одній реалізації перше оголошене поле може займати молодші біти одиниці, а в іншій – старші. Стандарт C прямо залишає цей порядок реалізації. Мова також не повністю фіксує інші властивості розкладки, зокрема поведінку, коли поле не вміщується у вільний простір. Отже, на представлення впливають compiler, target і ABI.[^iso-c-n1570]

Endianness описує порядок байтів багатобайтового scalar у пам’яті, але саме по собі не визначає, як compiler розміщує іменовані bit-fields у вибраній одиниці зберігання. Ототожнення цих двох понять часто призводить до помилок. Структура, що відповідає схемі пакета на одній машині, може утворювати інші байти після зміни compiler або target.[^iso-c-n1570]

Наприклад, байт протоколу з flag у біті нуль і трибітним mode у бітах один–три слід декодувати з явно отриманого байта за допомогою зсувів і масок. Такий код прямо задає позиції у wire format. Накладання структури C з bit-fields додає припущення про ABI, а при читанні сирого буфера може також створити проблеми вирівнювання та aliasing.

**Типові помилки:**

- Вважати, що порядок оголошення дорівнює нумерації бітів у протоколі.
- Робити висновок про bit-field layout лише з endianness процесора.
- Перевірити структуру на одному компіляторі й вважати її універсальним wire format.

Якщо структура потрібна для внутрішнього коду, зафіксуй compiler та ABI й перевір representation під час збірки або тестування. Для форматів обміну байтами розбирай байти явно, а потім застосовуй маски й зсуви за специфікацією протоколу.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
