---
id: emb-structs-0027
title: "Що робить unnamed zero-width bit-field?"
description: "Zero-width unnamed bit-field змушує наступний bit-field початися з нового allocation unit."
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

## Question code

```c
struct F {
    unsigned a : 3;
    unsigned   : 0;
    unsigned b : 5;
};
```

## Short answer

**Zero-width unnamed bit-field** змушує наступний bit-field початися з нового allocation unit.

Це спосіб вставити boundary між групами bit-fields. Реальний розмір і alignment усе одно залежать від базового типу та ABI компілятора.

Embedded-правило: це може допомогти для internal layout, але не робить bit-field mapping portable для hardware register manual.[^iso-c-n1570]

## Detailed explanation

Безіменне bit-field нульової ширини завершує поточну групу bit-fields свого оголошеного типу, тому наступне відповідне поле починається в новій allocation unit, а не займає решту попередньої.[^iso-c-n1570]

У `struct F` поле `a` має ширину три, потім `unsigned : 0` створює межу, а `b` оголошене після неї. Член нульової ширини не має імені й не зберігає значення; це директива розкладки в оголошенні структури. Вона корисна, коли групи полів мають починатися окремо, наприклад щоб нове поле не потрапило в невикористану частину одиниці.

Правило стандарту вужче за гарантію остаточного розміщення байтів: поле нульової ширини забороняє пакувати наступні bit-fields в одиницю, де розміщено попереднє поле. Воно не задає універсальний розмір allocation unit, byte offset, розмір структури чи однакову ABI поведінку для кожної комбінації базових типів. Важливий і оголошений тип: компілятори накладають обмеження на типи bit-fields і полів нульової ширини.[^iso-c-n1570]

Розглянь `a`, за яким ідуть безіменне поле нульової ширини та `b`. Можна стверджувати, що `b` розміщене після межі, визначеної реалізацією, але не називати конкретний byte offset без перевірки ABI цього compiler. Для звичайної розкладки структури використовуй звіт про layout або перевірку розміру; стандарт C не дозволяє отримати адресу самого bit-field.

**Типові помилки:**

- Приписувати zero-width field гарантоване вирівнювання на межу byte або word певного розміру.
- Вважати, що директива робить весь layout portable між ABI.
- Використовувати її як спосіб прив’язати поля до бітів апаратного register.

Отже, цей запис створює межу між групами bit-fields, але конкретне розміщення після межі визначають правила реалізації. Для wire format або периферії описуй позиції масками відносно явно прочитаного integer, а не покладайся на структуру C.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
