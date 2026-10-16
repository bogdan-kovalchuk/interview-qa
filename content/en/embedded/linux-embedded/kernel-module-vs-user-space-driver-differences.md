---
id: emb-linemb-0001
title: "What is the difference between a kernel module and a user-space driver in embedded Linux?"
track: embedded
section: linux-embedded
sources:
  - source_id: linux-kernel-docs
    title: "The Linux Kernel Documentation: Driver Implementation"
    url: https://www.kernel.org/doc/html/latest/driver-api/index.html
  - source_id: linux-uio-howto
    title: "The Userspace I/O HOWTO"
    url: https://www.kernel.org/doc/html/latest/driver-api/uio-howto.html
  - source_id: linux-vfio
    title: "VFIO - Virtual Function I/O"
    url: https://docs.kernel.org/driver-api/vfio.html
---

## Short answer

**A kernel driver, whether built in or loaded as a module, executes in kernel context and can use kernel facilities for interrupts, DMA, power management, and device subsystems; a defect can corrupt or crash the system.**[^linux-kernel-docs] A user-space driver keeps most device logic in an isolated process but still needs a kernel interface to expose the device. UIO suits simple memory-mapped devices outside standard subsystems, while VFIO supports protected direct access, including DMA, when the platform provides the required isolation.[^linux-uio-howto][^linux-vfio] Choose from integration, latency, DMA, security, recovery, and maintenance requirements.

## Detailed explanation

TODO
