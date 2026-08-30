---
id: emb-cppfound-0025
title: "Trap: легально у стандартному C?<br><pre class=\"code-block\"><code><span class=\"code-type\">void</span> *p = <span class=\"code-fn\">malloc</span>(<span class=\"code-num\">10</span>);<br>p++;</code></pre>"
description: "Why arithmetic on void pointers is not standard C."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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

<span class="warn">НІ, це невалідний стандартний C</span> (constraint violation). Стандарт забороняє pointer arithmetic на <code>void*</code> – розмір елемента невідомий (sizeof(void) не визначений), тому компілятор має видати діагностику.<br><br>GCC дозволяє як extension: трактує <code>sizeof(void) = 1</code>, тому <code>p++</code> -> +1 байт. З <code>-pedantic-errors</code>: помилка.<br><br>Правильно: перед arithmetic – cast до конкретного типу: <code>uint8_t *bp = (uint8_t*)p; bp++;</code>[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
