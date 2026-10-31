---
id: emb-cemb-0035
title: "Як визначити endianness системи без порушення strict aliasing?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Безпечно записати integer і скопіювати його bytes через `memcpy` у `unsigned char` buffer, бо character types можуть представляти object representation. Наприклад, `uint32_t x=1`, `memcpy(b,&x,4)`, потім перевірити `b[0]`. Для portable protocol code краще не залежати від host endianness, а явно збирати/розбирати bytes.[^dou-embedded-interview]

## Detailed explanation

### Порядок байтів (Endianness) та правило Strict Aliasing

Порядок байтів визначає, як багатобайтові величини зберігаються в адресній пам’яті процесора:
- **Little-Endian**: молодший байт записується за найменшою адресою пам’яті (характерно для більшості ядер ARM Cortex-M та архітектури x86).
- **Big-Endian**: старший байт записується за найменшою адресою (типово для мережевих стеків TCP/IP – Network Byte Order, а також деяких сімейств мікроконтролерів).

Поширена наївна перевірка порядку байтів виглядає так:
```c
// НЕБЕЗПЕЧНО: потенційне порушення Strict Aliasing та некоректне приведення типів
uint32_t val = 1;
bool is_little = (*(uint8_t *)&val == 1);
```
Згідно зі стандартом ISO C (§6.5 p7) [^iso-c-n1570], правило строгої псевдонімізації (`strict aliasing rule`) забороняє доступ до об’єкта одного типу через вказівник на несумісний тип. Хоча читання через символьні типи (`char`, `unsigned char`) формально дозволене як виняток у стандарті C, подібне приведення типів (`type punning`) для довільних покажчиків або через неініціалізовані поля `union` (особливо у C++) є невизначеною поведінкою (`undefined behavior`). Оптимізатор компілятора GCC/Clang на рівнях `-O2`/`-O3` вважає, що пам’ять двох різних типів не перетинається, і має право видалити або переставити інструкції.

### Безпечні та стандартизовані методи визначення

1. **Використання функції `memcpy`**:
   Стандарт C гарантує, що будь-який об’єкт можна безпечно переглянути як масив байтів шляхом копіювання його об’єктного представлення (`object representation`, §6.2.6.1 ISO C) [^iso-c-n1570]:
   ```c
   #include <stdint.h>
   #include <stdbool.h>
   #include <string.h>

   bool is_little_endian(void) {
       uint32_t test_val = 0x01020304U;
       uint8_t bytes[sizeof(test_val)];
       memcpy(bytes, &test_val, sizeof(test_val));
       return (bytes[0] == 0x04U);
   }
   ```
   Оптимізуючий компілятор повністю розпізнає цей патерн, усуває виклик `memcpy` і під час оптимізації згортає функцію у константу `return true` (або `return false`) без жодних накладних витрат у машинному коді.

2. **Читання через покажчик на `unsigned char`**:
   Стандарт C явно визначає, що `character types` (`char`, `signed char`, `unsigned char`) мають спеціальний статус і можуть використовуватись як псевдоніми для адресації будь-якого об’єкта:
   ```c
   bool is_little_endian_char(void) {
       uint16_t test_val = 1;
       const unsigned char *p = (const unsigned char *)&test_val;
       return (*p == 1);
   }
   ```

3. **Перевірка на етапі компіляції (Compile-Time)**:
   У прошивках мікроконтролерів рантайм-перевірка майже ніколи не потрібна, оскільки архітектура відома на етапі збирання:
   - У GCC/Clang доступний вбудований макрос: `#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__`.
   - У стандарті C++20 доступний тип переліку `std::endian::native == std::endian::little` із заголовка `<bit>`.

### Портативний інженерний патерн для протоколів

У надійному embedded-коді рекомендується взагалі відмовитися від залежності від порядкової схеми мікроконтролера. При передачі даних по UART, CAN, BLE або збереженні у Flash серіалізацію слід реалізовувати через явні побітові зсуви:
```c
// Перетворення 32-бітного слова у Big-Endian (Network Byte Order)
void serialize_u32_be(uint8_t *buf, uint32_t val) {
    buf[0] = (uint8_t)(val >> 24);
    buf[1] = (uint8_t)(val >> 16);
    buf[2] = (uint8_t)(val >> 8);
    buf[3] = (uint8_t)(val);
}
```
Такий код є 100% стандартизованим, переносимим між будь-якими CPU, не порушує вирівнювання чи аліасинг, а оптимізатор для ARM автоматично згортає його в одну інструкцію зміни порядку байтів `REV` та запис у буфер.
