---
id: emb-cppfound-0100
title: "Trap: where is the error?<br><pre class=\"code-block\"><code><span class=\"code-type\">char</span> *p = <span class=\"code-fn\">malloc</span>(<span class=\"code-num\">5</span>);<br>strcpy(p, \"hello\");<br>p[<span class=\"code-num\">5</span>] = '\\<span class=\"code-num\">0</span>';</code></pre>"
description: "Why allocating five bytes is insufficient for the string hello and its terminator."
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

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->


