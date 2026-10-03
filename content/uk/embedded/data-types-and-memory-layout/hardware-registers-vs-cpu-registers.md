---
id: emb-dtypes-0103
title: "Що таке hardware registers і чим memory-mapped register відрізняється від CPU general-purpose register?"
description: "Периферійний memory-mapped register має адресу в memory map; CPU general-purpose register є внутрішнім регістром ядра."
track: embedded
section: data-types-and-memory-layout
level: senior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: cmsis-peripheral-access
    title: "Arm CMSIS-Core: Peripheral Access"
    url: https://arm-software.github.io/CMSIS_5/Core/html/group__peripheral__gr.html
    accessed: 2026-10-04
    kind: official
    version: "5.6.0"
    applicability: "Показує модель доступу CMSIS до peripheral registers через структури й адреси; конкретна карта й атрибути залежать від MCU."
  - source_id: arm-cortex-m33-core-registers
    title: "Arm Cortex-M33 Processor Technical Reference Manual: Processor core registers summary"
    url: https://developer.arm.com/documentation/100230/0004/functional-description/programmers-model/processor-core-registers-summary
    accessed: 2026-10-04
    kind: official
    version: "r0p4"
    applicability: "Описує core registers саме Cortex-M33; не узагальнюється на всі ядра."
  - source_id: armv8a-memory-model
    title: "Arm: Armv8-A memory model guide, Device memory"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/Armv8-A%20memory%20model%20guide.pdf?revision=58b1dd0a-3800-4218-b21a-f95a0332034c
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює Device memory та MMIO side effects для Armv8-A; не замінює правила конкретного peripheral."
---

## Short answer

**Hardware register** – місце зберігання стану, визначене самим пристроєм; воно може бути регістром ядра або регістром периферії. **Memory-mapped register** периферії має адресу в memory map і зазвичай описується через pointer на `volatile` структуру; точні адреси й правила доступу задає документація MCU.[^cmsis-peripheral-access] CPU general-purpose register є частиною register bank ядра й використовується інструкціями без звернення до адреси периферії.[^arm-cortex-m33-core-registers]

## Detailed explanation

Термін hardware register ширший за «регістр периферії»: CPU general-purpose registers, status registers ядра й control/status registers периферії – різні апаратні сховища значень із різними правилами доступу. У C коді слово `register` також може означати лише змінну або оптимізаційну підказку; така змінна сама по собі не є фізичним регістром CPU.

У memory-mapped I/O периферійний регістр отримує адресу в системному address map. Програма читає чи записує цю адресу через load/store операції, а bus та peripheral decode спрямовують транзакцію до пристрою. У типових CMSIS headers набір регістрів подають як структуру з точними полями та offsets, а окремий pointer прив’язують до base address peripheral.[^cmsis-peripheral-access] На відміну від звичайної RAM, читання може мати побічний ефект: наприклад, читання FIFO забирає елемент або змінює peripheral state, тож кількість і порядок доступів мають значення.[^armv8a-memory-model] Частина бітів може бути read-only або write-one-to-clear; ширину й семантику запису звіряють із reference manual.

`volatile` у типовому embedded C/C++ повідомляє компілятору, що такі доступи є спостережуваними й не можна довільно прибирати або кешувати відповідне читання чи запис у регістрі. Воно саме по собі не забезпечує взаємного виключення, atomicity, cache coherency або потрібного порядку між різними memory regions; для цього потрібні правила архітектури, спеціальні інструкції чи API платформи.[^cmsis-peripheral-access]

CPU general-purpose register – інше: це, наприклад, `R0`–`R12` у Cortex-M33, внутрішні операнди ядра, які використовуються арифметичними та load/store інструкціями. Код C зазвичай не фіксує, у якому саме register compiler зберіг локальне значення; allocator може змінювати це між build-ами. Частина регістрів має спеціальне призначення, як stack pointer, link register і program counter, хоча вони теж належать до регістрів процесора.[^arm-cortex-m33-core-registers]

**Як розрізняти на практиці:**

- Якщо значення читають або пишуть за фіксованою адресою з device header, перевірте peripheral register description і його side effects.
- Якщо значення видно в debugger у register view ядра або воно операнд інструкції, це core register.
- Не робіть припущення, що кожне hardware register memory-mapped: конкретна архітектура може мати окремі адресні простори або спеціальні інструкції.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
