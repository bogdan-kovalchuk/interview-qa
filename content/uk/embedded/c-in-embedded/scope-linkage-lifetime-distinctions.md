---
id: emb-cemb-0041
title: "Що таке scope, linkage і lifetime у C, і чому ці поняття часто плутають?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Scope** – де ім'я видиме в source code. **Linkage** – чи одне й те саме ім'я може посилатися на той самий object/function між scopes або translation units. **Lifetime/storage duration** – коли існує сам об'єкт у пам'яті; наприклад, block-scope `static` має локальну видимість, але живе весь runtime.[^dou-embedded-interview]

## Detailed explanation

TODO
