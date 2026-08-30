---
id: emb-build-0002
title: "Назвіть основні команди git."
description: "Базові команди git охоплюють локальний цикл (init/add/commit/log/diff) і синхронізацію гілок (branch/switch/merge/rebase/pull/push)."
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? toolchain-and-build; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Базові команди:[^dou-embedded-interview]

`git init` – створити репозиторій; `git clone URL` – скопіювати існуючий; `git status` – подивитися стан; `git add` – додати зміни в staging area; `git commit` – створити commit; `git log` – історія; `git diff` – перегляд різниці.

Гілки та синхронізація: `git branch` – список/створення гілок; `git switch` або `git checkout` – перейти на гілку; `git merge` – об'єднати гілки; `git rebase` – перенести commits на іншу базу; `git pull` – отримати й інтегрувати зміни; `git push` – відправити commits на remote.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
