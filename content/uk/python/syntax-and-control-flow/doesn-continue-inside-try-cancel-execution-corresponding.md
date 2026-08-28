---
id: py-syntax-0008
title: "Чому `continue` усередині `try` не скасовує виконання відповідного `finally` перед наступною ітерацією?"
description: "finally завжди виконується «на виході» з try, незалежно від того, чи вихід відбувається через return, break або continue."
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [continue]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`finally` завжди виконується «на виході» з `try`, незалежно від того, чи вихід відбувається через `return`, `break` або `continue`.**[^py314-reference-expressions] Коли `continue` виконується в `try`-блоці, Python спочатку виконує `finally`-клаузу, і лише потім переходить до наступної ітерації циклу. <span class="warn">Якщо `finally` сам виконує `return`, `break` або `continue`, це перезаписує збережену інструкцію з `try`.</span>

## Detailed explanation

`finally` – це не «блок, який виконується після `try`», а блок, який виконується **на будь-якому
виході** з `try`. Мова перелічує ці виходи явно: нормальне завершення, виняток, `return`, `break` і
`continue`.[^py314-reference-compound-stmts]

Тому `continue` не скасовує `finally`, а відкладає себе. Інтерпретатор запам'ятовує намір перейти до
наступної ітерації, виконує `finally`, і лише потім цей намір виконує. Те саме з `return`: значення
вже обчислене, але повернення станеться після `finally`.

```python
for i in range(3):
    try:
        if i == 1:
            continue
        print('body', i)
    finally:
        print('finally', i)

# body 0 / finally 0 / finally 1 / body 2 / finally 2
```

Видно, що для `i == 1` тіло не виконалося далі, а `finally` – виконався. Саме на цьому тримається
надійність звільнення ресурсів: жоден спосіб вийти з блоку не дозволяє його оминути.

Небезпечна частина починається, коли `finally` сам виконує `return`, `break` або `continue`.
Збережений намір із `try` тоді просто губиться – включно з винятком, який мав поширитися
далі.[^py314-reference-simple-stmts]

```python
def f():
    try:
        raise ValueError('lost')
    finally:
        return 'swallowed'    # the exception disappears silently

f()   # 'swallowed' - no traceback, no error
```

**Що з цього варто запам'ятати:**
- `finally` виконується перед тим, як `continue`, `break` чи `return` справді відбудуться;
- виняток, що летить крізь `try`, теж чекає на `finally` і лише потім поширюється далі;
- `return` у `finally` пригнічує і виняток, і будь-який попередній `return` – це майже завжди
  помилка, і лінтери на неї лаються;
- `break` і `continue` у `finally` роблять те саме з керуванням: перезаписують збережений намір.

Практичне правило: у `finally` пишуть тільки прибирання. Будь-яка інструкція, що змінює потік
керування, перетворює «гарантований блок» на місце, де гарантії губляться.

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
