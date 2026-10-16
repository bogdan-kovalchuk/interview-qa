---
id: emb-fund-0017
title: "Чим архітектура Harvard відрізняється від von Neumann і як це впливає на доступ до Flash/RAM?"
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

У **von Neumann** code і data ділять один address space/bus. У **Harvard** instruction і data memories/buses розділені, тому Flash і RAM можуть мати різні правила доступу. На деяких MCU читання constants із program memory потребує спеціальних instructions/API, а self-programming Flash має обмеження по erase/write і timing.[^dou-embedded-interview]

## Detailed explanation

TODO
