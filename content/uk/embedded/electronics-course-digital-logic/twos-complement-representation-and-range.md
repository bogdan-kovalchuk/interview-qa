---
id: emb-eldig-0027
title: "Як утворюється від'ємне число в доповненні до двох (two's complement) і який діапазон 8 бітів?"
description: "Як утворюється від'ємне число в доповненні до двох (two's complement) і який діапазон 8 бітів?"
track: embedded
section: electronics-course-digital-logic
level: junior
type: concept
tags: []
status: published
updated: 2026-09-27
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 86 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Для отримання від'ємного числа інвертують усі біти вихідного додатного числа та додають до результату одиницю. Для <span class="formula">\(n\)</span> бітів допустимий діапазон значень становить від <span class="formula">\(-2^{n-1}\)</span> до <span class="formula">\(2^{n-1} - 1\)</span>. У 8-розрядній системі це відповідає числам від −128 до +127, причому одиниця в старшому біті (MSB) свідчить про від'ємний знак.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
