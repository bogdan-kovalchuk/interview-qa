---
id: emb-dtypes-0032
title: "Що таке memory-mapped I/O і навіщо `volatile` для таких регістрів?"
description: "Периферійні регістри доступні як звичайна пам'ять, а volatile забороняє компілятору кешувати чи видаляти звернення до них."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: gcc-volatiles
    title: "GCC: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює volatile-доступи у GCC та їхні обмеження; поведінка інших компіляторів може відрізнятися."
  - source_id: arm-dmb
    title: "Cache Coherency in ARMv7-A and ARMv7-R Systems"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/CacheCoherencyWhitepaper_6June2011.pdf?revision=e5a82cb4-0f87-4f5c-91cf-52b33a5cd1da
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює призначення DMB/DSB для впорядкування видимості; приклади та cache-поведінка залежать від конкретної системи."
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
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
---

## Short answer

**Memory-mapped I/O** – периферійні регістри доступні за адресами в адресному просторі CPU, але мають визначену платформою апаратну семантику.

`volatile` потрібен тому, що:
1. Апаратура може змінити status register між читаннями.
2. `volatile` позначає доступи, які реалізація компілятора мусить зберегти за своїми правилами.

`volatile` не робить доступ атомарним і не діє як memory barrier для звичайних записів.[^gcc-volatiles]

## Detailed explanation

Memory-mapped I/O відображає регістри периферії на адреси, до яких CPU звертається інструкціями читання та запису пам’яті. Для status register кожне читання може повертати новий стан апаратури, а запис у control register може запускати дію. Тому такі доступи мають апаратні побічні ефекти, яких немає у звичайної змінної.

Кваліфікатор `volatile` позначає об’єкт, доступи до якого мають бути спостережуваними для реалізації компілятора. Наприклад, цикл опитування volatile-поля регістра має повторно читати його, а не використовувати одне збережене значення. Стандарт C не задає повністю універсальну поведінку кожного volatile access; конкретні деталі документують компілятор і платформа.[^gcc-volatiles]

`volatile` не забезпечує atomicity, взаємне виключення між потоками, кеш-узгодженість DMA або порядок звичайних записів відносно периферійного доступу. Для таких вимог потрібні відповідні атомарні операції, memory barrier, cache maintenance чи API платформи. Регістри з write-one-to-clear семантикою також не слід оновлювати сліпим read-modify-write без перевірки документації MCU.

**Типова помилка:** вважати `volatile` достатнім для будь-якої синхронізації. Застосовуйте його до адреси регістра згідно з заголовком виробника, перевіряйте ширину і дозволені операції, а для міжпотокової синхронізації використовуйте окремий механізм.[^iso-c-n1570] Для прикладу, прапорець, який змінює ISR, може вимагати atomic access або критичної секції, якщо тип не читається атомарно на цільовому CPU. Аналогічно, передача буфера через DMA вимагає правил кешу та бар’єрів, визначених MCU; сам `volatile` не синхронізує ці пристрої. Завжди звіряйте спосіб доступу з документацією периферії та конкретною моделлю MCU.

Якщо CPU записує дані в буфер, який читає DMA, порядок доступів теж має значення: на Arm `__DMB()` може впорядкувати явні звернення до пам’яті, але він не очищає cache і не замінює потрібну для конкретного MCU cache maintenance.[^arm-dmb]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
