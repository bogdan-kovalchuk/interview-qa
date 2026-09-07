---
id: emb-patterns-0027
title: "Що таке guard clauses і навіщо вони?"
description: "Early-return перевірки на вході функції проти null-розіменування і невалідних параметрів."
track: embedded
section: common-code-patterns
level: junior
type: concept
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
err_t motor_set_speed(motor_t *m, int32_t rpm) {
  if (m == NULL)        return ERR_PARAM;
  if (rpm < MIN || rpm > MAX) return ERR_PARAM;
  if (m->state != RUNNING) return ERR_BUSY;
  // далі - лише валідні параметри
}
```

## Short answer

**Early-return перевірки на вході функції** проти null-розіменування і невалідних параметрів.

Після guard'ів основна логіка працює лише з гарантовано коректними даними – менше вкладеності, чистіший happy path.

Правило: кожна public API (application programming interface) функція починається з guard clauses (null + діапазон + стан).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
