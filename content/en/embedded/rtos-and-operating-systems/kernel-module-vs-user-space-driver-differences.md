---
id: emb-linemb-0001
title: "What is the difference between a kernel module and a user-space driver in embedded Linux?"
track: embedded
section: rtos-and-operating-systems
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
  - source_id: linux-kernel-hacking-guide
    title: "The Linux Kernel: Unreliable Guide To Hacking The Linux Kernel"
    url: https://docs.kernel.org/kernel-hacking/hacking.html
  - source_id: linux-spidev
    title: "The Linux Kernel: SPI userspace API"
    url: https://docs.kernel.org/spi/spidev.html
  - source_id: linux-i2c-dev
    title: "The Linux Kernel: Implementing I2C device drivers in userspace"
    url: https://docs.kernel.org/i2c/dev-interface.html
  - source_id: linux-gpio-chardev
    title: "The Linux Kernel: GPIO Character Device Userspace API"
    url: https://docs.kernel.org/userspace-api/gpio/chardev.html
  - source_id: linux-stable-api-nonsense
    title: "The Linux Kernel Driver Interface (stable API nonsense)"
    url: https://docs.kernel.org/process/stable-api-nonsense.html
  - source_id: linux-tuntap
    title: "The Linux Kernel: Universal TUN/TAP device driver"
    url: https://docs.kernel.org/networking/tuntap.html
  - source_id: linux-uinput
    title: "The Linux Kernel: uinput module"
    url: https://docs.kernel.org/input/uinput.html
---

## Short answer

**A kernel driver, whether built in or loaded as a module, executes in kernel context and can use kernel facilities for interrupts, DMA, power management, and device subsystems; a defect can corrupt or crash the system.**[^linux-kernel-docs] A user-space driver keeps most device logic in an isolated process but still needs a kernel interface to expose the device. UIO suits simple memory-mapped devices outside standard subsystems, while VFIO supports protected direct access, including DMA, when the platform provides the required isolation.[^linux-uio-howto][^linux-vfio] Choose from integration, latency, DMA, security, recovery, and maintenance requirements.

## Detailed explanation

TODO
