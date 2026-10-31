---
id: emb-irq-0002
title: "What is a watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: linux-watchdog-api
    title: "The Linux Watchdog driver API"
    url: https://docs.kernel.org/watchdog/watchdog-api.html
  - source_id: nrf52840-wdt
    title: "nRF52840 Product Specification: WDT – Watchdog timer"
    url: https://docs.nordicsemi.com/bundle/ps_nrf52840/page/wdt.html
  - source_id: zephyr-watchdog-api
    title: "Zephyr Project documentation: Watchdog driver API"
    url: https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface.html
  - source_id: esp-idf-watchdogs
    title: "ESP-IDF Programming Guide (ESP32): Watchdogs"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/wdts.html
---

## Short answer

**Watchdog Timer (WDT)** is a hardware timer that resets the microcontroller if the program does not "feed" it in time.[^dou-embedded-interview]

Principle: the program regularly writes a special value to the WDT register ("kick" or "feed"); if that stops, the timer fires and resets the system.

It protects against hangs, infinite loops and stack overflow. Types: **IWDG** (independent, runs from a separate oscillator and does not stop with the main clock) and **WWDG** (window watchdog – fed only inside a time window, so feeding too early is caught too).

## Detailed explanation

TODO
