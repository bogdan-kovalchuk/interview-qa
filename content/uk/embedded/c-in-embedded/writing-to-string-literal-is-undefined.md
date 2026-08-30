---
id: emb-cppfound-0011
title: "Trap: що станеться?<br><pre class=\"code-block\"><code>char *s = \"hello\";<br>s[0] = 'H';</code></pre>"
description: "Why modifying a string literal is undefined behavior."
track: embedded
section: c-in-embedded
level: junior
type: pitfall
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Рядковий літерал <code>"hello"</code> зберігається у <span class="key">.rodata</span> (Flash/read-only). <code>s</code> вказує на цю read-only область.<br><br>Запис <code>s[0] = 'H'</code> -> <span class="warn">undefined behavior</span>: на ПК – segfault, на MCU – HardFault (якщо MPU захищає Flash) або тихий запис у Flash (що не спрацьовує).<br><br>Правильно: <code>char arr[] = "hello";</code> – компілятор копіює рядок у writable масив (stack або .data). Тоді <code>arr[0] = 'H'</code> – легально.[^embeddedinterviewlab]

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
