---
id: emb-build-0003
title: "Що таке інтерактивний rebase?"
description: "git rebase -i відкриває список commits перед обраною базою, дозволяючи pick, reword, squash, edit чи drop кожен commit, переписуючи історію."
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

`git rebase -i` – режим редагування історії commits перед обраною базою.[^dou-embedded-interview] Він відкриває список commits, де можна змінити дії для кожного commit.

Типові дії: `pick` – залишити commit; `reword` – змінити повідомлення; `squash`/`fixup` – об'єднати commits; `edit` – зупинитися для правки commit; `drop` – видалити commit; можна також змінити порядок commits.

Використання: почистити локальну feature-гілку перед pull request, об'єднати дрібні fixup commits, виправити commit message. Важливо: це <span class="warn">переписує історію</span>, тому обережно з commits, які вже були відправлені й використовуються іншими.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
