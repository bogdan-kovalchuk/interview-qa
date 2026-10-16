---
id: py-testing-0016
title: "Коли property-based testing з generated examples і shrinking дає кращий пошук edge cases, ніж лише hand-picked examples?"
track: python
section: testing
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
  - source_id: hypothesis-api-reference
    title: "Hypothesis 6.169.0: API reference"
    url: https://hypothesis.readthedocs.io/en/latest/reference/api.html
  - source_id: hypothesis-tutorial-introduction
    title: "Hypothesis 6.169.0: Introduction to Hypothesis"
    url: https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html
---

## Short answer

**Hypothesis генерує для властивості багато вхідних прикладів (за замовчуванням 100) і зводить падаючий випадок до мінімального.**[^hypothesis-api-reference] Це корисно там, де простір вхідних даних великий, а властивість легко записати. На CPython 3.14 для властивості `split_fields(join_fields(fields)) == fields` Hypothesis знаходить `['']`, якого немає серед hand-picked прикладів на кшталт `['a', 'b']`.

## Detailed explanation

Hand-picked приклади перевіряють лише ті входи, які автор придумав. Property-based testing змінює підхід: ти описуєш властивість, яка має виконуватися для будь-якого входу з певної стратегії, а бібліотека генерує входи сама. У Hypothesis це `@given` зі стратегією; за замовчуванням тест виконується на 100 прикладах (`settings.max_examples`).[^hypothesis-api-reference] Генерація випадкова, тож знахідка ймовірна, але не гарантована в кожному запуску.[^hypothesis-tutorial-introduction] Перевага найбільша там, де простір входів великий, а граничні випадки неочевидні: автор рідко вгадує їх усі.

Приклад. Пара `join_fields` і `split_fields` має повертати той самий список. Автор додав guard для порожнього рядка, і цей guard зламав один випадок. Hand-picked тест проходить, а властивість падає:

```python
from hypothesis import given, strategies as st


def join_fields(fields: list[str]) -> str:
    return ",".join(fields)


def split_fields(line: str) -> list[str]:
    return line.split(",") if line else []   # BUG: [""] joins to "" and comes back as []


def test_hand_picked_example() -> None:
    assert split_fields(join_fields(["a", "b"])) == ["a", "b"]


@given(st.lists(st.text()))
def test_split_inverts_join(fields: list[str]) -> None:
    assert split_fields(join_fields(fields)) == fields
```

Hypothesis зводить падіння до мінімального входу: `fields=['']`. Один порожній рядок стає порожнім списком. Shrinking важливий тим, що розробник бачить найпростіший вхід, який ламає властивість, а не великий випадковий список.[^hypothesis-api-reference] Щоб зафіксувати цей випадок, над тестом ставлять `@example([''])`: explicit examples виконуються в окремій фазі, не зараховуються до `max_examples` і не shrink-аться.[^hypothesis-api-reference]

Property-based testing не замінює приклади з вимог. Він потребує властивості, яку можна записати. Якщо правильний результат відомий лише для конкретного входу, наприклад точні числа з бізнес-правил або очікуваний текст помилки, hand-picked приклад чесніший і читається краще. Слабка властивість, як-от `len(result) >= 0`, пройде для будь-якого коду, що повертає список. Властивість, яка повторює реалізацію, перевіряє лише те, що код узгоджений сам із собою.

**Типові помилки:**
- вважати, що property-based testing гарантовано знаходить усі edge cases: випадкова генерація дає ймовірність, а не гарантію;
- писати властивість, яка копіює реалізацію, замість незалежного інваріанта;
- залишати слабку властивість на кшталт `len(result) >= 0` і вважати, що вона щось перевіряє.
