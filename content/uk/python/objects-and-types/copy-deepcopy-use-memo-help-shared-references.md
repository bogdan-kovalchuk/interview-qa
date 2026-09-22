---
id: py-objtypes-0010
title: "Чому `copy.deepcopy()` використовує memo і як це допомагає з shared references або cyclic structures?"
description: "Memo – це словник {id(оригінал): копія}, який запобігає нескінченній рекурсії для циклічних посилань і уникає дублювання спільних об'єктів."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [copy-deepcopy]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Memo – це словник `{id(оригінал): копія}`, який запобігає нескінченній рекурсії для циклічних посилань і уникає дублювання спільних об'єктів.**[^py314-reference-datamodel] Коли `deepcopy` зустрічає об'єкт, який вже скопійовано (є в memo), він повертає існуючу копію замість рекурсивного копіювання. Для циклічної структури `a = []; a.append(a)` це єдиний спосіб завершити копіювання без `RecursionError`, зберігаючи структуру спільних посилань у копії.

## Detailed explanation

Функція `copy.deepcopy()` використовує словник `memo` як таблицю відповідностей `{id(оригінал): копія}`, яка слугує механізмом мемоізації під час обходу довільного графа об'єктів.[^py314-library-copy]

Під час глибокого копіювання складних структур виникають дві фундаментальні проблеми: циклічні посилання (коли об'єкт прямо чи опосередковано посилається сам на себе) та спільні посилання (коли кілька вузлів посилаються на один і той самий екземпляр у пам'яті). Без збереження історії відвіданих об'єктів алгоритм опинився б у нескінченній рекурсії на циклах або створив би надлишкові дублікати для спільних об'єктів, зруйнувавши топологію вихідного графа.

Критично важливим є момент наповнення `memo`. Коли `deepcopy()` починає обробку контейнера, новий порожній об'єкт створюється і записується в `memo` під ключем `id(оригінал)` **до** того, як починається рекурсивне копіювання його вмісту.[^py314-reference-datamodel] Якщо якийсь із дочірніх елементів посилається назад на батьківський вузол, рекурсивний виклик знаходить уже наявну незавершену копію в `memo` і повертає посилання на неї, успішно замикаючи цикл без `RecursionError`.

Для структур без циклів `memo` гарантує збереження ідентичності (identity preservation). Якщо список містить дві змінні, що вказують на спільний об'єкт `[shared, shared]`, копія отримає два посилання на один новий об'єкт `[new_shared, new_shared]`. При реалізації власного методу `__deepcopy__(self, memo)` розробник зобов'язаний приймати словник `memo` і передавати його у всі вкладені виклики `copy.deepcopy()`.

Приклад, що ілюструє обробку циклів, збереження спільних посилань і протокол `__deepcopy__`:

```python
import copy

# 1. Cyclic structure handling without infinite recursion
cyclic = []
cyclic.append(cyclic)

copied_cyclic = copy.deepcopy(cyclic)
print(copied_cyclic is cyclic)           # False (brand new object)
print(copied_cyclic[0] is copied_cyclic)  # True (cycle preserved without RecursionError)

# 2. Shared reference topology preservation
shared = {"count": 0}
graph = [shared, shared]

copied_graph = copy.deepcopy(graph)
print(copied_graph[0] is copied_graph[1])  # True (shared identity maintained)

copied_graph[0]["count"] += 1
print(copied_graph[1]["count"])            # 1 (both references see mutation)

# 3. Custom class integration with memo
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        dup = Node(copy.deepcopy(self.value, memo))
        memo[id(self)] = dup
        dup.next = copy.deepcopy(self.next, memo)
        return dup
```

**Архітектурні особливості та типові помилки:**
- забувати передавати `memo` у вкладені виклики `copy.deepcopy()` всередині користувацького методу `__deepcopy__`, що ламає захист від циклів;
- у разі реалізації `__deepcopy__` не реєструвати новий об'єкт у `memo` перед рекурсивним копіюванням дочірніх атрибутів, викликаючи переповнення стека на циклічних посиланнях;
- можливість передати власний словник `memo` у виклик `copy.deepcopy(x, memo=custom_memo)`, наприклад, для заміни певних ресурсів (сокети, підключення до бази) на заглушки або збереження синглтонів;
- враховувати накладні витрати: `deepcopy` формує словник із тисячами записів, тому для великих дерев даних часто доцільніше реалізовувати спеціалізований метод копіювання без проміжного хешування адрес.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
