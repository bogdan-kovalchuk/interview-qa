---
id: emb-hwbasic-0004
title: "Як оцінити signal integrity для довгої лінії або швидкого цифрового інтерфейсу на embedded-пристрої?"
description: "Оцінювання signal integrity перевіряє форму сигналу, відбиття, перешкоди, завершення лінії та часовий запас на реальному hardware."
track: embedded
section: hardware-basics
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

Оцінити довжину лінії відносно rise time: якщо propagation delay значна, лінію треба трактувати як transmission line. Перевірити impedance, termination, return path, ground reference, crosstalk, ringing і overshoot осцилографом з правильним probing. Для довгих/шумних ліній часто краще differential interface типу RS-485/CAN/Ethernet, нижча швидкість або гальванічна ізоляція.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
