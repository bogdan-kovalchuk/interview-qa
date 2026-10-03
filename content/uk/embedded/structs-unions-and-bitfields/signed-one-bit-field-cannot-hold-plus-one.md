---
id: emb-structs-0022
title: "Trap: чому signed bit-field на 1 біт майже завжди пастка?"
description: "1-bit signed field не може представляти значення +1 у two's complement моделі."
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

## Question code

```c
struct F {
    signed int flag : 1;
};
```

## Short answer

<span class="warn">У two’s complement 1-bit signed field має лише значення `0` і `-1`, тож не є boolean `0/1`.</span>

У звичайній two’s complement реалізації запис `1` у таке поле дає `-1`, тому перевірка `flag == 1` не спрацьовує. Конкретна поведінка перетворення значення, яке не представляється signed bit-field, залежить від правил C та реалізації.[^iso-c-n1570]

Для прапорця використовуй `_Bool` (або `bool` із `<stdbool.h>` у C до C23), якщо потрібні саме логічні значення `0/1`; для фіксованого однобітного представлення можна застосувати `unsigned int` bit-field.[^iso-c-n1570]

## Detailed explanation

Однобітове signed поле не є надійним способом зберігати звичайний прапорець `0/1`. У поширеній two’s complement моделі цей біт є знаком: доступні значення `0` і `-1`, а додатне `1` не представляється. Тому код, який задає `flag = 1` і потім перевіряє `flag == 1`, може отримати неочікуваний результат.[^iso-c-n1570]

Точна поведінка залежить від моделі signed integer і правил перетворення для конкретної реалізації. У C стандарт визначає bit-field як signed або unsigned integer type із заданою кількістю бітів, а значення, що не представляється цільовим signed типом, не має переносимого результату, який можна використовувати як логічну нормалізацію. Тож не покладайся на конкретне трактування одного біта без перевірки документації компілятора.[^iso-c-n1570]

Якщо потрібні семантичні значення false/true, використовуй `_Bool`: присвоєне йому ненульове значення нормалізується до `1`, а нульове – до `0`. Якщо важлива саме щільна unsigned розкладка, `unsigned int flag : 1` має діапазон `0`–`1`; однак загальний layout структури все одно залежить від реалізації, тож це не автоматична гарантія формату зовнішнього протоколу.[^iso-c-n1570]

**Типові помилки:**

- оголошувати `signed int flag : 1`, а далі використовувати його як boolean;
- вважати, що слово `signed` гарантує очікуваний діапазон для будь-якої ширини поля;
- плутати логічний тип `_Bool` із signed integer bit-field.

Пастка проявляється, коли прапорець після встановлення не дорівнює `1`, і гілка `if (flag == 1)` пропускається. Щоб уникнути цього, обери тип за потрібною семантикою, а значення та ABI перевіряй окремо від ширини поля.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
