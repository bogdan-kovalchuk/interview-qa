---
id: emb-hwbasic-0001
title: "Що таке булева алгебра?"
track: embedded
section: hardware-basics
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

**Булева алгебра** – математична система для значень істина/хиба або 1/0.[^dou-embedded-interview] Базові операції: AND (`&&` або логічне множення), OR (`||` або логічне додавання), NOT (`!`), а також XOR.

В електроніці вона описує логічні вентилі й цифрові схеми, а в програмуванні – умови, маски, флаги та оптимізацію логічних виразів. Наприклад, закони Де Моргана: `!(A && B) == (!A || !B)` і `!(A || B) == (!A && !B)`.

## Detailed explanation

TODO
