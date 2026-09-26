---
id: py-decor-0004
title: "Чого `functools.wraps` не гарантує щодо фактичної call signature wrapper-функції?"
description: "functools.wraps копіює лише metadata-атрибути (__name__, __doc__, __qualname__, __annotations__, __type_params__) і встановлює __wrapped__, але не змінює реальні параметри wrapper-функції."
track: python
section: decorators
level: senior
type: mechanism
tags: [functools-wraps]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`functools.wraps` копіює лише metadata-атрибути (`__name__`, `__doc__`, `__qualname__`, `__annotations__`, `__type_params__`) і встановлює `__wrapped__`, але не змінює реальні параметри wrapper-функції.**[^py314-glossary-term-decorator] Wrapper залишається функцією з `(*args, **kwargs)`. `inspect.signature()` за замовчуванням переходить за `__wrapped__` і показує оригінальну сигнатуру, але фактичний callable приймає будь-які аргументи – тому помилки невідповідності параметрів виникають лише всередині wrapper-а або в обгорнутій функції.

## Detailed explanation

Декоратор `functools.wraps` виконує лише метадані-мутації через функцію `functools.update_wrapper`: він копіює атрибути `__name__`, `__doc__`, `__qualname__`, `__annotations__`, `__type_params__` та встановлює посилання `__wrapped__` на оригінальний об'єкт.[^py314-library-functools-functools-wraps] При цьому `functools.wraps` принципово не змінює ані об'єкт байткоду (`__code__`), ані фактичні правила зв'язування аргументів інтерпретатором: фізична сигнатура виклику залишається рівно такою, як її визначено в оголошенні `wrapper` (найчастіше `(*args, **kwargs)`).

Хоча функція `inspect.signature()` за замовчуванням розгортає ланцюжок `__wrapped__` (`follow_wrapped=True`) і демонструє сигнатуру оригінальної функції, на рівні віртуальної машини CPython це є зручною ілюзією.[^py314-reference-compound-stmts-function-definitions] Інтерпретатор під час входу у `wrapper` зв'язує параметри відповідно до його реального коду. Якщо користувач передасть недостатньо або забагато позиційних чи ключових аргументів, виклик не буде відхилений на межі `wrapper`. Будь-який код передобробки всередині `wrapper` (логування, відкриття транзакцій, блокування lock) почне виконуватися, і лише рядок `func(*args, **kwargs)` згенерує `TypeError`.

Крім того, `functools.wraps` не надає гарантій статичної типізації: системі типізації (mypy, pyright) недостатньо runtime-атрибутів для збереження типів параметрів. Без явного використання `typing.ParamSpec` і `typing.Concatenate` декорована функція в очах статичного аналізатора втрачає вихідну сигнатуру або зводиться до `Callable[..., Any]`.

Демонстрація розбіжності між реальною сигнатурою та значенням за посиланням `__wrapped__`:

```python
import inspect
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper entered before argument verification")
        return func(*args, **kwargs)
    return wrapper

@log_call
def multiply(x: int, y: int) -> int:
    return x * y

# inspect.signature follows __wrapped__ by default
print(inspect.signature(multiply))  # (x: int, y: int) -> int
print(inspect.signature(multiply, follow_wrapped=False))  # (*args, **kwargs)

# Calling with invalid arguments still executes the wrapper preamble
try:
    multiply()  # missing arguments: x and y
except TypeError as error:
    print(f"Caught expected error: {error}")
```

**Архітектурні компроміси та підводні камені:**
- Помилкове припущення про ранню валідацію: побічні ефекти у `wrapper` (наприклад, інкремент лічильника викликів або запит до зовнішнього сервісу) відбуваються навіть тоді, коли викликана функція впаде з `TypeError` через некоректні аргументи.
- Прихована поведінка у фреймворках ін'єкції залежностей (FastAPI, pytest): якщо фреймворк спирається на інспекцію параметрів або кастомний `__code__`, розбіжність між інспектованою та реальною сигнатурами може призвести до некоректної передачі параметрів.
- Для гарантованої перевірки аргументів до виконання тіла `wrapper` необхідно використовувати `inspect.signature(func).bind(*args, **kwargs)` вручну всередині `wrapper`.
- Для збереження сигнатури у статичних аналізаторах обов'язково використовувати `ParamSpec` замість покладання виключно на `functools.wraps`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
