---
id: emb-macros-0038
title: "How do `#ifdef FOO` and `#if FOO` differ?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`#ifdef FOO`** checks only whether the macro is defined – true even for `#define FOO 0`.

`#if FOO` evaluates the value as an integer expression: for `#define FOO 0` it is false, and <span class="warn">for undefined `FOO`</span> the preprocessor substitutes `0`, so the condition is false without a diagnostic.

Protection: for feature flags with values use `#if defined(FOO) && FOO` to avoid confusing 'defined' with 'enabled'.[^iso-c-n1570]

## Detailed explanation

TODO
