---
id: emb-cppfound-0077
title: "Що таке strict aliasing rule і як він стосується pointer casting?"
description: "How strict aliasing constrains accesses through incompatible pointer types."
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

<span class="key">Strict aliasing rule</span> (C99 §6.5): компілятор може вважати що вказівники різних несумісних типів НЕ alias-ують (не вказують на одну область пам'яті).<br><br>Дозволяє агресивну оптимізацію: якщо змінили через <code>float*</code> – компілятор не зобов'язаний перечитати через <code>int*</code>.<br><br>Виключення: <code>char*</code> та <code>unsigned char*</code> можуть alias-увати будь-що.<br><br>Порушення: <code>int x; float *fp=(float*)&amp;x; *fp=1.0f;</code> -> UB. Захист: <code>memcpy</code> або <code>union</code> (у C).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
