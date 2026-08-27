---
id: db-idxplan-0002
title: "When is keyset pagination with a unique tie-breaker in `ORDER BY` better than `OFFSET/LIMIT` for performance and stability under concurrent writes?"
description: "When is keyset pagination with a unique tie-breaker in `ORDER BY` better than `OFFSET/LIMIT` for performance and stability under concurrent writes?"
track: databases
section: indexing-and-query-plans
level: middle
type: comparison
tags: [order-by, offset-limit]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L1207-L1250
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Keyset pagination is consistently faster at large page depths and guarantees no
duplicates/skips under concurrent data changes.**[^postgres-indexes] `OFFSET/LIMIT` must read
and discard every preceding row, so performance degrades linearly with the offset; if data
changes between page requests, duplicates or skipped rows can result. Keyset pagination uses the
last row of the previous page as a cursor (`WHERE (created_at, id) < (:last_created_at,
:last_id)`), so it runs in O(log n) via an index and ignores shifts. <span class="warn">Drawback:
you cannot jump to an arbitrary page (only next/prev).</span>

## Detailed explanation

`OFFSET n LIMIT m` has no special way to skip the first n rows: the planner executes the query
per `ORDER BY`, sequentially reads (and discards) n rows of the index or sort, and only then
returns the next m. So the cost grows linearly with the offset instead of staying constant: page
1000 reads and discards thousands of rows, even though only the last m are physically needed.

The instability problem arises because `OFFSET` counts a position relative to the current state
of the data, not relative to a specific row. If someone inserts a new row between the request for
page 1 and page 2 that falls within the range of the first offset rows, every following row
shifts by one position – the user either sees the same row twice, or skips a row, depending on
whether the change happened before or after the offset point.

Keyset pagination instead fixes the position by the value of the last row shown, not by a
counter: the condition `WHERE (created_at, id) < (:last_created_at, :last_id)` always returns the
rows strictly after a specific point in the ordered space, regardless of how many rows came
before it. This works via an index scan on the composite index `(created_at, id)` – the planner
jumps straight to the right spot in the B-tree, without reading the earlier pages.
[^postgres-indexes-ordering]

The tie-breaker (`id`) in the ordering is critical precisely because `created_at` on its own is
not unique: without the second column, several rows sharing the same `created_at` have no
defined relative order, so the page boundary can either skip or duplicate rows with the same
value. A unique tie-breaker turns `(created_at, id)` into a strictly monotonic key, for which the
`<` condition unambiguously defines the boundary.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
