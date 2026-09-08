---
id: emb-align-0006
title: "Навіщо структурі trailing (хвостовий) padding?"
description: "Щоб у масиві структур кожен наступний елемент теж був вирівняний."
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
    applicability: "Додаткові приклади padding і розміру структури."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є нормативним джерелом object layout."
---

## Short answer

**Щоб у масиві структур кожен наступний елемент теж був вирівняний.**

`sizeof(struct)` є також кроком між елементами масиву. Реалізація додає достатній trailing padding, щоб `arr[1]`, `arr[2]` і наступні елементи задовольняли вимогу вирівнювання структури.

У типовому ABI вирівнювання структури визначає поле з найсуворішим alignment, але явний over-alignment може зробити його більшим.[^embeddedinterviewlab]

## Detailed explanation

Масив зберігає елементи без проміжків: адреса `arr[i + 1]` розташована рівно на `sizeof arr[0]` байтів після `arr[i]`. Отже, розмір завершеного object type має водночас бути допустимим кроком до наступного об'єкта того самого типу.[^iso-c-n1570]

Припустімо, що `uint32_t` має розмір і alignment 4, а `uint8_t` – розмір і alignment 1:

```c
struct Sample {
    uint32_t value;  // offsets 0..3
    uint8_t  tag;    // offset 4
};                   // offsets 5..7 are trailing padding
```

Поля займають п'ять байтів, але `sizeof(struct Sample)` зазвичай дорівнює восьми. Без трьох trailing bytes елемент `items[1]` починався б через п'ять байтів після `items[0]`, а його поле `value` не лежало б за адресою, кратною чотирьом.

Trailing padding належить об'єкту структури та входить у `sizeof`; це не окремий проміжок, який додає масив. Тому assignment структури або `memcpy` розміром `sizeof(struct Sample)` копіює і ці байти, хоча їхні значення не визначені. LearnCpp наочно показує, як padding збільшує структуру порівняно із сумою розмірів полів.[^learncpp-struct-padding]

Не виводь wire format із `sizeof(struct)`. На межі ABI перевіряй і розмір, і offsets через `_Static_assert`/`static_assert`; для serialized data задавай явний byte layout.

## Sources

<!-- generated from frontmatter -->
