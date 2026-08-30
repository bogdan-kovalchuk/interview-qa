---
id: emb-build-0001
title: "Які три основні стани має git?"
description: "Файл у Git проходить три стани – modified, staged і committed – відповідно до робочої директорії, staging area і локального репозиторію."
track: embedded
section: toolchain-and-build
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
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

У базовій моделі Git файл проходить три стани:[^dou-embedded-interview]

- **Modified** – файл змінено у робочій директорії, але ще не додано в індекс.
- **Staged** – зміни додано в staging area командою `git add`; вони готові потрапити в наступний commit.
- **Committed** – зміни збережені в локальному репозиторії як commit.

Типовий цикл: редагування файлу, потім `git add file`, потім `git commit -m "message"`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
