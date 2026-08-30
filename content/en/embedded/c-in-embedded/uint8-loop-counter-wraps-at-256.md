---
id: emb-cppfound-0086
title: "Trap: does this loop run forever?<br><pre class=\"code-block\"><code><span class=\"code-type\">int</span> arr[<span class=\"code-num\">256</span>];<br><span class=\"code-type\">int</span> *p=arr;<br><span class=\"code-kw\">for</span>(<span class=\"code-type\">uint8_t</span> i=<span class=\"code-num\">0</span>;<br>i&lt;<span class=\"code-num\">256</span>;<br>i++) *p++=i;</code></pre>"
description: "Why an 8-bit loop counter cannot reach the terminating value 256."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

TODO

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
