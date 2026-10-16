---
id: emb-fund-0027
title: "Linux-контролер не може запускати нові процеси, хоча df показує вільне місце. Як перевірити inodes, tmpfs, file descriptors і logs?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Перевір `df -i` для inodes, `df -h` для `/tmp`/`/run` tmpfs, `ulimit -n` і `lsof` для file descriptors. Подивись `dmesg`, `journalctl`, OOM messages, read-only remount і errors filesystem. <span class="warn">Вільні bytes на rootfs не допоможуть, якщо закінчились inodes, PID limit, fd limit або tmpfs.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
