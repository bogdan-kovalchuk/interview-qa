---
id: db-sqlq-0002
title: "Чому parameterized SQL query захищає від injection, а string formatting чи escaping вручну не є надійною заміною?"
description: "Parameterized query розділяє SQL-структуру та дані: драйвер БД надсилає запит із placeholder'ами, а значення передаються окремо, тому вони ніколи не інтерпретуються як SQL-код."
track: databases
section: sql-queries
level: middle
type: pitfall
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/sql.md#L853-L893
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Parameterized query розділяє SQL-структуру та дані: драйвер БД надсилає запит із placeholder'ами, а значення передаються окремо, тому вони ніколи не інтерпретуються як SQL-код.**[^postgres-indexes] При string formatting або ручному escaping завжди існують edge cases: різні кодування (наприклад, Unicode normalization), екранування лапок у різних контекстах, або помилки в логіці escaping можуть дозволити зловмиснику вставити виконуваний SQL. <span class="warn">Ніколи не конкатенуйте user input у SQL-рядок – завжди використовуйте parameterized queries або ORM з автоматичним екрануванням.</span>

## Detailed explanation

Parameterized query (prepared statement) – це виконання SQL, коли текст запиту з placeholder'ами
(`?` або `%s`, залежно від драйвера) передається окремо від значень, а значення прив'язуються до
запиту після його розбору базою даних.[^postgres-indexes]

База даних спочатку парсить та планує запит із placeholder'ами як фіксовану структуру, а потім
підставляє значення як типізовані дані на етапі виконання (bind). Оскільки значення ніколи не
проходять через SQL-парсер як текст, вони фізично не можуть змінити структуру запиту – зловмисний
рядок на кшталт `' OR '1'='1` залишається просто рядковим значенням, а не частиною SQL-синтаксису.

String formatting (наприклад, f-string або `%`) чи ручний escaping намагаються досягти того самого
результату іншим шляхом: екранувати спецсимволи так, щоб рядок не міг «вирватися» за межі літералу.
Проблема в тому, що правила екранування залежать від контексту (лапки, кодування, специфічні
діалекти SQL), і будь-яка забута умова – наприклад, multi-byte кодування, яке дозволяє «з'їсти»
символ екранування, або відсутність екранування у нетипових місцях (LIMIT, назва колонки) –
відкриває injection. Escaping-функція, написана вручну, майже завжди покриває лише ті випадки, які
автор запам'ятав.

Приклад різниці між вразливим і безпечним підходом:

```python
# vulnerable: user input becomes part of the SQL text
query = f"SELECT * FROM users WHERE name = '{name}'"
cursor.execute(query)

# safe: value is bound separately, never parsed as SQL
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```

**Типові помилки з захистом від SQL injection:**
- вважати, що black-list екранування спецсимволів (лапки, крапка з комою) покриває всі випадки;
- використовувати string formatting для «довірених» значень (наприклад, ID з іншої таблиці), які
  насправді походять від user input;
- будувати динамічний SQL (назви таблиць, колонок, `ORDER BY`) через конкатенацію, бо placeholder
  тут синтаксично неможливий, і забувати про allowlist для таких місць.

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
