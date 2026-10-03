---
id: emb-structs-0032
title: "Що таке flexible array member?"
description: "Flexible array member – останнє поле структури з неповним розміром, наприклад uint8_t data[];."
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

**Flexible array member** – останнє поле структури з неповним розміром, наприклад `uint8_t data[];`.

Воно дозволяє виділити один memory block: header + variable-length payload. `sizeof(struct Packet)` не включає bytes payload, лише header і можливий padding перед flexible array.

Правило: flexible array member має бути останнім полем і структура має мати принаймні ще одне named поле.[^iso-c-n1570]

## Detailed explanation

Flexible array member – це останній член структури в C, оголошений як масив без заданої довжини, наприклад `uint8_t data[]`. Структура має містити ще принаймні один іменований член; такий масив не має власного фіксованого розміру в типі структури.[^iso-c-n1570]

Цей механізм дає змогу зберігати заголовок і payload в одному суміжному блоці пам’яті. Сам тип описує фіксовану частину – наприклад, довжину пакета, – а місце після неї можна виділити для потрібної кількості байтів. Це зменшує кількість окремих allocation-ів і спрощує передачу цілого пакета як одного об’єкта.

`sizeof(struct Packet)` не включає елементи гнучкого масиву. Водночас розмір структури може містити padding для вирівнювання, тож не можна припускати, що `data` починається за байтовим зміщенням, рівним сумі розмірів попередніх полів; використовуйте стандартні засоби на кшталт `offsetof` для обчислення зміщень.[^iso-c-n1570]

Приклад: структура з `uint16_t len` і `uint8_t data[]` може представляти мережевий або серійний пакет. Значення `len` задає логічну довжину payload, а код, що створив об’єкт, відповідає за виділення достатнього місця та за те, щоб читач не виходив за межі фактичного allocation.

**Типова помилка:** оголосити гнучкий масив не останнім полем або сприймати його як звичайний масив фіксованої довжини. Це спеціальна можливість C з чіткими обмеженнями; інші мови й режими C++ можуть не підтримувати цей синтаксис як стандартну конструкцію.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
