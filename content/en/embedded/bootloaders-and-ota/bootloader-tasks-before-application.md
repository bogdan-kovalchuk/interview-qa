---
id: emb-boot-0004
title: "What is an MCU bootloader, and what does it do before application firmware starts?"
description: "An MCU bootloader starts after reset, verifies or updates an image, selects a slot, and transfers control to application firmware."
track: embedded
section: bootloaders-and-ota
level: middle
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

A bootloader is a small firmware that starts first after reset. It can verify an image signature/CRC, select a slot, update firmware over UART/USB/CAN/BLE, configure the vector table, and transfer control to the application. In safety/security systems it also manages rollback, anti-bricking, and chain of trust.[^dou-embedded-interview]

## Detailed explanation

An MCU bootloader is a firmware module located in a protected Flash region (boot sector) that performs duties between reset and the launch of the main application firmware.

**Bootloader operation sequence:**

1. **Hardware reset.** The CPU loads SP and the reset handler from the vector table. The bootloader's reset handler receives control.

2. **Minimal initialization.** Clock (typically the internal RC oscillator at low frequency), GPIO for indication (LED), basic peripheral for the service channel (UART/USB).

3. **Application image verification.** Computing a CRC-32 or SHA-256 hash of the image in the primary slot. In secured systems – cryptographic signature verification (RSA-2048, ECDSA-P256). MCUboot uses a TLV (Type-Length-Value) structure to store signatures, hashes, and image metadata.[^mcuboot-design]

4. **Boot mode determination.** The bootloader checks triggers for entering service mode: a button, a flag in a register (RTC backup register), a command over the service interface. If a trigger is active, the bootloader enters update mode.

5. **Firmware update (if needed).** A new image is received over UART (XMODEM/YMODEM), USB (DFU, CDC), CAN, BLE, etc., and written to the secondary slot. Under the swap strategy, primary and secondary are exchanged using a scratch area; under overwrite, primary is replaced directly; under direct-XIP, the new image runs from the secondary slot without copying.

6. **Preparing to launch the application.** Writing the application vector table address into VTOR (Vector Table Offset Register). Resetting peripherals to a safe state. Setting MSP to the value from the application vector table. Jumping to the application entry point.

**Chain of trust.** In safety/security systems each boot stage is verified: the ROM bootloader (silicon-built-in) checks the bootloader's signature, and the bootloader checks the application's signature. This prevents execution of modified code.

**Anti-rollback.** MCUboot supports a security counter in the image TLV; the bootloader rejects an image with a counter lower than the stored value, preventing rollback to a vulnerable firmware version.

## Evaluation guide

### Expected signals

- Clearly describes the 6-step sequence: reset, minimal initialization, image verification, boot mode determination, firmware update (if needed), application launch.
- Mentions firmware integrity verification: CRC-32, SHA-256, cryptographic signature (RSA-2048, ECDSA-P256), MCUboot TLV structure.
- Distinguishes update strategies: swap (with scratch area), overwrite (direct primary replacement), direct-XIP (execution from secondary slot).
- Mentions VTOR for transferring control to the application and resetting peripherals to a safe state.
- Understands chain of trust: the ROM bootloader checks the bootloader's signature, and the bootloader checks the application's signature.
- Mentions anti-rollback via the security counter in the image TLV.

### Red flags

- Does not know about primary/secondary slots or the difference between swap, overwrite, and direct-XIP.
- Confuses the bootloader with a monitor or debug tool.
- Does not mention VTOR when describing the bootloader-to-application transition.
- Thinks the bootloader and application run simultaneously.
- Does not mention image verification (CRC, signature) as a mandatory step.

### Level-up follow-up

- How does the bootloader recover from an interrupted update (power loss during swap)?
- How do you implement chain of trust from the ROM bootloader to the application?
- Compare direct-XIP and swap: trade-offs between complexity, reliability, and update time.

## Sources

<!-- generated from frontmatter -->
