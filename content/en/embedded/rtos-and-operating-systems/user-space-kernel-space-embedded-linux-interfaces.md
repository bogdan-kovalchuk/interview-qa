---
id: emb-fund-0012
title: "How does user space communicate with kernel space in Embedded Linux through syscalls, ioctl, procfs, or sysfs?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-syscalls
    title: "Linux manual page: syscalls(2)"
    url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - source_id: linux-man-ioctl
    title: "Linux manual page: ioctl(2)"
    url: https://man7.org/linux/man-pages/man2/ioctl.2.html
  - source_id: linux-ioctl-guide
    title: "Linux kernel: ioctl based interfaces"
    url: https://docs.kernel.org/driver-api/ioctl.html
  - source_id: linux-sysfs
    title: "Linux kernel: sysfs - The filesystem for exporting kernel objects"
    url: https://docs.kernel.org/filesystems/sysfs.html
  - source_id: linux-sysfs-rules
    title: "Linux kernel: Rules on how to access information in sysfs"
    url: https://docs.kernel.org/admin-guide/sysfs-rules.html
  - source_id: linux-man-proc
    title: "Linux manual page: proc(5)"
    url: https://man7.org/linux/man-pages/man5/proc.5.html
  - source_id: linux-debugfs
    title: "Linux kernel: DebugFS"
    url: https://docs.kernel.org/filesystems/debugfs.html
  - source_id: linux-gpio-sysfs
    title: "Linux kernel: GPIO Sysfs Interface for Userspace"
    url: https://docs.kernel.org/userspace-api/gpio/sysfs.html
  - source_id: linux-man-socket
    title: "Linux manual page: socket(2)"
    url: https://man7.org/linux/man-pages/man2/socket.2.html
---

## Short answer

User space enters the kernel via `syscall`: `read`, `write`, `open`, `mmap`, and so on. For device-specific control `ioctl` is commonly used; for simple driver attributes – `sysfs`; and `procfs` is mainly for process and kernel diagnostic info. <span class="warn">Do not put an unstable binary protocol into sysfs</span>; it expects simple text attributes.[^dou-embedded-interview]

## Detailed explanation

TODO
