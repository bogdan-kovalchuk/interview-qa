---
id: emb-boot-0007
title: "What is OTA update and what risks must be covered: power loss, signature verification, rollback, and version compatibility?"
description: "OTA updates firmware over a network without physical access and requires atomic install, signature verification, anti-rollback policy, version compatibility, and power-loss recovery."
track: embedded
section: bootloaders-and-ota
level: senior
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

**OTA** – firmware update over a network without physical access to the device. Requires atomic install, image integrity, signature verification, anti-rollback policy, version compatibility with config/protocol, and recovery after power loss. <span class="warn">Without rollback or safe boot, OTA can turn a remote device into an inaccessible brick.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
