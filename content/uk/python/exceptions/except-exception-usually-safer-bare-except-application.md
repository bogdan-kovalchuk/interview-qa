---
id: py-excpt-0001
title: "Чому `except Exception` зазвичай безпечніший за bare `except` для application-level обробки?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-library-exceptions-exception-hierarchy
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#exception-hierarchy
  - source_id: py314-tutorial-errors-handling-exceptions
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html#handling-exceptions
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
---

## Short answer

**Bare `except` перехоплює всі `BaseException`, включно з `SystemExit` і `KeyboardInterrupt`, тоді як `except Exception` їх пропускає.**[^py314-library-exceptions-exception-hierarchy] Ці винятки сигналізують про вихід, переривання або закриття generator, а не про помилку обробки: `sys.exit()`, Ctrl-C і закриття generator через `close()`. Тому bare `except` може проковтнути запит на завершення, а `except Exception` дає йому дійти до верхнього рівня.[^py314-library-exceptions-exception-hierarchy]

## Detailed explanation

Bare `except:` – це обробник без виразу. Він має стояти останнім у списку обробників і перехоплює все, що піднімається в блоці `try`.[^py314-reference-compound-stmts-the-try-statement] У ієрархії винятків `BaseException` є коренем. Усі вбудовані винятки, крім `BaseExceptionGroup`, `GeneratorExit`, `KeyboardInterrupt` і `SystemExit`, походять від `Exception`, тобто від помилок програми, наприклад `ValueError` і `KeyError`. Ці чотири класи стоять поруч із `Exception`, а не під ним.[^py314-library-exceptions-exception-hierarchy]

Приклад показує, що `except Exception` не перехоплює запит на вихід:

```python
import sys

def run_job():
    sys.exit(3)                  # SystemExit: a request to stop, not a job failure

try:
    run_job()
except Exception as error:       # SystemExit is not an Exception, so it passes through
    print('job failed:', error)
print('not reached')             # the process exits with status 3 before this line
```

Якщо замінити `except Exception as error:` на bare `except:`, а print – на `print('job failed')`, програма надрукує `job failed` і продовжить виконання після блока (код завершення 0 замість 3): вихід буде проковтнуто.

`KeyboardInterrupt` навмисно успадковує `BaseException`, щоб звичайний код, який ловить `Exception`, його випадково не перехопив.[^py314-library-exceptions] `GeneratorExit` піднімається через `close()` і теж є `BaseException`, тож bare `except` усередині generator перехопить і його.[^py314-library-exceptions-exception-hierarchy] Якщо після такого перехоплення generator дасть значення через `yield`, `close()` викличе `RuntimeError`.[^py314-reference-expressions-generator-iterator-methods]

`except Exception` не означає «обробити все». Туторіал описує `Exception` як wildcard, який ловить майже все, і радить бути якомога конкретнішим щодо типів винятків.[^py314-tutorial-errors-handling-exceptions] Тому безпечніший підхід – вузький список очікуваних винятків, а широкий `except Exception` лишається на межі, де помилку логують або піднімають повторно, а не мовчки ковтають.

**Типові помилки:**
- писати bare `except:` «на всяк випадок» і ковтати `SystemExit` та `KeyboardInterrupt`;
- вважати, що `except Exception` ловить усе: він ловить майже все, але не `SystemExit`, `KeyboardInterrupt` і `GeneratorExit`;
- перехоплювати `Exception` і мовчки продовжувати, приховуючи помилки в коді.
