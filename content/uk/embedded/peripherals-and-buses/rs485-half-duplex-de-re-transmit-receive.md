---
id: emb-periph-0016
title: "Як працює RS485 half-duplex і як правильно керувати DE/RE pin під час transmit та receive?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

RS485 half-duplex має спільну differential bus, тому пристрій або передає, або слухає. Перед transmit увімкни driver через `DE`, зазвичай вимкни receiver через `RE` або залиш для echo-check, після повного завершення transmission повернися в receive. <span class="warn">Занадто раннє перемикання обрізає stop bit, занадто пізнє блокує відповідь іншого вузла.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
