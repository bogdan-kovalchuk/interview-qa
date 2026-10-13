---
id: py-excpt-0011
title: "Чому custom exception зазвичай має наслідувати `Exception`, а не `BaseException`?"
description: "Custom exception має наслідувати від Exception, щоб звичайний except Exception його перехоплював, не чіпаючи системних SystemExit, KeyboardInterrupt та GeneratorExit."
track: python
section: exceptions
level: middle
type: mechanism
tags: [exception, baseexception]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-exceptions
    title: "Python 3.14: Library/asyncio-exceptions"
    url: https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: CancelledError, його базовий клас BaseException з версії 3.8 і вимога піднімати його знову."
---

## Short answer

**Custom exception має наслідувати від `Exception`, щоб звичайний `except Exception` його перехоплював, не чіпаючи системних `SystemExit`, `KeyboardInterrupt` та `GeneratorExit`.**[^py314-library-exceptions] Ці три класи (плюс `BaseExceptionGroup`) наслідують безпосередньо від `BaseException`, оминаючи `Exception`.[^py314-library-exceptions] Якщо custom exception наслідувати від `BaseException`, стандартний `except Exception` його пропустить, а `except BaseException` перехопить і системні сигнали – що зазвичай небажано.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

Ієрархія built-in exceptions починається з `BaseException`. Від нього відгалужуються системні класи і `Exception`, і більшість помилок належить саме до `Exception`. Класи `SystemExit`, `KeyboardInterrupt`, `GeneratorExit` і `BaseExceptionGroup` наслідують безпосередньо від `BaseException`. Документація пояснює причину для `SystemExit`: він наслідує від `BaseException`, щоб код, який ловить `Exception`, його випадково не перехопив.[^py314-library-exceptions]

`except X` спрацьовує, коли виняток є екземпляром `X` або його підкласом.[^py314-reference-compound-stmts-the-try-statement] Тому `except Exception` ловить будь-який підклас `Exception`, але не `SystemExit` чи `KeyboardInterrupt`. Custom exception, що походить від `Exception`, автоматично потрапляє в категорію звичайних помилок, яку обробляє загальний обробник, а системні сигнали лишаються поза нею.

Наслідки видно на межі програми. Наприклад, цикл обробки задач часто має `except Exception`, який записує помилку і йде далі. Якщо помилка бібліотеки походить від `Exception`, цикл її бачить. Якщо від `BaseException`, вона пролітає повз обробник, і цикл завершується. Заміна обробника на `except BaseException` теж погана ідея: він ловить і `KeyboardInterrupt`, тож Ctrl+C можна проковтнути, якщо обробник продовжує роботу, і програма не зупиниться.

Винятком є сигнали керування, які загальний обробник не повинен поглинати. У стандартній бібліотеці це `asyncio.CancelledError`: з Python 3.8 він наслідує від `BaseException`, а не від `Exception`, і документація вимагає піднімати його знову майже в усіх ситуаціях.[^py314-library-asyncio-exceptions] Для власного винятку такого типу `BaseException` може бути обґрунтованим, але тоді це треба явно задокументувати для споживачів.

Приклад: `AppError` походить від `Exception`, `AppFatal` від `BaseException`. Вивід однаковий на CPython 3.13 і 3.14.

```python
class AppError(Exception):
    pass

class AppFatal(BaseException):
    pass

def run(exc_type):
    try:
        raise exc_type("boom")
    except Exception:
        return "caught by except Exception"
    except BaseException:
        return "caught only by except BaseException"

print(run(AppError))  # caught by except Exception
print(run(AppFatal))  # caught only by except BaseException
```

**Типові помилки:**
- наслідувати від `BaseException`, щоб «ловити все»: загальні обробники `except Exception` такі помилки пропускають;
- писати `except BaseException` і не піднімати виняток знову: так ковтаються `KeyboardInterrupt` і `SystemExit`;
- вважати, що `except Exception` ловить усе: системні класи лишаються поза ним.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
