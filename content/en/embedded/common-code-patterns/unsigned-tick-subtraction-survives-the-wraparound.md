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
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Supports modular unsigned arithmetic (6.2.5, paragraph 9), integer promotions (6.3.1.1) and the rules for volatile objects (6.7.3, paragraph 7); says nothing about specific timers or toolchains."
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Paper by a NASA/JPL author, hosted on his site: rule 2 requires a fixed upper bound for every loop, rule 7 requires checking return values and parameter validity. It is a guideline for safety-critical C, not a requirement for every project."
---

## Question code

```c
uint32_t start = tick();
while (!(REG->SR & FLAG)) {
  if (tick() - start > TIMEOUT_MS) return ERR_TIMEOUT;
}
```

## Short answer

**Record the start tick and compare the difference `tick() - start` with the limit on every iteration.**

Unsigned subtraction gives the correct elapsed time even after the counter wraps, provided `tick()` returns the same unsigned type as `start` and the wait is shorter than the counter period.[^iso-c-n1570] This keeps the loop from hanging forever if the hardware never sets the flag: after the timeout, return an error instead of waiting.[^holzmann-power-of-ten]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
