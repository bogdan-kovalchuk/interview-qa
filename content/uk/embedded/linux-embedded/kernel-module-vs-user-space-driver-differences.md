---
id: emb-linemb-0001
title: "У чому різниця між kernel-модулем та user-space драйвером в embedded Linux?"
track: embedded
section: linux-embedded
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
---

## Short answer

**Kernel-драйвер, вбудований у ядро або завантажений як модуль, виконується в kernel context і може використовувати механізми ядра для переривань, DMA, power management та стандартних підсистем пристроїв; його дефект здатен пошкодити або впустити систему.**[^linux-kernel-docs] User-space драйвер лишає основну логіку в ізольованому процесі, але потребує kernel-інтерфейсу для доступу до пристрою. UIO придатний для простих memory-mapped пристроїв поза стандартними підсистемами, а VFIO підтримує захищений прямий доступ, зокрема DMA, якщо платформа забезпечує потрібну ізоляцію.[^linux-uio-howto][^linux-vfio] Вибір залежить від інтеграції, latency, DMA, security, відновлення та супроводу.

## Detailed explanation

TODO
