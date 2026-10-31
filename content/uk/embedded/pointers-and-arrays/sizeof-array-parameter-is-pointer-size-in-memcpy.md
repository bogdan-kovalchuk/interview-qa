---
id: emb-cppfound-0039
title: "Що зробить `memcpy(dst, src, sizeof(src))` якщо `src` – параметр-масив функції?"
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

<span class="warn">Скопіює лише 4 або 8 байт</span> (розмір вказівника), а не розмір масиву.

У параметрі функції `src` – це `uint8_t*`, не масив. `sizeof(src) = sizeof(uint8_t*) = 4`. Тому `memcpy` копіює тільки 4 байти замість N.

Правильно: передавати розмір явно: `memcpy(dst, src, n * sizeof(src[0]))` або `memcpy(dst, src, n)` де `n` – окремий параметр.[^embeddedinterviewlab]

## Detailed explanation

Виклик `memcpy(dst, src, sizeof(src))` всередині функції, де `src` оголошений як масив, є однією з класичних підступних помилок у C, спричиненою правилом пристосування параметрів-масивів до покажчиків.[^iso-c-n1570]

### Механізм Array Parameter Decay у стандарті ISO C

У мові C масиви принципово не можуть передаватися у функцію за значенням (by value). Відповідно до стандарту ISO/IEC 9899 (§6.7.6.3 Function declarators, пункт 7):[^iso-c-n1570]

> «Оголошення параметра, що має тип «масив типу», має налаштовуватися (adjusted) до типу «вказівник на тип».»

Це означає, що всі наведені нижче сигнатури функцій є абсолютно ідентичними для компілятора:

```c
void send_packet(uint8_t src[128]);
void send_packet(uint8_t src[]);
void send_packet(uint8_t *src);
```

Числове значення розміру всередині квадратних дужок (`128`) повністю ігнорується компілятором: воно не резервує пам’ять і не контролює розмір аргументу під час виклику. Усередині тіла функції параметр `src` є звичайною локальною змінною-покажчиком типу `uint8_t *`.[^iso-c-n1570]

### Робота оператора sizeof та наслідки для memcpy

Оскільки `src` у тілі функції є покажчиком, оператор `sizeof(src)` оцінює саме тип покажчика (ISO/IEC 9899, §6.5.3.4):[^iso-c-n1570]

- На 32-бітних мікроконтролерах (наприклад, ARM Cortex-M) `sizeof(uint8_t *)` завжди дорівнює **4 байтам**;
- На 64-бітних архітектурах `sizeof(uint8_t *)` дорівнює **8 байтам**.

Відповідно, виклик `memcpy(dst, src, sizeof(src))` перетворюється на `memcpy(dst, src, 4)`. Замість копіювання повного буфера (наприклад, 128 байтів корисного навантаження кадру Ethernet або повідомлення CAN) копіюються лише перші 4 байти. Решта байтів цільового буфера `dst` залишається неініціалізованою або містить старі дані, що викликає важковловимі логічні збої протоколів передачі даних.[^embeddedinterviewlab]

### Діагностика компілятора

Сучасні компілятори (GCC, Clang) мають вбудовану перевірку для цього патерну помилки. Прапорець `-Wsizeof-array-argument` (входить до `-Wall`) генерує попередження:[^iso-c-n1570]

```text
warning: 'sizeof' on array function parameter 'src' will return size of 'uint8_t *'
```

Ігнорування попереджень компілятора в embedded-проектах часто призводить до потрапляння таких дефектів у релізні прошивки.

### Правильні інженерні рішення

1. **Явна передача довжини через окремий параметр (найпоширеніший патерн):**
   ```c
   void send_packet(uint8_t *dst, const uint8_t *src, size_t len) {
       memcpy(dst, src, len);
   }
   ```
2. **Передача вказівника на масив фіксованого розміру:**
   Якщо розмір буфера є суворо фіксованим, слід використовувати покажчик на масив:
   ```c
   void send_packet(uint8_t *dst, const uint8_t (*src)[128]) {
       memcpy(dst, *src, sizeof(*src)); // sizeof(*src) повертає рівно 128 байтів
   }
   ```
   У цьому випадку компілятор не виконує decay і суворо контролює відповідність типів під час виклику функції.[^iso-c-n1570]
3. **Інкапсуляція масиву в структуру:**
   Масиви всередині структур не розпадаються на покажчики при передачі:
   ```c
   typedef struct {
       uint8_t data[128];
   } Packet_t;

   void send_packet(Packet_t *dst, const Packet_t *src) {
       *dst = *src; // або memcpy(dst, src, sizeof(Packet_t));
   }
   ```
