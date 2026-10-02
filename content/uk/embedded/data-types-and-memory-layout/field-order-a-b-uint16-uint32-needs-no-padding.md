---
id: emb-dtypes-0078
title: "Як компілятор розміщує? `struct { uint8_t a; uint8_t b; uint16_t c; uint32_t d; }`"
description: "На поширеній ABI цей порядок може дати розмір 8 байтів без padding, але фактичний layout залежить від реалізації."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

На поширеній ABI, де `uint16_t` має alignment 2, а `uint32_t` – alignment 4, наведена структура може мати offsets 0, 1, 2 і 4 та розмір 8 байтів.[^iso-c-n1570] Однак C залишає спосіб вирівнювання членів реалізації, тому стандарт не гарантує цей layout або відсутність padding для всіх платформ. Перевіряй `sizeof` і `offsetof` саме на цільовому toolchain.[^iso-c-n1570]

## Detailed explanation

Компілятор розміщує члени `struct` у порядку оголошення: адреси пізніших членів зростають, а перед членом може бути безіменний padding для його вирівнювання. C задає, що кожний non-bit-field member вирівнюється способом, визначеним реалізацією, і дозволяє padding між членами та наприкінці структури. Тому правило «спочатку найбільші типи» є практичною евристикою для багатьох ABI, а не вимогою мови.[^iso-c-n1570]

У прикладі два `uint8_t` займають по одному байту, якщо typedef доступний; разом вони дають два байти перед `uint16_t`. На ABI з alignment 2 для `uint16_t` його offset буде 2, а після нього наступний вільний offset – 4. Якщо `uint32_t` вимагає alignment 4, він може початися на offset 4 без проміжного gap. Сума розмірів членів тоді дорівнює 8, а завершальний розмір структури зазвичай має бути кратним alignment самої структури. Саме ці припущення роблять показаний layout правдоподібним, але їх не встановлює універсально стандарт C.[^iso-c-n1570]

Навіть на типовій платформі не варто виводити binary protocol або формат запису у Flash лише з порядку членів. Компілятор може мати інші alignment вимоги, опції packing змінюють ABI, а padding bytes не є полями даних із гарантованим значенням. Для протоколу краще серіалізувати кожне поле явно у визначений byte order; для DMA чи апаратної структури треба звірити ABI та вимоги пристрою.

**Приклад перевірки на цільовій збірці:**

```c
sizeof(struct sample)
offsetof(struct sample, c)
offsetof(struct sample, d)
```

Очікування 8, 2 і 4 справджується лише за згаданих alignment припущень. Якщо результат відрізняється, знайди реальні offsets і padding замість того, щоб виправляти їх припущенням про «правильний» порядок полів.[^iso-c-n1570]

**Типова помилка:** плутати порядок членів у вихідному коді з гарантією їхньої щільної упаковки. `sizeof` і `offsetof` дають фактичний layout для конкретної компіляції; саме його потрібно перевірити перед залежністю від байтового представлення.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
