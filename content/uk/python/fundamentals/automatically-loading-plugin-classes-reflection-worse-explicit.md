---
id: py-fund-0011
title: "Чому автоматичне завантаження plugin-класів через reflection може бути гіршим за явний registry, навіть якщо усуває ручну реєстрацію?"
description: "Автоматичне завантаження через reflection робить набір активних plugin-класів неявним, крихким до зміни імен і таким, що не має allowlist."
track: python
section: fundamentals
level: senior
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

**Автоматичне завантаження через reflection робить набір активних plugin-класів неявним, крихким до зміни імен і таким, що не має allowlist.**[^py314-reference-executionmodel] Reflection-сканування (динамічний `import` модулів пакета, пошук підкласів через `__subclasses__()` або `getattr`) залежить від конвенцій іменування, порядку import і може підхопити непередбачені класи – test doubles, deprecated aliases або сторонні типи. Явний registry (словник чи список) дає контрольований allowlist, зменшує import-time side effects і легко тестується, бо активний набір класів видно в коді, а не ховається за runtime-скануванням.

## Detailed explanation

Reflection-завантаження plugin-класів – це пошук реалізацій під час виконання: динамічний import
усіх модулів пакета, обхід `__subclasses__()` базового класу або `getattr` за зібраним іменем,
замість переліку класів у коді.

Проблема не в самій техніці, а в тому, що набір активних plugin-ів перестає бути записаним
де-небудь. Він стає функцією від того, які модулі виявилися імпортованими на момент сканування, а це
залежить від порядку import, від того, чи хтось випадково імпортував тестовий модуль, і від
конвенції іменування файлів.[^py314-reference-executionmodel]

Обхід `__subclasses__()` показує це найяскравіше: метод повертає **всі** підкласи, які на цей момент
існують у процесі, включно з тими, що створені в тестах, з deprecated aliases і з абстрактними
проміжними базами.[^py314-reference-datamodel] Список не має жодного фільтра, крім самого факту
успадкування.

Приклад, який показує, що саме потрапляє в такий «автоматичний» набір:

```python
class Plugin:
    ...

class RealPlugin(Plugin):
    ...

class DeprecatedAlias(Plugin):
    ...

# in tests/test_plugins.py, imported by the test runner:
class FakePlugin(Plugin):
    ...

Plugin.__subclasses__()  # [RealPlugin, DeprecatedAlias, FakePlugin] - the fake is in production
```

Явний registry вирішує це тим, що робить набір даними, а не наслідком. Словник `PLUGINS = {'csv':
CsvPlugin, 'json': JsonPlugin}` можна прочитати, продіфити в code review, покрити тестом і змінити,
не боячись, що щось підхопиться саме́.

Друга ціна reflection – import-time side effects. Щоб знайти класи, треба спершу імпортувати всі
модулі пакета, а тіло модуля в Python виконується під час import, тож будь-яке відкриття файлу чи
з'єднання на рівні модуля виконається просто через факт сканування.[^py314-reference-executionmodel]

**Що конкретно ламається при reflection-завантаженні:**
- перейменування класу або файлу тихо вимикає plugin, і жоден тест не падає, бо його просто немає в
  наборі;
- у набір потрапляють класи, яких там не мало бути: test doubles, застарілі aliases, чужі типи з
  імпортованих бібліотек;
- набір залежить від порядку import, тож він може відрізнятися між запуском застосунку і запуском
  тестів;
- статичні аналізатори й пошук по коду не бачать зв'язку, бо в коді немає жодної згадки конкретного
  класу.

Reflection лишається доречним там, де набір справді відкритий і не контролюється автором – наприклад
у entry points, які реєструють сторонні пакети. Там за allowlist відповідає механізм встановлення
пакетів, а не сканування простору імен.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
