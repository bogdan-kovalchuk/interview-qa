---
id: emb-dtypes-0108
title: "How to safely parse a binary protocol frame without invalid type punning and alignment issues?"
description: "Check the frame length, read each field via memcpy or byte shifts, apply explicit byte-order conversion, and never cast a wire-format buffer to a struct unless layout and endianness are guaranteed."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Check the frame length, then read each field from the `uint8_t` buffer via `memcpy` or byte shifts. For multi-byte fields, explicitly apply `le16toh`/`ntohs` or a custom conversion. <span class="warn">Do not cast a wire-format buffer to a struct</span> unless layout, packing, alignment, and endianness are fixed and verified.[^dou-embedded-interview]

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
