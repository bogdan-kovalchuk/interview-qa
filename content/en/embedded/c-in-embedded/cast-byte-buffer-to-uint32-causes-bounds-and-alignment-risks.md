---
id: emb-cppfound-0034
title: "Find the bug<br><pre class=\"code-block\"><code><span class=\"code-type\">uint8_t</span> buf[<span class=\"code-num\">256</span>];<br><span class=\"code-type\">uint32_t</span> *p = (<span class=\"code-type\">uint32_t</span>*)buf;<br><span class=\"code-kw\">for</span>(<span class=\"code-type\">int</span> i=<span class=\"code-num\">0</span>;<br>i&lt;<span class=\"code-num\">256</span>;<br>i++) p[i]=<span class=\"code-num\">0</span>;</code></pre>"
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
  uk: 1
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

TODO

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
