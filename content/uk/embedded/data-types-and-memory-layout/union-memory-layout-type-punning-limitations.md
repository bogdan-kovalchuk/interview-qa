---
id: emb-dtypes-0109
title: "Як union представлений у пам'яті і які обмеження має type punning через union?"
description: "У union всі members починаються з одного offset, а розмір і alignment визначаються найбільшим member. Запис в один member перезаписує ті самі байти. Для переносимої інтерпретації байтів краще використовувати memcpy."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

У **union** всі members починаються з одного offset, а розмір і alignment визначаються найбільшим member. Запис в один member перезаписує ті самі байти, які можуть читатися через інший member, але правила доступу залежать від C/C++ стандарту, effective type і compiler behavior. <span class="warn">Для переносимої інтерпретації байтів у firmware краще використовувати `memcpy`</span>, а не покладатися на union type punning.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
