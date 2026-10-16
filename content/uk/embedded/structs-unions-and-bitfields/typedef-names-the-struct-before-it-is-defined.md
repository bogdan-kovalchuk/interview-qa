---
id: emb-structs-0050
title: "Що означає `typedef struct Foo Foo;`?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Це створює typedef-ім’я `Foo` для типу `struct Foo`**, часто ще до повного визначення структури.

Якщо тіло структури не задане, `Foo` є incomplete type. Можна використовувати `Foo *` у API, але не можна створювати `Foo object` by value до повного визначення.

Embedded-use case: opaque handles для драйверів: `Foo_Init(Foo *self)` або `Foo *Foo_Open(...)`.[^iso-c-n1570]

## Detailed explanation

`typedef struct Foo Foo;` оголошує тег структури `Foo` і створює для її типу typedef-ім’я `Foo`. У цій точці структура ще incomplete type: компілятор знає її назву, але не знає розміру та складу полів.[^iso-c-n1570]

Неповне оголошення корисне для opaque handle. Заголовок API може оголосити `struct Foo` і функції, які приймають або повертають `Foo *`, тоді як поля визначені лише у внутрішньому файлі реалізації. Клієнтський код може передавати й зберігати такий вказівник, але не може звертатися до полів, брати `sizeof(Foo)` чи створювати об’єкт `Foo` за значенням, доки тип неповний.[^iso-c-n1570]

Пізніше повне оголошення з тим самим тегом завершує тип: `struct Foo { int state; };`. Після цього об’єкти можна створювати, копіювати й адресувати їхні поля. Typedef не створює окремої структури й не є forward declaration іншого імені: `Foo` і `struct Foo` позначають той самий тип, а тег і typedef ім’я належать до різних просторів імен у C.[^iso-c-n1570]

Наприклад, публічний заголовок може містити лише `typedef struct Foo Foo;` та декларації `Foo *Foo_Open(void);` і `void Foo_Close(Foo *);`. Саме визначення структури розміщують у `.c` файлі. Типова помилка – оголосити змінну `Foo object;` у клієнтському коді: це вимагає відомого розміру, якого forward declaration не дає.[^iso-c-n1570]
