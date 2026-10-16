---
id: py-decor-0012
title: "Що станеться з decorated name, якщо decorator поверне `None` замість callable?"
track: python
section: decorators
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
---

## Short answer

**Ім’я decorated функції буде зв’язане з `None`.**[^py314-reference-compound-stmts-function-definitions] Декоратор `@decorator` приблизно еквівалентний `func = decorator(func)`: значення, яке він повертає, стає новим значенням імені. Якщо декоратор повертає `None` (явно або через відсутність `return`), то виклик `foo()` у CPython 3.13 і 3.14 підіймає `TypeError: 'NoneType' object is not callable`.

```python
def bad_decorator(func):
    return None

@bad_decorator
def foo():
    pass

print(type(foo), foo)  # <class 'NoneType'> None

foo()  # TypeError: 'NoneType' object is not callable
```

## Detailed explanation

Декоратор зазвичай є функцією, яка повертає іншу функцію, і застосовується через синтаксис `@`.[^py314-glossary-term-decorator] Застосування відбувається один раз, під час виконання `def` (definition time): декоратор викликається з об’єктом функції як єдиним аргументом, а значення, яке він повертає, Python прив’язує до імені функції замість самої функції.[^py314-reference-compound-stmts-function-definitions] Перевірки цього значення в момент визначення немає. Якщо декоратор повертає `None`, присвоєння проходить без помилки, і ім’я одразу вказує на `None`. Помилка з’являється при першому використанні імені: виклик дає `TypeError`, а доступ до атрибута, наприклад `foo.__name__`, дає `AttributeError` (у CPython 3.13 і 3.14).

Найчастіше так стається, коли декоратор створює wrapper, але забуває його повернути:

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')
        return func(*args, **kwargs)
    # forgot: return wrapper

@log_calls
def add(a, b):
    return a + b

print(add)            # None
print(callable(add))  # False
add(1, 2)             # TypeError: 'NoneType' object is not callable
```

Рядок `@log_calls` виконує `add = log_calls(add)`, тож `add` стає `None`. Оригінальну функцію через це ім’я вже не дістати. Відновити її можна лише тоді, коли на неї лишилося інше посилання, наприклад у змінній, яку декоратор зберіг раніше. Падіння видно там, де функцію викликають, а не там, де написано декоратор.

Повідомлення залежить від значення, яке повернув декоратор. Якщо він повертає, наприклад, число `42`, виклик дасть `TypeError: 'int' object is not callable`. Тому повідомлення `'NoneType' object is not callable` на декорованій функції зазвичай означає, що декоратор повернув `None` (явно або через відсутній `return`).

**Типові помилки:**
- очікувати, що помилка з’явиться під час `def`, а не під час першого виклику;
- забути `return wrapper` або `return func` у декораторі, який лише реєструє функцію;
- поставити `return` з відступом усередині `wrapper`, а не в тілі декоратора: тоді декоратор усе одно повертає `None`.
