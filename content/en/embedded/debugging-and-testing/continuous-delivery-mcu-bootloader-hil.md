---
id: emb-build-0025
title: "How can you provide Continuous Delivery for an MCU device with a physical target, bootloader, and hardware-in-the-loop tests?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: mcuboot-design
    title: "MCUboot documentation: Bootloader design"
    url: https://docs.mcuboot.com/design.html
  - source_id: mcuboot-imgtool
    title: "MCUboot documentation: Image tool"
    url: https://docs.mcuboot.com/imgtool.html
  - source_id: zephyr-twister
    title: "Zephyr Project documentation: Test Runner (Twister)"
    url: https://docs.zephyrproject.org/latest/develop/twister/index.html
---

## Short answer

The CD pipeline must build signed artifacts, flash the device through the bootloader/debug probe, run smoke/HIL tests, and collect logs/trace. Managed test rigs are needed: power cycling, serial logs, reset control, version readback, and failure recovery. The **release gate** must verify not only the build but also the update path, rollback, and basic hardware operation.[^dou-embedded-interview]

## Detailed explanation

TODO
