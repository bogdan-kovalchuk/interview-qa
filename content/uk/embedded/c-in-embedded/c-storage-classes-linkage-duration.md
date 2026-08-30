---
id: emb-cemb-0040
title: "Які storage classes є у C і як вони пов'язані з linkage та storage duration?"
description: "Storage-class specifiers у C впливають на видимість, linkage або тривалість існування об'єкта, але не всі однаково."
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

Основні specifiers: <code>auto</code>, <code>register</code>, <code>static</code>, <code>extern</code>, <code>_Thread_local</code>. <code>static</code> у block scope дає static storage duration, а на file scope дає internal linkage. <code>extern</code> зазвичай оголошує object/function з external linkage, але lifetime визначається самим об'єктом, не словом <code>extern</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
