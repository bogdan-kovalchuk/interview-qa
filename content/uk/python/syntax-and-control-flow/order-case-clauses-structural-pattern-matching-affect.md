---
id: py-syntax-0011
title: "Чому порядок `case` у structural pattern matching впливає на досяжність наступних patterns?"
description: "Case blocks у match/case перевіряються зверху вниз, і після першого успішного збігу виконується його блок, а решта case ігнорується."
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [case]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L164-L228
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Case blocks у `match/case` перевіряються зверху вниз, і після першого успішного збігу виконується його блок, а решта case ігнорується.**[^py314-reference-expressions] Тому ширший pattern (наприклад, capture variable або wildcard `_`) перед вужчим робить останній недосяжним – він ніколи не отримає керування. Irrefutable case block (наприклад, `case _:`) має стояти останнім, інакше наступні case blocks ніколи не спрацюють.

## Detailed explanation

`match` – це не таблиця переходів і не пошук найкращого збігу. Це послідовна перевірка зверху вниз:
перший pattern, який зіставився (і чий guard істинний), виконує свій блок, а решта не
розглядається.[^py314-reference-compound-stmts]

Тому порядок case – це логіка, а не оформлення. Ширший pattern, поставлений раніше, робить усі
вужчі за ним недосяжними: керування до них просто не дійде.

```python
match command:
    case [action, *rest]:        # matches ANY non-empty sequence
        generic(action, rest)
    case ['quit']:               # unreachable - the case above already matched
        do_quit()
```

Найгостріше це проявляється з irrefutable pattern – таким, що не може не зіставитися: голе ім'я
(`case value:`) або wildcard (`case _:`). Для них компілятор навіть не чекає рантайму: якщо такий
case стоїть не останнім, це `SyntaxError`.[^py314-reference-expressions]

```python
match value:
    case _:          # SyntaxError: wildcard makes remaining patterns unreachable
        default()
    case 42:
        answer()
```

Guard змінює картину, але не правило. `case x if x > 100:` не є irrefutable, бо guard може бути
хибним, тож такий case дозволено ставити перед іншими – і саме так пишуть діапазони, від вужчого до
ширшого.

**Як тримати порядок правильним:**
- специфічні літерали й точні структури – зверху, загальні форми – нижче;
- `case _:` – завжди останній, як `default` у switch;
- варіанти з guard упорядковувати від найвужчої умови до найширшої, бо перевіряються вони теж по
  черзі;
- якщо гілка виглядає мертвою, це майже завжди означає, що вище стоїть надто широкий pattern –
  зокрема capture з голим іменем, яке зіставляється з чим завгодно.

На відміну від `switch` у C, тут немає fallthrough: після виконання блоку `match` завершується, і
`break` не потрібен.[^py314-reference-simple-stmts]

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
