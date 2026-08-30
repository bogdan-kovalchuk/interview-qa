---
id: emb-cppfound-0003
title: "Trap: що відбудеться?<br><pre class=\"code-block\"><code>int *p;<br>*p = 5;</code></pre>"
description: "Why writing through an uninitialized pointer is undefined behavior."
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

<code>p</code> – <span class="warn">wild pointer</span>: неініціалізований вказівник містить garbage-адресу (випадкове значення зі стека).<br><br>Запис <code>*p = 5</code> -> undefined behavior: може перезаписати випадкову область пам'яті, іншу змінну, або спричинити <span class="warn">HardFault</span> на Cortex-M (якщо адреса поза RAM).<br><br>Захист: завжди ініціалізуй вказівники: <code>int *p = NULL;</code> або одразу <code>int *p = &amp;x;</code>[^embeddedinterviewlab]

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
