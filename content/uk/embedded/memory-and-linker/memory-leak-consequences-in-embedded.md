---
id: emb-memlink-0002
title: "Які проблеми можуть виникнути, якщо не звільнити пам'ять?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**Memory leak** – виділена пам'ять не повертається в систему, хоча більше не використовується.[^dou-embedded-interview] Наслідки:

- heap поступово вичерпується, тому `malloc` повертає `NULL`
- система уповільнюється або зависає
- в Embedded (MCU без MMU та ОС) це особливо критично: невеликий heap може закінчитися після годин або днів роботи, і пристрій піде в reset/fault або некоректний стан

Супутні проблеми: <span class="warn">dangling pointer</span> (доступ до звільненої пам'яті), <span class="warn">double free</span> (UB).

## Detailed explanation

TODO
