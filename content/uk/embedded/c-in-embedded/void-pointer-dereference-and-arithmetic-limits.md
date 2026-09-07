---
id: emb-cppfound-0014
title: "Що таке `void*` і які обмеження має цей тип вказівника?"
description: "The capabilities and restrictions of a void pointer."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
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

**void*** – type-erased pointer: може зберігати адресу об'єкта будь-якого типу без explicit cast.

Обмеження:
- <span class="warn">Не можна розіменувати</span> без cast: `*p` – помилка компіляції;
- <span class="warn">Не можна виконати arithmetic</span> без cast (стандарт C). GCC дозволяє як extension (розмір елемента = 1 байт).

Використання: `malloc`/`free`, `memcpy`/`memset`, generic callbacks, `qsort`. У embedded: generic ISR handler tables.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
