---
id: py-prac-0010
title: "Реалізуйте retry decorator з tuple transient exception types і `max_attempts`: він має зберегти metadata та re-raise останній exception з його traceback."
description: "Огорніть callable через functools.wraps і ловіть лише заданий exception tuple."
track: python
section: practical-coding
level: senior
type: coding
tags: [max-attempts]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-functools
  title: 'Python 3.13: Wrapper metadata'
  url: https://docs.python.org/3.13/library/functools.html#functools.wraps
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-raise
  title: 'Python 3.13: The raise statement'
  url: https://docs.python.org/3.13/reference/simple_stmts.html#the-raise-statement
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Реалізуйте `retry(max_attempts, exceptions)` для synchronous functions. Повторюйте лише задані transient exception types і повторно піднімайте остаточну помилку зі збереженням traceback.

## Constraints

- max_attempts включає початковий виклик і має бути додатним int, крім bool. exceptions – tuple із subclasses Exception; порожній tuple означає відсутність retries.
- Виклики мають допускати повторення; delay та backoff не включені.

## Short answer

**Огорніть callable через `functools.wraps` і ловіть лише заданий exception tuple.** Негайно повертайте результат success та використовуйте bare `raise` в остаточному handler. Перевіряйте число спроб до створення wrapper.

## Detailed explanation

Успішний результат зупиняє цикл, зокрема None. Non-transient failures обходять handler; bare raise зберігає active exception та frames його походження. Повторення side effects безпечне лише коли операція його підтримує. [^py313-functools] [^py313-raise]

## Examples

```python
assert retry(2, (OSError,))(lambda: 4)() == 4
```

## Solution

```python
from functools import wraps

def retry(max_attempts, exceptions):
    if type(max_attempts) is not int:
        raise TypeError("max_attempts must be int")
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    if not isinstance(exceptions, tuple) or any(
        not isinstance(t, type) or not issubclass(t, Exception) for t in exceptions
    ):
        raise TypeError("exceptions must be Exception subclasses")
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorate
```

## Complexity

Для не більш ніж a спроб overhead wrapper – O(a) за fixed exception tuple, плюс вартість викликів. Допоміжний loop state – O(1); пам’ять exception traceback залежить від call stack. [^py313-functools] [^py313-raise]

## Edge cases

Перевірте eventual success, вичерпані спроби, негайну non-transient failure, порожні exceptions та хибну конфігурацію.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

calls = []
@retry(3, (OSError,))
def flaky(value):
    """Return after two transient failures."""
    calls.append(value)
    if len(calls) < 3:
        raise OSError("temporary")
    return value
assert flaky(9) == 9 and calls == [9, 9, 9]
assert flaky.__name__ == "flaky" and flaky.__doc__
assert flaky.__wrapped__.__name__ == "flaky"
failure = OSError("permanent")
calls.clear()
def fail():
    calls.append(1)
    raise failure
with pytest.raises(OSError) as caught:
    retry(2, (OSError,))(fail)()
assert caught.value is failure and len(calls) == 2
frames = []
tb = caught.value.__traceback__
while tb:
    frames.append(tb.tb_frame.f_code.co_name)
    tb = tb.tb_next
assert "fail" in frames
calls.clear()
with pytest.raises(OSError):
    retry(3, (ValueError,))(fail)()
assert len(calls) == 1
calls.clear()
with pytest.raises(OSError):
    retry(3, ())(fail)()
assert len(calls) == 1
with pytest.raises(ValueError):
    retry(0, (OSError,))
for bad in ([OSError], (BaseException,), (1,)):
    with pytest.raises(TypeError):
        retry(1, bad)
assert retry(1, (OSError,))(lambda: None)() is None
```

## Evaluation guide

### Expected signals

Перевірте точне число викликів, metadata й оригінальні traceback frames. Не ловіть BaseException загалом.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як додати bounded backoff з injected sleep function?

## Sources

<!-- generated from frontmatter -->
