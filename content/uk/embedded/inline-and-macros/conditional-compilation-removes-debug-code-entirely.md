---
id: emb-macros-0017
title: "Як зробити debug-only код, який повністю зникає у release-збірці?"
description: "Conditional compilation: при DEBUG макрос розгортається у printf, інакше – у порожнечу, і код повністю прибирається ще до компіляції (нуль flash/RAM)."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
#ifdef DEBUG
  #define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
  #define DBG(fmt, ...)
#endif
```

## Short answer

**Conditional compilation**: при `DEBUG` макрос розгортається у `printf`, інакше – у порожнечу, і код повністю прибирається ще до компіляції (нуль flash/RAM).

Це краще за `if (debug)`, бо не лишає мертвих гілок і рядкових літералів у прошивці.

Правило: визначай `DEBUG` через build-флаг (`-DDEBUG`), а не в коді.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
