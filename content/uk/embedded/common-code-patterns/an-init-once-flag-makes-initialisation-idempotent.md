---
id: emb-patterns-0028
title: "Що таке init-once (idempotent) патерн?"
description: "Прапорець гарантує, що ініціалізація виконається лише раз, навіть якщо init викликати кілька разів."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
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

```c
static bool initialized = false;
err_t subsystem_init(void) {
  if (initialized) return ERR_OK; // idempotent
  // one-time HW setup
  initialized = true;
  return ERR_OK;
}
```

**Прапорець гарантує, що ініціалізація виконається лише раз**, навіть якщо `init` викликати кілька разів.

Спрощує startup-послідовність, коли кілька модулів залежать від однієї підсистеми.

Правило: init-once робить ініціалізацію безпечною для повторного виклику; стеж за thread/ISR-safety прапорця.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
