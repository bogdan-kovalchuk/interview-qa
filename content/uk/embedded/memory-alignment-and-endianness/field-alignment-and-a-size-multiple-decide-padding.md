---
id: emb-align-0003
title: "Які два правила визначають padding у структурі?"
description: "1. Кожне поле лежить за адресою, кратною його natural alignment (між полями вставляється padding)."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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
    applicability: "Додаткові приклади padding, розміру структури та перевпорядкування полів у C++."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є нормативним джерелом object layout."
---

## Short answer

1. Кожне поле починається з offset, придатного для його типу, тому реалізація може вставити internal padding. 2. Розмір структури містить trailing padding, потрібний для вирівнювання сусідніх елементів масиву.

У типовому ABI без явного over-alignment вирівнювання структури дорівнює найбільшому вирівнюванню її полів. Завжди перевіряй `sizeof` і `_Alignof` на конкретному target.[^embeddedinterviewlab]

## Detailed explanation

**Правило 1: вирівнювання полів**

Поля розташовуються в порядку оголошення, а compiler може вставляти між ними безіменний padding, але не перед першим полем. Кожне поле, яке не є bit-field, усе одно має задовольняти вимогу вирівнювання свого типу.[^iso-c-n1570]

Припустімо, що для цього target `_Alignof(uint32_t) == 4`:
```c
struct Example {
    uint8_t  a;    // size 1, alignment 1
    uint32_t b;    // size 4, alignment 4
    uint8_t  c;    // size 1, alignment 1
};
```

Один із типових варіантів layout:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [a][pad][pad][pad][  b  ][c][pad][pad][pad]
```

`a` займає offset 0. Три байти padding пересувають `b` на offset 4; `c` іде за ним на offset 8.

**Правило 2: крок структури**

Між елементами масиву немає проміжків, тому `sizeof(struct Example)` є також кроком масиву. Реалізація додає trailing padding, щоб наступний елемент починався за адресою, яка задовольняє вирівнювання структури.

За вказаних припущень про ABI найбільше вирівнювання поля дорівнює 4. Поля разом з internal padding займають 9 байт, а три trailing bytes збільшують розмір до 12. LearnCpp демонструє той самий загальний ефект: через padding розмір структури може перевищувати суму розмірів полів.[^learncpp-struct-padding]

Для цього прикладу:
```
sizeof(struct) = sum of field sizes + internal padding + trailing padding
```

Не серіалізуй і не відображай hardware layout сліпим копіюванням native structure. Padding, alignment полів, representation цілих чисел і byte order є властивостями ABI. Для wire format задай явний формат, використовуй fixed-width поля та окремо кодуй або декодуй кожне з них; для register map дотримуйся layout виробника й перевіряй offset через `_Static_assert` або `static_assert`.

Перевпорядкування полів за спаданням alignment часто зменшує padding, але воно може змінити ABI або binary format, тому безпечне лише тоді, коли layout контролюєш ти.

## Sources

<!-- generated from frontmatter -->
