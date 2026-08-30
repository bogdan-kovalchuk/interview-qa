---
id: emb-dtypes-0019
title: "Що таке little-endian і big-endian? Як Cortex-M зберігає `0x12345678`?"
description: "Little-endian зберігає молодший байт за нижчою адресою; Cortex-M за замовчуванням little-endian."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

**Endianness** - порядок байтів багатобайтових типів у пам'яті.

**Little-endian**: LSB (молодший байт) за нижчою адресою. Cortex-M за замовчуванням little-endian: `0x12345678` у пам'яті -> `[78][56][34][12]` (адреса зростає ->).

**Big-endian**: MSB перший. Використовується у мережевих протоколах (TCP/IP, MODBUS). Для конвертації: `htonl()` / `ntohl()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
