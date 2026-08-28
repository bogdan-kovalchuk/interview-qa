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
  - source_id: postgres-indexes
    title: "PostgreSQL docs: Indexes"
    url: https://www.postgresql.org/docs/current/indexes.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-transaction-iso
    title: "PostgreSQL docs: Transaction Iso"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-using-explain
    title: "PostgreSQL docs: Using Explain"
    url: https://www.postgresql.org/docs/current/using-explain.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-ddl-constraints
    title: "PostgreSQL docs: DDL Constraints"
    url: https://www.postgresql.org/docs/current/ddl-constraints.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-indexes-ordering
    title: "PostgreSQL docs: Indexes Ordering"
    url: https://www.postgresql.org/docs/current/indexes-ordering.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-queries-table-expressions
    title: "PostgreSQL docs: Queries Table Expressions"
    url: https://www.postgresql.org/docs/current/queries-table-expressions.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L154-L245
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Use a `LEFT JOIN` from the customers table to orders, and put the filter for paid orders (for
example, `status = 'paid'`) in the `ON` condition, not in `WHERE`.**[^postgres-indexes] The
condition in `ON` decides which rows of the right table get joined; when there is no match, the
customer row is still returned with `NULL` for orders. If the same filter is put in `WHERE`
instead, rows with `NULL` (customers with no paid orders) get filtered out, which effectively
turns the `LEFT JOIN` into an `INNER JOIN`.

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

**Common mistakes with predicate placement:**
- moving every filter condition into `WHERE` out of habit, without accounting for what that does
  to a `JOIN`;
- testing the query only on data where every customer already has at least one order, and missing
  that zero-order rows disappear;
- forgetting that `IS NULL` on a right-table column in `WHERE` is the correct way to filter for
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
