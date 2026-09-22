---
id: py-objtypes-0015
title: "Коли `Decimal` доцільніший за `float` і яку проблему він не вирішує автоматично без правильної precision та rounding policy?"
description: "Decimal доцільний, коли потрібне точне десяткове представлення: фінансові розрахунки, грошові значення, збереження значущих нулів (1.30 + 1.20 = 2.50)."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [decimal, float]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L444-L497
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Decimal` доцільний, коли потрібне точне десяткове представлення: фінансові розрахунки, грошові значення, збереження значущих нулів (`1.30 + 1.20 = 2.50`).**[^py314-reference-datamodel] Він усуває помилки двійкового представлення (`Decimal('0.1') + Decimal('0.2') == Decimal('0.3')` – точно `True`), але не вирішує автоматично проблему round-off при недостатній precision: арифметичний контекст (`decimal.getcontext()`) має стандартну precision 28 знаків, і якщо результат перевищує цю точність, відбувається округлення відповідно до поточної rounding policy.

## Detailed explanation

Тип `Decimal` із модуля `decimal` реалізує десяткову арифметику з фіксованою та рухомою комою відповідно до стандарту IEEE 854/754-2008, що виключає похибки двійкового представлення, притаманні типу `float`.[^py314-library-stdtypes] На відміну від `float`, який зберігає числа в двійковій системі, `Decimal` працює безпосередньо з десятковими знаками. Це критично важливо у фінансових та бухгалтерських розрахунках, де такі значення, як `0.10` або `0.05`, мають бути абсолютно точними, а також там, де нормативні вимоги вимагають збереження значущих нулів після коми (наприклад, грошовий формат із фіксованою кількістю копійок чи центів).

Однак перехід на `Decimal` не позбавляє автоматично від похибок округлення (round-off error). Будь-який дріб, що не є скінченним у десятковій системі (наприклад, $1/3 = 0.3333...$), неможливо зберегти абсолютно точно в скінченній кількості цифр. Усі обчислення виконуються в межах активного арифметичного контексту (`decimal.getcontext()`), який задає граничну точність (за замовчуванням `prec=28`) та режим округлення (наприклад, банківське округлення `ROUND_HALF_EVEN`). Якщо операція генерує більше цифр, ніж дозволяє `prec`, хвіст відкидається або округлюється, тому вираз `(Decimal(1) / Decimal(3)) * Decimal(3)` дасть `0.999999...`, а не точно `1`.

Крім того, критичною помилкою залишається ініціалізація `Decimal` через `float`: виклик `Decimal(0.1)` копіює вже неточне двійкове наближення з пам'яті, зводячи нанівець переваги класу.[^py314-reference-datamodel] Для коректної роботи екземпляри завжди слід ініціалізувати рядками, цілими числами або через `Decimal.from_float()`, якщо джерелом навмисно є двійкове число.

Приклад правильної ініціалізації, проблеми періодичних дробів та налаштування округлення:

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# 1. Exact string initialization vs float conversion pitfall
d1 = Decimal("0.1")
d2 = Decimal("0.2")
print(d1 + d2 == Decimal("0.3"))  # True

d_float = Decimal(0.1)  # Pitfall: imports binary float inaccuracy
print(f"{d_float:.25s}")  # 0.1000000000000000055511...

# 2. Precision limit on non-terminating decimals (1/3 in base 10)
getcontext().prec = 6
third = Decimal(1) / Decimal(3)
print(third)                 # 0.333333 (truncated to prec=6)
print(third * Decimal(3))    # 0.999999 (round-off error still occurs)

# 3. Explicit monetary rounding via quantize
price = Decimal("19.995")
final_price = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(final_price)           # 20.00
```

**Практичні рекомендації та підводні камені:**
- обов'язкова ініціалізація з рядків: використовуйте `Decimal('0.1')`, а не `Decimal(0.1)`;
- контроль контексту: для розрахунків із підвищеною точністю налаштовуйте `getcontext().prec` або використовуйте локальний контекст `decimal.localcontext()`;
- явне округлення для бізнес-логіки: використовуйте метод `.quantize()` для явного приведення результату до потрібного експонента та правила округлення (наприклад, `ROUND_HALF_UP` або `ROUND_HALF_EVEN`);
- компроміс у швидкодії: обчислення з `Decimal` значно повільніші за апаратні двійкові операції з `float` та споживають більше пам'яті.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
