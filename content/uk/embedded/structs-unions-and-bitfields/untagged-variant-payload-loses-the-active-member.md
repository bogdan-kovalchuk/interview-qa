---
id: emb-structs-0019
title: "Що не так із таким variant payload?"
description: "Немає tag-а, який каже, яке поле валідне."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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
---

## Question code

```c
union Payload {
    uint16_t temperature;
    uint32_t pressure;
};

union Payload p;
```

## Short answer

<span class="warn">Немає tag-а, який каже, яке поле валідне.</span>

Union економить пам'ять, але втрачає інформацію про активний варіант. Якщо receiver не знає тип payload із header або enum, він може неправильно інтерпретувати ті самі bytes.

Захист: використовуй `struct Message { enum Type type; union Payload payload; };` або отримуй discriminator із protocol header і перевіряй його перед доступом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
