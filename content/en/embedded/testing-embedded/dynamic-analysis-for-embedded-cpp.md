---
id: emb-testemb-0008
title: "Which dynamic-analysis approaches are possible for embedded C/C++: host sanitizers, Valgrind, tracing, and fault injection?"
description: "Host sanitizers cover portable logic; on target, use trace, coverage, fault injection, and HIL tests."
track: embedded
section: testing-embedded
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for testing embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

On the host, you can run **ASan/UBSan/TSan** for logic without hardware dependencies, and `Valgrind` is useful for Linux-target or host scenarios. On target, trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation, and HIL tests are more common. <span class="warn">A sanitizer on a PC does not prove correctness of ISRs, DMA cache coherency, or real timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
