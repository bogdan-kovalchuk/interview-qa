---
id: emb-macros-0038
title: "Чим відрізняються `#ifdef FOO` і `#if FOO`?"
description: "#ifdef FOO перевіряє лише факт визначення макроса – істинно навіть для #define FOO 0."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**`#ifdef FOO`** перевіряє лише факт визначення макроса – істинно навіть для `#define FOO 0`.

`#if FOO` обчислює значення як integer-вираз: для `#define FOO 0` буде хибно, а <span class="warn">для невизначеного `FOO`</span> препроцесор підставить `0` (істинно-хибно), не помилку.

Захист: для feature-флагів зі значеннями використовуй `#if defined(FOO) && FOO`, щоб не плутати «визначено» і «увімкнено».[^embeddedinterviewlab]

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
