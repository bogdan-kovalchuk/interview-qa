---
id: py-testing-0017
title: "Чому 100% line coverage не доводить, що всі important behaviors та assertions перевірені?"
description: "Line coverage показує лише виконані рядки: він не бачить непройденої гілки `if` і тесту без assertions, тому 100% не доводить, що поведінку перевірено."
track: python
section: testing
level: middle
type: pitfall
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
  - source_id: coverage-branch
    title: "Coverage.py 7.16.2: Branch coverage measurement"
    url: https://coverage.readthedocs.io/en/latest/branch.html#branch-coverage-measurement
    accessed: 2026-10-13
    kind: official
    version: "7.16.2"
    applicability: "Офіційна документація coverage.py 7.16.2: statement coverage проти branch coverage, часткові гілки і прапорець --branch."
---

## Short answer

**Line coverage показує лише, які рядки виконались.**[^coverage-branch] Він не каже, чи перевірено правильну поведінку: тест без assertions або з `assert True` може виконати кожен рядок функції і дати 100% line coverage, а помилка лишиться непоміченою. Branch coverage показує, чи пройдено обидві гілки кожного `if`,[^coverage-branch] а mutation testing перевіряє, чи ловлять тести навмисно внесені зміни в коді.[^mutmut-docs]

## Detailed explanation

Coverage вимірює виконання, а не перевірку. Line (statement) coverage фіксує, які рядки були виконані під час тестів. Тест, який лише викликає функцію, виконує ті самі рядки, що й тест із правильним `assert`, тому для coverage вони не відрізняються.

Функція з умовною знижкою, файл `billing.py`:

```python
def apply_discount(price, is_member):
    if is_member:
        price = price * 0.9
    return price
```

І два тести, файл `test_billing.py`. Перший лише викликає функцію, другий перевіряє результат:

```python
from billing import apply_discount


def test_runs_without_checking() -> None:
    apply_discount(100, True)           # executes every line, checks nothing


def test_member_price() -> None:
    assert apply_discount(100, True) == 90
```

Якщо запустити тільки перший, `billing.py` матиме 100% line coverage, хоча жодного результату не перевірено. Але й повний набір має прогалину. Гілка – це можливий перехід між рядками. У `if is_member:` є два переходи: до рядка 3 і далі, мимо тіла, до рядка 4. Обидва тести викликають функцію з `is_member=True`, тож перехід мимо тіла ніколи не виконується. Line coverage цього не бачить, бо кожен рядок усе ж виконано. `coverage run --branch` позначає такий `if` як частково покритий (`2->4`) і через це знижує відсоток покриття.[^coverage-branch]

Mutation testing перевіряє інше: він вносить навмисну зміну (мутант) і дивиться, чи впаде тест. Мутант, якого тести не спіймали, «вижив». Якщо змінити `0.9` на `0.8`, тест без assertion це пропустить, а `assert ... == 90` спіймає. Мутант, що прибирає `if is_member:` і дає знижку всім, у цьому наборі тестів вижив: жоден тест не викликає гілку без знижки, і branch coverage показує ту саму прогалину.[^mutmut-docs]

Coverage сам не знає, яким має бути результат, тому 100% не доводить правильність. Практичний порядок такий: спершу assertions на результат і побічні ефекти, потім branch coverage для критичних `if`, і лише потім mutation testing для важливих модулів.

**Типові помилки:**
- вважати 100% line coverage ознакою того, що всі гілки й поведінка перевірені;
- писати тести без assertions «для покриття»;
- не помічати, що `if` без `else` потребує тесту з обома значеннями умови.

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
