---
id: emb-patterns-0037
title: "How do you add a timeout to a flag-polling loop?"
description: "Record the start tick and check the elapsed difference against the limit on every iteration."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
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
uint32_t start = tick();
while (!(REG->SR & FLAG)) {
  if (tick() - start > TIMEOUT_MS) return ERR_TIMEOUT;
}
```

## Short answer

**Remember the start; on every iteration check the tick difference against the limit.**

Subtracting unsigned ticks survives counter wraparound correctly. This prevents an infinite hang if the hardware never sets the flag.

Rule: never busy-wait on a hardware flag without a timeout – always timeout plus an error return.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
