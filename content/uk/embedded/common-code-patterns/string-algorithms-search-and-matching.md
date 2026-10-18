---
id: emb-fund-0005
title: "Які алгоритми роботи з рядками знаєте?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Базові операції: пошук символу або підрядка, порівняння, копіювання, конкатенація, розбиття на токени, reverse, перевірка паліндрому, підрахунок частот символів.[^dou-embedded-interview] У C треба особливо стежити за `\0`, розміром буфера й переповненням.

Відомі алгоритми: **KMP** для пошуку підрядка за O(n+m), **Rabin-Karp** з rolling hash, **Boyer-Moore** для швидкого пошуку на практиці, Trie для множини рядків, Levenshtein distance для схожості рядків. Для embedded часто важливі прості алгоритми без heap і з контрольованим часом виконання.

## Detailed explanation

TODO
