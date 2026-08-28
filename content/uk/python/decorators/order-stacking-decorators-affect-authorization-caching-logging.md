---
id: py-decor-0009
title: "Як порядок stacking decorators впливає на authorization, caching і logging, якщо кожен wrapper може не викликати наступний?"
description: "Порядок визначає, який wrapper виконується першим (зовнішній = верхній decorator), і якщо він не викличе наступний – внутрішні decorator-и пропускаються."
track: python
section: decorators
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

**Порядок визначає, який wrapper виконується першим (зовнішній = верхній decorator), і якщо він не викличе наступний – внутрішні decorator-и пропускаються.**[^py314-glossary-term-decorator] Для authorization + caching + logging: authorization має бути найзовнішнішим, щоб відхилити запит до caching/logging. Якщо logging стоїть зовні authorization, то навіть відхилені запити логуються. Якщо caching зовні authorization – кешований результат може обійти перевірку прав. <span class="warn">Кожен wrapper, що не викликає `func(*args, **kwargs)`, фактично блокує весь ланцюжок нижче.</span>

## Detailed explanation

Stacking decorators над однією функцією створює ланцюжок wrapper-викликів: кожен wrapper вирішує,
чи викликати наступний у ланцюжку взагалі, і саме тому порядок написання decorators безпосередньо
впливає на поведінку системи, а не лише на естетику коду.[^py314-glossary-term-decorator]

Найзовнішній decorator (написаний першим над `def`) отримує керування першим при виклику і може
завершити обробку запиту, ніколи не викликавши внутрішні wrapper-и. Якщо такий wrapper не викликає
`func(*args, **kwargs)`, увесь ланцюжок нижче – включно з authorization, caching чи logging, які
мали б спрацювати пізніше – просто не виконується.

Для authorization + caching + logging порядок задає конкретні гарантії. Authorization зовні
означає, що жоден запит не дійде до caching чи logging без перевірки прав. Якщо caching стоїть
зовні authorization, кешований результат для одного user може віддатися іншому, чиї права ніколи не
перевірялися на цей виклик – це витік даних, а не просто зайва робота. Якщо logging стоїть зовні
authorization, у лог потрапляють і відхилені спроби, що для audit trail зазвичай бажано; але якщо
logging стоїть усередині authorization, відхилені запити взагалі не логуються, і слід атаки
губиться.

Приклад стеку, де порядок написання відповідає бажаній семантиці:

```python
def require_auth(func):
    def wrapper(request):
        if not request.user.is_authenticated:
            raise PermissionError('not authorized')
        return func(request)
    return wrapper

def cached(func):
    def wrapper(request):
        if request.path in _cache:
            return _cache[request.path]
        result = func(request)
        _cache[request.path] = result
        return result
    return wrapper

@require_auth
@cached
@logged
def handler(request):
    ...
```

**Практичний порядок і чому:**
- `authorization` – найзовнішній, бо без нього нічого нижче не повинно виконуватись;
- `caching` – одразу під authorization, щоб кеш ніколи не обходив перевірку прав;
- `logging` – найближче до функції, якщо потрібно логувати лише успішні виклики; зовні, якщо
  потрібен audit trail відхилених спроб теж;
- будь-яка зміна цього порядку – усвідомлене рішення про те, які запити бачить кожен шар, а не
  косметика.

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
