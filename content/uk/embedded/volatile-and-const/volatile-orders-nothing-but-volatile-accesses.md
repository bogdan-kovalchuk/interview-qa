---
id: emb-volconst-0038
title: "Чому `volatile` не є memory barrier?"
description: "volatile обмежує оптимізації доступів до volatile-об’єктів, але не є повноцінним CPU/compiler memory barrier для всієї пам’яті."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
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
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Документує межі volatile та його нездатність впорядковувати non-volatile memory accesses у GCC."
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
    accessed: 2026-10-04
    kind: official
    version: "DUI 0646B"
    applicability: "Описує cache maintenance Cortex-M7 і видимість даних зовнішнього DMA; конкретні вимоги залежать від конфігурації SoC."
---

## Short answer

**`volatile` обмежує оптимізації доступів до volatile-об’єктів, але не є повноцінним CPU/compiler memory barrier для всієї пам’яті.**

`volatile` не задає загального порядку звичайних memory accesses відносно volatile-доступів і не є повною CPU/compiler memory barrier. Точні правила volatile accesses залежать від мови, compiler та target. Cache synchronization, bus ordering, DMA visibility і inter-core ordering потребують окремих гарантій платформи.

Правило: для потрібного hardware ordering використовуй архітектурні primitives на кшталт `__DMB()`, `__DSB()`, `__ISB()` та compiler-specific засоби відповідно до документації платформи.[^gcc-volatile]

## Detailed explanation

`volatile` позначає об’єкт, значення якого може змінюватися поза звичайним потоком виконання C або доступ до якого має побічний ефект. Це корисно для MMIO register і деяких прапорців, але не створює загального бар’єра пам’яті для всіх операцій програми. У стандарті C точне визначення volatile access є implementation-defined; наприклад, GCC окремо документує свою поведінку.

Розрізняй три питання: чи компілятор виконає volatile access, чи впорядкує він звичайні accesses навколо нього, і чи апаратна система забезпечує потрібний порядок або видимість. Відповідь «так» на перше не гарантує «так» на решту. GCC прямо застерігає, що volatile object не можна використовувати як memory barrier для записів у non-volatile memory. Compiler barrier може обмежити перестановки компілятора, але не обов’язково видає інструкцію для CPU чи очищає cache.[^gcc-volatile]

На MCU потрібний засіб залежить від завдання: `DMB` впорядковує певні memory accesses на рівні архітектури, `DSB` очікує завершення попередніх явних accesses, `ISB` синхронізує подальше виконання інструкцій після зміни стану процесора. Це не взаємозамінні команди і їх не слід вставляти навмання. DMA coherency може додатково вимагати clean/invalidate cache або non-cacheable region; звичайний barrier не замінює ці дії.[^arm-cortex-m7]

**Типові помилки:**

- Використовувати volatile для синхронізації потоків C замість atomics або lock.
- Вважати, що запис volatile flag автоматично публікує попередні звичайні записи.
- Додавати `DMB` і припускати, що він очищає D-cache.

Спершу визнач, хто взаємодіє з пам’яттю – compiler, CPU, інше ядро чи DMA – а тоді вибирай засіб із документації compiler та MCU.[^gcc-volatile] [^arm-cortex-m7]

## Sources

<!-- generated from frontmatter -->
