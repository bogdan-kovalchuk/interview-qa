---
id: py-fund-0005
title: "Чому dynamic typing і strong typing не є протилежними характеристиками мови?"
description: "Dynamic typing описує момент визначення та перевірки type, а strong typing неформально описує суворість правил взаємодії між несумісними types."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L104-L137
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Dynamic typing описує момент визначення та перевірки type, а strong typing неформально описує суворість правил взаємодії між несумісними types.**[^py314-reference-executionmodel] У Python ім’я можна переприв’язувати до об’єктів різних types, але доступні операції все одно визначає type поточного об’єкта. Отже, ці характеристики відповідають на різні запитання й можуть співіснувати.

## Detailed explanation

Dynamic typing і strong typing – це відповіді на два різні запитання, тому вони не лежать на одній
осі й не можуть бути протилежними. Перше питання: **коли** відомий тип. Друге: **наскільки суворо**
мова ставиться до операцій між несумісними типами.

Dynamic typing означає, що тип пов'язаний з об'єктом, а не з іменем, і перевіряється в момент
виконання операції. Ім'я в Python – це просто посилання, і assignment може переприв'язати його до
об'єкта іншого типу, не порушивши нічого.[^py314-reference-executionmodel]

Strong typing – неформальний термін, і саме тому його часто плутають. Він означає, що мова не
виконує неявних перетворень між несумісними типами «щоб щось вийшло»: `1 + "1"` у Python – це
`TypeError`, а не `2` і не `"11"`.[^py314-reference-datamodel] У слабко типізованій мові той самий
вираз мовчки дав би результат.

Приклад, який показує обидві характеристики в одному фрагменті:

```python
x = 1
x = "one"        # dynamic: the name is rebound to an object of another type, no error

1 + "1"          # strong: TypeError, no implicit coercion between int and str
int("1") + 1     # 2 - conversion happens only when it is asked for explicitly
```

Перший рядок працює саме через dynamic typing, другий падає саме через strong typing. Обидва – про
Python, і жоден не суперечить іншому.

**Типові плутанини навколо цих термінів:**
- «динамічна означає слабка» – ні: Python динамічний і сильний, C статичний і відносно слабкий
  (неявні перетворення між числовими типами і вказівниками);
- «змінна змінила тип» – змінилося binding імені, а тип самого об'єкта незмінний від створення до
  знищення;
- «type hints роблять Python статично типізованим» – анотації не перевіряються під час виконання,
  вони існують для зовнішніх аналізаторів, і рантайм-семантика лишається динамічною;
- «strong typing – це формальний термін» – ні, формального означення немає, тому в суперечці корисно
  говорити про конкретну поведінку, а не про ярлик.

Практичний наслідок пари «динамічна плюс сильна» такий: помилка невідповідності типів у Python
знаходиться пізно (лише коли рядок виконається), але знаходиться голосно – винятком у місці
операції, а не тихим неправильним значенням, яке спливе через три шари
викликів.[^py314-faq-general]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
