---
id: db-txiso-0002
title: "How does the isolation level affect concurrent anomalies, and why can stronger isolation require retrying a transaction?"
description: "How does the isolation level affect concurrent anomalies, and why can stronger isolation require retrying a transaction?"
track: databases
section: transactions-and-isolation
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L753-L902
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A higher isolation level prevents more anomalies: Read Committed allows non-repeatable reads and
phantom reads, Repeatable Read removes them via a snapshot, and Serializable removes all anomalies,
including the serialization anomaly.**[^postgres-indexes] But stronger isolation means more
conflicts: under Repeatable Read, a concurrent update of the same row makes a transaction fail with
`could not serialize access due to concurrent update`, and under Serializable with `SQLSTATE 40001`
when a read/write dependency is detected. The application has to catch these errors and retry the
transaction from the start.

## Detailed explanation

An isolation level is a transaction setting that determines how isolated concurrent transactions
are from one another, and which read anomalies they can observe.[^postgres-transaction-iso]

Read Committed is the minimal practical level: each statement sees only committed data as of the
moment it runs, but two statements within the same transaction can see different values of the same
row (a non-repeatable read) or new rows that appeared in between (a phantom read). Repeatable Read
fixes a snapshot of the data at the start of the transaction, so both anomalies disappear – every
statement in the transaction sees the same snapshot. Serializable goes further: it guarantees that
the outcome of running transactions concurrently is equivalent to some serial order of running
them, removing even subtler anomalies such as the serialization anomaly, which Repeatable Read does
not catch.

The price of stronger isolation is conflicts instead of a silently wrong result. Instead of letting
a transaction read stale or incompatible data, the database detects the conflict and rejects one of
the transactions with a serialization error rather than silently corrupting consistency.

An example of handling a serialization failure under Repeatable Read or Serializable:

```sql
-- application retries the whole transaction on a serialization failure
BEGIN;
-- ... reads and writes ...
COMMIT;
-- on error SQLSTATE 40001 ('could not serialize access due to concurrent update'):
-- roll back and re-run the same transaction from the start
```

**Common mistakes with isolation levels:**
- choosing Serializable "just in case" without retry logic in the application, so a fraction of
  requests simply fail under load;
- confusing Repeatable Read with "a snapshot for the whole connection" – the snapshot is taken at
  the start of the transaction, not the session;
- assuming that a higher isolation level by itself removes the need for correct query design (for
  example, `SELECT ... FOR UPDATE` for explicit locking).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
