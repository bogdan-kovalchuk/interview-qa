---
id: emb-align-0009
title: "Що робить `__attribute__((packed))` і чим це небезпечно?"
description: "Атрибут packed мінімізує padding, але може залишити багатобайтові поля без звичайного вирівнювання."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Нормативна документація GCC для нестандартного type attribute packed."
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Додаткові відомості про структури"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення звичайного padding структури та порядку полів."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є документацією GNU attributes."
---

## Short answer

**Він просить GCC розмістити поля якомога щільніше, щоб мінімізувати storage.**

<span class="warn">Ризик</span>: багатобайтове поле може мати слабше alignment, ніж зазвичай вимагає його тип. Compiler може згенерувати безпечні byte accesses, але target-specific code усе одно може впасти, якщо отримає його адресу для aligned instruction.

Сприймай `packed` як compiler-specific засіб layout, а не як serialization або конвертацію endianness.[^embeddedinterviewlab]

## Detailed explanation

`__attribute__((packed))` – розширення GNU, а не ISO C. GCC документує, що для packed structure кожне поле, крім zero-width bit-fields, розміщується так, щоб мінімізувати потрібну пам'ять.[^gcc-packed]

```c
struct __attribute__((packed)) Packet {
    uint8_t  tag;
    uint32_t value;
};
```

Такий layout зазвичай займає п'ять байтів, а `value` починається з offset 1. Адреса всього `Packet` може задовольняти alignment packed type, тоді як `&packet.value` не є належно вирівняною для звичайного `uint32_t *`.

## Symptom

Симптоми варіюються від повільніших byte-wise instructions до alignment fault. Вони можуть змінитися через target flags або optimization, бо compiler добирає instructions за відомою йому інформацією про alignment. Warning `-Waddress-of-packed-member` особливо корисний, коли code бере pointer і втрачає контекст слабшого вирівнювання поля.

## Why it happens

Packing змінює layout, але не integer representation мови й не byte order протоколу. Він також не пакує вкладену structure рекурсивно, якщо її type окремо не позначено packed.[^gcc-packed]

Передавання адреси packed member в API, яке очікує `uint32_t *`, особливо небезпечне: callee має право припускати звичайне alignment для `uint32_t`.

## How to avoid

- Для wire format віддавай перевагу явному byte array та encode/decode helpers.
- Якщо packed layout неминучий, копіюй поле через `memcpy` у aligned storage перед використанням і окремо виконуй byte-order conversion.
- Не відображай MMIO через бездумно packed structure. Дотримуйся access width, offsets, reserved gaps і `volatile` qualification із device manual.
- Фіксуй обов'язковий зовнішній layout compile-time перевірками size/offset та конкретним compiler/ABI.

Приклади звичайного layout у LearnCpp корисні як контраст: перевпорядкування полів часто зменшує padding без послаблення alignment полів.[^learncpp-struct-padding]

## Sources

<!-- generated from frontmatter -->
