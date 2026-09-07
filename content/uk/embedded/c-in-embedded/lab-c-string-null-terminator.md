---
id: emb-cppfound-0072
title: "Як зберігається рядок у пам'яті і яка роль null-terminator?"
description: "How the null terminator marks the end of a C string."
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

Рядок у C – масив символів де останній елемент = **'\0' (null-terminator)**, байт зі значенням 0.

"hello" -> `['h','e','l','l','o','\0']` – 6 байт у пам'яті.

Null-terminator сигналізує стандартним функціям (`strlen`, `strcpy`, `printf %s`) де рядок закінчується. Без '\0' – читання виходить за межі -> UB.

Рядкові літерали автоматично мають '\0'. При ручному заповненні: `buf[n] = '\0';` обов'язково.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
