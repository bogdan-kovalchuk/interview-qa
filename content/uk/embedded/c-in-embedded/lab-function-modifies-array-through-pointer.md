---
id: emb-cppfound-0063
title: "Що виведе?<br><pre class=\"code-block\"><code>void f(int *p, int n){<br>  p[0]=99;<br>} int a[3]={1,2,3};<br>f(a,3);<br>printf(\"%d\",a[0]);</code></pre>"
description: "How a function changes the caller's array through a pointer parameter."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

<code>99</code>.<br><br><code>a</code> decay-ується до вказівника. Функція <code>f</code> отримує <code>int*</code> – вказівник на перший елемент <code>a[0]</code>. <code>p[0] = 99</code> -> змінює <code>a[0]</code> у caller.<br><br>Масиви у C передаються by reference (через вказівник на перший елемент) – функція може змінювати оригінальні дані. Якщо потрібна тільки читання: <code>const int *p</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
