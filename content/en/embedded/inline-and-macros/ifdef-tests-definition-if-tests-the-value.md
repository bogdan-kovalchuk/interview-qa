---
id: emb-macros-0038
title: "How do `#ifdef FOO` and `#if FOO` differ?"
description: "#ifdef FOO checks only whether the macro is defined, returning true even for #define FOO 0."
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

## Short answer

**`#ifdef FOO`** checks only whether the macro is defined – true even for `#define FOO 0`.

`#if FOO` evaluates the value as an integer expression: for `#define FOO 0` it is false, and <span class="warn">for undefined `FOO`</span> the preprocessor substitutes `0` (true-false), not an error.

Protection: for feature flags with values use `#if defined(FOO) && FOO` to avoid confusing 'defined' with 'enabled'.[^embeddedinterviewlab]

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
