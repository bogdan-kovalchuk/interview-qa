---
id: db-idxplan-0002
title: "Коли keyset pagination з unique tie-breaker у `ORDER BY` краща за `OFFSET/LIMIT` за performance та stability при concurrent writes?"
description: "Keyset pagination зазвичай краща для глибокої послідовної навігації, але не гарантує відсутності пропусків і дублікатів за будь-яких конкурентних змін."
track: databases
section: indexing-and-query-plans
level: middle
type: comparison
tags: [order-by, offset-limit]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: postgres-17-limit-offset
    title: "PostgreSQL 17: LIMIT and OFFSET"
    url: https://www.postgresql.org/docs/17/queries-limit.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Підтверджує, що OFFSET rows усе одно обчислюються, а для передбачуваних підмножин потрібен unique ORDER BY."
  - source_id: postgres-transaction-iso
    title: "PostgreSQL docs: Transaction Iso"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-indexes-ordering
    title: "PostgreSQL 17: Indexes and ORDER BY"
    url: https://www.postgresql.org/docs/17/indexes-ordering.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Підтверджує ordered B-tree scans і multicolumn ordering."
  - source_id: postgres-17-row-comparisons
    title: "PostgreSQL 17: Row and Array Comparisons"
    url: https://www.postgresql.org/docs/17/functions-comparisons.html#ROW-WISE-COMPARISON
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Визначає lexicographic row comparison, яке використовує composite keyset cursor."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L1207-L1250
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Keyset pagination зазвичай краща для глибокої послідовної навігації, бо шукає від останнього
ordered key замість обчислення й відкидання всіх попередніх rows.**[^postgres-17-limit-offset][^postgres-indexes-ordering]
За незмінного unique ordering key і сталого напрямку insert перед cursor не зсуває наступні
сторінки так, як в `OFFSET/LIMIT`. Але це не гарантує відсутності пропусків або дублікатів, якщо
ordering keys оновлюють, rows видаляють або запити сторінок бачать різні snapshots.
<span class="warn">Компроміс – немає прямого переходу до довільного номера сторінки.</span>

## Detailed explanation

`OFFSET n LIMIT m` не має спеціального способу пропустити перші n рядків: планувальник виконує
запит за `ORDER BY`, послідовно читає (та відкидає) n рядків індексу чи сортування, а потім
повертає наступні m. Пропущені rows усе одно обчислює server, тому великий offset може бути
неефективним.[^postgres-17-limit-offset]

Проблема нестабільності виникає тому, що `OFFSET` рахує позицію в snapshot, видимому поточному
statement, а не відносно конкретного row. У PostgreSQL Read Committed послідовні запити сторінок
можуть бачити різні snapshots.[^postgres-transaction-iso] Тому insert або delete перед точкою
offset може зсунути наступні rows і спричинити duplicate або omission.

Keyset pagination натомість фіксує межу значенням останнього показаного row. PostgreSQL row
comparison застосовує lexicographic field order, тому
`WHERE (created_at, id) < (:created_at, :id)` відповідає cursor для
`ORDER BY created_at DESC, id DESC`.[^postgres-17-row-comparisons] За відповідного B-tree index
робота складається з index seek та читання rows запитаної сторінки, а не з голого O(log n), яке
не враховує повернення самої сторінки.[^postgres-indexes-ordering]

Tie-breaker (`id`) у сортуванні критичний саме тому, що `created_at` сам по собі не унікальний:
без другого стовпця кілька рядків з однаковим `created_at` не мають визначеного відносного
порядку, тому межа сторінки може або пропустити, або продублювати рядки з однаковим значенням.
Unique tie-breaker створює total order і робить межу однозначною. Але він не завадить row перейти
через cursor, якщо ordering value зміниться. Для руху назад треба обернути і comparison, і sort
direction у запиті, а потім відновити порядок відображення.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
