---
id: py-testing-0008
title: "Коли parametrization краща за копіювання одного test body для кількох cases?"
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
  - source_id: pytest-how-to-parametrize
    title: "pytest documentation: @pytest.mark.parametrize"
    url: https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
  - source_id: pytest-ref-param
    title: "pytest documentation: pytest.param"
    url: https://docs.pytest.org/en/stable/reference/reference.html#pytest.param
---

## Short answer

**Parametrization краща, коли тестова логіка однакова, а відрізняються лише вхідні дані та очікуваний результат.**[^pytest-how-to-parametrize] `@pytest.mark.parametrize` запускає один body для кожного набору значень, а `pytest.param(..., id="empty_input")` дає набору читабельний ID, як `test_parse[empty_input]`.[^pytest-ref-param] Копіювання body дублює логіку: зміна перевірки вимагає правки в кожній копії. <span class="warn">Якщо логіка різна для cases, окремі тест-функції зазвичай читаються краще, бо спільний body починає обростати умовами.</span>

## Detailed explanation

`@pytest.mark.parametrize` запускає одне тіло тесту для кожного набору значень. Pytest створює окремий test item на кожен набір, і кожен звітується окремо.[^pytest-how-to-parametrize] Це доречно, коли логіка однакова, а відрізняються вхідні дані й очікуваний результат: тоді перевірку змінюють в одному місці.

Копіювання body теж дає окремі тести, але кожна копія – окрема функція з власним дублікатом логіки. Нічого не гарантує, що копії лишаться синхронними, а назви функцій доводиться вигадувати вручну. Parametrize будує ID зі значень або з `pytest.param(..., id=...)`.[^pytest-ref-param] Без явного `id` ID складається зі значень, наприклад `test_eval[6*9-42]` у прикладі документації.[^pytest-how-to-parametrize]

Приклад: одна функція перевірки і три набори з читабельними ID:

```python
import pytest


def parse_port(text):
    return int(text.strip())


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param("8080", 8080, id="typical_port"),
        pytest.param(" 1 ", 1, id="min_port_with_spaces"),
        pytest.param("65535", 65535, id="max_port"),
    ],
)
def test_parse_port(text, expected):
    assert parse_port(text) == expected
```

`pytest -v` показує `test_parse_port[typical_port]`, `test_parse_port[min_port_with_spaces]` і `test_parse_port[max_port]`, тож падіння одразу видно з назвою випадку.

Межі застосування: коли набори потребують різного setup, різних перевірок або різних mock, спільне тіло починає обростати `if` за параметрами, і окремі тест-функції читаються краще. Значення параметрів передаються як є, без копіювання: якщо той самий mutable-об’єкт стоїть у кількох наборах, зміна, зроблена в одному тесті, буде видна наступним.[^pytest-how-to-parametrize]

**Типові помилки:**
- параметризувати тести з різною логікою, через що тіло тесту заповнюється умовами за випадком;
- залишати ID за замовчуванням для складних значень, через що в звіті не видно, який випадок упав;
- ставити той самий mutable-об’єкт у кількох наборах parametrize, який тест змінює, і отримувати залежність між випадками.
