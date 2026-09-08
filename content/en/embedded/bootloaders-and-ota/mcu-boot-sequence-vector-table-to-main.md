---
id: emb-boot-0003
title: "How does program loading work in a microcontroller?"
description: "After reset the Cortex-M hardware reads the vector table, loads SP and the reset handler, startup code copies .data and clears .bss, clocks are initialized, and main() is called."
track: embedded
section: bootloaders-and-ota
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Authoritative section-level reference for bootloaders and ota concepts; details of specific devices and toolchains can differ."
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
    accessed: 2026-09-08
    kind: official
    version: "E"
    applicability: "ARMv7-M architecture; reset behavior, vector table, and exception model."
---

## Short answer

After power-on or reset (ARM Cortex-M):[^dou-embedded-interview]

- Hardware reads the **Vector Table** from address `0x00000000` (Flash)
- Loads the initial SP value from the word at `0x00000000`
- Loads the Reset Handler address into PC from `0x00000004`
- **Startup code** (crt0 / startup.s) copies the `.data` section from Flash to RAM, fills `.bss` with zeros
- Initializes clocking (PLL, clock tree)
- Calls `main()`.

The program is stored in **Flash (non-volatile)**. Execution can happen directly from Flash (XIP – execute-in-place) or, for performance-critical code, the code is copied to RAM.

## Detailed explanation

On ARM Cortex-M, after power-on or hardware reset, the processor performs a sequence defined by the ARMv7-M architecture:

1. **Vector table read.** The hardware reads the first two 32-bit words from the Flash base address (typically `0x00000000`, or `0x08000000` with aliasing). The word at `0x00000000` is the initial Main Stack Pointer (MSP) value; the word at `0x00000004` is the Reset Handler address.

2. **Reset Handler execution.** This is the first instruction the CPU executes. It is usually the `Reset_Handler` function in the startup file (`startup_stm32f4xx.s`, `startup_nrf52.s`, etc.).

3. **Startup code (crt0).** The Reset Handler calls the system initialization function (`SystemInit`), which sets up basic clocking. It then copies the `.data` section (initialized global variables) from Flash to RAM at addresses defined by the linker script. It fills the `.bss` section (uninitialized global variables) with zeros. For C++, it invokes global object constructors (`__libc_init_array`).

4. **Call to `main()`.** After the startup code completes, control passes to `main()`.

The program is stored in Flash (non-volatile memory). Execution can happen directly from Flash (XIP – execute-in-place) or, for performance-critical code and low-latency ISRs, the code is copied to RAM.

The vector table contains up to 240 exception/interrupt vectors (for ARMv7-M); besides SP and Reset Handler, it includes addresses for NMI_Handler, HardFault_Handler, MemManage_Handler, etc.[^armv7m-arm]

## Sources

<!-- generated from frontmatter -->
