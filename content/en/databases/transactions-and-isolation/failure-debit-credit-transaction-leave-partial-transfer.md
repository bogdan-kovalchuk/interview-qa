---
id: db-txiso-0001
title: "After a failure between the debit and the credit, a transaction must not leave a partial transfer: which ACID property does this illustrate, and what does the application still have to decide about retrying?"
description: "After a failure between the debit and the credit, a transaction must not leave a partial transfer: which ACID property does this illustrate, and what does the application still have to decide about retrying?"
track: databases
section: transactions-and-isolation
level: middle
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L652-L733
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**This illustrates Atomicity: a transaction either runs to completion or does not run at all – on
failure, all its changes are rolled back.**[^postgres-indexes] But the application still has to
solve the retry problem: whether it is safe to repeat the operation (idempotency), how to tell
whether the original transaction committed or not (for example, after a network timeout), and how
to avoid duplicating side effects (email, notification) on a retry.

## Detailed explanation

Atomicity is an ACID property that guarantees a transaction runs as a single indivisible
operation: all of its changes are applied, or none of them are.[^postgres-transaction-iso]

If a failure (a network drop, a process crash, a constraint violation) happens between the debit
and the credit operation, the database rolls back all changes made by that transaction, including
ones that had already run locally within it. No intermediate state – money debited from one
account but not yet credited to the other – is ever left visible to other transactions.

Atomicity only guarantees that the database itself will not leave a partial transfer. It says
nothing about the client that started the transaction and never received a confirmation – after a
network timeout, there is no way to tell for certain whether the transaction committed on the
server or rolled back. The application has to decide on its own what to do with that uncertainty.

**What the application still has to decide for a safe retry:**
- whether the operation is idempotent – whether it is safe to repeat it several times without a
  double debit (for example, via an idempotency key);
- how to check the actual state after a timeout – reading the transaction back by a known
  identifier instead of blindly retrying it;
- how to avoid duplicating side effects (an email notification, a call to an external payment
  gateway) that carry no transactional guarantees of their own.

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
