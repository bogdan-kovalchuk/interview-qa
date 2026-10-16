---
id: emb-cppfound-0001
title: "Що таке вказівник у C і що він зберігає?"
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

**Вказівник** – змінна, що зберігає **адресу** іншого об'єкта або функції в пам'яті. Він не зберігає саме значення, а лише місцезнаходження.

Дві фундаментальні операції:
- `&x` – взяття адреси: повертає адресу об'єкта `x`;
- `*p` – розіменування: читає/записує значення за адресою `p`.

Вони обернені: `*(&x) == x` завжди. У embedded вказівники критичні для доступу до hardware registers, DMA буферів, callback-функцій.[^embeddedinterviewlab]

## Detailed explanation

TODO
