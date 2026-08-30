---
id: emb-dtypes-0106
title: "Що таке cache coherency і memory barrier у multi-core MCU, MPU або Embedded Linux системі?"
description: "Cache coherency означає узгодженість даних між CPU caches, DMA і peripheral views of memory. Memory barrier задає порядок memory operations, щоб CPU/compiler не переставили critical accesses."
track: embedded
section: data-types-and-memory-layout
level: senior
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Cache coherency</span> означає узгодженість даних між CPU caches, DMA і peripheral views of memory.<br><span class="key">Memory barrier</span> задає порядок memory operations, щоб CPU/compiler не переставили critical accesses.<br><span class="warn">Для DMA часто потрібні cache clean/invalidate і barriers, інакше device або CPU бачить stale data.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
