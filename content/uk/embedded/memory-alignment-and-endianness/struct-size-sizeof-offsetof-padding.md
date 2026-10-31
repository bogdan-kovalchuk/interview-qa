---
id: emb-cemb-0005
title: "Як визначити розмір структур?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Розмір структури визначають оператором `sizeof(struct_type)` або `sizeof variable`.[^dou-embedded-interview] Він включає всі поля, внутрішній padding між ними й можливий trailing padding у кінці, щоб масив таких структур мав правильне вирівнювання кожного елемента.

Для аналізу layout використовують `offsetof(struct_type, field)` з `<stddef.h>`. Приклад: `struct S { char c; int x; };` часто має розмір 8, а не 5, бо `int` вирівнюється на 4 байти. Точний розмір залежить від ABI, компілятора, packing options і порядку полів.

## Detailed explanation

### Оператор `sizeof` та правила стандарту C

Розмір структури в мові C визначається за допомогою вбудованого оператора `sizeof(struct Type)` або `sizeof expr`.[^iso-c-n1570] Оператор `sizeof` обчислюється на етапі компіляції та повертає ціле число типу `size_t`, що представляє загальну кількість байтів, яку об’єкт займає в пам’яті.

Фундаментальне правило: розмір структури не обов’язково дорівнює сумі розмірів її членів.[^iso-c-n1570] Загальний розмір обчислюється за формулою:
`sizeof(struct) = сума_розмірів_полів + internal_padding + trailing_padding`.

### Дослідження зміщень полів через `offsetof`

Для аналізу внутрішньої топології структури та знаходження точних меж заповнення використовується стандартний макрос `offsetof(type, member)` із заголовного файлу `<stddef.h>`.[^iso-c-n1570] Він повертає кількість байтів від початку структури до зазначеного поля.

```c
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

struct Packet {
    uint8_t  header;  // зміщення 0, розмір 1
    // 3 байти internal padding
    uint32_t payload; // зміщення 4, розмір 4
    uint16_t crc;     // зміщення 8, розмір 2
    // 2 байти trailing padding
};

void inspect_layout(void) {
    size_t off_hdr = offsetof(struct Packet, header);  // 0
    size_t off_pay = offsetof(struct Packet, payload); // 4
    size_t off_crc = offsetof(struct Packet, crc);     // 8
    size_t total   = sizeof(struct Packet);            // 12
}
```

Кількість байтів padding між двома полями обчислюється як:
`padding = offsetof(struct Packet, payload) - (offsetof(struct Packet, header) + sizeof(uint8_t))` (тобто `4 - (0 + 1) = 3` байти).

### Чому розмір структури кратний її максимальному вирівнюванню

Компілятор гарантує, що значення `sizeof(struct S)` завжди є кратним максимальній вимозі вирівнювання серед усіх елементів структури (`alignof(struct S)` у C11 або `_Alignof`).[^iso-c-n1570]

Це обумовлено адресним простором під час створення масивів:[^armv7m]
```c
struct Packet buffer[4];
```
У мові C елементи масиву розташовані поспіль без будь-яких проміжків: адреса `buffer[i]` дорівнює `(uintptr_t)buffer + i * sizeof(struct Packet)`. Якби кінцевого заповнення не було (розмір був би 10 замість 12), адреса другого елемента `buffer[1]` дорівнювала б 10. Але поле `payload` має зміщення 4 всередині структури, тому його адреса в пам’яті склала б `10 + 4 = 14`. Оскільки 14 не ділиться на 4, процесор ARM Cortex-M зазнав би штрафу швидкодії або аварійно зупинився б із `UsageFault`/`HardFault` при спробі виконати інструкцію `LDR`.[^armv7m]

### Compile-time верифікація розміру в Embedded

Вбудовані системи часто взаємодіють із регістрами апаратної периферії або бінарними пакетами. Покладання на «ручний» підрахунок розміру веде до прихованих багів. Розмір та зміщення критичних структур обов’язково перевіряють на етапі компіляції за допомогою `static_assert` (або `_Static_assert` у C11):

```c
#include <assert.h>

static_assert(sizeof(struct Packet) == 12, "Packet structure size changed unexpectedly!");
static_assert(offsetof(struct Packet, payload) == 4, "Payload offset misalignment!");
```

### Типові помилки та підводні камені

- **Припущення про однаковий розмір на різних платформах:** розмір структури з полями типу `int` або вказівниками різниться між 32-бітним мікроконтролером (розмір вказівника 4 байти) та 64-бітним хост-комп’ютером (розмір вказівника 8 байтів).
- **Порожні структури:** у стандарті C оголошення `struct Empty {};` не дозволене (хоча підтримується розширенням GCC як розмір 0). У C++ порожня структура гарантовано має розмір не менше 1 байта, щоб кожен об’єкт мав унікальну адресу в пам’яті.
- **Гнучкі масиви (Flexible array members):** для `struct Msg { uint8_t len; uint8_t data[]; };` оператор `sizeof` повертає лише розмір заголовка без урахування масиву `data`.
