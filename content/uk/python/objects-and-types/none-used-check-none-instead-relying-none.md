---
id: py-objtypes-0002
title: "Чому для перевірки на `None` використовують `is None`, а не покладаються на `== None`?"
description: "None – це синглтон: у процесі існує лише один об'єкт None, тому коректна перевірка – за ідентичністю через is."
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [is-none]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L587-L609
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`None` – це синглтон: у процесі існує лише один об'єкт `None`, тому коректна перевірка – за ідентичністю через `is`.**[^py314-reference-datamodel] Оператор `is` не перевантажується і гарантує порівняння саме з цим єдиним об'єктом. Оператор `==` може бути перевантажений у довільному класі через `__eq__`, що дає хибний результат.

## Detailed explanation

У Python `None` є єдиним екземпляром вбудованого класу `NoneType` і представляє відсутність значення як синглтон.[^py314-reference-datamodel]

Оскільки протягом усього життєвого циклу процесу існує рівно один об'єкт `None`, вираз `val is None` порівнює покажчик змінної `val` безпосередньо з адресою цього синглтона. Ця операція на рівні байт-коду CPython транслюється у спеціальну оптимізовану інструкцію (`IS_OP`), яка виконується на рівні C-структур без виклику користувацьких методів.

Натомість вираз `val == None` викликає метод `val.__eq__(None)`. Будь-який користувацький клас або стороння бібліотека може реалізувати `__eq__` так, що він поверне `True` для об'єкта, який не є `None`, або викине виняток.[^py314-library-stdtypes] Ба більше, у деяких бібліотеках (наприклад, масивах або числових структурах) вираз `== None` повертає контейнер булевих значень, що при обчисленні умови `if val == None:` призводить до помилки.

Окрім надійності, перевірка через `is` захищає від небажаних обчислювальних витрат і гарантує однозначну семантику, визначену стандартом PEP 8.

Приклад, що демонструє різницю між `== None` та `is None`:

```python
class MisbehavingSentinel:
    def __eq__(self, other):
        # Flawed equality that claims match with everything
        return True

class FragileObject:
    def __eq__(self, other):
        # Some proxy objects or custom types reject direct equality
        raise TypeError("Direct equality comparison is unsupported")

sentinel = MisbehavingSentinel()
fragile = FragileObject()

# Equality invokes __eq__ and can produce false positives or errors:
print(sentinel == None)  # True: misleading result caused by custom __eq__
# fragile == None        # raises TypeError

# Identity check tests the memory address directly without calling __eq__:
print(sentinel is None)  # False: distinct object from the singleton
print(fragile is None)   # False: safe, fast, and never raises
```

**Практичні наслідки та типові помилки:**
- використання `val == None` у перевірках аргументів за замовчуванням: об'єкти з нестандартним `__eq__` помилково вважаються відсутніми;
- заміна `is None` на булеву перевірку `if not val:`: порожні контейнери (`[]`, `""`, `0`, `False`) оцінюються як хибні, що викликає приховані дефекти, коли `0` або порожній рядок є допустимими значеннями;
- зниження продуктивності: `val is None` – це швидка перевірка покажчика, тоді як `val == None` вимагає повного динамічного пошуку та виклику методу `__eq__`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
