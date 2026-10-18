---
id: emb-cemb-0030
title: "Що таке padding у структурі і чому порядок полів може змінити її розмір?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Padding** – невикористані байти, які компілятор додає для alignment наступного поля або всієї структури. Якщо розташувати поля від більших alignment-вимог до менших, padding часто зменшується. <span class="warn">Не можна покладатися на padding bytes як на стабільні дані</span>: вони можуть бути неініціалізовані й не підходять для прямого порівняння чи передачі по шині.[^dou-embedded-interview]

## Detailed explanation

TODO
