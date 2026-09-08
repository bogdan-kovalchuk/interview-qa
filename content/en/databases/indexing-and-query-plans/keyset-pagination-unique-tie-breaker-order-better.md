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
  - source_id: postgres-17-limit-offset
    title: "PostgreSQL 17: LIMIT and OFFSET"
    url: https://www.postgresql.org/docs/17/queries-limit.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Documents that OFFSET rows are still computed and that a unique ORDER BY is required for predictable subsets."
  - source_id: postgres-transaction-iso
    title: "PostgreSQL docs: Transaction Iso"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official PostgreSQL documentation."
  - source_id: postgres-indexes-ordering
    title: "PostgreSQL 17: Indexes and ORDER BY"
    url: https://www.postgresql.org/docs/17/indexes-ordering.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Documents ordered B-tree scans and multicolumn ordering."
  - source_id: postgres-17-row-comparisons
    title: "PostgreSQL 17: Row and Array Comparisons"
    url: https://www.postgresql.org/docs/17/functions-comparisons.html#ROW-WISE-COMPARISON
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Defines lexicographic row-constructor comparison used by a composite keyset cursor."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L1207-L1250
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Keyset pagination is usually better for deep sequential navigation because it seeks from the
last ordered key instead of computing and discarding every preceding row.**[^postgres-17-limit-offset][^postgres-indexes-ordering]
With an immutable unique ordering key and a consistent direction, inserts before the cursor do not
shift later pages as they do with `OFFSET/LIMIT`. It does not guarantee freedom from skips or
duplicates when ordering keys are updated, rows are deleted, or page requests use different
snapshots. <span class="warn">The trade-off is no direct jump to an arbitrary page number.</span>

## Detailed explanation

`OFFSET n LIMIT m` has no special way to skip the first n rows: the planner executes the query
per `ORDER BY`, sequentially reads (and discards) n rows of the index or sort, and only then
returns the next m. The skipped rows still have to be computed by the server, so a large offset
can be inefficient.[^postgres-17-limit-offset]

The instability problem arises because `OFFSET` counts a position in the snapshot visible to the
current statement, not relative to a specific row. Under PostgreSQL Read Committed, consecutive
page requests can observe different snapshots.[^postgres-transaction-iso] An insert or delete
before the offset point can therefore shift later rows and cause a duplicate or omission.

Keyset pagination instead fixes the boundary by the value of the last row shown. PostgreSQL row
comparison applies lexicographic field order, so `WHERE (created_at, id) < (:created_at, :id)`
matches a descending `ORDER BY created_at DESC, id DESC` cursor.[^postgres-17-row-comparisons]
With a matching B-tree index, the work is an index seek plus the rows in the requested page, rather
than a bare O(log n) claim that ignores returning the page itself.[^postgres-indexes-ordering]

The tie-breaker (`id`) in the ordering is critical precisely because `created_at` on its own is
not unique: without the second column, several rows sharing the same `created_at` have no
defined relative order, so the page boundary can either skip or duplicate rows with the same
value. A unique tie-breaker makes the order total and the boundary unambiguous. It still cannot
prevent a row from moving across the cursor when an ordering value changes. To navigate backward,
reverse both the comparison and sort direction for the query, then restore display order.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
