---
id: emb-cemb-0011
title: "Як відбувається виклик функції?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Під час виклику функції компілятор дотримується **calling convention** конкретної ABI.[^dou-embedded-interview] Аргументи передаються в регістрах або на stack, адреса повернення зберігається, керування переходить на код функції, а функція створює свій **stack frame** для локальних змінних і збережених регістрів.

Після виконання результат повертається зазвичай у регістрі або через прихований вказівник для великих структур. Потім відновлюються потрібні регістри й stack pointer, виконується return на адресу виклику. Деталі відрізняються між x86-64, ARM Cortex-M, AAPCS тощо, але ідея одна: узгоджений контракт між caller і callee.

## Detailed explanation

TODO
