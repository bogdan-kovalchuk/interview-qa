---
id: emb-fund-0001
title: "Які системні виклики ви знаєте?"
description: "Системні виклики групуються за категоріями – файлова система, процеси, пам'ять, мережа, синхронізація і пристрої."
track: embedded
section: fundamentals
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Основні категорії:[^dou-embedded-interview]

- **Файлова система**: `open()`, `read()`, `write()`, `close()`, `lseek()`, `stat()`, `unlink()`
- **Процеси**: `fork()`, `exec()`, `wait()`, `exit()`, `getpid()`
- **Пам'ять**: `mmap()`, `munmap()`, `brk()`
- **Мережа**: `socket()`, `bind()`, `connect()`, `send()`, `recv()`
- **Синхронізація**: `futex()`
- **Пристрої**: `ioctl()`.

Переглянути всі: `man 2 syscalls` або файл `arch/x86/entry/syscalls/syscall_64.tbl` у ядрі.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
