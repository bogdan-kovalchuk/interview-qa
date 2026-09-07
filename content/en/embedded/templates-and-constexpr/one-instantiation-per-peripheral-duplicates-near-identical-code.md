---
id: emb-tmplcx-0024
title: "Trap: why can `Uart<USART1>` and `Uart<USART2>` inflate Flash?"
description: "Each instantiation per peripheral can produce nearly identical code, differing only in the base address constant."
track: embedded
section: templates-and-constexpr
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">Each instantiation per peripheral can produce nearly identical code – only the base address constant differs.</span>

On small MCUs (microcontroller unit) this adds up quickly if you do the same with `Uart<...>`, `Spi<...>`, `I2c<...>` for many peripherals.

Mitigation: a non-template `UartImpl` with base address as a ctor parameter plus a thin template wrapper with a `constexpr` address; confirm the savings with the linker map.[^embeddedinterviewlab]

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
