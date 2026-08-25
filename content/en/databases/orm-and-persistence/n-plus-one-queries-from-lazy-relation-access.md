---
id: db-orm-0001
title: "Why does a list page issue one query per row?"
description: "Lazy relation loading turns one query into one plus one per row, and it only hurts at production size."
track: databases
section: orm-and-persistence
level: middle
type: pitfall
tags: [n-plus-one, lazy-loading, query-count, orm]
status: published
updated: 2026-09-04
content_revision: 2
reconciled_with:
  uk: 2
frameworks: [django, sqlalchemy]
applies_to:
  - product: Django
    version: "5.2"
  - product: SQLAlchemy
    version: "2.0"
anki:
  export: true
sources:
  - source_id: django-52-select-related
    title: "Django QuerySet API: select_related and prefetch_related"
    url: https://docs.djangoproject.com/en/5.2/ref/models/querysets/#select-related
    accessed: 2026-09-03
    kind: official
    version: "5.2"
    applicability: "Django ORM relation loading; the join and second-query strategies."
  - source_id: sqlalchemy-20-lazy-loading
    title: "SQLAlchemy ORM: relationship loading techniques"
    url: https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html
    accessed: 2026-09-03
    kind: official
    version: "2.0"
    applicability: "Default lazy loading and the selectin, joined and subquery strategies."
---

## Short answer

**A relation that loads lazily runs its query the first time each object touches it**, so a loop over
`n` rows runs one query for the list and `n` more for the relation. Nothing in the code looks like a
query: the attribute access is what triggers it.[^sqlalchemy-20-lazy-loading] The fix is to declare
the relation eagerly on the queryset, with a join for to-one relations and a second batched query for
to-many ones.[^django-52-select-related] <span class="warn">It is invisible on ten rows in development
and fatal on ten thousand in production.</span>

## Detailed explanation

An ORM maps a relation to an attribute, and an attribute access looks free. Under lazy loading the
related object is not fetched with its parent; the mapper stores enough to fetch it later and issues
the query the first time the attribute is read. One row costs one extra query, which is invisible.
A page listing rows repeats that per row.[^sqlalchemy-20-lazy-loading]

```python
for order in Order.objects.all():          # 1 query
    print(order.customer.name)             # 1 query per order
```

The cost is not the work the database does. Each of those statements is a primary key lookup, cheap
for the database once the page is warm. The cost is the round trip: connection handling, statement planning
and network latency, paid `n` times in sequence, so the page time grows linearly with the result set
and is dominated by waiting rather than by work. This is also why the problem hides in development,
where the fixture has twenty rows and the database is a local socket.

Eager loading removes the repetition in one of two shapes. A join fetches parent and related rows in a
single statement, which suits to-one relations where the parent row is not duplicated much. A second
query fetches all related rows for the already-known parent keys and stitches them in memory, which
suits to-many relations, where a join would multiply the parent row by the size of its collection
and inflate the transferred result.[^django-52-select-related]

Neither shape is free of its own trap. A join across several to-many relations produces a cartesian
product; batching adds a second round trip, and because the parents are selected before the children
are fetched, filtering parents by a child column still needs a join or a subquery in the parent
query. Choosing between them means knowing the cardinality, not applying a rule.

## Symptom

An endpoint that returns a list is slow in proportion to the number of items, while each individual
query in the log is fast. The query log for one request contains hundreds of nearly identical
statements differing only in a primary key. Response time is roughly flat per item, and the database
CPU is low while the application waits.

## Why it happens

The relation is configured to load lazily, which is the default in both Django and
SQLAlchemy.[^sqlalchemy-20-lazy-loading] The loop reads the related attribute once per parent object,
and each read that is not already loaded emits its own statement. The code contains no explicit query,
so the defect survives code review; only the query count reveals it. Serialisers and template loops
make it worse, because the access moves out of the view into a layer nobody reads as data access.

## How to avoid

Declare the loading strategy on the queryset where the data is fetched, not in the loop:

```python
Order.objects.select_related("customer").prefetch_related("items")
```

Use the join strategy for to-one relations and the batched second query for to-many relations.
Keep the declaration next to the queryset that the view uses, so that adding a field to a serialiser
and forgetting the relation is caught in one place. Then hold the line with a test that asserts the
number of queries for a representative endpoint, and run it against a fixture large enough for the
difference to be visible.

## Evaluation guide

### Expected signals

- States the query count as `1 + n` and connects it to attribute access rather than to a bug in the
  loop.
- Distinguishes the join strategy from the batched second query, and ties each to to-one and to-many.
- Names round-trip latency, not database work, as what makes it slow.
- Says how they would detect it: a query counter or log in a test, not eyeballing the page.

### Red flags

- Answers "add an index" or "add a cache" without mentioning the number of statements.
- Applies eager loading to every relation on every queryset as a blanket rule.
- Cannot say why it did not show up in development.

### Level-up follow-up

Ask how they would stop it from coming back after the fix. A strong answer proposes an assertion on
the number of queries in a test around the endpoint, so a later refactor that reintroduces lazy access
fails in CI rather than in production.

## Sources

<!-- generated from frontmatter -->
