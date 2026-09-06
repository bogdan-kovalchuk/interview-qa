---
id: emb-patterns-0022
title: "Чому в safety-critical коді return codes – дефолтний патерн?"
description: "MISRA C (Motor Industry Software Reliability Association C) вимагає не ігнорувати return values, а IEC 62304 вимагає керованого процесу обробки software faults."
track: embedded
section: common-code-patterns
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
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**MISRA C (Motor Industry Software Reliability Association C) вимагає не ігнорувати return values, а IEC 62304 вимагає керованого процесу обробки software faults.**

Return codes змушують викликача інспектувати результат, тоді як sentinel чи мовчазний збій легко проігнорувати. Це робить помилки видимими в аудиті.

Правило: у сертифікованих системах кожен виклик, що може впасти, повертає визначений код, і кожен код перевіряється.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
