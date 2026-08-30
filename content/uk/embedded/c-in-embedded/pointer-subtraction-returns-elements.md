---
id: emb-cppfound-0091
title: "Trap: що виведе?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">5</span>];<br><span class=\"code-type\">int</span> *p=arr+<span class=\"code-num\">3</span>;<br><span class=\"code-type\">int</span> *q=arr+<span class=\"code-num\">1</span>;<br><span class=\"code-fn\">printf</span>(\"%td\", p-q);</code></pre>"
description: "Why subtracting pointers returns an element distance rather than a byte count."
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

<code>2</code>. Це не trap, але перевіряє розуміння pointer subtraction.<br><br>Справжній trap: люди очікують <span class="warn">байтову різницю</span> (8 байт), але отримують <span class="key">кількість елементів</span> (2). <code>p - q</code> = <code>(arr+3) - (arr+1) = 2</code>.<br><br>Байтова різниця: <code>2 * sizeof(int) = 8</code>. Але <code>ptrdiff_t</code> повертає елементи. Якщо потрібна байтова різниця: <code>(char*)p - (char*)q</code> або <code>(uintptr_t)p - (uintptr_t)q</code>.[^embeddedinterviewlab]

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


