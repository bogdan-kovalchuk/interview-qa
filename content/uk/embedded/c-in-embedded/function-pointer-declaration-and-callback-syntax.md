---
id: emb-cppfound-0023
title: "Що таке function pointer і який синтаксис його оголошення?"
description: "How to declare and call a function pointer."
track: embedded
section: c-in-embedded
level: junior
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

<span class="key">Function pointer</span> – вказівник на функцію: зберігає адресу коду функції для виклику через нього.<br><br>Синтаксис: <code>return_type (*name)(param_types);</code><br>Приклад: <code>void (*isr)(void) = &amp;my_handler;</code><br><br>Виклик: <code>(*isr)();</code> або просто <code>isr();</code> (обидва коректні).<br><br>Застосування у embedded: ISR dispatch tables, state machine transitions, RTOS task functions, callback API (<code>HAL_UART_RegisterCallback</code>).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
