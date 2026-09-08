---
id: emb-align-0005
title: "Як перевпорядкувати поля, щоб зменшити padding?"
description: "Якщо layout не зафіксований, групуй поля за спаданням alignment, щоб зменшити внутрішні прогалини."
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
    applicability: "Додатковий приклад 12 проти 8 байт і порада впорядковувати поля за спаданням розміру."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++, який називає LearnCpp першоджерелом навчальних матеріалів; не є нормативним джерелом layout."
---

## Question code

```c
struct { uint8_t a; uint32_t b; uint8_t c; };
```

## Short answer

Групуй поля за спаданням alignment:

```c
struct {
  uint32_t b; // @0
  uint8_t  a; // @4
  uint8_t  c; // @5, +2 tail
};
```

За вказаного чотирибайтового alignment для `uint32_t` значення `sizeof` стає 8 замість 12: малі поля розташовані поруч, internal padding зникає, але два trailing bytes залишаються.

Це безпечно лише тоді, коли layout контролюєш ти; не перевпорядковуй непомітно public ABI, protocol, file format або register map.[^embeddedinterviewlab]

## Detailed explanation

Припустімо, що `uint8_t` має розмір і alignment 1, а `uint32_t` – розмір і alignment 4. C зберігає порядок оголошення полів і дозволяє безіменний padding між ними та наприкінці структури.[^iso-c-n1570]

```c
struct { uint8_t a; uint32_t b; uint8_t c; };
```

Початковий порядок дає такий layout:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [a][pad][pad][pad][  b  ][c][pad][pad][pad]
```
`a` займає offset 0, три байти internal padding пересувають `b` на offset 4, а `c` займає offset 8. Три trailing padding bytes роблять крок масиву кратним 4, тому `sizeof` дорівнює 12.

Тепер поставимо поле з найсуворішим alignment першим:

```c
struct {
    uint32_t b;  // size 4, alignment 4
    uint8_t  a;  // size 1, alignment 1
    uint8_t  c;  // size 1, alignment 1
};
```

```
Offset: 0  1  2  3  4  5  6  7
        [  b  ][a][c][pad][pad]
```

У новому layout немає internal padding, але є два trailing bytes, тому `sizeof` дорівнює 8. Масив зі 100 елементів займає 800 замість 1200 байт. LearnCpp показує той самий ефект 12 проти 8 і радить використовувати спадання розміру полів як практичну евристику.[^learncpp-struct-padding]

Точнішим ключем сортування є alignment. Розмір і alignment часто пов'язані для scalar types, але це не універсальне правило. Практичний порядок дій:

1. Перевір `_Alignof(T)` або `alignof(T)` для target types.
2. Згрупуй поля від суворішого alignment до слабшого, а пов'язані малі поля тримай поруч.
3. Перевір `sizeof` і критичні offset через compile-time assertions.
4. Виміряй, чи виправдовує економія storage можливу втрату readability або locality.

Не застосовуй це перетворення там, де зовнішній layout є частиною контракту: memory-mapped hardware registers, network packets, persistent binary files, shared-memory ABI або structures, які використовує окремо зібраний code. Packing не є універсальною заміною, бо може створити unaligned access.

## Sources

<!-- generated from frontmatter -->
