---
id: emb-cppfound-0099
title: "Чим небезпечний неініціалізований вказівник (wild pointer) і як захиститись?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Wild pointer** – вказівник з garbage-адресою (значення стека), не NULL. Перевірка `if(p != NULL)` не виявляє його.

Небезпеки:
- Запис за довільною адресою -> corruption критичних даних;
- На MCU: запис у периферійні регістри -> непередбачувана поведінка hardware;
- Важко відтворити – залежить від стану стека.

Захист:
- Завжди ініціалізуй: `int *p = NULL;` або одразу `= &x`;
- `-fsanitize=address` при розробці;
- Static analysis: PC-lint, Coverity.[^embeddedinterviewlab]

## Detailed explanation

TODO
