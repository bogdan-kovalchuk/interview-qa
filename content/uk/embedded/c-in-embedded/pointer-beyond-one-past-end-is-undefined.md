---
id: emb-cppfound-0041
title: "Trap: UB?<br><pre class=\"code-block\"><code>int arr[4]={0};<br>int *p=arr;<br>p+=5;<br>*p=1;</code></pre>"
description: "Why forming a pointer beyond one-past-the-end is undefined behavior."
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="warn">Так, UB</span> (навіть без розіменування).<br><br>Формування вказівника <code>p += 5</code> виходить за межі масиву більш ніж на 1: <code>arr</code> має 4 елементи, тому валідні вказівники: <code>arr</code> до <code>arr+4</code> (включно "one-past-the-end"). <code>arr+5</code> -> UB вже при формуванні.<br><br>One-past-the-end (<code>arr+4</code>) – дозволено формувати, але <span class="warn">не розіменовувати</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
