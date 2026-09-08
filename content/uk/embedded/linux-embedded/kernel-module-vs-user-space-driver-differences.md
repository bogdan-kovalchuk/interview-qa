---
id: emb-linemb-0001
title: "У чому різниця між kernel-модулем та user-space драйвером в embedded Linux?"
description: "Kernel-драйвер інтегрується з підсистемами ядра та привілейованими апаратними механізмами; user-space драйвер лишає основну логіку пристрою в ізольованому процесі за інтерфейсом на кшталт UIO або VFIO."
track: embedded
section: linux-embedded
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: linux-kernel-docs
    title: "The Linux Kernel Documentation: Driver Implementation"
    url: https://www.kernel.org/doc/html/latest/driver-api/index.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація Linux kernel про розробку драйверів."
  - source_id: linux-uio-howto
    title: "The Userspace I/O HOWTO"
    url: https://www.kernel.org/doc/html/latest/driver-api/uio-howto.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація Linux про придатність UIO та надання пристрою user space."
  - source_id: linux-vfio
    title: "VFIO - Virtual Function I/O"
    url: https://docs.kernel.org/driver-api/vfio.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація Linux про захищений прямий доступ до пристроїв із user space."
---

## Short answer

**Kernel-драйвер, вбудований у ядро або завантажений як модуль, виконується в kernel context і може використовувати механізми ядра для переривань, DMA, power management та стандартних підсистем пристроїв; його дефект здатен пошкодити або впустити систему.**[^linux-kernel-docs] User-space драйвер лишає основну логіку в ізольованому процесі, але потребує kernel-інтерфейсу для доступу до пристрою. UIO придатний для простих memory-mapped пристроїв поза стандартними підсистемами, а VFIO підтримує захищений прямий доступ, зокрема DMA, якщо платформа забезпечує потрібну ізоляцію.[^linux-uio-howto][^linux-vfio] Вибір залежить від інтеграції, latency, DMA, security, відновлення та супроводу.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
