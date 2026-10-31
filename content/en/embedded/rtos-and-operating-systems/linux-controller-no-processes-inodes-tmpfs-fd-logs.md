---
id: emb-fund-0027
title: "Linux controller cannot start new processes even though df shows free space. How to check inodes, tmpfs, file descriptors, and logs?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-fork
    title: "fork(2) - Linux manual page"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-man-getrlimit
    title: "getrlimit(2) - Linux manual page"
    url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
  - source_id: linux-man-proc-sys-kernel
    title: "proc_sys_kernel(5) - Linux manual page"
    url: https://man7.org/linux/man-pages/man5/proc_sys_kernel.5.html
  - source_id: linux-man-proc-sys-fs
    title: "proc_sys_fs(5) - Linux manual page"
    url: https://man7.org/linux/man-pages/man5/proc_sys_fs.5.html
  - source_id: linux-man-open
    title: "open(2) - Linux manual page"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-man-df
    title: "df(1) - Linux manual page"
    url: https://man7.org/linux/man-pages/man1/df.1.html
  - source_id: linux-tmpfs
    title: "The Linux Kernel: Tmpfs"
    url: https://docs.kernel.org/filesystems/tmpfs.html
  - source_id: linux-man-unlink
    title: "unlink(2) - Linux manual page"
    url: https://man7.org/linux/man-pages/man2/unlink.2.html
  - source_id: linux-man-proc-pid-fd
    title: "proc_pid_fd(5) - Linux manual page"
    url: https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
  - source_id: linux-man-wait
    title: "wait(2) - Linux manual page"
    url: https://man7.org/linux/man-pages/man2/wait.2.html
  - source_id: linux-cgroup-v2
    title: "The Linux Kernel: Control Group v2"
    url: https://docs.kernel.org/admin-guide/cgroup-v2.html
  - source_id: linux-ext4-admin
    title: "The Linux Kernel: ext4 General Information"
    url: https://docs.kernel.org/admin-guide/ext4.html
  - source_id: linux-man-mke2fs
    title: "mke2fs(8) - Linux manual page"
    url: https://man7.org/linux/man-pages/man8/mke2fs.8.html
---

## Short answer

Check `df -i` for inodes, `df -h` for `/tmp`/`/run` tmpfs, `ulimit -n` and `lsof` for file descriptors. Look at `dmesg`, `journalctl`, OOM messages, read-only remount and filesystem errors. <span class="warn">Free bytes on rootfs won't help if inodes, PID limit, fd limit or tmpfs are exhausted.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
