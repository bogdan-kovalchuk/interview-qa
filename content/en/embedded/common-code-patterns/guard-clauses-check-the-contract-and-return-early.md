---
id: emb-patterns-0027
title: "What are guard clauses and what are they for?"
description: "Early-return checks at function entry against null dereference and invalid parameters"
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
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

**Early-return checks at function entry** against null dereference and invalid parameters.

After the guards, the main logic works only with guaranteed-valid data – less nesting, a cleaner happy path.

Rule: every public API (application programming interface) function starts with guard clauses (null + range + state).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
