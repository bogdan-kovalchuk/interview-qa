---
id: py-site-9001
title: Як працює згенероване дзеркало контенту?
description: Тестовий файл, який доводить, що Starlight споживає згенерований Markdown.
track: python
section: fundamentals
level: junior
type: concept
tags: [site-spike, mirror]
status: published
updated: 2026-09-03
content_revision: 1
anki:
  export: true
sources:
  - title: Astro Starlight documentation
    url: https://starlight.astro.build/
    accessed: 2026-09-03
    kind: official
---

## Short answer

Python-інструмент копіює вихідний Markdown до стандартної docs collection Starlight і додає обчислені маршрутні метадані.

## Detailed explanation

Starlight читає лише згенероване дзеркало через `docsLoader`. Вихідне дерево не залежить від Astro.

## Follow-up

- [Як зберігається коректність посилань із base path?](qid:py-site-9002)

## Sources

Згенеровано з frontmatter для spike.
