---
id: emb-cemb-0031
title: "Як реалізувати OOP-подібний інтерфейс у C через struct, function pointers і opaque handles?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Публічний API оголошує opaque тип `typedef struct uart uart_t;`, а реалізація ховає поля struct у `.c`. Методи приймають `uart_t*`, а polymorphism можна зробити через table з function pointers: `read`, `write`, `ioctl`. Так driver API має інкапсуляцію без C++ ABI і без відкриття внутрішнього MMIO/стану.[^dou-embedded-interview]

## Detailed explanation

### Інкапсуляція через Opaque Pointers (неповні типи)

У чистому C інкапсуляція реалізується за допомогою неповних типів структур (`incomplete types`, §6.7.2.3 ISO C) [^iso-c-n1570].

У публічному заголовному файлі драйвера (`uart.h`) розміщується лише попереднє оголошення структури без визначення її тіла:

```c
// uart.h
typedef struct uart_dev uart_dev_t;

// Публічні методи (інтерфейс приймає opaque handle)
int uart_write(uart_dev_t *dev, const uint8_t *data, size_t len);
int uart_read(uart_dev_t *dev, uint8_t *data, size_t len);
```

Оскільки компілятор на етапі підключення `uart.h` не знає розміру та полів `struct uart_dev`, користувацький код не може:
1. Створити змінну на стеку (`sizeof(struct uart_dev)` невідомий).
2. Напряму прочитати або пошкодити внутрішні змінні об’єкта (базові адреси апаратних регістрів MMIO, вказівники на кільцеві буфери, лічильники помилок або м’ютекси RTOS).

Повне визначення структури розміщується суто всередині файлу реалізації (`uart.c`), що забезпечує абсолютне приховування деталей реалізації.

### Поліморфізм через таблиці операцій (vtable у C)

Якщо інтерфейс повинен підтримувати кілька апаратних реалізацій (наприклад, драйвер UART на базі DMA, переривань або програмного bit-banging), використовується поліморфізм через таблиці вказівників на функції.

Зберігати вказівники на функції безпосередньо всередині кожного екземпляра структури неефективно, оскільки це марнує оперативну пам’ять RAM. Замість цього застосовують патерн віртуальної таблиці, подібний до C++ `vtable` чи архітектури ядра Linux (`struct file_operations` у VFS):

```c
// Внутрішній або абстрактний заголовок інтерфейсу
struct uart_ops {
    int (*write)(uart_dev_t *dev, const uint8_t *data, size_t len);
    int (*read)(uart_dev_t *dev, uint8_t *data, size_t len);
};

// Повне визначення об’єкта драйвера у файлі реалізації
struct uart_dev {
    const struct uart_ops *ops; // Вказівник на таблицю операцій у Flash (.rodata)
    uint32_t base_addr;         // Приватні апаратні дані
    uint8_t  irq_num;
};

// Диспетчеризація виклику (поліморфний виклик)
int uart_write(uart_dev_t *dev, const uint8_t *data, size_t len) {
    if (dev && dev->ops && dev->ops->write) {
        return dev->ops->write(dev, data, len);
    }
    return -1;
}
```

Таблиця операцій `const struct uart_ops stm32_uart_ops` маркується константою і повністю розміщується компілятором у незалежній Flash-пам’яті (секція `.rodata`), заощаджуючи RAM.

### Робота без динамічної пам’яті (Static Allocation)

В embedded-розробці створення об’єктів через динамічну купу (`malloc`) часто суворо заборонене стандартами функціональної безпеки. Інтерфейс на непрозорих дескрипторах легко адаптується до статичного розміщення:

```c
// Отримання дескриптора наперед виділеного статичного екземпляра
uart_dev_t *uart_get_instance(uint8_t channel);
```

Драйвер створює масив екземплярів `static struct uart_dev instances[MAX_UARTS];` у секції `.bss`, а функція повертає вказівник на відповідний елемент.

### Накладні витрати на рівні процесора

- **Розмір об’єкта**: кожен екземпляр несе накладні витрати лише в один 32-бітний вказівник на таблицю операцій (4 байти RAM на ARM Cortex-M).
- **Швидкодія**: виклик `dev->ops->write(dev, ...)` на рівні асемблера розгортається у непрямий перехід `LDR r2, [r0, #ops_offset]`, `LDR r3, [r2, #func_offset]`, `BLX r3`. Це додає незначну затримку (декілька тактів) і запобігає вбудовуванню коду (`inlining`), проте забезпечує високу модульність і можливість підміни драйвера на Mock-реалізацію під час модульного тестування (Unit Testing) на хост-машині.
