---
id: emb-volconst-0028
title: "Trap: що не так із таким API?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
void uart_send(uint8_t *data, size_t len);
const uint8_t msg[] = { 0x55, 0xAA };
uart_send(msg, 2);
```

## Short answer

<span class="warn">API втрачає const-correctness.</span>

Якщо `uart_send` лише читає buffer, параметр слід оголосити як `const uint8_t *data`. Інакше передавання `const` buffer спричиняє несумісність типів pointer; явне зняття `const` не робить запис допустимим і може приховати помилку.

Read-only input parameters оголошуй як `const T *`, щоб сигнатура відповідала поведінці функції.[^iso-c-n1570]

## Detailed explanation

Ознака проблеми – caller має `const uint8_t msg[]`, але не може передати його функції, оголошеній як `void uart_send(uint8_t *data, size_t len)`, без діагностики про несумісні типи pointer. Якщо прибрати кваліфікатор явним cast, попередження зникає, але контракт лишається небезпечним: реалізація функції все ще може спробувати записати у buffer.[^iso-c-n1570]

У C кваліфікатор `const` у типі елемента означає, що lvalue, отримане розіменуванням такого pointer, не можна використовувати для модифікації об’єкта. Pointer-to-const може вказувати як на об’єкт, оголошений `const`, так і на звичайний об’єкт, який функція лише читає. Тому `const uint8_t *data` приймає обидва випадки й точно описує read-only input контракт.[^iso-c-n1570]

У прикладі `msg` має const-qualified element type, а параметр `uint8_t *` цього кваліфікатора не має. Не можна безпечно передати pointer до більш кваліфікованого типу параметру, який дозволяє запис: це зняло б захист типу. Правильний API для функції, яка лише передає байти UART, має приймати `const uint8_t *data`. Якщо функція справді змінює буфер, параметр має залишатися writable, і це має бути частиною її контракту.[^iso-c-n1570]

Наприклад, `void uart_send(const uint8_t *data, size_t len);` дозволяє передати як `msg`, так і звичайний змінюваний масив без втрати const-correctness. Усередині такої функції можна читати `data[i]`, але не присвоювати йому нові значення. Це також полегшує статичному аналізатору розпізнавання input-only параметрів. Не додавай `const` лише формально: якщо функція має змінювати дані, її API повинен чесно відображати цю дію.[^iso-c-n1570]

**Типова помилка:** cast-ити `const uint8_t *` до `uint8_t *`, щоб обійти попередження. Замість цього виправ сигнатуру, якщо функція читає дані, або передай mutable копію, якщо їй справді потрібен writable buffer.[^iso-c-n1570]
