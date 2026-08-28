---
id: py-fund-0002
title: "Чому поділ мов лише на «compiled» та «interpreted» некоректно описує Python?"
description: "Compilation та interpretation описують різні етапи виконання, тому не є взаємовиключними ярликами мови."
track: python
section: fundamentals
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
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L38-L67
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Compilation та interpretation описують різні етапи виконання, тому не є взаємовиключними ярликами мови.**[^py314-reference-executionmodel] Наприклад, CPython компілює source code у bytecode, після чого інтерпретатор виконує цей bytecode. Інша реалізація Python може застосовувати JIT або інше внутрішнє представлення, не змінюючи основну семантику мови.

## Detailed explanation

Compilation і interpretation – це властивості **реалізації**, а не мови. Компіляція означає переклад
коду з однієї форми в іншу перед виконанням; інтерпретація означає виконання коду в певному
представленні. Мова визначає лише семантику, а не спосіб, у який хтось її виконує.

Тому питання «Python – компільований чи інтерпретований?» поставлене неправильно. Правильне
питання – про конкретну реалізацію. CPython робить **обидві** речі: компілює вихідний код у bytecode,
а потім інтерпретує цей bytecode у циклі віртуальної машини.[^py314-reference-executionmodel]

```python
# CPython does both steps, in this order:
source.py  ->  parse  ->  AST  ->  compile  ->  code object (bytecode)
                                                     |
                                                     v
                                        the VM interprets the bytecode
```

Інші реалізації розкладають ті самі етапи інакше. PyPy інтерпретує bytecode, а гарячі ділянки
компілює в машинний код під час виконання (JIT). Cython транслює підмножину Python у C, який далі
компілюється звичайним компілятором. Жодна з них не змінює семантику мови – змінюється лише шлях до
виконання.

Та сама плутанина існує і в інших мов. Java компілюється в bytecode, який виконує JVM, часто з JIT.
JavaScript у сучасних рушіях компілюється в машинний код, хоч історично його звали інтерпретованим. C
зазвичай компілюють, але існують і інтерпретатори C.

**Що насправді варто розрізняти замість ярликів:**
- **у що** транслюється код: у bytecode, у машинний код, у код іншої мови;
- **коли** це відбувається: заздалегідь (AOT), під час першого запуску, чи на гарячому шляху (JIT);
- **що виконує результат**: процесор напряму чи віртуальна машина;
- **що з цього гарантує мова**: у випадку Python – нічого з переліченого, це все деталі
  реалізації.[^py314-faq-general]

Практичний наслідок: твердження «Python повільний, бо інтерпретований» некоректне вже за побудовою.
Швидкість визначає конкретна реалізація і навантаження, а не ярлик; той самий код на PyPy може бути
в рази швидшим без жодної зміни в
source.[^py314-reference-datamodel]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
