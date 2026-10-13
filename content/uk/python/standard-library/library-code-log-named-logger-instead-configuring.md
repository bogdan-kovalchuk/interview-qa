---
id: py-stdlib-0015
title: "Чому library code має логувати через named logger, а не налаштовувати root logger при import?"
description: "logging.getLogger(__name__) дає logger в ієрархії пакета, а basicConfig() або handler на root logger при import змінює вивід для всіх записів, що доходять до root."
track: python
section: standard-library
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-logger-hierarchy
    title: "Python 3.14: Library/logging, Logger Objects"
    url: https://docs.python.org/3.14/library/logging.html#logger-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: getLogger з тим самим іменем повертає той самий Logger; крапкові імена утворюють ієрархію предків, а root є предком усіх logger-ів."
  - source_id: py314-library-logging-logger-propagate
    title: "Python 3.14: Library/logging, Logger.propagate"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.propagate
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: записи передаються handlers предків, якщо propagate істинний; рівні й фільтри предків для цього не враховуються."
  - source_id: py314-library-logging-basicconfig
    title: "Python 3.14: Library/logging, basicConfig"
    url: https://docs.python.org/3.14/library/logging.html#logging.basicConfig
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: basicConfig нічого не робить, якщо root logger уже має handlers, якщо не задано force=True."
  - source_id: py314-howto-logging-library
    title: "Python 3.14: Howto/logging, Configuring Logging for a Library"
    url: https://docs.python.org/3.14/howto/logging.html#configuring-logging-for-a-library
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14 (HOWTO з логування): бібліотека не додає handlers, крім NullHandler на top-level logger, і не логує в root logger."
---

## Short answer

**`logging.getLogger(__name__)` повертає logger у ієрархії пакета: `mylib.parser` є нащадком `mylib`, а всі logger-и – нащадками root.**[^py314-library-logger-hierarchy] Записи передаються handlers предків, і рівні та фільтри предків для цього не враховуються.[^py314-library-logging-logger-propagate] Через це `basicConfig()` або handler на root, доданий при import, змінює вивід для всіх записів, що доходять до root.[^py314-library-logging-basicconfig] Бібліотека лише створює log events: HOWTO радить додати `NullHandler` лише на top-level logger бібліотеки (наприклад, `mylib`) і не додавати інших handlers до її logger-ів.[^py314-howto-logging-library]

## Detailed explanation

Ім’я logger-а – це крапкова ієрархія. `mylib` є предком `mylib.parser`, а root є предком усіх logger-ів, тож запис, створений у `mylib.parser`, рухається вгору по ланцюжку.[^py314-library-logger-hierarchy] Запис обробляють handlers самого logger-а, а потім передають handlers предків, поки `propagate` істинний. Рівні й фільтри предків при цьому не перевіряються.[^py314-library-logging-logger-propagate] Саме тому бібліотечний запис потрапляє до handlers застосунку, навіть якщо бібліотека нічого про них не знає.

Чому не можна налаштовувати root при import: `basicConfig()` додає handler на root і задає рівень root logger-а, тож рішення про вивід ухвалює бібліотека замість застосунку. Якщо бібліотека викликала його першою, пізніший виклик застосунку нічого не змінить, бо root уже має handlers, доки не передано `force=True`.[^py314-library-logging-basicconfig]

Приклад (виконано на CPython 3.13 і 3.14):

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

Перший виклик `warning` мовчить, бо `NullHandler` на `mylib` обробляє запис і нічого не виводить. Після `basicConfig()` рішення про формат і рівень ухвалює застосунок, і той самий запис виходить у його форматі. Бібліотека керує лише своїми logger-ами, а не виводом процесу.[^py314-howto-logging-library]

**Типові помилки:**
- викликати `basicConfig()` у модулі бібліотеки: пізніший виклик застосунку стає no-op, і формат він задати не може.[^py314-library-logging-basicconfig]
- додавати до logger-ів бібліотеки handlers, крім `NullHandler` на top-level logger: це прямо заборонено HOWTO[^py314-howto-logging-library], а коли застосунок налаштовує root, запис виводиться двічі, бо `propagate` передає його далі.[^py314-library-logging-logger-propagate]
- писати в root logger з коду бібліотеки: застосунок тоді не може окремо задати рівень чи handlers для неї.[^py314-howto-logging-library]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
