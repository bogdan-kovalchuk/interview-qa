---
id: emb-fund-0004
title: "Що таке файловий дескриптор?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**File descriptor (fd)** – невід'ємне ціле число, що ідентифікує відкритий ресурс у процесі: файл, сокет, pipe, пристрій.[^dou-embedded-interview] Ядро зберігає таблицю fd для кожного процесу.

Стандартні: `0` = stdin, `1` = stdout, `2` = stderr.

Цикл: `fd = open("file", O_RDONLY);`, потім `read(fd, buf, n);`, потім `close(fd);`. В Linux «все є файлом» – через fd можна працювати з пристроями (`/dev/gpio`), sysfs, і навіть таймерами (`timerfd`).

## Detailed explanation

TODO
