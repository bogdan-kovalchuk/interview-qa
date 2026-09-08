---
id: emb-boot-0002
title: "Що таке bootloader?"
description: "Bootloader – невелика програма, що запускається першою після reset, перевіряє й оновлює firmware та передає керування application."
track: embedded
section: bootloaders-and-ota
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу bootloaders-and-ota; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Bootloader** – невелика програма, яка запускається першою після reset або перед основною firmware.[^dou-embedded-interview] Вона готує систему і вирішує, що запускати далі.

Типові функції: мінімальна ініціалізація hardware, перевірка цілісності firmware, вибір образу, оновлення firmware, запуск main application. Bootloader може підтримувати flashing через UART, USB, CAN, Ethernet або OTA.

У MCU bootloader часто лежить в окремій Flash-області й передає керування application через vector table/reset handler.

## Detailed explanation

Bootloader виконує роль проміжного шару між увімкненням пристрою та запуском основної програми. Після reset апаратний блок MCU завантажує з vector table початковий stack pointer (SP) та адресу reset handler, потім переходить на reset handler – точку входу bootloader.

Bootloader виконує мінімальну ініціалізацію: налаштовує необхідні clock та GPIO. Далі перевіряє цілісність образу application – обчислює контрольну суму (CRC-32, SHA-256) або верифікує криптографічний підпис (RSA-2048, ECDSA-P256 у MCUboot). Якщо валідація не пройдена, bootloader переходить у режим відновлення (failsafe): очікує новий firmware через резервний канал (UART, USB).

Якщо образ валідний, bootloader перевіряє, чи потрібно запускати service mode. Тригери: натискання кнопки, прапорець у RTC-регістрі, команда від іншого MCU. Якщо тригера немає – передає керування application.

Якщо новий firmware отримано (через UART, USB, CAN, BLE тощо), bootloader записує його у secondary slot flash-пам'яті. За стратегії swap – міняє місцями primary і secondary слоти; за стратегією overwrite – перезаписує primary. При наступному завантаженні bootloader перевіряє новий образ і, якщо він валідний, запускає його.[^mcuboot-design]

Перед передачею керування bootloader налаштовує векторну таблицю application (записує адресу vector table application у VTOR – Vector Table Offset Register на ARM Cortex-M) та скидає периферію у безпечний стан.

MCUboot – канонічний приклад: два слоти образів, підтримка стратегій overwrite / swap / direct-XIP, криптографічна верифікація. Простіші bootloader можуть не мати підпису чи swap-логіки, але базові обов'язки (перевірка образу, вибір слота, передача керування) залишаються незмінними.

## Sources

<!-- generated from frontmatter -->
