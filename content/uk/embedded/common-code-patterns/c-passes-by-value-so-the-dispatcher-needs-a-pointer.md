---
id: emb-patterns-0005
title: "Trap: чому диспетчер FSM має приймати `state_t *state`, а не `state_t state`?"
description: "У C аргументи передаються за значенням – зміна локальної копії state зникне після повернення, і перехід стану загубиться."
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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

У C аргументи передаються за значенням – зміна локальної копії `state` зникне після повернення, і перехід стану загубиться. FSM тут означає finite state machine. 

```c
// баг: правиться лише копія
void process(state_t state, ...);
// fix: правиться справжній стан
void process(state_t *state, ...);
```

Особливо легко забути з `enum`, бо він поводиться як звичайний int.

Захист: щоб функція змінила змінну, що переживає виклик, передавай вказівник.[^embeddedinterviewlab]

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
