---
id: emb-cppfound-0054
title: "Що таке pointer aliasing і як він впливає на оптимізацію?"
description: "How strict aliasing affects pointer-based optimization."
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
---

## Short answer

<span class="key">Pointer aliasing</span> – ситуація коли два вказівники різних типів вказують на одну область пам'яті.<br><br>Strict aliasing rule (C99 §6.5): компілятор може вважати, що вказівники різних типів не alias-ують (окрім <code>char*</code>/<code>unsigned char*</code>). Це дозволяє більш агресивну оптимізацію.<br><br>Порушення: <code>int x; float *fp = (float*)&amp;x; *fp = 1.0f;</code> -> UB.<br><br>Захист: <code>memcpy</code> для type punning, <code>char*</code> для byte access, <code>restrict</code> для явної гарантії no-aliasing.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

