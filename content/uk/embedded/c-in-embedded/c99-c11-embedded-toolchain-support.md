---
id: emb-cemb-0039
title: "Чим важливі C99 і C11 для embedded C, і які можливості C11 не завжди доступні на MCU toolchains?"
description: "C99 і C11 додали корисні embedded-можливості, але підтримку C11 features треба перевіряти для конкретного MCU toolchain."
track: embedded
section: c-in-embedded
level: middle
type: concept
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

C99 приніс `stdint.h`, `stdbool.h`, designated initializers, mixed declarations і `inline`, що дуже корисно для embedded. C11 додав atomics, threads, alignment features і static assertions. <span class="warn">На MCU toolchains C11 threads/atomics можуть бути неповними або залежати від runtime/libc</span>, тому треба перевіряти конкретний compiler і flags.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
