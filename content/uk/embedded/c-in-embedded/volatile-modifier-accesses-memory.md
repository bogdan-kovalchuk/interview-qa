---
id: emb-cemb-0026
title: "Опишіть використання модифікатора `volatile`."
description: "`volatile` змушує компілятор виконувати читання і записи, які можуть змінюватися поза звичайним потоком виконання."
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

Забороняє компілятору кешувати значення змінної в регістрі або прибирати доступ як "зайвий" – при кожному зверненні виконується реальне читання/запис.[^dou-embedded-interview]

Використовується коли значення може змінитися поза звичайним потоком виконання:<br>• <span class="key">Регістри периферії</span>: <code>volatile uint32_t *GPIOA = (uint32_t *)0x40020000;</code><br>• <span class="key">Змінна, яку змінює ISR</span>: <code>volatile bool flag = false;</code><br>• <span class="key">Signal handler</span> або hardware status flag.<br><br>Для потоків сам по собі <code>volatile</code> <span class="warn">не є синхронізацією</span>: не гарантує atomicity, ordering або mutual exclusion. Для цього потрібні <code>mutex</code>, critical section або atomics.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
