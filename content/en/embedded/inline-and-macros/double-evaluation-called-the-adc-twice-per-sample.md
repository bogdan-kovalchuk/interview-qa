---
id: emb-macros-0028
title: "Trap: how can repeated macro argument evaluation distort an ADC filter?"
description: "A macro substitutes an argument expression repeatedly, so an adc_read() call in it may run multiple times."
track: embedded
section: inline-and-macros
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
  - source_id: gcc-cpp-invocation
    title: "GCC: Invocation (The C Preprocessor)"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents invoking GCC's preprocessor with -E and its output; other compilers may use different options."
---

## Question code

```c
#define FILT(s) ((s) + ((adc_read() - (s)) >> 3))
```

## Short answer

The macro substitutes parameter `s` twice in its replacement list, so passing `adc_read()` as the argument evaluates it twice; the body also contains a separate `adc_read()` call.[^iso-c-n1570]

If each call starts a new conversion, the formula mixes different samples; the exact behavior depends on the implementation of `adc_read()`. Read once into a local variable or pass a stable value to a `static inline` function.[^iso-c-n1570]

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
