---
id: emb-cppfound-0098
title: "What does this hardware-register code do?<br><pre class=\"code-block\"><code><span class=\"code-type\">uint32_t</span> reg=*((<span class=\"code-kw\">volatile</span> <span class=\"code-type\">uint32_t</span>*)<span class=\"code-num\">0x40020010</span>);<br>reg|=(<span class=\"code-num\">1</span>&lt;&lt;<span class=\"code-num\">5</span>);<br>*((<span class=\"code-kw\">volatile</span> <span class=\"code-type\">uint32_t</span>*)<span class=\"code-num\">0x40020010</span>)=reg;</code></pre>"
description: "What a volatile read-modify-write sequence does and why it can race with an ISR."
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
    applicability: "Origin of the question and answer; answer not independently verified."
---

## Short answer

TODO

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

