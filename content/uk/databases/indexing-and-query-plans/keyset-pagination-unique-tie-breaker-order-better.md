---
id: db-idxplan-0002
title: "Коли keyset pagination з unique tie-breaker у `ORDER BY` краща за `OFFSET/LIMIT` за performance та stability при concurrent writes?"
description: "Keyset pagination стабільно швидша при великій глибині сторінок і гарантує відсутність дублікатів/пропусків при конкурентних змінах даних."
track: databases
section: indexing-and-query-plans
level: middle
type: comparison
tags: [order-by, offset-limit]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: postgres-indexes
    title: "PostgreSQL docs: Indexes"
    url: https://www.postgresql.org/docs/current/indexes.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-transaction-iso
    title: "PostgreSQL docs: Transaction Iso"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-using-explain
    title: "PostgreSQL docs: Using Explain"
    url: https://www.postgresql.org/docs/current/using-explain.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-ddl-constraints
    title: "PostgreSQL docs: DDL Constraints"
    url: https://www.postgresql.org/docs/current/ddl-constraints.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-indexes-ordering
    title: "PostgreSQL docs: Indexes Ordering"
    url: https://www.postgresql.org/docs/current/indexes-ordering.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-queries-table-expressions
    title: "PostgreSQL docs: Queries Table Expressions"
    url: https://www.postgresql.org/docs/current/queries-table-expressions.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L1207-L1250
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Keyset pagination стабільно швидша при великій глибині сторінок і гарантує відсутність дублікатів/пропусків при конкурентних змінах даних.**[^postgres-indexes] `OFFSET/LIMIT` мусить прочитати й відкинути всі попередні рядки, тому продуктивність падає лінійно зі збільшенням offset; крім того, якщо між запитами сторінок дані змінюються (insert/delete), можливі дублікати або пропуски. Keyset pagination використовує значення останнього елемента попередньої сторінки як курсор (`WHERE (created_at, id) < (:last_created_at, :last_id)`), тому працює за O(log n) через індекс і не чутлива до зсувів. <span class="warn">Недолік: неможливо стрибнути на довільну сторінку (тільки next/prev).</span>

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
