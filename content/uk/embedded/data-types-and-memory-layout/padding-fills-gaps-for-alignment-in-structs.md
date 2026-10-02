---
id: emb-dtypes-0024
title: "Що таке padding у структурах і звідки він береться?"
description: "Реалізація може вставляти padding між членами struct або після них, щоб задовольнити вимоги вирівнювання target."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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

**Padding** – простір, який реалізація може вставити між членами структури або після них, щоб задовольнити вимоги вирівнювання. Для ABI, де `char` має розмір 1, а `int` вимагає 4-байтового вирівнювання, `struct { char c; int x; }` розміщує `x` на offset 4, з трьома байтами між членами. Точні offsets і повний розмір залежать від реалізації та ABI; це не універсальні гарантії C.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

Padding – це байти, які реалізація може розмістити між членами або наприкінці `struct`, зокрема для виконання вимог вирівнювання.[^iso-c-n1570]

Вирівнювання визначає адреси, на яких реалізація розміщує об’єкти певного типу. Доступ до вирівняного значення може відповідати обмеженням процесора й ABI. Стандарт C задає порядок членів структури та правила щодо padding, але не встановлює універсального вирівнювання для `int` чи однакового layout на всіх MCU.[^iso-c-n1570]

Для поширеного ABI, де `char` має розмір і вирівнювання один байт, а `int` має вирівнювання чотири байти, у `struct { char c; int x; }` член `c` займає offset 0, а `x` починається з offset 4. Між ними є три байти padding. За тих самих припущень структура має розмір 8 байтів: чотири байти до `x` і чотири для `int`. Це приклад конкретних ABI-властивостей, а не обіцянка мови для кожної реалізації.[^iso-c-n1570]

Padding може бути і в кінці структури, щоб послідовні елементи масиву структур мали належне вирівнювання. Саме тому `sizeof(struct)` може бути більшим за суму `sizeof` членів. Порядок членів іноді змінюють, щоб зменшити внутрішні проміжки, але перед таким рішенням треба оцінити читабельність і стабільність зовнішнього формату.

**Типові помилки:**

- Вважати розмір структури сумою розмірів її полів.
- Переносити offset з одного compiler/ABI на інший без перевірки.

**Приклад розрахунку:**

```text
char c: offset 0, size 1
padding: 3 bytes, then int x at offset 4 (assumed 4-byte alignment)
size: 4 + 4 = 8 bytes (under these ABI assumptions)
```

Якщо layout важливий для протоколу чи Flash-образу, перевіряйте `sizeof` та `offsetof` на потрібному toolchain і визначайте формат явно, а не покладайтеся на неявні проміжки компілятора.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
