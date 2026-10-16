---
id: emb-irq-0012
title: "Що таке interrupt vector і як він відрізняється між MCU startup code та Linux kernel?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

На MCU **interrupt vector table** зазвичай лежить за фіксованою адресою і містить initial stack pointer та addresses handlers. Startup code задає weak default handlers, а firmware замінює потрібні ISR. У Linux hardware interrupt routing прихований за architecture/kernel IRQ subsystem: driver реєструє handler через kernel API, а не редагує startup vector table напряму.[^dou-embedded-interview]

## Detailed explanation

TODO
