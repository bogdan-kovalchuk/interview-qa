---
id: emb-structs-0047
title: "Trap: що не так із `#pragma pack` у public header без обережності?"
description: "Він може змінити packing для наступних структур у чужому коді."
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
  - source_id: gcc-structure-layout-pragmas
    title: "GCC documentation: Structure-Layout Pragmas"
    url: https://gcc.gnu.org/onlinedocs/gcc/Structure-Layout-Pragmas.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує для GCC зміну alignment наступних struct/union та семантику pack(push)/pack(pop); інші компілятори можуть відрізнятися."
---

## Short answer

<span class="warn">Він може змінити packing для наступних структур у чужому коді.</span>

У GCC `#pragma pack(n)` впливає на alignment наступних оголошень `struct` і `union`; без відновлення попереднього стану це може змінити layout типів, оголошених пізніше у тому самому translation unit.[^gcc-structure-layout-pragmas]

Оточуй потрібний тип парою `#pragma pack(push, 1)` і `#pragma pack(pop)`, перевіряй підтримку в конкретному компіляторі та зафіксуй очікувані `sizeof`/offsets перевірками.[^gcc-structure-layout-pragmas]

## Detailed explanation

`#pragma pack` – це директива компілятора, яка може змінити правила alignment для наступних оголошень агрегатних типів; якщо стан не відновити, подальший код у тому самому translation unit успадкує його.[^gcc-structure-layout-pragmas]

На відміну від звичайного локального оголошення типу, pragma змінює стан обробки компілятором. Наприклад, `#pragma pack(1)` просить компілятор розташовувати members зі зменшеним максимальним alignment. Це може прибрати padding і змінити `sizeof` та offsets полів. Код, який очікує природне вирівнювання або стабільний ABI – зокрема драйвери, бібліотеки та структури RTOS – може отримати інший layout, якщо заголовок залишив packing увімкненим.[^gcc-structure-layout-pragmas]

Директиви `pack` не є частиною переносимої семантики мови C: це поведінка конкретного toolchain. GCC описує власну stack-семантику: `push` зберігає поточне налаштування, а `pop` відновлює його; підтримка й деталі відрізняються між компіляторами. Тому заголовок, призначений для кількох toolchain-ів, має явно обмежити платформу й використовувати документований для них синтаксис.[^gcc-structure-layout-pragmas]

**Приклад:**

```c
#pragma pack(push, 1)
struct WireHeader { uint8_t kind; uint32_t length; };
#pragma pack(pop)
```

Тут packing обмежений оголошенням `WireHeader`, якщо конкретний компілятор підтримує цю форму. Без `pop` подальші типи в підключених після цього фрагмента заголовках можуть отримати інший layout. Сам `pop` має відповідати push, зокрема коли є умовна компіляція чи ранній вихід із макросного include-фрагмента.[^gcc-structure-layout-pragmas]

**Типова помилка:** написати `#pragma pack(1)` у public header і припустити, що його дія закінчиться разом із `struct`. Симптоми – неочікувані offsets, помилки сумісності ABI або невирівняні доступи. Застосовуй симетричні `push/pop`, не покладайся на непідтверджені атрибути та перевіряй layout через `sizeof` і `offsetof` для підтримуваних компіляторів.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
