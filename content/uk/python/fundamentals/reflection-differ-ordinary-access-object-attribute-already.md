---
id: py-fund-0009
title: "Чим reflection відрізняється від звичайного доступу до заздалегідь відомого атрибута об’єкта?"
description: "За звичайного доступу ім’я атрибута зафіксоване в коді, а reflection визначає або досліджує структуру об’єкта під час runtime."
track: python
section: fundamentals
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L394-L407
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**За звичайного доступу ім’я атрибута зафіксоване в коді, а reflection визначає або досліджує структуру об’єкта під час runtime.**[^py314-reference-executionmodel] Наприклад, `obj.run` звертається до відомого атрибута, тоді як `getattr(obj, name)` обирає його за runtime string, а `inspect` може досліджувати live objects. Reflection використовує звичайний attribute protocol, а не обходить його.

## Detailed explanation

Різниця не в механізмі, а в тому, звідки береться ім'я атрибута. `obj.run` і `getattr(obj, 'run')` –
це буквально одна й та сама операція: компілятор перетворює крапку на той самий пошук через
`__getattribute__`.[^py314-reference-datamodel] Reflection нічого не обходить і нічого не порушує.

Різниця в тому, що при звичайному доступі ім'я зафіксоване в коді на етапі написання, а при
reflection воно стає **значенням**: рядком, який можна прочитати з конфігурації, зібрати з частин або
отримати з іншого об'єкта.

Друга частина reflection – це не доступ, а **дослідження**: дізнатися, що взагалі є в об'єкта, які в
методу параметри, звідки він походить. Для цього є `dir()`, `type()`, `vars()` і модуль `inspect`.

```python
handler = obj.run                  # the name is fixed at write time
handler = getattr(obj, name)       # the name is a value, decided at run time

dir(obj)                           # what attributes exist at all
inspect.signature(obj.run)         # (self, timeout: int = 30) - introspection, not access
```

Практична ціна reflection – втрата статичних гарантій. Компілятор і аналізатори не знають, яке ім'я
буде обчислене, тому вони не попередять про друкарську помилку, не перейменують атрибут під час
рефакторингу і не покажуть, що метод узагалі викликається. Помилка виявиться в рантаймі, у момент
самого доступу.[^py314-reference-executionmodel]

**Де reflection доречний:**
- serialization і ORM: код має працювати з полями, яких він не знає на етапі написання;
- plugin API з фіксованим набором hook-імен, оголошеним у контракті;
- інструменти – відладчики, профайлери, тестові фреймворки, які за визначенням досліджують чужий
  код;
- фабрики, де відповідність «рядок конфігурації – реалізація» перевіряється через allowlist.

**Де це радше запах:**
- `getattr` з іменем, склеєним з рядків, замість словника;
- обхід `dir()` у пошуках методів «за префіксом» замість явного інтерфейсу;
- reflection у внутрішньому коді, де набір типів відомий і закритий.

Коротко: звичайний доступ – це «я знаю, що мені треба»; reflection – «я дізнаюся під час виконання,
що тут є». Обидва користуються тим самим протоколом, і другий платить за гнучкість
непомітністю.[^py314-faq-general]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
