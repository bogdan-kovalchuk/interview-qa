---
id: py-stdlib-0015
title: "Why should library code log through a named logger instead of configuring the root logger on import?"
track: python
section: standard-library
sources:
  - source_id: py314-library-logger-hierarchy
    title: "Python 3.14: Library/logging, Logger Objects"
    url: https://docs.python.org/3.14/library/logging.html#logger-objects
  - source_id: py314-library-logging-logger-propagate
    title: "Python 3.14: Library/logging, Logger.propagate"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.propagate
  - source_id: py314-library-logging-basicconfig
    title: "Python 3.14: Library/logging, basicConfig"
    url: https://docs.python.org/3.14/library/logging.html#logging.basicConfig
  - source_id: py314-howto-logging-library
    title: "Python 3.14: Howto/logging, Configuring Logging for a Library"
    url: https://docs.python.org/3.14/howto/logging.html#configuring-logging-for-a-library
---

## Short answer

**`logging.getLogger(__name__)` returns a logger inside the package hierarchy: `mylib.parser` is a descendant of `mylib`, and every logger is a descendant of root.**[^py314-library-logger-hierarchy] Records are passed to the handlers of ancestor loggers, whose levels and filters are ignored for this.[^py314-library-logging-logger-propagate] So a `basicConfig()` call or a root handler added at import time changes the output of every record that reaches root.[^py314-library-logging-basicconfig] A library only creates log events: the HOWTO advises a `NullHandler` only on the top-level logger (for example `mylib`) and no other handlers.[^py314-howto-logging-library]

## Detailed explanation

A logger name is a dotted hierarchy. `mylib` is an ancestor of `mylib.parser`, and root is an ancestor of every logger, so a record created in `mylib.parser` travels up the chain.[^py314-library-logger-hierarchy] The handlers of that logger process the record first, and then the handlers of its ancestors receive it, as long as `propagate` is true. The levels and filters of the ancestors are not checked along the way.[^py314-library-logging-logger-propagate] That is why a library's record reaches the application's handlers even when the library knows nothing about them.

Why root must not be configured at import: `basicConfig()` adds a handler to root and sets the level of the root logger, so the library makes the output decision instead of the application. If the library calls it first, a later call from the application changes nothing, because root already has handlers, unless `force=True` is passed.[^py314-library-logging-basicconfig]

An example, run on CPython 3.13 and 3.14:

```python
import logging

# Library side: a named logger, and a NullHandler on the package logger. No basicConfig().
log = logging.getLogger("mylib.parser")
logging.getLogger("mylib").addHandler(logging.NullHandler())

log.warning("bad line")                               # no output: the NullHandler on "mylib" handles the record

# Application side: the only place that decides where and how logs are shown.
logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")
log.warning("bad line")                               # mylib.parser WARNING bad line
```

The first `warning` call is silent, because the `NullHandler` on `mylib` handles the record and prints nothing. After `basicConfig()`, the application decides the format and the level, and the same record comes out in its format. The library controls only its own loggers, not the output of the process.[^py314-howto-logging-library]

**Common mistakes:**
- calling `basicConfig()` in a library module: the application's later call becomes a no-op, so it cannot set the format.[^py314-library-logging-basicconfig]
- adding handlers to library loggers other than a `NullHandler` on the top-level logger: the HOWTO forbids this[^py314-howto-logging-library], and when the application configures root, each record is printed twice, because `propagate` passes it on.[^py314-library-logging-logger-propagate]
- logging to the root logger from library code: the application can then not set the level or handlers for that library separately.[^py314-howto-logging-library]
