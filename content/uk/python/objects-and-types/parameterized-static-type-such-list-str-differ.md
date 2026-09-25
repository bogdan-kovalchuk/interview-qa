---
id: py-objtypes-0022
title: "Чим parameterized static type на кшталт `list[str]` відрізняється від runtime-перевірки вмісту конкретного списку?"
description: "list[str] – це статична анотація типу, яку type checker (mypy, pyright) перевіряє під час аналізу коду; Python у runtime не валідує вміст контейнера."
track: python
section: objects-and-types
level: senior
type: comparison
tags: [list-str]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`list[str]` – це статична анотація типу, яку type checker (mypy, pyright) перевіряє під час аналізу коду; Python у runtime не валідує вміст контейнера.**[^py314-reference-datamodel] Runtime-перевірка (наприклад `all(isinstance(x, str) for x in lst)`) виконується під час виконання програми й працює з реальними даними, а не з декларацією. У Python 3.14 parameterized generics на кшталт `list[str]` доступні як builtin subscription, але не вставляють жодних runtime-checkів у код.

## Detailed explanation

Параметризований тип `list[str]` існує виключно як статична декларація для інструментів статичного аналізу (mypy, pyright) та об'єкт метаданих у runtime, тоді як перевірка вмісту вимагає динамічного обходу структури даних під час виконання програми.[^py314-reference-datamodel]

Починаючи з PEP 585 у Python 3.9+, вираз `list[str]` створює об'єкт `types.GenericAlias` безпосередньо через підписку вбудованого класу `list`.[^py314-library-stdtypes] Проте інтерпретатор CPython ніколи не перевіряє типи елементів при додаванні в список чи передачі аргументів у функцію: операція `lst.append(123)` виконується без помилок, навіть якщо змінна анотована як `list[str]`. Спроба виконати `isinstance(lst, list[str])` викликає `TypeError: Parameterized generics cannot be used with class or instance checks`, оскільки Python навмисно відмовився від дорогої перевірки контейнерів на кожному кроці виконання.

Динамічна перевірка вмісту (наприклад, генераторний вираз `all(isinstance(x, str) for x in lst)`) працює з поточним станом списку в оперативній пам'яті й має часову складність $O(n)$. Якби інтерпретатор автоматично контролював типи елементів у mutable контейнерах, будь-яка мутація чи передача посилання коштувала б лінійного часу замість $O(1)$, руйнуючи модель продуктивності мови. Тому в архітектурі Python існує чіткий поділ відповідальності: статичні перевірки гарантують коректність контрактів на етапі CI/CD, а runtime-валідація (через Pydantic або явні цикли) застосовується виключно на ненадійних межах вводу-виводу (HTTP-запити, читання файлів, черги повідомлень).

Різниця між статичним GenericAlias та перевіркою вмісту у runtime:

```python
import types

# 1. Parameterized generic produces a GenericAlias object at runtime:
alias = list[str]
print(type(alias) is types.GenericAlias)  # True

# 2. Type annotations do not constrain runtime operations:
items: list[str] = ["alpha", "beta"]
items.append(42)  # CPython permits heterogeneous elements without runtime errors

# 3. Parameterized generics cannot be used in isinstance checks:
try:
    isinstance(items, list[str])
except TypeError as exc:
    print(exc)  # Parameterized generics cannot be used with class or instance checks

# 4. Validating contents at runtime requires an explicit O(n) scan:
valid = all(isinstance(item, str) for item in items)
print(valid)  # False
```

**Архітектурні компроміси та типові помилки:**
- використання `isinstance(data, list[str])` у коді, що призводить до падіння з `TypeError` у runtime;
- надмірна runtime-валідація вкладених колекцій у внутрішніх циклах, яка перетворює алгоритми зі складністю $O(1)$ на важкі $O(n)$ операції;
- очікування, що static type checker запобігатиме runtime-помилкам при отриманні некоректних даних з зовнішніх джерел (JSON, БД) без проміжної валідації;
- ігнорування того, що mutable список може бути змінений через інше посилання після проходження runtime-перевірки.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
