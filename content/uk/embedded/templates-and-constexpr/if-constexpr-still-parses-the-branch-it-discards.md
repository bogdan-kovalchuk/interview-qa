---
id: emb-tmplcx-0019
title: "Trap: чим `if constexpr` безпечніший за `#ifdef` щодо помилок?"
description: "#ifdef повністю вирізає невибрану гілку – синтаксичні помилки/опечатки в ній ніколи не помічаються."
track: embedded
section: templates-and-constexpr
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 2
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">`#ifdef` повністю вирізає невибрану гілку – синтаксичні помилки/опечатки в ній ніколи не помічаються.</span>

`if constexpr` змушує компілятор перевірити синтаксис обох гілок (якщо вони не залежать від template-параметра), тож баг у «неактивній» платформі виявиться одразу.

Захист: для платформо-перемикань надавай перевагу `if constexpr` – менше прихованих багів у непротестованих шляхах.[^embeddedinterviewlab]

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
