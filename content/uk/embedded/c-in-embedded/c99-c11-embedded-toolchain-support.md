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
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

C99 приніс <code>stdint.h</code>, <code>stdbool.h</code>, designated initializers, mixed declarations і <code>inline</code>, що дуже корисно для embedded. C11 додав atomics, threads, alignment features і static assertions. <span class="warn">На MCU toolchains C11 threads/atomics можуть бути неповними або залежати від runtime/libc</span>, тому треба перевіряти конкретний compiler і flags.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
