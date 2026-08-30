---
id: emb-cppfound-0073
title: "Яке значення матиме <code>*(uint8_t*)(&amp;val)</code> якщо <code>uint32_t val = 0x12345678</code> (little-endian)?"
description: "How a byte pointer exposes the least significant byte on little-endian systems."
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

<span class="key">0x78</span>.<br><br>Cast <code>(uint8_t*)(&amp;val)</code> – вказівник на перший байт <code>val</code> у пам'яті. На little-endian: LSB знаходиться за найменшою адресою -> <code>0x78</code>.<br><br>Розкладка у пам'яті: <code>[78][56][34][12]</code>. Наступний байт: <code>*((uint8_t*)(&amp;val) + 1) = 0x56</code>.<br><br>Доступ через byte pointer дозволений для character types (<code>unsigned char*</code>). На практиці <code>uint8_t</code> зазвичай є typedef до <code>unsigned char</code>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
