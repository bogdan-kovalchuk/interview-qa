---
id: emb-volconst-0027
title: "Trap: чи завжди локальний `const` масив автоматично лежить у Flash?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: avr-libc-program-space
    title: "AVR-LibC: Data in Program Space"
    url: https://avrdudes.github.io/avr-libc/avr-libc-user-manual/pgmspace.html
---

## Short answer

<span class="warn">Ні, не завжди.</span>

`const` забороняє змінювати об’єкт через цей identifier, але не задає фізичне розміщення. Локальний automatic `const` object може потребувати stack storage або бути оптимізований; file-scope чи `static const` зазвичай потрапляє до read-only секції, але не обов’язково у Flash.

Для великої незмінної LUT використовуй `static const` або file-scope `const`, а фактичне розміщення перевіряй у map file.[^avr-libc-program-space]

## Detailed explanation

Помилка проявляється як несподіване споживання RAM: локальний масив оголошено `const`, але його розмір усе одно впливає на потребу stack або компілятор створює копію для доступу. І навпаки, глобальну `const` таблицю вважають гарантовано розміщеною у Flash, хоча прошивка або linker script залишили її у RAM.[^avr-libc-program-space]

Причина в тому, що `const` описує доступ через тип, а не storage duration і не адресу. Автоматичний об’єкт має automatic storage duration; об’єкт, оголошений на рівні файла або зі `static`, має static storage duration. Сам стандарт C визначає ці тривалості, але не задає секцій `.rodata` чи `.data`, стеку MCU або розташування у Flash.[^iso-c-n1570]

Компілятор і linker обирають реалізацію з урахуванням ABI, оптимізації та memory map. Для типового GCC ELF об’єктний файл розрізняє writable initialized data й read-only data, але linker script вирішує, до якої пам’яті прив’язати вихідні секції. На деяких Harvard архітектурах читання Flash вимагає окремих атрибутів чи функцій доступу; сам `const` не змінює адресний простір і не гарантує сумісності pointer.[^avr-libc-program-space]

Приклад: `void f(void) { const uint16_t lut[256] = { 1, 2 }; }` має автоматичний об’єкт, якщо компілятор не усуне його чи не перетворить використання. Для таблиці, спільної для викликів, `static const uint16_t lut[256] = { 1, 2 };` задає static storage duration і read-only доступ. Однак перевірка map file та документації MCU все одно потрібна, якщо вимога полягає саме у збереженні в Flash.[^iso-c-n1570] [^avr-libc-program-space]

**Типова помилка:** вважати слово `const` наказом linker-у помістити дані у Flash. Визнач storage duration, перевір секції та фактичну адресу у map file, а для конкретного MCU звір спосіб читання program memory з документацією платформи.[^avr-libc-program-space]
