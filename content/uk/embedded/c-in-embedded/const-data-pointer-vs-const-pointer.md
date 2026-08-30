---
id: emb-cppfound-0026
title: "Чим відрізняється <code>const int *p</code> від <code>int * const p</code>?"
description: "How const applies to pointed-to data and to the pointer itself."
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

<code>const int *p</code> (або <code>int const *p</code>) – <span class="key">вказівник на константний int</span>:<br>• <code>*p = 5</code> – заборонено (дані захищені);<br>• <code>p = &amp;y</code> – дозволено (адресу можна змінити).<br><br><code>int * const p</code> – <span class="key">константний вказівник на int</span>:<br>• <code>*p = 5</code> – дозволено;<br>• <code>p = &amp;y</code> – заборонено (адреса фіксована).<br><br><code>const int * const p</code> – і дані, і адреса незмінні. Правило: читай справа наліво.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
