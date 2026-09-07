---
id: emb-macros-0028
title: "Trap: why did adding a MIN/MAX clamp to a filter macro add noise to the ADC readings?"
description: "The macro argument containing adcread() is evaluated multiple times, causing double evaluation and noisy samples."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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
#define FILT(s) ((s) + ((adc_read() - (s)) >> 3))
```

## Short answer

<span class="warn">The argument expression with `adc_read()` is evaluated multiple times</span> in the macro body (double evaluation).

Each expansion of `adc_read()` triggers a new ADC conversion with a different value and noise, and the extra conversions also waste energy. The filter computes on mismatched samples.

Protection: use `static inline` with a single parameter, or read `adc_read()` into a local variable once before computation.[^embeddedinterviewlab]

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
