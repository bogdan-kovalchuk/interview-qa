---
id: emb-dtypes-0106
title: "Що таке cache coherency і memory barrier у multi-core MCU, MPU або Embedded Linux системі?"
description: "Cache coherency означає узгодженість даних між CPU caches, DMA і peripheral views of memory. Memory barrier задає порядок memory operations, щоб CPU/compiler не переставили critical accesses."
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
  - source_id: linux-memory-barriers
    title: "Linux kernel memory barriers"
    url: https://docs.kernel.org/core-api/wrappers/memory-barriers.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює ordering, coherency та окрему потребу в cache maintenance для DMA у контексті Linux kernel; це не універсальний API для MCU."
---

## Short answer

**Cache coherency** означає узгодженість даних між CPU caches, DMA і peripheral views of memory. **Memory barrier** задає порядок memory operations, але сам по собі не очищає й не інвалідує кеш. <span class="warn">Для DMA потрібні операції cache maintenance та barriers, визначені платформою; coherent DMA memory також потребує правильного ordering.</span>[^linux-memory-barriers]

## Detailed explanation

Cache coherency визначає, чи бачать кілька агентів – ядра CPU та DMA-пристрій – узгоджений вміст спільної пам’яті. На coherent-платформі апаратний протокол підтримує це узгодження між кешами; на non-coherent платформі CPU може мати dirty cache line, якої ще немає в RAM, або читати стару копію після запису пристрою. Спільна адреса сама по собі не гарантує, що всі агенти бачать однакові байти.[^linux-memory-barriers]

Memory barrier розв’язує іншу задачу: він обмежує порядок, у якому memory operations стають видимими іншим агентам. Наприклад, CPU заповнює DMA descriptor, а потім передає пристрою прапорець готовності. Без належного ordering пристрій може побачити прапорець раніше за поля descriptor. Linux DMA API застерігає, що coherent mapping не скасовує потреби у barrier. Barrier не очищає кеш; cache clean/invalidate також не замінюють синхронізацію порядку.[^linux-memory-barriers]

Для багатоядерного CPU coherent cache domain зазвичай автоматизує передачу cache lines між ядрами, але це не тотожне синхронізації програмних потоків. Потрібні атомарні операції чи відповідні primitive, які задають happens-before, інакше навіть coherent кеш не усуває data race. Для пристрою DMA треба окремо з’ясувати, чи входить він у цей coherency domain конкретної платформи.[^linux-memory-barriers]

Послідовність залежить від напрямку передачі, атрибутів пам’яті, coherency домену й API платформи. Для CPU-to-device може знадобитися clean перед запуском DMA; для device-to-CPU – invalidate або синхронізація mapping після завершення. На MCU слід користуватися reference manual та HAL, а в Linux – DMA mapping/sync API. MMIO має окремі правила доступу та ordering.[^linux-memory-barriers]

Приклад: CPU оновлює descriptor у coherent DMA memory і ставить ownership bit для пристрою. Тут потрібен ordering між записами descriptor і прапорцем, хоча cache clean може не знадобитися. Якщо буфер streaming/non-coherent, перед передачею треба виконати потрібну DMA sync/cache maintenance, інакше пристрій може прочитати старі дані.[^linux-memory-barriers]

**Типові помилки:**
- Вважати, що будь-який memory barrier очищає D-cache.
- Припускати, що кожен DMA-пристрій автоматично coherent із CPU.
- Переносити cache-maintenance послідовність між архітектурами без перевірки API та меж cache line.[^linux-memory-barriers]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
