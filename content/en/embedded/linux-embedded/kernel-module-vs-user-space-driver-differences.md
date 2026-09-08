---
id: emb-linemb-0001
title: "What is the difference between a kernel module and a user-space driver in embedded Linux?"
description: "A kernel driver integrates with kernel subsystems and privileged hardware services; a user-space driver keeps most device logic in an isolated process behind a kernel interface such as UIO or VFIO."
track: embedded
section: linux-embedded
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: linux-kernel-docs
    title: "The Linux Kernel Documentation: Driver Implementation"
    url: https://www.kernel.org/doc/html/latest/driver-api/index.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official Linux kernel documentation on driver development."
  - source_id: linux-uio-howto
    title: "The Userspace I/O HOWTO"
    url: https://www.kernel.org/doc/html/latest/driver-api/uio-howto.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official Linux documentation on when UIO is suitable and how it exposes a device to user space."
  - source_id: linux-vfio
    title: "VFIO - Virtual Function I/O"
    url: https://docs.kernel.org/driver-api/vfio.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official Linux documentation on protected direct device access from user space."
---

## Short answer

**A kernel driver, whether built in or loaded as a module, executes in kernel context and can use kernel facilities for interrupts, DMA, power management, and device subsystems; a defect can corrupt or crash the system.**[^linux-kernel-docs] A user-space driver keeps most device logic in an isolated process but still needs a kernel interface to expose the device. UIO suits simple memory-mapped devices outside standard subsystems, while VFIO supports protected direct access, including DMA, when the platform provides the required isolation.[^linux-uio-howto][^linux-vfio] Choose from integration, latency, DMA, security, recovery, and maintenance requirements.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
