---
id: emb-cppfound-0034
title: "Знайдіть помилку?<br><pre class=\"code-block\"><code><span class=\"code-type\">uint8_t</span> buf[<span class=\"code-num\">256</span>];<br><span class=\"code-type\">uint32_t</span> *p = (<span class=\"code-type\">uint32_t</span>*)buf;<br><span class=\"code-kw\">for</span>(<span class=\"code-type\">int</span> i=<span class=\"code-num\">0</span>;<br>i&lt;<span class=\"code-num\">256</span>;<br>i++) p[i]=<span class=\"code-num\">0</span>;</code></pre>"
description: "How a byte buffer cast can cause bounds and alignment problems."
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

<span class="warn">Out-of-bounds write!</span> <code>buf</code> – 256 байт. <code>p</code> – <code>uint32_t*</code>, кожен елемент = 4 байти. Цикл <code>p[0]..p[255]</code> записує <code>256 × 4 = 1024 байти</code> – у 4 рази більше розміру буфера.<br><br>Правильно: <code>for(int i=0; i &lt; 256/sizeof(uint32_t); i++) p[i]=0;</code> або <code>memset(buf, 0, sizeof(buf))</code>.<br><br>Також: <code>uint8_t buf[256]</code> може бути не вирівняний для <code>uint32_t</code> -> misaligned access.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
