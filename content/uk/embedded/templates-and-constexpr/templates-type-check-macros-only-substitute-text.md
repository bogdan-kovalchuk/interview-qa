---
id: emb-tmplcx-0022
title: "Templates vs макроси: ключові відмінності?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Templates: повний type checking, аргументи раз, дебаг, constexpr-обчислення. Макроси: текст, double evaluation, лише preprocessor output.**

Ціна: templates ризикують code bloat (копія на інстанціацію) і повільнішим білдом; макроси – швидкі й портативні на C89, але небезпечні.

Правило: у C++ обирай templates для типобезпеки; макроси лишай для того, що шаблон не вміє (`#`/`##`, conditional compilation).[^embeddedinterviewlab]

## Detailed explanation

TODO
