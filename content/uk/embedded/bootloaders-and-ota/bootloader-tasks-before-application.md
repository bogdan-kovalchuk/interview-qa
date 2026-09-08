---
id: emb-boot-0004
title: "Що таке bootloader у MCU і які задачі він виконує перед запуском application firmware?"
description: "Bootloader стартує після reset, перевіряє або оновлює image, вибирає slot і передає керування application firmware."
track: embedded
section: bootloaders-and-ota
level: middle
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

Bootloader – маленький firmware, який стартує першим після reset. Він може перевірити image signature/CRC, вибрати slot, оновити firmware через UART/USB/CAN/BLE, налаштувати vector table і передати керування application. У safety/security системах він також контролює rollback, anti-bricking і chain of trust.[^dou-embedded-interview]

## Detailed explanation

Bootloader MCU – це firmware-модуль, розташований у захищеній області Flash (boot sector), який виконує обов'язки між reset та запуском основної application firmware.

**Послідовність роботи bootloader:**

1. **Апаратний reset.** CPU завантажує SP і reset handler з vector table. Reset handler bootloader'а отримує керування.

2. **Мінімальна ініціалізація.** Clock (зазвичай внутрішній RC-осцилятор на низькій частоті), GPIO для індикації (LED), базова периферія для сервісного каналу (UART/USB).

3. **Перевірка образу application.** Обчислення CRC-32 або SHA-256 хешу образу у primary slot. У захищених системах – криптографічна верифікація підпису (RSA-2048, ECDSA-P256). MCUboot використовує TLV-структуру (Type-Length-Value) для зберігання підписів, хешів та метаданих образу.[^mcuboot-design]

4. **Визначення режиму завантаження.** Bootloader перевіряє тригери для входу у service mode: кнопка, прапорець у регістрі (RTC backup register), команда через сервісний інтерфейс. Якщо тригер активний – bootloader переходить у режим оновлення.

5. **Оновлення firmware (якщо потрібно).** Новий образ приймається через UART (XMODEM/YMODEM), USB (DFU, CDC), CAN, BLE тощо і записується у secondary slot. За стратегії swap – primary і secondary міняються місцями з використанням scratch-області; за стратегією overwrite – primary перезаписується напряму; за стратегією direct-XIP – новий образ виконується безпосередньо з secondary slot.

6. **Підготовка до запуску application.** Запис адреси vector table application у VTOR (Vector Table Offset Register). Скидання периферії у безпечний стан. Встановлення MSP у значення з vector table application. Перехід на entry point application.

**Chain of trust.** У safety/security системах кожен етап завантаження верифікується: ROM bootloader (вбудований у кремній) перевіряє signature bootloader'а, bootloader перевіряє signature application. Це запобігає виконанню модифікованого коду.

**Anti-rollback.** MCUboot підтримує security counter у TLV образу; bootloader відхиляє образ із counter меншим за збережений, запобігаючи відкату на вразливу версію firmware.

## Evaluation guide

### Expected signals

- Чітко описує послідовність із 6 кроків: reset, мінімальна ініціалізація, верифікація образу, визначення режиму, оновлення (якщо потрібно), запуск application.
- Згадує верифікацію цілісності firmware: CRC-32, SHA-256, криптографічний підпис (RSA-2048, ECDSA-P256), TLV-структуру MCUboot.
- Розрізняє стратегії оновлення: swap (з scratch-областю), overwrite (прямий перезапис primary), direct-XIP (виконання з secondary slot).
- Згадує VTOR для передачі керування application та скидання периферії у безпечний стан.
- Розуміє chain of trust: ROM bootloader перевіряє signature bootloader'а, bootloader перевіряє signature application.
- Згадує anti-rollback через security counter у TLV образу.

### Red flags

- Не знає про primary/secondary slot або про різницю між swap, overwrite і direct-XIP.
- Плутає bootloader з monitor або debug-інструментом.
- Не згадує VTOR при описі переходу від bootloader до application.
- Вважає, що bootloader і application виконуються одночасно.
- Не згадує верифікацію образу (CRC, підпис) як обов'язковий етап.

### Level-up follow-up

- Як bootloader відновлюється після перерваного оновлення (power loss під час swap)?
- Як реалізувати chain of trust від ROM bootloader до application?
- Порівняти direct-XIP і swap: trade-offs між складністю, надійністю та часом оновлення.

## Sources

<!-- generated from frontmatter -->
