---
id: py-gil-0007
title: "Чому GIL не усуває race conditions у Python application code?"
description: "GIL гарантує атомарність окремої bytecode-інструкції, але складені операції (read-modify-write) складаються з кількох bytecode і можуть бути перервані між інструкціями."
track: python
section: concurrency-and-gil
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython with GIL"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L559-L688
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**GIL гарантує атомарність окремої bytecode-інструкції, але складені операції (read-modify-write) складаються з кількох bytecode і можуть бути перервані між інструкціями.**[^py314-library-threading] Наприклад, `x += 1` компілюється в три bytecode: `LOAD x`, `ADD 1`, `STORE x` – між ними GIL може бути передано іншому thread. Тому навіть у GIL-enabled build необхідні явні примітиви синхронізації (`threading.Lock`, `queue.Queue`).

## Detailed explanation

GIL часто сприймають як гарантію того, що «в Python threads безпечні за замовчуванням», але це
неточне спрощення. GIL гарантує лише те, що дві bytecode-інструкції ніколи не виконуються буквально
одночасно – він нічого не каже про те, що відбувається *між* інструкціями одного логічного
виразу.[^py314-library-threading]

Кожен вислів Python-коду, який виглядає як одна операція, компілятор перетворює на послідовність
окремих bytecode-інструкцій. GIL може бути передано іншому thread після *будь-якої* з них, а не
лише між вислівами. Тому «атомарність на рівні bytecode» не означає «атомарність на рівні рядка
коду».

```python
counter = 0

def increment():
    global counter
    counter += 1  # LOAD_FAST/GLOBAL, BINARY_ADD, STORE -- not one instruction
```

Приклад класичного read-modify-write: `counter += 1` виглядає як одна дія, але компілюється в
кілька bytecode – завантажити значення, додати одиницю, зберегти результат. Якщо два threads
одночасно виконують цей рядок, можливий сценарій: обидва читають старе значення до того, як хтось
із них встигне записати нове, і один інкремент губиться.

Ця проблема стосується не лише простих операторів. `list.append()` захищений внутрішньою
реалізацією й не переривається, а от послідовність на кшталт `if key not in dict: dict[key] = ...`
– це вже дві окремі операції, між якими GIL може перемкнути thread, і перевірка стає застарілою до
моменту запису (check-then-act race).

**Чому це саме application-код, а не сам GIL:**
- GIL захищає внутрішній стан CPython (reference counts, структури даних інтерпретатора) – це
  безпека реалізації, а не логіки програми;
- composite-операції на рівні Python-коду (read-modify-write, check-then-act) складаються з
  кількох незалежних кроків, і між ними GIL вільно перемикає threads;
- бібліотечні одно-bytecode операції справді атомарні (наприклад, `list.append(x)`), тому легко
  помилково поширити цю властивість на весь код.

Захист від такого race conditions – явна синхронізація: `threading.Lock` навколо critical section
або структури даних з atomic операціями (`queue.Queue`), незалежно від того, наскільки простим
виглядає код.[^py314-library-threading]

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
