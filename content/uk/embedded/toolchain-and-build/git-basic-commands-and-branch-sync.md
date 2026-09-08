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
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
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
  - source_id: git-scm-doc
    title: "Git documentation"
    url: "https://git-scm.com/doc"
    accessed: 2026-09-08
    kind: official
    version: "current"
    applicability: "Official Git reference for version control concepts; specific workflows may vary by Git version."
---

## Short answer

Базові команди:[^dou-embedded-interview]

`git init` – створити репозиторій; `git clone URL` – скопіювати існуючий; `git status` – подивитися стан; `git add` – додати зміни в staging area; `git commit` – створити commit; `git log` – історія; `git diff` – перегляд різниці.

Гілки та синхронізація: `git branch` – список/створення гілок; `git switch` або `git checkout` – перейти на гілку; `git merge` – об'єднати гілки; `git rebase` – перенести commits на іншу базу; `git pull` – отримати й інтегрувати зміни; `git push` – відправити commits на remote.

## Detailed explanation

Основні команди Git можна згрупувати за призначенням:[^git-scm-doc]

**Робота з репозиторієм:**
- `git init` – створити новий репозиторій
- `git clone URL` – клонувати існуючий репозиторій

**Цикл modify -> stage -> commit:**
- `git status` – показати стан файлів (modified/staged/untracked)
- `git add file` – додати зміни у staging area
- `git commit -m "message"` – створити commit зі staged змін
- `git diff` – показати зміни між working directory та staging area
- `git diff --staged` – показати зміни між staging area та останнім commit

**Робота з історією:**
- `git log` – показати історію commit-ів
- `git log --oneline` – компактний вигляд історії
- `git blame file` – показати, хто і коли змінив кожний рядок файлу

**Гілки та синхронізація:**
- `git branch` – список, створення або видалення гілок
- `git switch branch` – перейти на іншу гілку
- `git merge branch` – інтегрувати зміни з іншої гілки
- `git rebase` – перенести commits на іншу базу (лінійна історія)
- `git pull` – отримати зміни з remote та інтегрувати їх (fetch + merge)
- `git push` – відправити локальні commits на remote
- `git fetch` – отримати зміни з remote без інтеграції

Типовий робочий процес:

```bash
$ git switch -c feature-x

$ vim file.c

$ git add file.c
$ git commit -m "Implement feature X"

$ git push origin feature-x
```

Git команди працюють разом для управління історією та співпраці. Розуміння трьох станів (modified, staged, committed) допомагає зрозуміти, що робить кожна команда.

## Sources

<!-- generated from frontmatter -->
