---
id: db-txiso-0001
title: "Після збою між debit і credit транзакція не має залишити partial transfer: яку ACID property це ілюструє і що application все ще має вирішити для retry?"
description: "Це властивість Atomicity (атомарність): транзакція виконується повністю або не виконується взагалі – у разі помилки відбувається відкат усіх змін."
track: databases
section: transactions-and-isolation
level: middle
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L652-L733
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Це властивість Atomicity (атомарність): транзакція виконується повністю або не виконується взагалі – у разі помилки відбувається відкат усіх змін.**[^postgres-indexes] Але application все одно має вирішити проблему retry: чи безпечно повторити операцію (ідемпотентність), як визначити, чи початкова транзакція закомітилася чи ні (наприклад, через network timeout), і як уникнути дублювання побічних ефектів (email, notification) при повторній спробі.

## Detailed explanation

Atomicity (атомарність) – це властивість ACID, яка гарантує, що транзакція виконується як єдина
неподільна операція: усі її зміни або застосовуються повністю, або жодна з них не застосовується.
[^postgres-transaction-iso]

Якщо збій (мережевий обрив, падіння процесу, помилка constraint) стається між debit і credit
операціями, база даних відкочує (rollback) усі зміни цієї транзакції, включно з тими, що вже
встигли виконатися локально в межах транзакції. Жоден проміжний стан – гроші списані з одного
рахунку, але ще не зараховані на інший – не залишається видимим для інших транзакцій.

Atomicity гарантує лише те, що сама база даних не залишить partial transfer. Вона нічого не каже
про клієнта, який ініціював транзакцію і не отримав підтвердження – через network timeout
неможливо однозначно визначити, чи транзакція закомітилася на сервері, чи відкотилася. Application
має самостійно вирішити, що робити в цій невизначеності.

**Що application має вирішити для безпечного retry:**
- чи операція ідемпотентна – чи safe повторити її кілька разів без подвійного списання (наприклад,
  через idempotency key);
- як перевірити фактичний стан після timeout – зробити read транзакції за відомим ідентифікатором
  замість сліпого повтору;
- як уникнути дублювання побічних ефектів (email-сповіщення, виклик зовнішнього платіжного
  шлюзу), які самі по собі не мають transactional гарантій.

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
