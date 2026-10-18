---
id: emb-fund-0003
title: "Що таке system call?"
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

**System call (syscall)** – механізм запиту сервісів ядра з user-space.[^dou-embedded-interview] Оскільки user-space не має прямого доступу до апаратури та ресурсів ядра, програма виконує syscall для переходу в kernel mode.

Механізм (x86-64): програма поміщає номер syscall у `rax`, аргументи у `rdi/rsi/rdx...`, виконує інструкцію `syscall`. Ядро переключається в privileged mode, виконує обробник і повертає результат.

Забезпечує ізоляцію: user-space процеси не можуть пошкодити пам'ять ядра або інших процесів.

## Detailed explanation

TODO
