---
id: emb-fund-0012
title: "Як user space спілкується з kernel space в Embedded Linux через syscalls, ioctl, procfs або sysfs?"
description: "User space входить у kernel через <code>syscall</code>: <code>read</code>, <code>write</code>, <code>open</code>, <code>mmap</code> тощо."
track: embedded
section: fundamentals
level: middle
type: concept
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

User space входить у kernel через <code>syscall</code>: <code>read</code>, <code>write</code>, <code>open</code>, <code>mmap</code> тощо. Для device-specific control часто використовують <code>ioctl</code>, для простих атрибутів driver-а – <code>sysfs</code>, а <code>procfs</code> переважно для process/kernel diagnostic info. <span class="warn">Не варто робити нестабільний binary protocol у sysfs</span>; там очікуються прості текстові атрибути.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

