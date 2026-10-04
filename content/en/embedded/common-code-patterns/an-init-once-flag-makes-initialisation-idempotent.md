---
id: emb-patterns-0028
title: "What is the init-once (idempotent) pattern?"
description: "A flag guarantees initialization runs only once even if init is called multiple times"
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

## Sources

<!-- generated from frontmatter -->
