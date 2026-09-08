---
id: db-relmod-0001
title: "How do primary key, foreign key, unique, and check constraints move data integrity from application code into the schema?"
description: "How do primary key, foreign key, unique, and check constraints move data integrity from application code into the schema?"
track: databases
section: relational-model
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: PostgreSQL
    version: "17"
anki:
  export: true
sources:
  - source_id: postgres-ddl-constraints
    title: "PostgreSQL 17: Constraints"
    url: https://www.postgresql.org/docs/17/ddl-constraints.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Defines PostgreSQL 17 primary-key, foreign-key, unique, check, and NULL behavior."
  - source_id: postgres-17-set-constraints
    title: "PostgreSQL 17: SET CONSTRAINTS"
    url: https://www.postgresql.org/docs/17/sql-set-constraints.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Defines immediate and deferred constraint-check timing in PostgreSQL 17."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L65-L85
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Constraints declare integrity rules in the schema, so PostgreSQL enforces them for every writer,
not only for one application path.**[^postgres-ddl-constraints] `PRIMARY KEY` requires unique,
non-null values; `FOREIGN KEY` enforces references; `UNIQUE` controls duplicate key values; and
`CHECK` tests a row expression. Their exact NULL behavior and check timing matter.

## Detailed explanation

Mechanically, each of these constraints is implemented differently, even though the goal is
shared – prevent a transaction from committing a state that violates the declared rule. In
PostgreSQL 17, adding a `PRIMARY KEY` creates a unique B-tree index and marks its columns
`NOT NULL`.[^postgres-ddl-constraints]

`FOREIGN KEY` requires each non-null referencing value to match a row in the referenced columns
and applies the configured action when that row changes, such as `NO ACTION`, `RESTRICT`,
`CASCADE`, or `SET NULL`.[^postgres-ddl-constraints] The referenced columns must be backed by a
primary key, unique constraint, or suitable non-partial unique index. PostgreSQL does not
automatically index the referencing columns, so that separate performance decision remains with
the schema designer.

By default, a PostgreSQL `UNIQUE` constraint permits multiple nulls, but `NULLS NOT DISTINCT`
changes that behavior. The SQL standard leaves unique-constraint null treatment
implementation-defined, so this default is not a portable DBMS guarantee.[^postgres-ddl-constraints]

`CHECK` accepts a row when its expression is true or null. Consequently, `CHECK (price > 0)` does
not reject a null price; add `NOT NULL` when null itself is invalid. PostgreSQL does not support
cross-row or cross-table `CHECK` guarantees; use a constraint type designed for that relationship.
[^postgres-ddl-constraints]

Timing is not identical for every constraint. Non-deferrable constraints are checked immediately,
while deferrable unique, primary-key, foreign-key, and exclusion constraints can be checked at
transaction commit; PostgreSQL `CHECK` and `NOT NULL` constraints are always immediate.
[^postgres-17-set-constraints] A violation raises an error and leaves the transaction needing a
rollback or savepoint recovery – it does not silently perform an immediate full rollback itself.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
