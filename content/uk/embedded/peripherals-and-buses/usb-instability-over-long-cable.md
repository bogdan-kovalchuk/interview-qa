---
id: emb-periph-0014
title: "USB-пристрій нестабільний на відстані 5-10 метрів. Які обмеження USB, кабелю, живлення і альтернативні інтерфейси треба перевірити?"
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

Перевірити специфікаційний ліміт довжини для потрібної USB speed, якість cable, shielding, hubs/repeaters і падіння VBUS під навантаженням. На 5-10 м часто з'являються signal integrity проблеми, ground potential difference і живлення device нижче мінімуму. Альтернативи: powered hub/active cable, USB extender, RS-485/CAN/Ethernet або перенести MCU ближче до sensor.[^dou-embedded-interview]

## Detailed explanation

TODO
