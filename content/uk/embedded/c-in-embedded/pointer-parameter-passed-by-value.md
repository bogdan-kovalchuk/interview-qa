---
id: emb-cppfound-0090
title: "Знайдіть помилку: чи переміститься зовнішній pointer?"
description: "Why changing a pointer parameter does not change the caller's pointer."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Question code

```c
void advance(char *p, int n){
  p += n;
}
```

## Short answer

<span class="warn">НІ.</span> У C параметри передаються **за значенням**. Функція отримує копію вказівника `p`. `p += n` змінює локальну копію, але не оригінальний вказівник у caller-і.

Для зміни caller-ського pointer: потрібен double pointer: `void advance(char **p, int n){ *p += n; }` Виклик: `advance(&cursor, 5);`

Класична помилка при реалізації парсерів і потокових обробників.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
