---
id: emb-safety-0001
title: "What watchdog functions exist, and how does an independent watchdog differ from a window watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 – Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
  - source_id: zephyr-watchdog-api
    title: "Zephyr Project documentation: Watchdog driver API"
    url: https://docs.zephyrproject.org/latest/doxygen/html/group__watchdog__interface.html
  - source_id: zephyr-wdt-window
    title: "Zephyr Project documentation: wdt_window struct reference"
    url: https://docs.zephyrproject.org/latest/doxygen/html/structwdt__window.html
  - source_id: esp-idf-watchdogs
    title: "ESP-IDF Programming Guide (ESP32): Watchdogs"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/wdts.html
  - source_id: nrf52840-wdt
    title: "nRF52840 Product Specification: WDT – Watchdog timer"
    url: https://docs.nordicsemi.com/bundle/ps_nrf52840/page/wdt.html
  - source_id: ti-tps3430
    title: "TI TPS3430 Window Watchdog Timer with Programmable Reset Delay (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/tps3430.pdf
---

## Short answer

A watchdog resets the system if firmware does not perform a refresh in time. **Independent watchdog** typically has a separate low-speed clock and works even during main clock problems. **Window watchdog** requires a refresh neither too early nor too late, so it catches both hangs and runaway loops.[^dou-embedded-interview]

## Detailed explanation

TODO
