---
id: emb-irq-0002
title: "What is a watchdog?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

**Watchdog Timer (WDT)** is a hardware timer that resets the microcontroller if the program does not "feed" it in time.[^dou-embedded-interview]

Principle: the program regularly writes a special value to the WDT register ("kick" or "feed"); if that stops, the timer fires and resets the system.

It protects against hangs, infinite loops and stack overflow. Types: **IWDG** (independent, runs from a separate oscillator and does not stop with the main clock) and **WWDG** (window watchdog – fed only inside a time window, so feeding too early is caught too).

## Detailed explanation

TODO
