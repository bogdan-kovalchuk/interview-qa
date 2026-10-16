---
id: emb-patterns-0028
title: "What is the init-once (idempotent) pattern?"
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
static bool initialized = false;
err_t subsystem_init(void) {
  if (initialized) return ERR_OK; // idempotent
  // one-time HW setup
  initialized = true;
  return ERR_OK;
}
```

## Short answer

**A flag guarantees that initialization runs only once**, even if `init` is called multiple times.

It simplifies the startup sequence when several modules depend on the same subsystem.

Set the flag only after setup succeeds; a plain `bool` does not protect concurrent calls from threads or an ISR, so serialize them explicitly.[^iso-c-n1570]

## Detailed explanation

TODO
