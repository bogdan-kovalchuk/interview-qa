---
id: db-relmod-0001
title: "Як primary key, foreign key, unique та check constraints переносять data integrity з application code у schema?"
description: "Constraints декларують правила валідації безпосередньо в схемі БД, і СУБД застосовує їх автоматично при кожній операції INSERT/UPDATE/DELETE, незалежно від application code."
track: databases
section: relational-model
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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
    applicability: "Визначає поведінку primary key, foreign key, unique, check і NULL у PostgreSQL 17."
  - source_id: postgres-17-set-constraints
    title: "PostgreSQL 17: SET CONSTRAINTS"
    url: https://www.postgresql.org/docs/17/sql-set-constraints.html
    accessed: 2026-09-08
    kind: official
    version: "17"
    applicability: "Визначає immediate і deferred timing перевірки constraints у PostgreSQL 17."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L65-L85
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Constraints декларують integrity rules у schema, тому PostgreSQL застосовує їх до кожного writer,
а не лише до одного application path.**[^postgres-ddl-constraints] `PRIMARY KEY` вимагає unique
non-null values; `FOREIGN KEY` забезпечує references; `UNIQUE` контролює duplicate key values; а
`CHECK` перевіряє row expression. Важливо враховувати точну поведінку NULL і timing перевірки.

## Detailed explanation

Механічно кожен із цих constraints реалізується по-різному, хоча мета спільна – заборонити
невалідний стан закомітитися. У PostgreSQL 17 додавання `PRIMARY KEY` створює unique B-tree index
і позначає його columns як `NOT NULL`.[^postgres-ddl-constraints]

`FOREIGN KEY` вимагає, щоб кожне non-null reference value відповідало row у referenced columns,
і застосовує визначену дію при зміні цього row, наприклад `NO ACTION`, `RESTRICT`, `CASCADE` або
`SET NULL`.[^postgres-ddl-constraints] Referenced columns мають спиратися на primary key, unique
constraint або відповідний non-partial unique index. PostgreSQL не створює index для referencing
columns автоматично, тому це окреме performance-рішення автора schema.

За замовчуванням PostgreSQL `UNIQUE` дозволяє кілька nulls, але `NULLS NOT DISTINCT` змінює цю
поведінку. SQL standard лишає обробку nulls у unique constraint implementation-defined, тому цей
default не є переносною гарантією всіх DBMS.[^postgres-ddl-constraints]

`CHECK` приймає row, коли expression дорівнює true або null. Тому `CHECK (price > 0)` не відхиляє
null price; якщо null заборонено, треба додати `NOT NULL`. PostgreSQL не підтримує cross-row або
cross-table гарантії через `CHECK`; для такого зв'язку потрібен відповідний constraint type.
[^postgres-ddl-constraints]

Timing не однаковий для всіх constraints. Non-deferrable constraints перевіряються immediately,
а deferrable unique, primary-key, foreign-key та exclusion constraints можна перевірити під час
transaction commit; PostgreSQL `CHECK` і `NOT NULL` завжди immediate.[^postgres-17-set-constraints]
Порушення дає error і лишає transaction у стані, що потребує rollback або відновлення до
savepoint, а не мовчки виконує повний rollback одразу.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
