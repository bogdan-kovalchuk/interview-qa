---
id: emb-cemb-0036
title: "What is a bit-field in C, and why is it risky for MMIO registers or protocols?"
description: "Bit-field layout is implementation-defined, so it is not a portable representation for MMIO or wire protocols."
track: embedded
section: c-in-embedded
level: middle
type: pitfall
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

A **bit-field** is a struct field with a specified number of bits, for example `unsigned mode:3`. Its bit order, allocation unit, padding, and even the signedness of some forms depend on the implementation. <span class="warn">This is dangerous for MMIO and wire protocols</span>: it is better to use masks/shifts over `uint32_t`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
