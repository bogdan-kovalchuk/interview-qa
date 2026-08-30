---
id: emb-testemb-0008
title: "Які dynamic analysis підходи можливі для embedded C/C++: sanitizers на host, Valgrind, trace, fault injection?"
description: "На host можна запускати ASan/UBSan/TSan для логіки без hardware dependency, а Valgrind корисний для Linux-target або host-сценаріїв.На target частіше …"
track: embedded
section: testing-embedded
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
---

## Short answer

На host можна запускати <span class="key">ASan/UBSan/TSan</span> для логіки без hardware dependency, а <code>Valgrind</code> корисний для Linux-target або host-сценаріїв.<br>На target частіше використовують trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation і HIL tests.<br><span class="warn">Sanitizer на PC не доводить коректність ISR, DMA cache coherency або реального timing.</span>[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
