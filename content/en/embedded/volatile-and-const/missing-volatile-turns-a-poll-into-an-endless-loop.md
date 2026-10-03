---
id: emb-volconst-0005
title: "What can happen to this loop without `volatile`?"
description: "The compiler can turn the loop into an infinite one because the flag never changes within the visible code."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GCC volatile-access behavior and the lack of a memory-barrier guarantee; other compilers can differ."
---

## Question code

```c
uint8_t flag = 0;

while (flag == 0) {
    /* flag встановлює ISR */
}
```

## Short answer

If an ISR changes this object asynchronously without informing the compiler, the loop may become <span class="warn">infinite</span>: ordinary C code does not change `flag`.

The optimiser may read `flag` once and reuse it even if the ISR changes memory.[^iso-c-n1570]

Mitigation: declare the flag as `volatile uint8_t flag` if required by your toolchain's ISR model. If atomicity or ordering of other data matters, add an appropriate critical section or atomic/barrier API.[^iso-c-n1570] [^gcc-volatile]

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
