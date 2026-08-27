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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L65-L85
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Constraints declare validation rules directly in the database schema, and the DBMS enforces
them automatically on every `INSERT`/`UPDATE`/`DELETE`, independent of application
code.**[^postgres-indexes] `PRIMARY KEY` guarantees uniqueness and NOT NULL; `FOREIGN KEY`
enforces referential integrity against a value in another table; `UNIQUE` prevents duplicates;
and `CHECK` validates an arbitrary boolean condition, such as `price > 0`. This means that even
if the application code has a bug or bypasses validation, the database will not admit invalid
data.

## Detailed explanation

Mechanically, each of these constraints is implemented differently, even though the goal is
shared – reject an invalid state before it ever reaches the table. `PRIMARY KEY` is syntactic
sugar over a `UNIQUE` index plus `NOT NULL` on the same columns: the DBMS builds a B-tree index
on the key and, on every `INSERT`/`UPDATE`, checks through that index whether such a key already
exists before allowing the operation – so the uniqueness check itself costs O(log n), not
O(n).[^postgres-indexes]

`FOREIGN KEY` performs a lookup in the parent table at write time: before inserting or updating a
row with a reference, the DBMS checks the parent table's primary (or unique) key index for the
existence of the matching value, and on deletion or update of the parent row it applies the
configured action (`RESTRICT`, `CASCADE`, `SET NULL`). Without an index on the parent table
side, this check would be O(n) per write, so a FK practically always relies on an existing
unique index.[^postgres-ddl-constraints]

`UNIQUE` is the same mechanism as the uniqueness part of `PRIMARY KEY`, but without the
`NOT NULL` requirement; several `NULL` values in a unique column do not conflict with each
other, because `NULL` is by definition never equal to `NULL`.

`CHECK` is fundamentally different: it is not an index but a boolean expression that the DBMS
evaluates for each row separately at write time, comparing only values within that same row
(`price > 0`, `end_date > start_date`) – it cannot reference other rows or other tables, unlike
a FK.

What all four share is the moment they are applied: the check happens in the very same
transaction as the write operation itself, and on violation the transaction is rolled back, so
it is impossible to commit data that violates a constraint, even if a concurrency bug in the
application code skipped the validation.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
