---
id: emb-raii-0001
title: "Що таке RAII і як розшифровується?"
description: "RAII (Resource Acquisition Is Initialization) – lifetime ресурсу прив'язаний до lifetime C++-об'єкта."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

**RAII (Resource Acquisition Is Initialization)** – lifetime ресурсу прив'язаний до lifetime C++-об'єкта.

Конструктор захоплює ресурс, деструктор звільняє його. Компілятор гарантує очищення при виході зі scope: нормальним шляхом, через early `return`, а якщо exceptions увімкнені – також через stack unwinding.

Правило: усе, що має «взяти і віддати», загортай в об'єкт із ctor/dtor.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
