---
id: py-prac-0023
title: "Складіть tests для Two Sum API, який повертає indices першої пари в lexicographic order, не використовує element двічі і повертає `None` без solution."
description: "Tests перевіряють чотири властивості: сума пари дорівнює target, пара лексикографічно найменша, жоден індекс не використано двічі, None коли розв’язку немає."
track: python
section: practical-coding
level: middle
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: кортежі та інші послідовності порівнюються за першим елементом, що відрізняється."
  - source_id: py314-library-unittest-assertequal
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: assertEqual перевіряє рівність і падає, якщо значення не рівні."
---

## Short answer

**Тести перевіряють чотири властивості: сума пари дорівнює target, пара `(i, j)` з `i < j` лексикографічно найменша, жоден індекс не використано двічі, а без розв’язку повертається `None`.** Кортежі в Python порівнюються за першим елементом, що відрізняється.[^py314-reference-expressions-value-comparisons] Кейси: `[2,7,11,15], target=9 -> (0,1)`; `[3,2,4], target=6 -> (1,2)`, а не `(0,0)`; `[1,2,3], target=100 -> None`; порожній список, від’ємні числа, дублікати.

## Detailed explanation

Тести для `two_sum` перевіряють контракт функції, а не її поточну реалізацію. Контракт такий: функція повертає пару `(i, j)` з `i < j`, для якої `nums[i] + nums[j] == target`. Серед усіх таких пар вона повертає лексикографічно найменшу, а `None`, якщо пари немає. Кожен кейс перевіряє одну властивість, тож падіння тесту одразу вказує на порушене правило.

**Лексикографічний порядок** – найтонша вимога. Кортежі порівнюються за першим елементом, що відрізняється.[^py314-reference-expressions-value-comparisons] Тому `(0, 3)` менше за `(1, 2)`: перші елементи `0` і `1` різні, і вирішують саме вони. Для `[1, 2, 3, 4]` і `target=5` є дві пари з сумою 5: `(0, 3)` і `(1, 2)`. Правильна відповідь – `(0, 3)`. Реалізація з зовнішнім циклом за `j` знаходить `(1, 2)` першою, і тест з цим входом таку помилку виявляє.

**Повторне використання індексу.** Внутрішній цикл, що починається з `0`, дозволяє `j == i`. Для `[3, 2, 4]` і `target=6` пара `(0, 0)` дає `3 + 3 == 6`, хоча елемент використано двічі. Нижче помилкова реалізація і тест, який її ловить. Тест очікує `(1, 2)`, а `assertEqual` порівнює очікуване значення з результатом і падає, якщо вони не рівні.[^py314-library-unittest-assertequal]

```python
import unittest


def two_sum_reuse(nums, target):
    # Bug: j may equal i, so one element is used twice.
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


class TestTwoSum(unittest.TestCase):
    def test_element_not_reused(self):
        # Fails with: AssertionError: Tuples differ: (0, 0) != (1, 2)
        self.assertEqual(two_sum_reuse([3, 2, 4], 6), (1, 2))


if __name__ == "__main__":
    unittest.main()
```

Правильна реалізація починає внутрішній цикл з `i + 1`, тож `j` завжди більший за `i`.

**Крайні випадки.** Порожній список і список з одним елементом повертають `None`, бо пара має складатися з двох різних індексів. Від’ємні числа: `[-3, 4, 3, 90]` з `target=0` дає `(0, 2)`, тож тест не спирається на додатні значення. Дублікати: `[3, 3]` з `target=6` дає `(0, 1)`: два різні індекси з однаковим значенням – легальна пара.

**Обмеження.** Кілька фіксованих кейсів не доводять коректність для всіх входів. Для більших даних можна порівнювати функцію з простим перебором як еталоном або використати property-based тести. Еталон має бути очевидно правильним, інакше дві однакові помилки пройдуть перевірку разом.

**Типові помилки:**
- перевіряти лише `sum == target`, без порядку і без заборони повторного індексу;
- записувати очікуваний результат, не перерахувавши, яка пара лексикографічно найменша;
- не тестувати `None` і порожній вхід, тому реалізація, що викидає виняток замість `None`, лишиться непоміченою.

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
