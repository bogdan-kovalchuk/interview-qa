---
id: emb-boot-0005
title: "What happens during the MCU boot sequence from reset vector to main or scheduler start?"
description: "After reset the CPU loads SP and the reset handler from the vector table, startup code copies .data, clears .bss, runs constructors, enters main, and the firmware starts the scheduler."
track: embedded
section: bootloaders-and-ota
level: senior
type: concept
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

After reset the CPU takes the initial stack pointer and reset handler from the vector table. Startup code sets up the low-level runtime: clock minimally or later, copies `.data` from flash to RAM, clears `.bss`, calls constructors in C++, and enters `main`. Then the firmware initializes HAL/drivers, interrupts, RTOS objects, and starts the scheduler.[^dou-embedded-interview]

## Detailed explanation

After reset the CPU on ARM Cortex-M performs a sequence defined by the ARMv7-M architecture:

1. **Hardware reset.** The CPU loads the initial MSP from address `0x00000000` (Flash base) and the Reset Handler address from `0x00000004`. PC receives the Reset Handler address – execution begins there.

2. **Reset Handler and startup code.** The Reset Handler is typically `Reset_Handler` in the startup file (`startup.s`). It calls `SystemInit` (basic clock setup) and performs C/C++ runtime initialization: copies `.data` from Flash to RAM, fills `.bss` with zeros, invokes C++ global object constructors (`__libc_init_array`).

3. **Call to `main()`.** After runtime initialization completes, `main` is called.

4. **HAL/driver initialization.** In `main` the firmware initializes the HAL (Hardware Abstraction Layer) or drivers: clocking (PLL, clock tree, prescalers), GPIO, peripherals (UART, SPI, I2C, ADC), DMA.

5. **Interrupt configuration.** Setting up the NVIC (Nested Vectored Interrupt Controller): interrupt priorities (preemption priority, sub-priority), registering ISR handlers in the vector table, enabling required interrupts.

6. **Creating RTOS objects.** If an RTOS is used (FreeRTOS, Zephyr, ThreadX): queues, semaphores, mutexes, and task descriptors are created.

7. **Starting the scheduler.** `osKernelStart()` (CMSIS-RTOS) or its equivalent is called. The scheduler begins running tasks according to their priorities. For bare-metal systems `main` typically enters an infinite loop (`while(1)`) with event polling or interrupt waiting (`__WFI()`).

**Key point for the bootloader-to-application transition:** the bootloader writes a new value into VTOR (Vector Table Offset Register) so the CPU uses the application's vector table, not the bootloader's. Without this, application interrupts would be handled through the bootloader's handlers, causing a crash.

**`.data`/`.bss` initialization and constructors** are mandatory before `main`; otherwise global variables would contain garbage and C++ objects would not be constructed. This is a C/C++ ABI requirement.[^armv7m-arm]

## Evaluation guide

### Expected signals

- Clearly names the vector table addresses: SP from `0x00000000`, reset handler from `0x00000004`; understands why this order exists (ARMv7-M spec).
- Explains .data/.bss initialization as a C/C++ ABI requirement, not just "copy-paste from the linker script".
- Mentions VTOR and explains why the bootloader must update it before transferring control.
- Distinguishes bare-metal superloop from RTOS scheduler; names specific RTOSes (FreeRTOS, Zephyr, ThreadX).
- Mentions NVIC priority grouping (preemption vs sub-priority) and its effect on ISR latency.
- Describes __libc_init_array / constructors for C++ and why they are critical.

### Red flags

- Does not know that the first two Flash words are SP and PC, not code.
- Confuses Cortex-M boot with Cortex-A (MMU, Linux boot, U-Boot -> kernel).
- Does not mention .bss or thinks RAM is initialized by hardware.
- Does not understand the difference between MSP and PSP (Main vs Process Stack Pointer).
- Cannot explain why VTOR is needed for the bootloader-to-application transition.

### Level-up follow-up

- How does the boot sequence change with a secure bootloader (TrustZone, SAU)?
- How does clock initialization (PLL lock time) affect boot time, and how do you minimize it?
- How do C++ exceptions and RTTI affect the startup code and vector table (exception tables)?

## Sources

<!-- generated from frontmatter -->
