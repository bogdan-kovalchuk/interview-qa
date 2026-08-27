---
id: db-idxplan-0001
title: "Чому index може пришвидшити read query, але збільшити storage та write cost?"
description: "Індекс – це окрема структура даних (зазвичай B-дерево), що зберігає копії значень індексованих колонок разом із посиланнями на рядки таблиці."
track: databases
section: indexing-and-query-plans
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/infrastructure/database.md#L406-L463
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Індекс – це окрема структура даних (зазвичай B-дерево), що зберігає копії значень індексованих колонок разом із посиланнями на рядки таблиці.**[^postgres-indexes] При читанні індекс дозволяє знайти потрібні рядки за O(log n) замість повного сканування таблиці. Але кожен `INSERT`, `UPDATE` або `DELETE` мусить оновити всі відповідні індекси, що додає I/O та CPU. Крім того, індекси займають додаткове місце на диску пропорційно кількості індексованих колонок та рядків.

## Detailed explanation

Структурно B-дерево індексу зберігає впорядковані ключі в збалансованому дереві сторінок: кожен
внутрішній вузол містить діапазони, що ведуть до дочірніх сторінок, а листові вузли – самі
значення й вказівники на фізичне розташування рядка в таблиці. Висота такого дерева зростає
логарифмічно від кількості рядків, тому пошук за ключем – це, по суті, кілька читань сторінок
(зазвичай 2-4 навіть на мільйонах рядків), а не сканування всієї таблиці.[^postgres-indexes]

Вартість запису йде не лише від додавання нового ключа: коли листова сторінка індексу заповнена,
вставка спричиняє split сторінки – це заміна однієї операції запису на дві сторінки плюс
оновлення батьківського вузла, що каскадно може дійти до кореня. У PostgreSQL додається ще одна
ціна через MVCC: `UPDATE` створює нову версію рядка, і якщо оновлена колонка індексована,
кожен індекс на таблиці отримує додатковий запис на нову версію, тоді як стара версія лишається
в індексі до `VACUUM`. Тому кількість індексів на таблиці множить вартість кожного
`INSERT`/`UPDATE`.[^postgres-ddl-constraints]

Місце на диску зростає, бо індекс фізично дублює значення індексованих колонок (і, для
складеного індексу, усі його колонки) для кожного рядка таблиці – для широких колонок
(наприклад, `text`) чи багатоколонкових індексів це може становити суттєву частку розміру самої
таблиці, а іноді й перевищувати його.

Тому рішення про додавання індексу – завжди компроміс, залежний від співвідношення читання й
запису: таблиця з переважно `SELECT` і рідкісними записами виграє від додаткових індексів майже
без штрафу, тоді як таблиця з високою частотою `INSERT`/`UPDATE` платить за кожен зайвий індекс
відчутним сповільненням запису.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
