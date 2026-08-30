---
id: emb-cppfound-0047
title: "Що таке flexible array member (FAM) у C99 і де він зберігається?"
description: "How C99 flexible array members are laid out and allocated."
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

<span class="key">Flexible Array Member</span> (FAM) – останнє поле структури з невказаним розміром: <code>struct Packet { uint8_t len; uint8_t data[]; };</code><br><br><code>sizeof(struct Packet)</code> не включає <code>data</code>. FAM виділяється разом зі структурою: <code>malloc(sizeof(Packet) + n)</code> – тоді <code>data</code> займає <code>n</code> байт одразу після полів структури.<br><br>Зберігається у тому ж блоці пам'яті що й структура (heap або static). Не може бути єдиним членом struct і не може у масиві.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

