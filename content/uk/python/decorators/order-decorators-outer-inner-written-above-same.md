---
id: py-decor-0002
title: "У якому порядку застосовуються два decorators `@outer` і `@inner`, записані над однією функцією?"
description: "Decorators застосовуються знизу вгору: спочатку @inner, потім @outer, тобто еквівалент func = outer(inner(func))."
track: python
section: decorators
level: middle
type: mechanism
tags: [outer, inner]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L3-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Decorators застосовуються знизу вгору: спочатку `@inner`, потім `@outer`, тобто еквівалент `func = outer(inner(func))`.**[^py314-glossary-term-decorator] Кожний наступний decorator отримує результат попереднього.

```python
def outer(func):
    print('outer applied')
    return func

def inner(func):
    print('inner applied')
    return func

@outer
@inner
def hello(): pass
```

Вивід при визначенні: `inner applied`, потім `outer applied`.

## Detailed explanation

Застосування decorator – це виклик його функції одразу під час виконання `def` (definition time),
а не під час подальшого виклику декорованої функції. Python обробляє список decorators над однією
функцією знизу вгору: спочатку викликається той, що ближче до `def`, і лише його результат
передається наступному.[^py314-glossary-term-decorator]

Це прямий наслідок синтаксису: `@outer` `@inner` `def hello(): ...` – це скорочення для
`hello = outer(inner(hello))`, і Python обчислює вкладені виклики зсередини назовні, тобто
`inner(hello)` рахується першим.[^py314-reference-compound-stmts-function-definitions] Кожен
наступний decorator отримує вже обгорнуту функцію як аргумент, а не оригінал.

Порядок *застосування* (хто кого обгортає під час визначення) варто відрізняти від порядку
*виконання* під час виклику. Якщо кожен wrapper робить щось до і після виклику наступної функції, то
на виклику код `outer` спрацьовує першим (бо він зовнішній), потім код `inner`, потім оригінальна
функція, а після повернення – у зворотному порядку. Це той самий стек викликів, що й у звичайній
вкладеній функції, і саме тут найлегше сплутати «хто застосований першим» із «чий код виконається
першим».

Приклад, який показує різницю між порядком застосування і порядком виконання:

```python
def outer(func):
    def wrapper(*args, **kwargs):
        print('outer: before')
        result = func(*args, **kwargs)
        print('outer: after')
        return result
    return wrapper

def inner(func):
    def wrapper(*args, **kwargs):
        print('inner: before')
        result = func(*args, **kwargs)
        print('inner: after')
        return result
    return wrapper

@outer
@inner
def hello():
    print('hello')

hello()  # order: outer:before, inner:before, hello, inner:after, outer:after
```

**Типові помилки з порядком decorators:**
- вважати, що порядок написання не має значення, якщо decorators «просто щось логують»;
- плутати порядок застосування (знизу вгору, один раз при визначенні) з порядком виконання
  wrapper-коду (при кожному виклику, зовнішній першим);
- переставляти decorators під час рефакторингу без перевірки, чи не зламало це поведінку, яка
  залежала від того, хто кого обгортає.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
