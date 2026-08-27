---
id: cs-cmplx-0003
title: "Чому в Big O відкидають constants і lower-order terms, але вони все ще важливі для real input sizes?"
description: "Big O описує швидкість зростання при n -> нескінченність, коли домінантний член переважає над константами й доданками нижчого порядку."
track: cs
section: complexity-and-analysis
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
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L156-L161
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Big O описує швидкість зростання при n -> нескінченність, коли домінантний член переважає над константами й доданками нижчого порядку.**[^py314-library-collections] Наприклад, 3n² + 5n + 100 спрощується до O(n²), бо для великих n домінує квадратичний член. Однак для реальних скінченних input constant factor і доданки нижчого порядку визначають фактичний час виконання – алгоритм O(n²) з малою константою може випереджати O(n log n) на практичних значеннях n.

## Detailed explanation

Формальне означення f(n) = O(g(n)) означає, що існують константи c > 0 і n0, для яких f(n) <=
c*g(n) для всіх n >= n0. Ця нерівність навмисно ігнорує саме значення c: асимптотика описує клас
зростання, а не конкретний час виконання на конкретному процесорі. Тому 500n і n дають один клас
O(n), хоча різниця у 500 разів цілком реальна на будь-якому вході.

Причина, чому доданки нижчого порядку зникають, та сама: при n -> нескінченність відношення
нижчого доданка до домінантного прямує до нуля, тому він стає нехтовно малим порівняно з головним
членом. Але слово "нескінченність" тут – джерело помилки: для конкретного n = 1000 доданок 100n
може бути більшим за n², якщо квадратичний член має малий коефіцієнт, а константа 100 – ні.

На практиці це проявляється так: сортування вставками, O(n²), із дуже маленькою внутрішньою
константою (простий цикл без викликів функцій, добра локальність кешу) регулярно обганяє merge
sort, O(n log n), на масивах до кількох десятків чи сотень елементів – саме тому в реальних
реалізаціях (наприклад, `sort` у багатьох мовах) є поріг, нижче якого викликається insertion
sort. Big O гарантує лише, який алгоритм переможе асимптотично, коли n стане достатньо великим,
але не каже, наскільки великим має бути це n.

Тому в інтерв'ю й на практиці асимптотику варто читати як прогноз масштабування, а не як пряме
порівняння швидкості: вона відповідає на питання "у скільки разів зросте час, якщо вхід зросте
вдесятеро", а не на питання "який варіант швидший на моїх даних зараз". Для другого питання
потрібен профайлінг або бенчмарк на реальних розмірах input, а не аналіз складності.
[^py314-library-collections]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
