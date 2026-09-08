---
id: emb-boot-0006
title: "Які способи firmware update існують: wired flashing, bootloader, dual-bank, A/B image, OTA і rollback?"
description: "Wired flashing через SWD/JTAG/UART простий для factory/service, bootloader приймає image з UART/USB/CAN/network, dual-bank або A/B дозволяють записати новий image без стирання робочого, rollback повертає на попередню valid версію."
track: embedded
section: bootloaders-and-ota
level: senior
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

**Wired flashing** через SWD/JTAG/UART простий для factory/service, але не для field updates. Bootloader може приймати image з UART/USB/CAN/network; dual-bank або A/B дозволяють записати новий image без стирання робочого. Rollback потрібен, щоб повернутися на попередню valid версію після failed boot або health check.[^dou-embedded-interview]

## Detailed explanation

Оновлення firmware на мікроконтролерах використовує кілька підходів, кожен з власним компромісом між складністю, надійністю та вимогами до hardware.

**Wired flashing** через SWD/JTAG/UART надає прямий доступ до пам'яті через debug інтерфейс. Це найпростіший і найнадійніший метод для factory programming та service, але він вимагає фізичного контакту з пристроєм і не підходить для field updates.

**Bootloader-based update** – спеціальна програма на пристрої, яка запускається перед основним firmware і може приймати новий image з UART, USB, CAN або мережі. Bootloader зазвичай перевіряє integrity image (checksum або signature) перед записом у flash. Недолік: якщо power loss станеться під час запису у flash, і старий image вже стерто, пристрій стає brick.

**Dual-bank (dual-image) scheme** вирішує цю проблему. Flash пам'ять розділена на дві рівні частини: одна містить active firmware, інша призначена для оновлення. Bootloader записує новий image в неактивний банк, поки поточний firmware продовжує працювати. Після запису bootloader перевіряє signature і integrity нового image, і лише тоді перемикає active bank на наступному boot. Якщо verification не пройдена, старий image залишається working.

**A/B scheme** (system update) – варіант dual-bank, де update application запускається з RAM або окремого recovery розділу, а не з основного flash. Це дозволяє використовувати весь основний flash для application image (немає 50/50 поділу), але потребує достатньо RAM для виконання update application.

**Rollback** – критичний механізм для production OTA. Bootloader виконує health check після кожного boot (наприклад, перевірка чи основний процес запускається, чи відповідає watchdog). Якщо новий firmware не проходить health check протягом N boot attempts, bootloader автоматично перемикається на попередній valid image. Rollback mechanism, разом із signature verification та anti-rollback counter (для запобігання downgrade attacks), є фундаментом безпечної системи оновлення, і dual-bank/A/B схеми проектуються саме для його підтримки.[^mcuboot-design]

## Evaluation guide

### Expected signals

- Розрізняє методи за потребою у фізичному доступі та здатністю до field update
- Розуміє, що dual-bank і A/B існують для уникнення bricking під час update
- Згадує rollback і signature verification як обов'язкові для production OTA
- Розуміє компроміс між складністю та надійністю

### Red flags

- Плутає bootloader update з wired flashing
- Не згадує rollback як обов'язковий механізм
- Вважає, що OTA не потребує signature verification
- Не розрізняє dual-bank і A/B схеми

### Level-up follow-up

- Як реалізувати anti-rollback policy, і чому вона важлива?
- Як забезпечити atomic update на пристрої з обмеженим flash?

## Sources

<!-- generated from frontmatter -->
