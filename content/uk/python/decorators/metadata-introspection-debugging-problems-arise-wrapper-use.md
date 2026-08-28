---
id: py-decor-0003
title: "Які проблеми з metadata, introspection і debugging виникають, якщо wrapper не використовує `functools.wraps`?"
description: "Без functools.wraps декорована функція втрачає __name__, __doc__, __qualname__ та __annotations__ – замість них підставляються атрибути wrapper-функції."
track: python
section: decorators
level: middle
type: pitfall
tags: [functools-wraps]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L247-L278
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Без `functools.wraps` декорована функція втрачає `__name__`, `__doc__`, `__qualname__` та `__annotations__` – замість них підставляються атрибути wrapper-функції.**[^py314-glossary-term-decorator] Наприклад, `example.__name__` стане `'wrapper'`, а `__doc__` – `None`. Це ламає `help()`, stack traces показують неправильне ім'я, а інструменти на кшталт Sphinx генерують хибну документацію. Рішення – викликати `@functools.wraps(func)` на wrapper.

## Detailed explanation

Без `functools.wraps` wrapper-функція, яку decorator повертає замість оригіналу, стає новим
об'єктом з власними `__name__`, `__doc__`, `__qualname__`, `__module__` і `__annotations__`, і саме
ці порожні за замовчуванням атрибути бачить будь-який код, що звертається до декорованої
функції.[^py314-glossary-term-decorator]

Причина в тому, як `def wrapper(*args, **kwargs): ...` визначається всередині decorator: це нова
функція з нуля, і Python не копіює метадані замкненої функції автоматично. `functools.wraps(func)`
саме й виконує це копіювання – переносить перелічені атрибути з `func` на `wrapper`, а також додає
`wrapper.__wrapped__ = func` як посилання на оригінал.[^py314-library-functools-functools-wraps]

Без цього кроку introspection ламається одразу на кількох рівнях. `help(decorated)` показує
docstring (або її відсутність) від wrapper, а не від функції, яку насправді викликають.
`inspect.signature(decorated)` повертає узагальнений `(*args, **kwargs)` замість реальних
параметрів, тож інструменти статичного аналізу й автодоповнення в IDE не бачать справжню сигнатуру.
Автогенератори документації на кшталт Sphinx підставляють у сторінку неправильний опис функції.

Для debugging наслідок ще прикріший: stack trace, logging і профайлери показують ім'я `wrapper`
замість імені функції, яку кандидат насправді написав. Якщо decorator застосований до кількох
різних функцій, усі вони в traceback виглядають однаково, і зрозуміти, яка саме впала, стає
складніше без додаткового контексту.

Приклад decorator без `functools.wraps` і наслідок для introspection:

```python
def logged(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@logged
def greet(name):
    """Greet a person by name."""
    ...

print(greet.__name__)  # wrapper, not "greet"
print(greet.__doc__)   # None, not "Greet a person by name."
```

**Типові прояви без `functools.wraps`:**
- `__name__` і `__qualname__` показують `wrapper` замість справжнього імені функції;
- `__doc__` губиться, і `help()` виводить нерелевантну або порожню довідку;
- `__annotations__` зникають, тож type checkers й IDE не бачать сигнатуру оригіналу;
- `inspect.signature()` повертає `(*args, **kwargs)` замість реальних параметрів;
- traceback і логи показують `wrapper` як місце помилки, а не оригінальну функцію.

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
