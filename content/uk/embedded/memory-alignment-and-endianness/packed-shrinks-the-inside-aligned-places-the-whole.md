---
id: emb-align-0042
title: "Як `__attribute__((aligned))` і `packed` можуть працювати разом?"
description: "packed зменшує padding усередині типу, а aligned(N) задає мінімальне вирівнювання самого об’єкта або типу."
track: embedded
section: memory-alignment-and-endianness
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
  - source_id: gcc-common-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує поведінку GNU-атрибутів packed та aligned; це документація GCC, а не переносима вимога стандарту C."
---

## Short answer

**`packed` зменшує padding усередині типу, а `aligned(N)` задає мінімальне вирівнювання самого об’єкта або типу.**

Це може бути корисно для wire headers або DMA descriptors, де layout має бути щільним, але початкова адреса повинна бути вирівняна для апаратури. Водночас для MMIO (memory-mapped I/O) register blocks <span class="warn">не варто автоматично ставити `packed`</span>: регістри зазвичай мають природні 32-bit offsets, а пропуски краще описувати reserved fields.

Правило: у GCC `packed` зменшує padding членів, а `aligned(N)` задає мінімальне вирівнювання; для register maps перевіряй ширину доступу й `offsetof`, а не просто пакуй структуру.[^gcc-common-attributes]

## Detailed explanation

`packed` і `aligned(N)` керують різними властивостями об’єкта в розширеннях GCC. `packed` для структури розміщує її члени щільніше, мінімізуючи потрібну пам’ять; окремо `aligned(N)` задає мінімальне вирівнювання типу або об’єкта в байтах. Тому структура може мати компактні внутрішні offsets, але сам екземпляр починатися з адреси, кратної більшому значенню вирівнювання.[^gcc-common-attributes]

Це GNU-розширення, а не переносима гарантія стандарту C. Точний результат залежить від компілятора, цілі та місця застосування атрибута. Атрибут на зовнішній структурі також не обов’язково пакує внутрішню вкладену структуру. Перевіряй фактичні `sizeof`, `_Alignof` і `offsetof` для потрібної збірки; якщо контракт має пережити інший компілятор, опиши байти формату явно.[^gcc-common-attributes][^iso-c-n1570]

Наприклад, компактний wire header може містити 8-бітне поле, а за ним 32-бітне. Без padding друге поле потенційно матиме зсув, не кратний природному вирівнюванню `uint32_t`. `aligned(4)` на типі може вирівняти початок усього об’єкта, але не обов’язково змінить цей внутрішній offset. На деяких мікроконтролерах невирівняний доступ повільніший або заборонений, тож не можна вважати, що щільне розміщення означає безпечне пряме читання кожного поля.[^gcc-common-attributes]

**Типова помилка:** сприймати `packed` як серіалізатор або як гарантію безпечного MMIO. Атрибут не задає byte order, ширину апаратного доступу чи формат чисел. Для мережі декодуй байти явно; для регістрів звір offsets і розмір операцій із документацією мікроконтролера.[^gcc-common-attributes]

## Sources

<!-- generated from frontmatter -->
