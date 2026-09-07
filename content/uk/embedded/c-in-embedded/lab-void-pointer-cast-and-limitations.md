---
id: emb-cppfound-0069
title: "Навіщо потрібен cast при роботі з `void*` і які обмеження?"
description: "C and C++ conversion rules and limitations of void pointers."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

В **C**: присвоєння `void*` до `T*` (і навпаки) не потребує explicit cast – автоматичне перетворення. `int *p = malloc(n);` – коректно у C.

В **C++**: <span class="warn">обов'язковий explicit cast</span>: `int *p = (int*)malloc(n);`.

Обмеження void*:
- Не можна розіменувати без cast;
- Не можна pointer arithmetic (стандарт C);
- Не зберігає type-safety.

Перед розіменуванням: `*(int*)vp = 42;`. Це правило зберігає правильний тип доступу.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
