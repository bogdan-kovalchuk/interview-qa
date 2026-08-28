---
id: db-txiso-0002
title: "Як isolation level впливає на concurrent anomalies і чому stronger isolation може вимагати retry transaction?"
description: "Вищий isolation level запобігає більше аномалій: Read Committed допускає non-repeatable read і phantom read, Repeatable Read усуває їх через snapshot, а Serializable усуває всі аномалії включаючи serialization anomaly."
track: databases
section: transactions-and-isolation
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: postgres-indexes
    title: "PostgreSQL docs: Indexes"
    url: https://www.postgresql.org/docs/current/indexes.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-transaction-iso
    title: "PostgreSQL docs: Transaction Iso"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-using-explain
    title: "PostgreSQL docs: Using Explain"
    url: https://www.postgresql.org/docs/current/using-explain.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-ddl-constraints
    title: "PostgreSQL docs: DDL Constraints"
    url: https://www.postgresql.org/docs/current/ddl-constraints.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-indexes-ordering
    title: "PostgreSQL docs: Indexes Ordering"
    url: https://www.postgresql.org/docs/current/indexes-ordering.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: postgres-queries-table-expressions
    title: "PostgreSQL docs: Queries Table Expressions"
    url: https://www.postgresql.org/docs/current/queries-table-expressions.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація PostgreSQL."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L753-L902
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Вищий isolation level запобігає більше аномалій: Read Committed допускає non-repeatable read і phantom read, Repeatable Read усуває їх через snapshot, а Serializable усуває всі аномалії включаючи serialization anomaly.**[^postgres-indexes] Але сильніша ізоляція означає більше конфліктів: у Repeatable Read при конкурентному оновленні того ж рядка транзакція отримує помилку `could not serialize access due to concurrent update`, а в Serializable – `SQLSTATE 40001` при виявленні read/write dependencies. Application мусить перехоплювати ці помилки і повторювати транзакцію спочатку.

## Detailed explanation

Isolation level – це налаштування транзакції, яке визначає, наскільки конкурентні транзакції
ізольовані одна від одної і які аномалії читання вони можуть побачити.[^postgres-transaction-iso]

Read Committed – мінімальний практичний рівень: кожен запит бачить лише закомічені дані на момент
свого виконання, але два запити в межах однієї транзакції можуть побачити різні значення того
самого рядка (non-repeatable read) або нові рядки, що з'явилися між ними (phantom read). Repeatable
Read фіксує snapshot даних на момент початку транзакції, тому обидві аномалії зникають – кожен
запит у транзакції бачить той самий знімок. Serializable іде далі: він гарантує, що результат
конкурентного виконання транзакцій еквівалентний якомусь послідовному порядку їх виконання,
усуваючи навіть тонші аномалії на кшталт serialization anomaly, які Repeatable Read не ловить.

Ціна за сильнішу ізоляцію – конфлікти замість мовчазно неправильного результату. Замість того щоб
дозволити транзакції прочитати застарілі чи несумісні дані, база даних виявляє конфлікт і відхиляє
одну з транзакцій помилкою серіалізації, а не мовчки псує консистентність.

Приклад обробки помилки серіалізації в Repeatable Read чи Serializable:

```sql
-- application retries the whole transaction on a serialization failure
BEGIN;
-- ... reads and writes ...
COMMIT;
-- on error SQLSTATE 40001 ('could not serialize access due to concurrent update'):
-- roll back and re-run the same transaction from the start
```

**Типові помилки з isolation level:**
- обирати Serializable «про всяк випадок» без retry-логіки в application, через що частина запитів
  просто падає під навантаженням;
- плутати Repeatable Read зі «снапшотом на весь час з'єднання» – snapshot береться на початок
  транзакції, а не сесії;
- вважати, що вищий isolation level сам по собі усуває необхідність правильного дизайну запитів
  (наприклад, `SELECT ... FOR UPDATE` для явного блокування).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
