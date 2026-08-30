---
id: emb-fund-0005
title: "Які алгоритми роботи з рядками знаєте?"
description: "Базові операції з рядками – пошук, порівняння, токенізація – доповнюються алгоритмами KMP, Rabin-Karp і Boyer-Moore для пошуку підрядка."
track: embedded
section: fundamentals
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

Базові операції: пошук символу або підрядка, порівняння, копіювання, конкатенація, розбиття на токени, reverse, перевірка паліндрому, підрахунок частот символів.[^dou-embedded-interview] У C треба особливо стежити за `\0`, розміром буфера й переповненням.

Відомі алгоритми: **KMP** для пошуку підрядка за O(n+m), **Rabin-Karp** з rolling hash, **Boyer-Moore** для швидкого пошуку на практиці, Trie для множини рядків, Levenshtein distance для схожості рядків. Для embedded часто важливі прості алгоритми без heap і з контрольованим часом виконання.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
