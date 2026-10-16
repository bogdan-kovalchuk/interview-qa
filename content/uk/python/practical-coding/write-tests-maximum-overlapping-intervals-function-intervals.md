---
id: py-prac-0024
title: "Складіть tests для maximum-overlapping-intervals function: інтервали closed `[start, end]`, тому start і end в одну мить вважаються overlapping."
track: python
section: practical-coding
sources:
  - source_id: py314-tutorial-controlflow-the-range-function
    title: "Python 3.14: Tutorial/control flow"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#the-range-function
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
---

## Short answer

**Ключовий boundary – closed intervals: дотичні `[1,5]` і `[5,10]` дають overlap == 2 у точці 5.** На відміну від `range(1, 5)`, який не містить 5,[^py314-tutorial-controlflow-the-range-function] closed-інтервал містить обидва кінці. Тести: повна вкладеність `[(1,10),(2,9),(3,8)] -> 3`; без перетину `[(1,3),(5,7)] -> 1`; порожній список -> 0; один інтервал -> 1; усі однакові `[(1,5)]*4 -> 4`; вироджений `[(3,3),(3,3)] -> 2`.

## Detailed explanation

Функція `max_overlap` приймає список closed-інтервалів `[start, end]` і повертає, скільки інтервалів найбільше мають спільну точку. Closed означає, що обидва кінці належать інтервалу. Тому `[1, 5]` і `[5, 10]` мають спільну точку 5, і їхній overlap дорівнює 2. Саме цей boundary треба тестувати першим, бо він легко ламається при неправильному порівнянні.

Вбудований `range` працює з іншою, half-open, моделлю: кінцева точка не входить у послідовність.[^py314-tutorial-controlflow-the-range-function] Якщо перенести цю модель на інтервали, `[1, 5]` і `[5, 10]` перестануть перетинатися, і функція поверне 1. Щоб цього не сталося, sweep-line алгоритм обробляє події з однаковою координатою так: старт раніше за кінець. Події зберігаються як кортежі `(координата, тип)`, а `events.sort()` сортує їх лексикографічно, тому `(5, 0)` (старт) іде перед `(5, 1)` (кінець).[^py314-reference-expressions-value-comparisons]

Нижче реалізація і два тести. Half-open варіант, у якому кінець обробляється раніше за старт, на тесті дотику дає `AssertionError: 1 != 2`, тому дотик треба перевіряти явно.

```python
import unittest


def max_overlap(intervals):
    # Closed intervals: at the same coordinate, starts are handled before ends.
    events = []
    for start, end in intervals:
        events.append((start, 0))  # 0 = start
        events.append((end, 1))    # 1 = end
    events.sort()
    best = current = 0
    for _, kind in events:
        if kind == 0:
            current += 1
            best = max(best, current)
        else:
            current -= 1
    return best


class TestMaxOverlap(unittest.TestCase):
    def test_touching_closed_intervals(self):
        # [1, 5] and [5, 10] both contain the point 5.
        self.assertEqual(max_overlap([(1, 5), (5, 10)]), 2)

    def test_degenerate_intervals(self):
        self.assertEqual(max_overlap([(3, 3), (3, 3)]), 2)


if __name__ == "__main__":
    unittest.main()
```

Вироджений випадок `[(3, 3), (3, 3)]` дає 2: обидва інтервали містять точку 3, тож тест перевіряє, що однакові start і end не скасовують одне одного. Порожній список дає 0, один інтервал – 1, а `[(1, 5)] * 4` – 4. Ці кейси перевіряють, що лічильник коректно росте і зменшується.

**Обмеження.** Фіксовані кейси не доводять коректність для всіх інтервалів. Для випадкових даних корисні еталонна реалізація на простішому алгоритмі або property-based тести.

**Типові помилки:**
- тестувати лише неперетинні та вкладені інтервали, а дотик пропускати;
- вважати, що `[1, 5]` і `[5, 10]` не перетинаються, бо `range(1, 5)` не містить 5;
- сортувати події без правила для однакової координати, від чого залежить відповідь.
