---
id: db-sqlq-0001
title: "Як запитом повернути всіх customers, включно з нулем paid orders, і де розмістити predicate, щоб не перетворити `LEFT JOIN` фактично на `INNER JOIN`?"
description: "Використовуйте LEFT JOIN від таблиці customers до orders, а фільтр по оплачених замовленнях (наприклад, status = 'paid') розміщуйте в умові ON, а не в WHERE."
track: databases
section: sql-queries
level: middle
type: practical
tags: [left-join, inner-join]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L154-L245
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Використовуйте `LEFT JOIN` від таблиці customers до orders, а фільтр по оплачених замовленнях (наприклад, `status = 'paid'`) розміщуйте в умові `ON`, а не в `WHERE`.**[^postgres-indexes] Умова в `ON` визначає, які рядки правої таблиці з'єднуються; якщо збігу немає, customers все одно повертається з `NULL` для orders. Якщо ж той самий фільтр помістити в `WHERE`, рядки з `NULL` (customers без paid orders) будуть відфільтровані, що фактично перетворить `LEFT JOIN` на `INNER JOIN`.

## Detailed explanation

`LEFT JOIN` – це тип з'єднання, який повертає всі рядки лівої таблиці незалежно від того, чи є для
них збіг у правій таблиці; якщо збігу немає, колонки правої таблиці заповнюються
`NULL`.[^postgres-queries-table-expressions]

Умова в `ON` виконується під час самого з'єднання: вона визначає, які рядки правої таблиці
приєднати до кожного рядка лівої, але не видаляє рядки лівої таблиці, для яких збігу немає – вони
залишаються з `NULL`. Умова у `WHERE` виконується вже після того, як з'єднання побудоване, і працює
як звичайний фільтр по результуючому набору.

Якщо фільтр по колонці правої таблиці (наприклад, `orders.status = 'paid'`) розмістити в `WHERE`,
то рядки customers без paid orders матимуть `NULL` у цій колонці, і умова `NULL = 'paid'` дає
`UNKNOWN`, тому такі рядки відфільтровуються. Результат виглядає так, ніби `LEFT JOIN` перетворився
на `INNER JOIN`, хоча синтаксично залишився `LEFT JOIN`.

Різниця між правильним і помилковим розміщенням фільтра:

```sql
-- correct: filter lives in ON, customers without paid orders still appear
SELECT c.id, c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'paid';

-- wrong: filter in WHERE drops customers with no matching paid order
SELECT c.id, c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'paid';
```

**Типові помилки з розміщенням предиката:**
- переносити всі умови фільтрації у `WHERE` за звичкою, не враховуючи, що це вимагає `JOIN`;
- перевіряти запит лише на даних, де кожен customer має хоча б одне замовлення, і не помічати, що
  zero-order рядки зникають;
- забувати, що умова `IS NULL` на колонці правої таблиці в `WHERE` – єдиний коректний спосіб
  фільтрувати «рядки без збігу» після `LEFT JOIN`.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
