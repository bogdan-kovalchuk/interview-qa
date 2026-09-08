---
id: py-strtxt-0001
title: "У чому різниця між str і bytes у Python 3, і коли використовувати кожен тип?"
description: "У Python 3 str представляє Unicode-текст, а bytes є незмінною послідовністю байтових значень; межа між ними потребує явного encoding або decoding."
track: python
section: strings-and-text
level: middle
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`str` є незмінною послідовністю Unicode code points для тексту, а `bytes` є незмінною послідовністю цілих чисел від 0 до 255 для encoded text або довільних binary data.**[^py314-library-stdtypes] Усередині програми текст варто тримати як `str`, а на binary чи protocol boundaries використовувати `bytes`, якщо цього вимагає API. Encoding перетворює `str` на `bytes` із явно заданими character encoding та error policy, а decoding виконує зворотне перетворення. Об'єкт `bytes` не зберігає інформації про те, яке encoding його створило.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
