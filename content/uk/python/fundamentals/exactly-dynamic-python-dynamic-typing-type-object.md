---
id: py-fund-0004
title: "Що саме є динамічним у dynamic typing Python: тип об’єкта чи зв’язок імені з об’єктом?"
description: "Динамічним є зв’язок імені з об’єктом, а не тип уже створеного об’єкта."
track: python
section: fundamentals
level: middle
type: mechanism
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

**Динамічним є зв’язок імені з об’єктом, а не тип уже створеного об’єкта.**[^py314-reference-executionmodel] Кожен об’єкт має власний незмінний type, але assignment може переприв’язати те саме ім’я до іншого об’єкта, зокрема іншого type. Тому «зміна типу змінної» на практиці означає нове binding імені.

## Detailed explanation

У Python ім'я і об'єкт – це різні речі. Об'єкт має identity, type і value, і його type незмінний від
створення до знищення. Ім'я – це запис у namespace, який вказує на об'єкт, і саме цей запис можна
переприв'язати.[^py314-reference-datamodel]

Тому фраза «змінна змінила тип» описує не те, що сталося. Сталося інше: assignment записав у той
самий namespace посилання на **інший** об'єкт, у якого свій власний type. Старий об'єкт не
змінювався і не перетворювався – він просто перестав бути доступним під цим іменем.

Це видно через `id()`, який показує identity об'єкта: після переприв'язування identity інша, тобто
перед нами інший об'єкт, а не той самий у новому вигляді.

```python
x = 1
print(type(x), id(x))    # <class 'int'>  140234...

x = "one"
print(type(x), id(x))    # <class 'str'>  140235...  - a different object entirely
```

Наслідок, який має практичне значення: усі імена, що вказували на старий об'єкт, продовжують вказувати
саме на нього. Переприв'язування одного імені не змінює інші.

```python
a = [1, 2]
b = a
a = "gone"     # rebinds only `a`
print(b)       # [1, 2] - `b` still refers to the original list
```

Це також пояснює, чому мутація і переприв'язування – різні операції: `a.append(3)` змінює **об'єкт**,
який бачать усі імена, а `a = [...]` змінює лише **ім'я**.

**Що саме динамічне, а що ні:**
- динамічне: зв'язок імені з об'єктом, і його можна змінювати скільки завгодно разів;
- динамічне: пошук атрибута й вибір операції, бо вони визначаються типом об'єкта в момент
  виконання;[^py314-reference-executionmodel]
- **не** динамічне: type уже створеного об'єкта – він фіксований і не змінюється;
- **не** динамічне: те, які операції доступні – це вирішує type поточного об'єкта, а не бажання
  коду.

Саме тому анотація `x: int` нічого не забороняє в рантаймі: вона описує намір для зовнішнього
аналізатора, а механіка binding лишається тією самою.[^py314-faq-general]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
