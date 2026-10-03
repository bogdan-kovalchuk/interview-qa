---
id: emb-structs-0051
title: "Trap: чому копіювання struct із pointer fields може бути shallow copy багом?"
description: "Structure assignment копіює pointer value, а не дані, на які він вказує."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
---

## Short answer

<span class="warn">Structure assignment копіює pointer value, а не дані, на які він вказує.</span>

Після `b = a` обидві структури можуть вказувати на той самий buffer. Якщо одна структура звільняє або змінює buffer, інша бачить наслідки. У embedded це часто трапляється з DMA buffers, queues і driver config pointers.

Захист: визнач ownership: pointer є borrowed і це документовано, або потрібна deep copy, або buffer передається окремо з lifetime contract.[^iso-c-n1570]

## Detailed explanation

Присвоєння структури в C копіює значення кожного її члена; для pointer member це саме значення адреси, а не об’єкт, на який адреса вказує. Така поверхнева копія є коректною операцією мови, але вона не створює незалежну копію динамічного буфера чи іншого ресурсу.[^iso-c-n1570]

Після `b = a` поля `a.data` і `b.data` містять ту саму адресу. Зміна байтів через один вказівник видима через інший, а звільнення пам’яті одним власником залишає другий вказівник висячим. Повторне звільнення або використання після звільнення може спричинити undefined behavior. У firmware подібна помилка трапляється, коли копіюють конфігурацію драйвера, descriptor черги чи структуру навколо DMA buffer, не визначивши власника ресурсу.[^iso-c-n1570]

Наприклад, передавання структури за значенням у функцію теж копіює pointer, але не передає автоматично право звільняти його. Потрібно встановити контракт: borrowed pointer живе довше за кожного користувача й не звільняється ним; власник може передавати ownership; або функція виконує deep copy виділеної пам’яті й копіює самі дані. Для статичного буфера чи memory-mapped регістру правила володіння будуть іншими, тож не слід бездумно копіювати все за адресою.[^iso-c-n1570]

**Як уникнути помилки:**

- Документуй, хто створює, змінює та звільняє ресурс, і скільки він живе.
- Якщо потрібна незалежна копія, копіюй дані у власний буфер із перевіркою розміру.
- Для DMA додатково дотримуйся вимог платформи до lifetime, вирівнювання та cache coherency.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
