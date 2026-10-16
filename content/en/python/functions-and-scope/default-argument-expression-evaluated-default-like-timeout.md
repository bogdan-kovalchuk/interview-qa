---
id: py-funcs-0007
title: "When is a default argument expression evaluated, and why might a default like `timeout=get_timeout()` fail to reflect later configuration changes?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
---

## Short answer

**The default expression is evaluated when the `def` statement runs, once per execution of `def`, not on every call to the function.**[^py314-reference-compound-stmts-function-definitions] The function keeps the already computed result. If `get_timeout()` returns, for example, `30` during the module import, then every later call without an argument receives `30`, even if the configuration has changed. To make the value match the current configuration, compute it in the function body.

## Detailed explanation

Default values are evaluated from left to right when the `def` statement runs. Python stores the result of the evaluation, not the expression itself, so `get_timeout()` in the signature is called once, when `def` runs, and later calls to `fetch(...)` without `timeout` use the stored number.[^py314-reference-compound-stmts-function-definitions]

In this example `get_timeout()` runs during `def`, and changing the environment after the import changes nothing:

```python
import os

def get_timeout():
    print('get_timeout() called')         # runs once, while def executes
    return int(os.environ.get('TIMEOUT', '30'))

def fetch(url, timeout=get_timeout()):   # the default is computed here
    return f'{url} timeout={timeout}'

os.environ['TIMEOUT'] = '60'             # configuration changes after the import
print(fetch('a'))                        # a timeout=30 (default computed earlier)
print(fetch('b'))                        # b timeout=30
print(fetch('c', timeout=5))             # c timeout=5 (explicit argument)
```

The same holds for any expression that depends on state at the time of `def`: `datetime.now()`, a file read at that moment, the current user. For a module, `def` runs during import. If `def` runs several times, for example in a factory function that creates new functions, the expression is evaluated on each such run.[^py314-reference-compound-stmts-function-definitions]

To make the value reflect the configuration at call time, use `None` as the default and compute the value in the function body:

```python
import os

def get_timeout():
    return int(os.environ.get('TIMEOUT', '30'))

def fetch(url, timeout=None):
    if timeout is None:
        timeout = get_timeout()          # evaluated on every call
    return f'{url} timeout={timeout}'

print(fetch('a'))                        # a timeout=30
os.environ['TIMEOUT'] = '60'
print(fetch('b'))                        # b timeout=60
```

The cost is one extra line. The signature shows `timeout=None`, and the real value is read at call time.

**Common mistakes:**
- assuming that `timeout=get_timeout()` is called on every call to `fetch`;
- changing the configuration after the import and expecting already defined default values to update;
- putting `datetime.now()` in a default and expecting the current time on every call.
