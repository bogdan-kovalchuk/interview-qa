---
id: py-funcs-0023
title: "Чи змінюють type annotations runtime-семантику виклику звичайної Python-функції та чи перевіряє інтерпретатор типи аргументів автоматично?"
description: "Ні: самі по собі type annotations не змінюють runtime-семантику виклику, і інтерпретатор не перевіряє типи аргументів автоматично."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-annotations
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#annotations
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
---

## Short answer

**Ні: самі по собі type annotations не змінюють runtime-семантику виклику, і інтерпретатор не перевіряє типи аргументів автоматично.**[^py314-reference-compound-stmts-annotations] Анотації – це метадані, які зберігаються у функції й видні через `__annotations__`; вони не впливають на передавання аргументів чи перевірку під час виклику. Статичну перевірку виконують зовнішні інструменти, як-от mypy чи pyright.[^py314-library-typing] Перевірку під час виконання роблять окремі бібліотеки або власний код. <span class="warn">Поширена помилка:</span> очікувати автоматичну перевірку типів, як у статично типізованих мовах; у Python її немає.

## Detailed explanation

Перша частина відповіді – про те, що робить сам Python. Документація мови каже, що анотації зазвичай використовують для type hints, але мова їх не застосовує. Присутність анотацій не змінює runtime-семантику коду, окрім випадків, коли якийсь механізм сам читає анотації, як-от dataclasses чи `functools.singledispatch`.[^py314-reference-compound-stmts-annotations] Тож `a: int` – це запис у метаданих, а не перевірка значення, яке справді передали.

Симптом видно на короткому прикладі:

```python
def add(a: int, b: int) -> int:
    return a + b

def scale(value: int, factor: float) -> int:
    return value * factor

print(add("1", "2"))                 # 12, two str values pass without TypeError
print(scale(3, 1.5))                 # 4.5, the int return annotation is not checked
print(add.__annotations__)           # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

Функція виконує `+` над тим, що отримала. Для рядків `+` визначено (конкатенація), тому помилки немає. Інтерпретатор не порівнює значення з анотаціями: `scale` повертає `float`, хоча анотація обіцяє `int`. Ці результати однакові в Python 3.13 і 3.14; змінюється лише момент, коли обчислюються самі анотації.

Перевірку дають інші інструменти. Type checker читає анотації без запуску програми і може позначити такий виклик ще до виконання.[^py314-library-typing] Runtime-перевірку пишуть явно, наприклад через `isinstance`, або беруть з окремих бібліотек, але це вже власний код, а не функція мови.

**Типові помилки:**
- очікувати, що `a: int` відхилить рядок під час виклику: без type checker помилка з’явиться лише там, де операція впаде сама;
- вважати, що `-> int` гарантує тип результату: `scale(3, 1.5)` повертає `4.5`;
- будувати захист від некоректних типів лише на анотаціях: перевірку треба писати явно або брати з бібліотеки.

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
