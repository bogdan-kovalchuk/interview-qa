---
id: py-site-9002
title: Чому внутрішні посилання мають містити base path проєкту?
description: Тестовий файл для перевірки production-посилань і resolver page.
track: python
section: fundamentals
level: junior
type: concept
tags: [site-spike, base-path]
status: published
updated: 2026-09-03
content_revision: 1
anki:
  export: true
sources:
  - title: Astro configuration reference
    url: https://docs.astro.build/en/reference/configuration-reference/
    accessed: 2026-09-03
    kind: official
---

## Short answer

Project site у GitHub Pages працює під назвою репозиторію, тому кореневі посилання проєкту потребують префікса `/interview-qa/`.

## Detailed explanation

Production-збірка застосовує налаштований base path до ресурсів і навігації Starlight. Дзеркало матеріалізує посилання на питання з тим самим префіксом.

## Sources

Згенеровано з frontmatter для spike.
