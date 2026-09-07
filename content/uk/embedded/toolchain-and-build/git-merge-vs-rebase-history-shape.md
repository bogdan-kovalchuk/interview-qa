---
id: emb-build-0007
title: "В чому полягає різниця між merge та rebase?"
description: "git merge зберігає розгалужену історію через merge commit, а git rebase переносить commits на нову базу і робить історію лінійною, переписуючи хеші."
track: embedded
section: toolchain-and-build
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`git merge` об'єднує дві гілки, зберігаючи їхню історію; якщо історії розійшлися, Git створює merge commit.[^dou-embedded-interview] Плюс: чесно показує, коли й де гілки були об'єднані; мінус: історія може стати розгалуженою.

`git rebase` переносить commits поточної гілки поверх іншої бази, ніби робота починалась від новішого commit. Плюс: лінійна й чистіша історія; Мінус: rebase переписує commit hash-и.

Практичне правило: **merge** безпечний для спільних/published гілок; **rebase** зручний для локальної feature-гілки перед merge, але не варто rebase-ити чужу опубліковану історію без домовленості.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
