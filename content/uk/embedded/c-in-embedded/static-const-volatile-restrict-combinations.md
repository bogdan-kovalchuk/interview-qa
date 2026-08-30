---
id: emb-cemb-0032
title: "Для чого потрібні static, const, volatile і restrict у C, і які комбінації мають сенс?"
description: "Практичне питання про embedded-розробку та її обмеження."
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

<code>static</code> керує linkage або storage duration, <code>const</code> забороняє зміну через цей lvalue, <code>volatile</code> змушує реально виконувати access, а <code>restrict</code> обіцяє відсутність aliasing для оптимізації. Для MMIO типовий pointer: <code>volatile uint32_t *</code>; для read-only register може бути <code>volatile const uint32_t *</code>. <code>static const</code> часто кладе таблиці у flash/rodata, а <code>restrict</code> доречний у DSP/buffer code, якщо контракт справді виконується.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

