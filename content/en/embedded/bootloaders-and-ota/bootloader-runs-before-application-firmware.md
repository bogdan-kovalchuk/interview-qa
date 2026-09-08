---
id: emb-boot-0002
title: "What is a bootloader?"
description: "A bootloader is a small program that starts first after reset, prepares the system, and decides which firmware image to run next."
track: embedded
section: bootloaders-and-ota
level: junior
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
---

## Short answer

**Bootloader** is a small program that runs first after reset or before the main firmware.[^dou-embedded-interview] It prepares the system and decides what to run next.

Typical functions: minimal hardware initialization, firmware integrity check, image selection, firmware update, launching the main application. A bootloader can support flashing over UART, USB, CAN, Ethernet, or OTA.

In MCUs the bootloader usually resides in a separate Flash region and transfers control to the application via the vector table / reset handler.

## Detailed explanation

The bootloader acts as the intermediary between power-on and application startup. After reset, the MCU hardware loads the initial stack pointer (SP) and reset handler address from the vector table, then jumps to the reset handler – the bootloader's entry point.

The bootloader performs minimal initialization: sets up essential clocks and GPIO. It then verifies the application image integrity – computing a checksum (CRC-32, SHA-256) or verifying a cryptographic signature (RSA-2048, ECDSA-P256 in MCUboot). If verification fails, the bootloader enters a failsafe mode: it waits for a new firmware image over a backup channel (UART, USB).

If the image is valid, the bootloader checks whether to enter service mode. Triggers include: a button press, a flag in an RTC register, a command from another MCU. If no trigger is present, it transfers control to the application.

If new firmware has been received (over UART, USB, CAN, BLE, etc.), the bootloader writes it to the secondary slot in flash. Under the swap strategy it swaps the primary and secondary slots; under overwrite it replaces the primary image. On the next boot the bootloader verifies the new image and, if valid, runs it.[^mcuboot-design]

Before transferring control, the bootloader configures the application's vector table (writes the application vector table address into VTOR – the Vector Table Offset Register on ARM Cortex-M) and resets peripherals to a safe state.

MCUboot is the canonical example: two image slots, support for overwrite / swap / direct-XIP strategies, and cryptographic verification. Simpler bootloaders may lack signature checks or swap logic, but the core duties (image verification, slot selection, control transfer) remain the same.

## Sources

<!-- generated from frontmatter -->
