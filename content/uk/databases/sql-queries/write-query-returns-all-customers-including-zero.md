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
  - source_id: postgres-queries-table-expressions
    title: "PostgreSQL 17: Table Expressions"
    url: https://www.postgresql.org/docs/17/queries-table-expressions.html#QUERIES-FROM
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Визначає outer joins, ON conditions і null-extended rows у PostgreSQL 17."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L154-L245
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Використовуйте `LEFT JOIN` від `customers` до `orders`, розмістіть `o.status = 'paid'` в `ON` і
агрегуйте через `COUNT(o.id)`.**[^postgres-queries-table-expressions] Predicate в `ON` обмежує
matching paid orders, але зберігає кожного customer як null-extended row. Тоді `COUNT(o.id)` дає
нуль; `COUNT(*)` помилково порахував би такий row як один. Перенесення status predicate у `WHERE`
видаляє customers без paid order.

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
-- correct: one row per customer, including a zero paid-order count
SELECT c.id, c.name, COUNT(o.id) AS paid_order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
GROUP BY c.id, c.name;

-- wrong: filter in WHERE drops customers with no matching paid order
SELECT c.id, c.name, COUNT(o.id) AS paid_order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'paid'
GROUP BY c.id, c.name;
```

**Типові помилки з розміщенням предиката:**
- переносити всі умови фільтрації у `WHERE` за звичкою, не враховуючи, що це вимагає `JOIN`;
- перевіряти запит лише на даних, де кожен customer має хоча б одне замовлення, і не помічати, що
  zero-order рядки зникають;
- забувати, що `IS NULL` для non-nullable key правої таблиці в `WHERE` – один зі способів
  відфільтрувати «rows без збігу» після `LEFT JOIN`.

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
