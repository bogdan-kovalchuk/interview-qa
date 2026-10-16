---
id: emb-fund-0027
title: "Linux controller cannot start new processes even though df shows free space. How to check inodes, tmpfs, file descriptors, and logs?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Check `df -i` for inodes, `df -h` for `/tmp`/`/run` tmpfs, `ulimit -n` and `lsof` for file descriptors. Look at `dmesg`, `journalctl`, OOM messages, read-only remount and filesystem errors. <span class="warn">Free bytes on rootfs won't help if inodes, PID limit, fd limit or tmpfs are exhausted.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
