---
id: emb-cemb-0041
title: "Що таке scope, linkage і lifetime у C, і чому ці поняття часто плутають?"
description: "Scope описує видимість імені, linkage – зв'язок імен між translation units, а lifetime – час існування об'єкта."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Scope</span> – де ім'я видиме в source code. <span class="key">Linkage</span> – чи одне й те саме ім'я може посилатися на той самий object/function між scopes або translation units. <span class="key">Lifetime/storage duration</span> – коли існує сам об'єкт у пам'яті; наприклад, block-scope <code>static</code> має локальну видимість, але живе весь runtime.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
