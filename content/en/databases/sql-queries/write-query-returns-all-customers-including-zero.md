---
id: db-sqlq-0001
title: "How do you write a query that returns all customers, including those with zero paid orders, and where should the predicate go so it doesn't effectively turn the `LEFT JOIN` into an `INNER JOIN`?"
description: "How do you write a query that returns all customers, including those with zero paid orders, and where should the predicate go so it doesn't effectively turn the `LEFT JOIN` into an `INNER JOIN`?"
track: databases
section: sql-queries
level: middle
type: practical
tags: [left-join, inner-join]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: postgres-queries-table-expressions
    title: "PostgreSQL 17: Table Expressions"
    url: https://www.postgresql.org/docs/17/queries-table-expressions.html#QUERIES-FROM
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Defines outer joins, ON conditions, and null-extended rows in PostgreSQL 17."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L154-L245
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Use a `LEFT JOIN` from `customers` to `orders`, put `o.status = 'paid'` in `ON`, and aggregate
with `COUNT(o.id)`.**[^postgres-queries-table-expressions] The `ON` predicate limits matching paid
orders while preserving every customer as a null-extended row. `COUNT(o.id)` then returns zero for
that row; `COUNT(*)` would incorrectly count it as one. Moving the status predicate to `WHERE`
removes customers without a paid order.

## Detailed explanation

A `LEFT JOIN` is a join type that returns every row of the left table regardless of whether it has
a match in the right table; when there is no match, the right table's columns are filled with
`NULL`.[^postgres-queries-table-expressions]

The condition in `ON` runs during the join itself: it decides which rows of the right table get
attached to each row of the left table, but it does not drop left-table rows that have no match –
they stay, with `NULL`. The condition in `WHERE` runs after the join has already been built, and
acts as an ordinary filter over the resulting row set.

If a filter on a right-table column (for example, `orders.status = 'paid'`) is put in `WHERE`,
customer rows with no paid orders will have `NULL` in that column, and `NULL = 'paid'` evaluates to
`UNKNOWN`, so those rows get filtered out. The result looks as if the `LEFT JOIN` turned into an
`INNER JOIN`, even though it is still syntactically a `LEFT JOIN`.

The difference between correct and incorrect placement of the filter:

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

**Common mistakes with predicate placement:**
- moving every filter condition into `WHERE` out of habit, without accounting for what that does
  to a `JOIN`;
- testing the query only on data where every customer already has at least one order, and missing
  that zero-order rows disappear;
- forgetting that `IS NULL` on a non-nullable right-table key in `WHERE` is one way to filter for
  "rows with no match" after a `LEFT JOIN`.

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
