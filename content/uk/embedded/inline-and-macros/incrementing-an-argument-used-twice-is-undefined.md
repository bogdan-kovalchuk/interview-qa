---
id: emb-macros-0046
title: "Trap: скільки разів інкрементується `a`?"
description: "Надійної відповіді немає: це undefined behavior."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

## Short answer

```c
#define SQR(x) ((x) * (x))
int a = 2;
int b = SQR(a++);
```

<span class="warn">Надійної відповіді немає: це undefined behavior.</span>

Макрос підставляє аргумент у два місця: `((a++) * (a++))`. Дужки рятують від precedence, але не від double evaluation. Два інкременти одного scalar object у межах одного виразу не впорядковані між собою, тому стандарт C не визначає ні результат множення, ні фінальне значення `a`.

Захист: правильні дужки не лікують side effects; для аргументів з ефектами потрібна `static inline` функція або локальна змінна перед макросом.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
