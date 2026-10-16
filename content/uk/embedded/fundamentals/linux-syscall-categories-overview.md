---
id: emb-fund-0001
title: "Які системні виклики ви знаєте?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
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
