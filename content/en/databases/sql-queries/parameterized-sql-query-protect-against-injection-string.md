---
id: db-sqlq-0002
title: "Why does a parameterized SQL query protect against injection, while string formatting or manual escaping is not a reliable substitute?"
description: "Why does a parameterized SQL query protect against injection, while string formatting or manual escaping is not a reliable substitute?"
track: databases
section: sql-queries
level: middle
type: pitfall
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L853-L893
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A parameterized query separates the SQL structure from the data: the database driver sends the
query with placeholders, and the values are passed separately, so they are never interpreted as SQL
code.**[^postgres-indexes] With string formatting or manual escaping there are always edge cases:
different encodings (for example, Unicode normalization), quote escaping in different contexts, or
bugs in the escaping logic can let an attacker insert executable SQL. <span class="warn">Never
concatenate user input into a SQL string – always use parameterized queries or an ORM with automatic
escaping.</span>

## Detailed explanation

A parameterized query (prepared statement) executes SQL where the query text with placeholders
(`?` or `%s`, depending on the driver) is sent separately from the values, and the values are
bound to the query after the database has already parsed it.[^postgres-indexes]

The database first parses and plans the query with placeholders as a fixed structure, then
substitutes the values as typed data at execution time (bind). Because the values never pass
through the SQL parser as text, they cannot physically change the structure of the query – a
malicious string such as `' OR '1'='1` stays a plain string value, not part of the SQL syntax.

String formatting (for example, an f-string or `%`) or manual escaping tries to reach the same
result a different way: escape special characters so the string cannot "break out" of the literal.
The problem is that escaping rules depend on context (quoting, encoding, SQL dialect specifics),
and any forgotten case – for instance, a multi-byte encoding that lets an attacker "eat" the escape
character, or missing escaping in an unusual place (LIMIT, a column name) – opens an injection. A
hand-written escaping function almost always covers only the cases its author remembered.

An example of the difference between the vulnerable and the safe approach:

```python
# vulnerable: user input becomes part of the SQL text
query = f"SELECT * FROM users WHERE name = '{name}'"
cursor.execute(query)

# safe: value is bound separately, never parsed as SQL
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```

**Common mistakes with SQL injection protection:**
- assuming that blacklist-escaping special characters (quotes, semicolons) covers every case;
- using string formatting for "trusted" values (for example, an ID from another table) that
  actually originate from user input;
- building dynamic SQL (table names, column names, `ORDER BY`) through concatenation, since a
  placeholder is syntactically impossible there, and forgetting an allowlist for such spots.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
