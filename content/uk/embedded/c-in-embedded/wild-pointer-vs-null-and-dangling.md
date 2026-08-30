---
id: emb-cppfound-0038
title: "Що таке wild pointer і чим він відрізняється від NULL та dangling pointer?"
description: "The distinction between wild, NULL, and dangling pointers."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Wild pointer</span> – неініціалізований вказівник із garbage-значенням (випадкова адреса зі стека).<br><br>Порівняння:<br>• <span class="key">NULL pointer</span>: явно невалідна адреса 0, можна перевірити;<br>• <span class="key">Dangling pointer</span>: вказував на валідний об'єкт, який знищено;<br>• <span class="key">Wild pointer</span>: ніколи не вказував на валідний об'єкт.<br><br>Всі три -> UB при розіменуванні. Wild pointer найнебезпечніший: його адреса ненульова і випадкова – перевірку <code>if(p != NULL)</code> проходить.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
