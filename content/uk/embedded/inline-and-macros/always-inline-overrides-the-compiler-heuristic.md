---
id: emb-macros-0032
title: "Що робить `__attribute__((always_inline))` і коли воно потрібне?"
description: "Примушує компілятор inline-ити функцію навіть коли його евристика обрала б звичайний виклик (зазвичай разом з inline)."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
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

## Short answer

**Примушує компілятор inline-ити функцію** навіть коли його евристика обрала б звичайний виклик (зазвичай разом з `inline`).

У embedded потрібне для крихітних обгорток доступу до регістрів, критичних до латентності ділянок або коли виклик у hot path/ISR (interrupt service routine) недопустимий. Протилежне – `__attribute__((noinline))`.

Правило: `inline` – це підказка, яку компілятор може ігнорувати; `always_inline` – директива. Не зловживай: роздування коду шкодить I-cache і flash.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
