---
id: emb-patterns-0027
title: "What are guard clauses and what are they for?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
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

Guard clauses do not define a complete contract: check only preconditions specified for that API, and check them before unsafe operations such as dereferencing a pointer.[^iso-c-n1570]

## Detailed explanation

TODO
