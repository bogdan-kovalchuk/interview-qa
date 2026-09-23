---
id: py-objtypes-0011
title: "Коли custom class має реалізувати `__copy__` або `__deepcopy__` замість довіри стандартній поведінці?"
description: "Власні __copy__/__deepcopy__ потрібні, коли стандартна поведінка порушує інваріанти класу: клас керує зовнішнім ресурсом або має shared state, який не слід копіювати (цикли deepcopy безпечно обробляє через memo)."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [copy, deepcopy]
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

**Власні `__copy__`/`__deepcopy__` потрібні, коли стандартна поведінка порушує інваріанти класу: клас керує зовнішнім ресурсом або має shared state, який не слід копіювати (цикли `deepcopy` безпечно обробляє через memo).**[^py314-reference-datamodel] За замовчуванням `copy.copy` створює новий об'єкт і копіює посилання на атрибути, а `copy.deepcopy` рекурсивно копіює все через `memo` dict. <span class="warn">Якщо клас містить, наприклад, кеш або logging handler, ці атрибути часто мають залишатися спільними між копіями – це контролюють саме через `__deepcopy__`.</span>

## Detailed explanation

Реалізація методів `__copy__` та `__deepcopy__` необхідна тоді, коли стандартний механізм модуля `copy` не може коректно відтворити стан об'єкта або порушує його інваріанти.[^py314-library-copy] За замовчуванням `copy.copy()` створює новий екземпляр того ж типу і копіює посилання на його атрибути, а `copy.deepcopy()` рекурсивно створює копії всіх знайдених складових об'єктів. Якщо об'єкт володіє системними дескрипторами (відкриті файли, мережеві sockets, thread locks) або взаємодіє зі спільними службами на кшталт connection pool чи logger, наївне копіювання призводить до помилок (наприклад, дублювання дескриптора або спроби серіалізації непідтримуваного об'єкта).[^py314-reference-datamodel]

Метод `__copy__(self)` викликається функцією `copy.copy()` без додаткових аргументів і має повернути новий екземпляр із shallow копіюванням потрібних полів. Метод `__deepcopy__(self, memo)` приймає словник `memo`, який запобігає зацикленню при наявності циклічних посилань. Усередині `__deepcopy__` розробник зобов'язаний зберегти створений екземпляр у `memo[id(self)]` перед рекурсивним копіюванням вкладених атрибутів, інакше циклічне посилання всередині структури призведе до `RecursionError`.

Крім того, власна реалізація дозволяє реалізувати вибіркове глибоке копіювання: клонувати стан даних, але зберегти спільні посилання на кеш, конфігурацію чи сервіси.

Приклад вибіркового копіювання стану із захистом від циклічних посилань через `memo`:

```python
import copy


class SessionData:
    def __init__(self, user_id: int, tags: list[str], shared_cache: dict):
        self.user_id = user_id
        self.tags = tags
        self.shared_cache = shared_cache  # should remain shared across copies

    def __copy__(self):
        # Shallow copy: duplicate list, keep shared cache reference
        return type(self)(self.user_id, list(self.tags), self.shared_cache)

    def __deepcopy__(self, memo):
        # Prevent infinite recursion on cyclic references
        if id(self) in memo:
            return memo[id(self)]
        new_instance = type(self)(self.user_id, [], self.shared_cache)
        memo[id(self)] = new_instance
        new_instance.tags = copy.deepcopy(self.tags, memo)
        return new_instance


cache = {"hits": 0}
s1 = SessionData(1, ["admin", "dev"], cache)
s2 = copy.deepcopy(s1)

s2.tags.append("tester")
s2.shared_cache["hits"] += 1

print(s1.tags)          # ['admin', 'dev'] (isolated copy)
print(s2.tags)          # ['admin', 'dev', 'tester']
print(s1.shared_cache)  # {'hits': 1} (shared reference preserved)
```

**Типові випадки застосування власних методів копіювання:**
- ізоляція зовнішніх дескрипторів: дублювання файлових дескрипторів через системні виклики (наприклад, `os.dup`) замість спільного володіння;
- збереження shared state: запобігання клонуванню синглтонів, кешів, пулів з'єднань або логерів;
- оптимізація швидкодії: пропуск копіювання тимчасових даних або кешованих результатів;
- уникнення `TypeError`: явна обробка об'єктів, які модуль `copy` не вміє копіювати за замовчуванням.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
