---
id: emb-dtypes-0010
title: "За AAPCS32 який розмір матиме `struct { char c; int x; }`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: aapcs32-layout
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
---

## Short answer

За AAPCS32, для `struct { char c; int x; }` очікуваний розмір – 8 байтів: `c` має offset 0, `x` – offset 4, після нього є 0 байтів trailing padding. Це випливає з 1-байтового `char`, 4-байтового й 4-байтово вирівняного `int`, а також вирівнювання struct за найсуворішим полем; це ABI конкретного target, а не загальна гарантія мови C. Перевіряйте фактичний layout через `sizeof` та `offsetof`.[^aapcs32-layout]

## Detailed explanation

Стандарт C зберігає порядок полів структури, але дозволяє padding між полями та після останнього поля. Тому сам факт, що MCU має 32-бітні регістри, недостатній для обчислення розміру struct: потрібні розмір типів і правила alignment конкретного ABI.[^iso-c-n1570]

За AAPCS32 `char` має розмір і вирівнювання 1 байт, а `int` – 4 байти й вирівнювання 4 байти. Отже, після `c` компілятор додає три байти, щоб `x` починався на offset 4. Структура має вирівнювання 4 байти; її члени займають 8 байтів разом, тож trailing padding у цьому прикладі немає. Висновок чинний для AAPCS32 без спеціальних packing або alignment атрибутів, які змінюють layout.[^aapcs32-layout]

Уявіть послідовність байтів від початку об’єкта: байт 0 містить `c`, байти 1–3 є padding, а байти 4–7 містять `x`. Вирівнювання структури важливе і для масиву таких об’єктів: кожен наступний елемент має починатися на межі, придатній для його `int`, тому розмір елемента має бути кратним вирівнюванню структури.[^aapcs32-layout]

Padding не є полем, яке можна назвати або надійно використовувати для даних застосунку. Його байти також означають, що порівняння двох структур через `memcmp` не обов’язково еквівалентне порівнянню їхніх полів: значення padding не задає семантичну рівність об’єктів.[^iso-c-n1570]

Не виводьте layout лише з назви процесора: інший ABI, опція packing, атрибут поля чи pragma можуть змінити результат. У коді перевірте `sizeof(struct S)` та `offsetof(struct S, x)` для конкретної збірки; у C макрос `offsetof` з `<stddef.h>` повертає offset члена в байтах.[^iso-c-n1570]

**Типова помилка:** переносити розрахунок на іншу toolchain або припускати, що кожен Cortex-M використовує тотожні compiler options. Для зовнішніх форматів даних серіалізуйте поля явно замість запису сирої структури.
