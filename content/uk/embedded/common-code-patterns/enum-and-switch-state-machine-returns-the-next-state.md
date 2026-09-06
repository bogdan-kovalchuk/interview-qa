---
id: emb-patterns-0002
title: "Як виглядає state machine на `enum` + `switch`?"
description: "Вкладений switch по стану, всередині – перевірка події і повернення нового стану."
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
oven_state_t step(oven_state_t s, oven_event_t e) {
  switch (s) {
  case STATE_IDLE:
    if (e == EVT_START) return STATE_HEATING;
    break;
  // ... інші стани
  }
  return s; // no transition
}
```

**Вкладений `switch` по стану, всередині – перевірка події і повернення нового стану.**

Переваги: легко крокувати в дебагері, компілятор попереджає про пропущені `enum` case. Якщо переходу немає – повертаємо поточний стан.

Правило: enum+switch – найкращий вибір для невеликих FSM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
