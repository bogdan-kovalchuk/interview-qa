---
id: emb-fund-0004
title: "What is a file descriptor?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: posix-2024-definitions
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 3. Definitions"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html
  - source_id: linux-man-open
    title: "Linux manual page: open(2)"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-man-dup
    title: "Linux manual page: dup(2)"
    url: https://man7.org/linux/man-pages/man2/dup.2.html
  - source_id: linux-man-close
    title: "Linux manual page: close(2)"
    url: https://man7.org/linux/man-pages/man2/close.2.html
  - source_id: linux-man-getrlimit
    title: "Linux manual page: getrlimit(2)"
    url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
  - source_id: linux-man-proc-pid-fd
    title: "Linux manual page: proc_pid_fd(5)"
    url: https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
  - source_id: linux-adding-syscalls
    title: "Linux kernel documentation: Adding a New System Call"
    url: https://docs.kernel.org/process/adding-syscalls.html
  - source_id: linux-gpio-chardev
    title: "Linux kernel documentation: GPIO Character Device Userspace API"
    url: https://docs.kernel.org/userspace-api/gpio/chardev.html
  - source_id: linux-gpio-v2-get-line-ioctl
    title: "Linux kernel documentation: GPIO_V2_GET_LINE_IOCTL"
    url: https://docs.kernel.org/userspace-api/gpio/gpio-v2-get-line-ioctl.html
---

## Short answer

**File descriptor (fd)** is a non-negative integer that identifies an open resource within a process: file, socket, pipe, or device.[^dou-embedded-interview] The kernel maintains an fd table for each process.

Standard ones: `0` = stdin, `1` = stdout, `2` = stderr.

Cycle: `fd = open("file", O_RDONLY);`, then `read(fd, buf, n);`, then `close(fd);`. In Linux "everything is a file" – through an fd you can work with devices (`/dev/gpiochip0`), sysfs, and even timers (`timerfd`).

## Detailed explanation

TODO
