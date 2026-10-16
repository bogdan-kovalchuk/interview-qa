---
id: py-excpt-0016
title: "Як залогувати exception із traceback, не дублюючи його бездумно на кожному рівні call stack?"
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
  - source_id: py314-library-logging-logger-exception
    title: "Python 3.14: Library/logging"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.exception
  - source_id: py314-library-logging-logger-debug
    title: "Python 3.14: Library/logging"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.debug
  - source_id: py314-reference-simple-stmts-raise
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#raise
---

## Short answer

**Exception із traceback логують один раз – там, де його остаточно обробляють і більше не перекидають далі.** Це практика, а не правило модуля `logging`. Traceback записують через `logger.exception()` або `logger.error(..., exc_info=True)`.[^py314-library-logging-logger-exception][^py314-library-logging-logger-debug] Нижчі рівні, які лише додають контекст, можуть піднімати новий exception через `raise ... from exc`, що зберігає оригінал як `__cause__`.[^py314-reference-simple-stmts-raise] Логування на кожному рівні дає дублікати.

## Detailed explanation

Дублікати з’являються, бо `logger.exception()` додає інформацію про exception, що зараз обробляється, і кожен такий виклик пише окремий запис із traceback. Для `logger.error(..., exc_info=True)` правило те саме: якщо `exc_info` істинний і exception не передано явно, береться поточний exception з `sys.exc_info()`.[^py314-library-logging-logger-exception][^py314-library-logging-logger-debug] Тож якщо кожен рівень стека логує в своєму `except`, один збій з’являється в логах стільки разів, скільки рівнів його логували.

Правильне місце для логування – там, де exception перестає поширюватися: рівень, що відповів користувачу, повернув резервний результат або завершив процес. Нижчі рівні, які лише додають контекст, не логують, а піднімають новий exception з `from exc`. Це записує оригінал як `__cause__`, і коли exception ніхто не обробив, обидва виводяться разом.[^py314-reference-simple-stmts-raise] У прикладі `read_config()` нічого не логує, `load_settings()` додає контекст, а `main()` логує один раз:

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("app")

def read_config(path):
    with open(path) as f:               # no logging here: the caller decides
        return f.read()

def load_settings(path):
    try:
        text = read_config(path)
    except OSError as exc:
        raise RuntimeError(f"cannot load settings from {path}") from exc
    return text.split()

def main():
    try:
        load_settings("missing.cfg")
    except RuntimeError:
        logger.exception("startup failed")  # one record, with the whole chain
        # ERROR app: startup failed
        # Traceback: ... FileNotFoundError ... "The above exception was the direct cause ..."
        # RuntimeError: cannot load settings from missing.cfg

main()
```

Два уточнення. По-перше, `logger.exception()` призначений для обробника: документація вказує викликати його з exception handler.[^py314-library-logging-logger-exception] Поза `except` поточного exception немає, і в CPython 3.13 та 3.14 виводиться `NoneType: None`. По-друге, якщо нижчий рівень справді відновився і exception далі не піднімається, його варто записати один раз на тому рівні, де це сталося. Правило одне: логує той, хто зупинив поширення exception.

**Типові помилки:**
- викликати `logger.exception()` у кожному `except` на шляху викликів: один збій з’являється в логах кілька разів;
- логувати exception і піднімати його далі голим `raise`, а вище знову логувати: та сама історія з дублікатами;
- писати `logger.error(str(exc))` без `exc_info`: текст повідомлення є, але traceback втрачено.
