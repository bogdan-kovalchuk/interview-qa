---
id: py-fund-0010
title: "Коли monkey patching може бути виправданим і які ризики воно створює для локальності змін, тестів та оновлення залежностей?"
description: "Monkey patching виправданий переважно як короткоживуча, контрольована підміна в тесті або вузький compatibility workaround, коли dependency injection недоступний."
track: python
section: fundamentals
level: middle
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L300-L331
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Monkey patching виправданий переважно як короткоживуча, контрольована підміна в тесті або вузький compatibility workaround, коли dependency injection недоступний.**[^py314-reference-executionmodel] Він приховує залежності, змінює shared state, може зробити тести order-dependent і зламатися після оновлення dependency. У тестах краще застосовувати scoped `unittest.mock.patch()` у правильному namespace, щоб підміна гарантовано скасовувалася.

## Detailed explanation

Monkey patching – це заміна атрибута вже існуючого модуля, класу або об'єкта під час виконання.
Оскільки клас у Python – теж об'єкт зі змінюваним `__dict__`, присвоєння `SomeClass.method = other`
працює завжди й миттєво впливає на весь процес.[^py314-reference-datamodel]

Ціна – саме в цьому «на весь процес». Патч не має області видимості: він не обмежений модулем, який
його зробив, не скасовується сам і не видно в тому коді, поведінку якого змінює. Читач функції, яка
викликає `requests.get`, не має жодного натяку, що десь у conftest її підмінили.

Патчити треба саме клас, а не екземпляр – і це найчастіша помилка. Функція, присвоєна атрибуту
екземпляра, не стає bound method: протокол дескриптора спрацьовує лише для атрибутів класу, тож
`self` не передасться.[^py314-reference-datamodel]

```python
class Service:
    def fetch(self):
        return 'real'

def fake(self):
    return 'patched'

Service.fetch = fake          # correct: descriptor protocol binds `self`
Service().fetch()             # 'patched'

obj = Service()
obj.fetch = fake              # wrong: an instance attribute, not a bound method
obj.fetch()                   # TypeError: fake() missing 1 required positional argument
```

У тестах правильний інструмент – `unittest.mock.patch()`, бо він скасовує підміну на виході з
context manager або декоратора. Патчити треба там, **де ім'я шукається**, а не там, де воно
визначене: якщо модуль зробив `from x import get`, підміняти треба `mymodule.get`, а не `x.get`.

**Коли monkey patching виправданий:**
- у тесті, через scoped `patch()`, з гарантованим відкотом;
- як вузький workaround несумісності в сторонній бібліотеці, доки не вийде виправлення – з
  коментарем, посиланням на issue і планом видалення;
- для інструментації (профайлер, трасування), яка свідомо втручається в чужий код.

**Чому це погано як архітектурне рішення:**
- залежність стає невидимою: у сигнатурах і імпортах її немає;
- тести стають order-dependent, якщо патч не скасовано – результат залежить від порядку запуску;
- оновлення бібліотеки може тихо зламати патч, бо він спирається на приватну деталь;
- два патчі одного атрибута конфліктують мовчки, виграє останній.

Там, де вибір є, dependency injection дає той самий результат явно: залежність передається
аргументом, видима в сигнатурі й підмінюється без глобального стану.[^py314-reference-executionmodel]

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
