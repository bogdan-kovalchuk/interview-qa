---
id: emb-dtypes-0017
title: "Чим відрізняється `static` локальна змінна від звичайної локальної?"
description: "Звичайна локальна живе на стеку і зникає після виклику, static локальна живе у статичній пам'яті увесь час програми."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-06
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
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? data-types-and-memory-layout; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

**Звичайна локальна** - на стеку, lifetime = тривалість виклику функції, не ініціалізується автоматично.

**Static локальна** - у `.bss`/`.data` (статична пам'ять), lifetime = весь час програми, ініціалізується один раз (нулем або заданим значенням). Зберігає значення між викликами.

<span class="warn">Мінус: функція не reentrant</span> - не потокобезпечна без синхронізації.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
