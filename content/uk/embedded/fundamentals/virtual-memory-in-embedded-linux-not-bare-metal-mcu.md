---
id: emb-fund-0011
title: "Для чого потрібна virtual memory в Embedded Linux і чому її зазвичай немає на bare-metal MCU?"
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

Virtual memory дає кожному process власний address space, memory protection, lazy mapping, shared libraries, `mmap` і copy-on-write. Bare-metal MCU зазвичай має малу RAM/Flash, deterministic requirements і часто тільки MPU або взагалі без memory protection. Тому там працюють з physical addresses, linker script і прямим MMIO.[^dou-embedded-interview]

## Detailed explanation

TODO
