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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
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

TODO

## Sources

<!-- generated from frontmatter -->
