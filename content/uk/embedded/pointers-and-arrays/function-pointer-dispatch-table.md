---
id: emb-cppfound-0057
title: "Що таке dispatch table і як реалізувати через function pointers?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Dispatch table** – масив function pointers для вибору обробника за індексом. Замінює великі `switch`-конструкції.

```c
typedef void (*handler_t)(void);
handler_t table[16] = {
    isr0, isr1, isr2, ...
};
// Call:
table[irq_num]();
```

Переваги: O(1) dispatch, легко розширити, підходить для RTOS task tables, state machines, protocol demultiplexers. У embedded: Cortex-M Vector Table – вбудований dispatch table у Flash.[^embeddedinterviewlab]

## Detailed explanation

Таблиця диспетчеризації (dispatch table, або jump table) – це архітектурний патерн проектування у системному та вбудованому програмуванні на мові C, який реалізує вибір і виклик функції за числовим індексом за фіксований час O(1). Стандарт ISO/IEC 9899 (§6.3.2.1, §6.5.2.2) регламентує роботу з покажчиками на функції та їх викликами.[^iso-c-n1570]

### Архітектура та принцип роботи dispatch table

Замість послідовної перевірки умов (`if-else`) або розгалужених блоків `switch-case`, де компілятор може згенерувати ланцюжок умовних переходів зі складністю O(N) або бінарний пошук O(log N), dispatch table зберігає покажчики на функції-обробники безпосередньо в масиві.

Індекс масиву відповідає коду команди (command opcode), номеру переривання, стану автомата чи ідентифікатору події. Виклик потрібного обробника здійснюється за дві операції:
1. Індексація масиву для отримання адреси функції.
2. Непрямий перехід (indirect call) за отриманою адресою.

### Реалізація на C: типізація, const у Flash та designated initializers

Для чистої та безпечної реалізації у вбудованих системах використовуються такі підходи:[^iso-c-n1570]

```c
#include <stdint.h>
#include <stddef.h>

// 1. Чітке визначення типу покажчика на функцію
typedef void (*cmd_handler_t)(const uint8_t *payload, uint16_t len);

// 2. Оголошення прототипів функцій-обробників
static void handle_ping(const uint8_t *payload, uint16_t len);
static void handle_read(const uint8_t *payload, uint16_t len);
static void handle_write(const uint8_t *payload, uint16_t len);

// 3. Створення таблиці у Flash пам’яті (const) з використанням designated initializers (C99)
typedef enum {
    CMD_PING  = 0,
    CMD_READ  = 1,
    CMD_WRITE = 2,
    CMD_COUNT = 3
} cmd_id_t;

static const cmd_handler_t dispatch_table[CMD_COUNT] = {
    [CMD_PING]  = handle_ping,
    [CMD_READ]  = handle_read,
    [CMD_WRITE] = handle_write,
};
```

Використання кваліфікатора `const` є критично важливим для мікроконтролерів:
- Таблиця розміщується у секції `.rodata` у Flash-пам’яті (ROM), не витрачаючи дефіцитну оперативну пам’ять SRAM.
- Зберігання у Flash унеможливлює випадкове пошкодження покажчиків або перезапис адрес внаслідок переповнення сусідніх буферів у SRAM.

### Переваги над switch-case у системах реального часу

1. **Детермінізм часу виконання:** час обчислення адреси та виклику є строго постійним (O(1)) незалежно від кількості обробників. Це фундаментальна вимога для систем жорсткого реального часу (hard real-time).
2. **Розширюваність (Open-Closed Principle):** додавання нової команди не вимагає переписування гігантського `switch` на сотні рядків; достатньо додати новий елемент у масив.
3. **Генерація компактного асемблерного коду:** на ARM Cortex-M виклик таблиці транслюється всього в 3–4 інструкції: завантаження базової адреси таблиці, завантаження адреси функції (`LDR r3, [r0, r1, LSL #2]`) та перехід за посиланням `BLX r3`.

### Апаратний приклад: таблиця векторів переривань ARM Cortex-M

Найвідомішим апаратним втіленням dispatch table в embedded є **Векторна таблиця ARM Cortex-M (Vector Table)**:
- Розташовується за нульовою адресою Flash (або задається через регістр `VTOR` – Vector Table Offset Register).
- Являє собою неперервний масив 32-бітних слів: нульовий елемент – початкова адреса вершини стека (Initial MSP), а наступні елементи – адреси обробників винятків та апаратних переривань (`Reset_Handler`, `NMI_Handler`, `HardFault_Handler`, `SysTick_Handler`, `USART1_IRQHandler` тощо).
- При виникненні апаратного переривання контролер NVIC апаратно зчитує відповідну комірку вектора і передає керування за вказаною адресою.

### Захисне програмування: перевірка меж та валідація покажчиків

У коді прошивок перед здійсненням виклику через dispatch table обов’язково виконуються два кроки валідації:[^iso-c-n1570]

```c
void execute_command(uint8_t cmd, const uint8_t *data, uint16_t len) {
    // 1. Обов’язкова перевірка виходу за межі діапазону масиву
    if (cmd >= CMD_COUNT) {
        handle_unknown_command(cmd);
        return;
    }

    // 2. Перевірка на NULL (якщо таблиця розріджена або команда не реалізована)
    cmd_handler_t handler = dispatch_table[cmd];
    if (handler != NULL) {
        handler(data, len);
    } else {
        handle_unimplemented_command(cmd);
    }
}
```
Відсутність перевірки індексу веде до стрибка за випадковою адресою пам’яті з подальшим викликом `HardFault`, а виклик нульового покажчика призведе до збою системи.
