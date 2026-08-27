---
id: db-idxplan-0001
title: "Why can an index speed up a read query but increase storage and write cost?"
description: "Why can an index speed up a read query but increase storage and write cost?"
track: databases
section: indexing-and-query-plans
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L406-L463
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**An index is a separate data structure (usually a B-tree) that stores copies of the indexed
column values together with pointers to the table rows.**[^postgres-indexes] On reads, the index
lets you find the rows you need in O(log n) instead of a full table scan. But every `INSERT`,
`UPDATE`, or `DELETE` must update every matching index, which adds I/O and CPU. On top of that,
indexes take extra disk space proportional to the number of indexed columns and rows.

## Detailed explanation

Structurally, a B-tree index stores ordered keys in a balanced tree of pages: each internal node
holds ranges that lead to child pages, and the leaf nodes hold the values themselves and
pointers to the row's physical location in the table. The height of this tree grows
logarithmically with the row count, so a key lookup is, in essence, a handful of page reads
(usually 2-4 even at millions of rows), not a scan of the whole table.[^postgres-indexes]

Write cost does not come only from adding a new key: when an index leaf page fills up, an
insertion triggers a page split – trading one write for two pages plus an update of the parent
node, which can cascade all the way to the root. PostgreSQL adds one more cost on top through
MVCC: an `UPDATE` creates a new version of the row, and if the updated column is indexed, every
index on the table gets an extra entry for the new version, while the old version stays in the
index until `VACUUM`. So the number of indexes on a table multiplies the cost of every
`INSERT`/`UPDATE`.[^postgres-ddl-constraints]

Disk space grows because an index physically duplicates the values of the indexed columns (and,
for a composite index, all of its columns) for every table row – for wide columns (such as
`text`) or multi-column indexes this can amount to a substantial fraction of the table's own
size, and sometimes exceed it.

So the decision to add an index is always a trade-off that depends on the read-to-write ratio: a
table that is mostly `SELECT` with rare writes benefits from extra indexes at almost no cost,
while a table with a high rate of `INSERT`/`UPDATE` pays a noticeable write slowdown for every
extra index.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
