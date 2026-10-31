---
id: emb-fund-0023
title: "How should you approach writing a simple Linux kernel driver for a character device or platform device?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-platform-devices
    title: "The Linux Kernel: Platform Devices and Drivers"
    url: https://docs.kernel.org/driver-api/driver-model/platform.html
  - source_id: linux-driver-model-driver
    title: "The Linux Kernel: Device Drivers (driver model)"
    url: https://docs.kernel.org/driver-api/driver-model/driver.html
  - source_id: linux-devres
    title: "The Linux Kernel: Devres - Managed Device Resource"
    url: https://docs.kernel.org/driver-api/driver-model/devres.html
  - source_id: linux-driver-infrastructure
    title: "The Linux Kernel: Device drivers infrastructure"
    url: https://docs.kernel.org/driver-api/infrastructure.html
  - source_id: linux-kernel-api-char-devices
    title: "The Linux Kernel API: Char devices"
    url: https://docs.kernel.org/core-api/kernel-api.html
  - source_id: linux-misc-devices
    title: "The Linux Kernel: Miscellaneous Devices"
    url: https://docs.kernel.org/driver-api/misc_devices.html
  - source_id: linux-kernel-hacking-guide
    title: "The Linux Kernel: Unreliable Guide To Hacking The Linux Kernel"
    url: https://docs.kernel.org/kernel-hacking/hacking.html
  - source_id: linux-fs-api-summary
    title: "Linux Filesystems API summary (simple_read_from_buffer)"
    url: https://docs.kernel.org/filesystems/api-summary.html
---

## Short answer

For a character device, define file operations: `open`, `read`, `write`, `ioctl`, plus registration and lifetime cleanup. For a platform driver, implement `probe`/`remove`, take resources from devicetree, map MMIO, register IRQ, and expose the interface. <span class="warn">In a kernel driver you cannot think like in user space: different allocation rules, locking, sleep context, and error handling.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
