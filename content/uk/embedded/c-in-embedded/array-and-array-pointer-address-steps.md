---
id: emb-cppfound-0083
title: "Яка адреса <code>arr</code>, <code>&amp;arr</code>, <code>arr+1</code>, <code>&amp;arr+1</code> якщо <code>int arr[4]</code> за адресою <code>0x1000</code>?"
description: "How array and pointer types produce different address increments."
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

<code>arr</code> -> <code>0x1000</code> (decay до <code>int*</code>, вказує на arr[0]).<br><code>&amp;arr</code> -> <code>0x1000</code> (вказує на весь масив, тип <code>int(*)[4]</code>). Та сама адреса, різний тип!<br><br><code>arr+1</code> -> <code>0x1004</code> (крок = <code>sizeof(int) = 4</code>).<br><code>&amp;arr+1</code> -> <code>0x1010</code> (крок = <code>sizeof(int[4]) = 16</code>).<br><br>Ось де різниця типів проявляється: однакова початкова адреса, різний крок.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

