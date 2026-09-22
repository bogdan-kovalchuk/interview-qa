---
id: py-objtypes-0014
title: "Чому `0.1 + 0.2 == 0.3` може бути `False` і як коректно порівнювати приблизні floating-point результати?"
description: "0.1 + 0.2 == 0.3 дає False, тому що float у Python зберігається як IEEE 754 binary64, і десяткові дроби 0.1 та 0.2 не мають точного двійкового представлення."
track: python
section: objects-and-types
level: middle
type: pitfall
tags: [0-1-0-2-0-3]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L401-L443
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`0.1 + 0.2 == 0.3` дає `False`, тому що `float` у Python зберігається як IEEE 754 binary64, і десяткові дроби 0.1 та 0.2 не мають точного двійкового представлення.**[^py314-reference-datamodel] Результат `0.1 + 0.2` дорівнює `0.30000000000000004`. Для коректного порівняння використовують `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)`, який перевіряє `abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`. <span class="warn">При порівнянні з нулем обов'язково вказуйте `abs_tol > 0`, інакше `rel_tol` не дасть результату.</span>

## Detailed explanation

Нерівність `0.1 + 0.2 == 0.3` виникає через те, що апаратні числа з рухомою комою формату IEEE 754 binary64 зберігають числа у двійковій системі числення, у якій дроби $1/10$ та $2/10$ перетворюються на нескінченні періодичні двійкові дроби.[^py314-library-stdtypes] Оскільки розрядна сітка мантиси обмежена 53 бітами (приблизно 15–17 значущих десяткових цифр), дріб обтинається та округлюється до найближчого двійкового значення. Число `0.1` зберігається як `0.10000000000000000555...`, а `0.2` – як `0.20000000000000001110...`. Їхня сума дає `0.30000000000000004440...`, тоді як літерал `0.3` округлюється до `0.29999999999999998889...`. Оператор `==` виконує точне побітове порівняння, тому результат дорівнює `False`.

Для коректного порівняння результатів обчислень із рухомою комою не слід застосовувати оператор `==`. Стандартна бібліотека надає функцію `math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)`, яка порівнює значення з урахуванням відносної (`rel_tol`) та абсолютної (`abs_tol`) похибки. Відносна похибка масштабується відповідно до величини операндів, що дозволяє порівнювати як дуже великі, так і звичайні числа без ручного перерахунку епсилона.

Особливою пасткою є порівняння значень із нулем. Формула `math.isclose` перевіряє умову `abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`. Якщо одне з чисел дорівнює `0.0`, член `rel_tol * max(abs(a), 0.0)` дорівнює `rel_tol * abs(a)`, що математично не може задовольнити нерівність при стандартному `rel_tol < 1.0`.[^py314-reference-datamodel] Тому при порівнянні з нулем або чисел, близьких до нуля, обов'язково вказують ненульовий `abs_tol`.

Приклад порівняння наближених значень та типової помилки з нульовим порогом:

```python
import math

a = 0.1 + 0.2
b = 0.3

print(a == b)         # False (exact bitwise inequality)
print(f"{a:.17f}")    # 0.30000000000000004
print(f"{b:.17f}")    # 0.29999999999999999

# Correct comparison with relative tolerance
print(math.isclose(a, b))  # True (rel_tol=1e-09 by default)

# Near-zero comparison pitfall: rel_tol alone always fails against 0.0
diff = 1e-11
print(math.isclose(diff, 0.0))                 # False (rel_tol * diff < diff)
print(math.isclose(diff, 0.0, abs_tol=1e-9))   # True (abs_tol handles zero bounds)
```

**Типові помилки та рекомендації:**
- пряме порівняння `==` або `!=`: ніколи не використовуйте для `float` після арифметичних операцій;
- ігнорування `abs_tol` біля нуля: виклик `math.isclose(val, 0.0)` без явного `abs_tol` завжди повертає `False` для будь-якого ненульового значення;
- використання `round()` для порівняння: `round(a, 2) == round(b, 2)` менш надійне через граничні ефекти округлення на стику розрядів;
- фінансові розрахунки: для грошових операцій використовуйте модуль `decimal`, де десяткові дроби зберігаються без похибок двійкового перетворення.

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
