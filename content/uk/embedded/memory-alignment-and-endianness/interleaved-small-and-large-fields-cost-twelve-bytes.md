---
id: emb-align-0004
title: "Яким буде `sizeof`, якщо uint32 має чотирибайтове вирівнювання?"
description: "Зазвичай 12 байт: три байти internal і три байти trailing padding."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Додаткові відомості про структури"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткові приклади того, як порядок полів змінює padding і розмір структури."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є нормативним джерелом object layout."
---

## Question code

```c
typedef struct {
  uint8_t  flags;
  uint32_t timestamp;
  uint8_t  sensor_id;
} bad_t;
```

## Short answer

**Зазвичай 12 байт, якщо `uint8_t` має розмір і alignment 1, а `uint32_t` – розмір і alignment 4.**

Layout: `flags`@0 (1B) -> <span class="warn">3B padding</span> -> `timestamp`@4 (4B) -> `sensor_id`@8 (1B) -> <span class="warn">3B trailing padding</span> (щоб розмір був кратний 4).

Перевпорядкування полів за спаданням alignment зменшує цей layout до 8 байт. Сам факт, що MCU є 32-бітним, не гарантує таких значень ABI.[^embeddedinterviewlab]

## Detailed explanation

Точний результат залежить від реалізації, тому спочатку треба назвати припущення про ABI. За типового для MCU layout із короткої відповіді compiler зберігає порядок оголошення та вставляє безіменний padding там, де це потрібно.[^iso-c-n1570]

```c
typedef struct {
    uint8_t  flags;      // size 1, alignment 1
    uint32_t timestamp;  // size 4, alignment 4
    uint8_t  sensor_id;  // size 1, alignment 1
} bad_t;
```

Розрахунок offset такий:

1. `flags` займає offset 0.
2. Для `timestamp` потрібен offset, кратний 4, тому offsets 1–3 є padding, а `timestamp` займає offsets 4–7.
3. `sensor_id` займає offset 8.
4. Об'єкт уже займає 9 байт. Три trailing padding bytes роблять крок масиву рівним 12, тому `timestamp` залишається вирівняним у кожному елементі.

Підсумковий byte layout:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [f][p][p][p][t0][t1][t2][t3][s][p][p][p]
```

За цих припущень `sizeof(bad_t)` не може дорівнювати 6, бо це ігнорувало б internal padding і вирівняний крок масиву. LearnCpp наводить аналогічний приклад 12 проти 8 та підкреслює, що розмір структури може перевищувати суму розмірів її полів.[^learncpp-struct-padding]

Якщо binary compatibility не фіксує порядок полів, згрупуй поля з найсуворішим alignment на початку:
```c
typedef struct {
    uint32_t timestamp;  // offsets 0..3
    uint8_t  flags;      // offset 4
    uint8_t  sensor_id;  // offset 5
} good_t;                // offsets 6..7 are trailing padding
```

Перевір layout target замість припущення:

```c
_Static_assert(sizeof(bad_t) == 12, "unexpected bad_t layout");
_Static_assert(sizeof(good_t) == 8, "unexpected good_t layout");
```

Не перевпорядковуй поля public ABI, wire format, persistent binary format або hardware register map лише заради економії місця.

## Sources

<!-- generated from frontmatter -->
