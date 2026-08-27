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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L65-L85
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Constraints декларують правила валідації безпосередньо в схемі БД, і СУБД застосовує їх автоматично при кожній операції `INSERT`/`UPDATE`/`DELETE`, незалежно від application code.**[^postgres-indexes] `PRIMARY KEY` гарантує унікальність і NOT NULL; `FOREIGN KEY` забезпечує referential integrity відносно значення в іншій таблиці; `UNIQUE` запобігає дублікатам; а `CHECK` валідує довільну Boolean-умову, наприклад `price > 0`. Це означає, що навіть якщо application code має баг або обходить валідацію, БД не допустить некоректних даних.

## Detailed explanation

Механічно кожен із цих constraints реалізується по-різному, хоча мета спільна – заборонити
невалідний стан ще до того, як він потрапить у таблицю. `PRIMARY KEY` – це синтаксичний цукор
над `UNIQUE` індексом плюс `NOT NULL` на тих самих колонках: СУБД будує B-дерево індексу на
ключі й при кожному `INSERT`/`UPDATE` перевіряє через цей індекс, чи вже існує такий ключ,
перш ніж дозволити операцію – тобто перевірка унікальності сама коштує O(log n), а не
O(n).[^postgres-indexes]

`FOREIGN KEY` під час запису виконує пошук у батьківській таблиці: перш ніж вставити чи оновити
рядок із посиланням, СУБД перевіряє індекс первинного (чи унікального) ключа батьківської
таблиці на існування відповідного значення, а при видаленні чи оновленні батьківського рядка –
застосовує визначену дію (`RESTRICT`, `CASCADE`, `SET NULL`). Без індексу на стороні батьківської
таблиці ця перевірка була б O(n) на кожен запис, тому FK практично завжди спирається на
існуючий унікальний індекс.[^postgres-ddl-constraints]

`UNIQUE` – це той самий механізм, що й унікальна частина `PRIMARY KEY`, але без вимоги
`NOT NULL`; кілька `NULL` значень в унікальній колонці не конфліктують одне з одним, бо `NULL`
за визначенням не дорівнює `NULL`.

`CHECK` відрізняється принципово: це не індекс, а булевий вираз, який СУБД обчислює для кожного
рядка окремо на момент запису, порівнюючи лише значення в межах того самого рядка (`price > 0`,
`end_date > start_date`) – він не може посилатися на інші рядки чи інші таблиці, на відміну
від FK.

Спільна риса всіх чотирьох – момент застосування: перевірка відбувається в тій самій
транзакції, що й сама операція запису, і при порушенні транзакція відкочується, тому неможливо
закомітити дані, які порушують constraint, навіть якщо через паралельний баг у application code
валідацію було пропущено.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
