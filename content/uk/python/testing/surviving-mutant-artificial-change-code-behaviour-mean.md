---
id: py-testing-0019
title: "Що означає surviving mutant після штучної зміни behavior коду і як це виявляє слабкі assertions чи missing cases?"
description: "Surviving mutant – штучна зміна коду (мутант), після якої жоден тест не впав; це сигнал про можливу прогалину в тестах, а не доказ її наявності."
track: python
section: testing
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
  - source_id: mutmut-docs-workflow
    title: "mutmut documentation: Workflow"
    url: https://mutmut.readthedocs.io/en/latest/#workflow
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація mutmut, розділ Workflow: mutmut run, mutmut browse і написання тесту, який має вбити мутанта. Не визначає термін surviving mutant."
  - source_id: mutmut-docs-type-checker
    title: "mutmut documentation: Filter generated mutants with type checker"
    url: https://mutmut.readthedocs.io/en/latest/#filter-generated-mutants-with-type-checker
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація mutmut, розділ про фільтрацію мутантів: якщо тести не виявляють зміну, яку type checker міг би відхилити (наприклад, x: str = 'foo' на None), значення не перевірено належно. Не визначає термін surviving mutant."
---

## Short answer

**Surviving mutant – це штучна зміна коду (мутант, наприклад `>=` замінено на `>`), після якої жоден тест не впав.** Якщо тести не помічають таку зміну, зазвичай бракує assertion або граничного випадку, як `age == 18`. Не кожен survivor є прогалиною, бо мутант може не змінювати поведінку. `mutmut browse` показує мутантів, і для вибраного пишуть тест, який має його вбити.[^mutmut-docs-workflow]

## Detailed explanation

Mutation testing перевіряє не те, чи рядок виконався, а те, чи тести помічають зміну поведінки. Інструмент створює мутанта: копію коду з однією малою зміною (оператор, літерал, умова), яка лишається коректним Python. Мутант вважається **вбитим** (killed), якщо хоча б один тест упав, і **вижилим** (surviving), якщо жоден тест не впав. Вижилий мутант показує, що набір тестів не відрізняє змінену поведінку від оригінальної.

Розгляньмо функцію `is_adult`, де мутант замінює `>=` на `>`. Слабкий тест перевіряє лише `30` і `5`: оригінал і мутант дають однаковий результат на цих значеннях, тож мутант виживає, хоча рядок зі зміною виконується. Додавання граничного випадку `18` вбиває мутанта. Приклад запускає обидві перевірки:

```python
def is_adult(age):
    return age >= 18          # original code

def is_adult_mutant(age):
    return age > 18           # mutant: '>=' replaced by '>'

def weak_test(fn):
    assert fn(30) is True
    assert fn(5) is False

def stronger_test(fn):
    weak_test(fn)
    assert fn(18) is True     # boundary case

def survives(test, fn):
    try:
        test(fn)
    except AssertionError:
        return False          # a test failed: the mutant is killed
    return True               # no test failed: the mutant survives

print(survives(weak_test, is_adult_mutant))      # True: the mutant survives
print(survives(stronger_test, is_adult_mutant))  # False: the mutant is killed
```

Ця різниця та сама, що між покриттям і перевіркою: виконаний рядок ще не означає перевірену поведінку. Mutmut описує схожий випадок, коли зміну може відхилити type checker (наприклад, `x: str = 'foo'` на `x: str = None`): якщо тести її не виявляють, значення x недостатньо перевірене.[^mutmut-docs-type-checker] Тому survivor є приводом відкрити конкретний випадок і вирішити, чого бракує: assertion, граничного значення чи взагалі тесту.

Не кожен survivor є прогалиною. Зміна може не впливати на результат для жодного вхідного значення (наприклад, `x + 0` замість `x`); такого мутанта неможливо вбити, і його варто позначити, а не писати тест навмання. У робочому процесі mutmut мутантів переглядають через `mutmut browse`, для вибраного пишуть тест, який має його вбити, і перезапускають мутанта.[^mutmut-docs-workflow]

**Типові помилки:**
- вважати 100% покриття рядків доказом, що тести перевіряють поведінку;
- додавати тести, які лише викликають код, без перевірки результату чи граничних значень;
- писати тест на кожного survivor, не перевіривши, чи він еквівалентний оригіналу.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
