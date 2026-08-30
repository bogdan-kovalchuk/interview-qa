---
id: emb-cemb-0023
title: "Які варіанти використання `volatile` знаєте?"
description: "`volatile` змушує компілятор виконувати читання і записи, які можуть змінюватися поза звичайним контролем коду, але не робить операції атомарними."
track: embedded
section: c-in-embedded
level: junior
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

<code>volatile</code> каже компілятору, що значення може змінитися поза звичайним контролем поточного коду, тому кожне читання або запис треба реально виконувати, а не кешувати в регістрі чи прибирати оптимізацією.[^dou-embedded-interview]

Типові випадки: memory-mapped регістри периферії (<code>volatile uint32_t *reg</code>), змінні, які змінює ISR або signal handler, hardware status flags, прості debug/benchmark випадки. Важливо: <code>volatile</code> <span class="warn">не робить операції атомарними</span>, не гарантує ordering/synchronization і не замінює <code>mutex</code>, critical section або <code>std::atomic</code>.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
