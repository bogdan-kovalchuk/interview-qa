---
id: emb-cppfound-0089
title: "Яка різниця між <code>memcpy</code> і pointer cast для копіювання між типами?"
description: "Why memcpy avoids aliasing and alignment problems during type punning."
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

<span class="key">Pointer cast + dereference</span>: <code>uint32_t x = *(uint32_t*)bytes;</code> – потенційний UB (strict aliasing, misalignment). Компілятор може оптимізувати "неправильно".<br><br><span class="key">memcpy</span>: <code>uint32_t x; memcpy(&amp;x, bytes, 4);</code> – завжди коректно: не порушує aliasing, компілятор оптимізує до одного LDR якщо вирівняно.<br><br>Правило: для type punning використовуй <code>memcpy</code> (або <code>union</code> у C). Pointer cast безпечний лише для <code>char*</code>/<code>unsigned char*</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->


