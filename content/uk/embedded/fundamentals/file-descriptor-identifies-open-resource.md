---
id: emb-fund-0004
title: "Що таке файловий дескриптор?"
description: "Файловий дескриптор – невід'ємне ціле число, яким ядро ідентифікує відкритий ресурс процесу: файл, сокет, pipe чи пристрій."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

**File descriptor (fd)** – невід'ємне ціле число, що ідентифікує відкритий ресурс у процесі: файл, сокет, pipe, пристрій.[^dou-embedded-interview] Ядро зберігає таблицю fd для кожного процесу.

Стандартні: `0` = stdin, `1` = stdout, `2` = stderr.

Цикл: `fd = open("file", O_RDONLY);`, потім `read(fd, buf, n);`, потім `close(fd);`. В Linux «все є файлом» – через fd можна працювати з пристроями (`/dev/gpio`), sysfs, і навіть таймерами (`timerfd`).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
