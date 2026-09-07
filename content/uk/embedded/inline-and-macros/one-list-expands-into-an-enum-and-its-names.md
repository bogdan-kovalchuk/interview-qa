---
id: emb-macros-0022
title: "Як X-macro синхронізує `enum` і масив рядків?"
description: "Один список ERR_LIST розгортають двічі з різним X, тож enum і масив рядків оновлюються разом."
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
#define ERR_LIST(X) \
  X(ERR_NONE, "OK") \
  X(ERR_TIMEOUT, "Timeout")
```

## Short answer

Той самий список розгортають двічі з різним `X`:

```c
#define AS_ENUM(n, s) n,
typedef enum { ERR_LIST(AS_ENUM) } err_t;

#define AS_STR(n, s) [n] = s,
static const char *const names[] = { ERR_LIST(AS_STR) };
```

Один список – два згенерованих об'єкти. Новий код помилки додається в одному місці, і `enum`, і `names[]` оновлюються разом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
