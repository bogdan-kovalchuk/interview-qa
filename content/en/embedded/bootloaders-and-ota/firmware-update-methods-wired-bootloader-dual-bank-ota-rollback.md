---
id: emb-boot-0006
title: "What firmware update methods exist: wired flashing, bootloader, dual-bank, A/B image, OTA, and rollback?"
description: "Wired flashing suits factory use, a bootloader accepts images over serial or network, dual-bank or A/B preserves the working image, and rollback restores the last valid version after failure."
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
---

## Short answer

**Wired flashing** over SWD/JTAG/UART is simple for factory/service but not for field updates. A bootloader can accept an image over UART/USB/CAN/network; dual-bank or A/B allows writing a new image without erasing the working one. Rollback is needed to return to the previous valid version after a failed boot or health check.[^dou-embedded-interview]

## Detailed explanation

Firmware update on microcontrollers uses several approaches, each with its own trade-off between complexity, reliability, and hardware requirements.

**Wired flashing** over SWD/JTAG/UART provides direct memory access through the debug interface. It is the simplest and most reliable method for factory programming and service, but it requires physical contact with the device and is not suitable for field updates.

**Bootloader-based update** is a special program on the device that runs before the main firmware and can accept a new image over UART, USB, CAN, or network. The bootloader typically checks image integrity (checksum or signature) before writing to flash. Drawback: if power loss occurs during the flash write, and the old image has already been erased, the device becomes a brick.

**Dual-bank (dual-image) scheme** solves this problem. Flash memory is divided into two equal partitions: one holds the active firmware, the other is for the update. The bootloader writes the new image to the inactive bank while the current firmware keeps running. After the write, the bootloader verifies the signature and integrity of the new image and only then switches the active bank on the next boot. If verification fails, the old image remains working.

**A/B scheme** (system update) is a dual-bank variant where the update application runs from RAM or a separate recovery partition, not from the main flash. This allows using the entire main flash for the application image (no 50/50 split), but requires enough RAM to run the update application.

**Rollback** is a critical mechanism for production OTA. The bootloader runs a health check after each boot (for example, verifying that the main process starts, or that the watchdog responds). If the new firmware fails the health check within N boot attempts, the bootloader automatically switches back to the previous valid image. The rollback mechanism, together with signature verification and an anti-rollback counter (to prevent downgrade attacks), is the foundation of a secure update system, and dual-bank/A/B schemes are designed specifically to support it.[^mcuboot-design]

## Evaluation guide

### Expected signals

- Distinguishes methods by physical access requirement and field update capability
- Understands that dual-bank and A/B exist to prevent bricking during update
- Mentions rollback and signature verification as mandatory for production OTA
- Understands the trade-off between complexity and reliability

### Red flags

- Confuses bootloader update with wired flashing
- Does not mention rollback as a mandatory mechanism
- Believes OTA does not need signature verification
- Cannot distinguish dual-bank from A/B schemes

### Level-up follow-up

- How to implement anti-rollback policy, and why is it important?
- How to ensure atomic update on a device with limited flash?

## Sources

<!-- generated from frontmatter -->
