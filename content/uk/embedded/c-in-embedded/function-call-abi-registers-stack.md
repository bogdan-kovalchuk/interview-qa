---
id: emb-cemb-0042
title: "Як працює function call на рівні ABI: stack frame, registers, return address і calling convention?"
description: "ABI визначає передавання аргументів, збереження registers, stack frame та повернення з function call."
track: embedded
section: c-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

ABI задає, які аргументи й return value ідуть у registers, що кладеться на stack і які registers має зберігати caller/callee. Під час call зберігається return address, створюється stack frame для locals/spills, потім callee повертає результат і відновлює потрібний стан. Для debug HardFault корисно дивитися SP, LR, PC і stack frame.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
