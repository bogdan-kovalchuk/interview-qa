---
id: emb-fund-0027
title: "Linux-контролер не може запускати нові процеси, хоча df показує вільне місце. Як перевірити inodes, tmpfs, file descriptors і logs?"
description: "Перевір df -i для inodes, df -h для /tmp/run tmpfs, ulimit -n і lsof для file descriptors. Подивись dmesg, journalctl, OOM messages, read-only remount і errors filesystem."
track: embedded
section: fundamentals
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Перевір <code>df -i</code> для inodes, <code>df -h</code> для <code>/tmp</code>/<code>/run</code> tmpfs, <code>ulimit -n</code> і <code>lsof</code> для file descriptors.<br>Подивись <code>dmesg</code>, <code>journalctl</code>, OOM messages, read-only remount і errors filesystem.<br><span class="warn">Вільні bytes на rootfs не допоможуть, якщо закінчились inodes, PID limit, fd limit або tmpfs.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
