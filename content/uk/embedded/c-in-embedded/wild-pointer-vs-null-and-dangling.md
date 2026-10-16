---
id: emb-cppfound-0038
title: "Що таке wild pointer і чим він відрізняється від NULL та dangling pointer?"
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

**Wild pointer** – неініціалізований вказівник із garbage-значенням (випадкова адреса зі стека).

Порівняння:
- **NULL pointer**: явно невалідна адреса 0, можна перевірити;
- **Dangling pointer**: вказував на валідний об'єкт, який знищено;
- **Wild pointer**: ніколи не вказував на валідний об'єкт.

Всі три -> undefined behavior (UB) при розіменуванні. Wild pointer найнебезпечніший: його адреса ненульова і випадкова – перевірку `if(p != NULL)` проходить.[^embeddedinterviewlab]

## Detailed explanation

TODO
