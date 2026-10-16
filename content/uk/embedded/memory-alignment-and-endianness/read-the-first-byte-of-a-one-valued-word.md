---
id: emb-align-0016
title: "Як визначити endianness у runtime?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: learncpp-object-sizes
    title: "Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Question code

```c
bool is_little_endian(void) {
    const uint32_t word = 1;
    unsigned char first;
    memcpy(&first, &word, sizeof first);
    return first == 1;
}
```

## Short answer

**Якщо байт за найнижчою адресою дорівнює `1`, representation типу `uint32_t` є little-endian.**

У значенні `1` установлений лише найменш значущий байт. Копіювання першого байта об'єкта в `unsigned char` дає `0x01` на звичайній little-endian платформі й `0x00` на звичайній big-endian платформі.

Правило: для цільового MCU endianness зазвичай відома на етапі компіляції; runtime-перевірка потрібна хіба що в портативних бібліотеках і тестах.[^embeddedinterviewlab]

## Detailed explanation

`memcpy` копіює байти object representation, не порушуючи правил alignment або effective type. Це також усуває різницю переносності: читання іншого члена union допускається із застереженнями в C, але не є загальним переносним способом type punning у C++.

Для `word == 1` little-endian representation зберігає `01 00 00 00` від найнижчої адреси вгору, тому функція повертає `true`. Big-endian representation зберігає `00 00 00 01`, тому вона повертає `false`. Строго кажучи, `false` означає лише «це не перевірений little-endian layout»; незвичайні mixed-endian представлення потребували б перевірки всіх чотирьох байтів.

Стандарт C визначає object representation і дозволяє копіювати його як символьні байти, але не встановлює один порядок байтів цілих чисел.[^iso-c-n1570] Отже, цей тест спостерігає реалізацію, а не встановлює гарантію мови.

У firmware для одного відомого MCU та ABI compile-time інформація про ціль зазвичай зрозуміліша й дає змогу прибрати мертві гілки conversion. Runtime-визначення корисне переважно тоді, коли один binary справді підтримує кілька host layouts, або в діагностичних тестах. Воно не визначає порядок байтів зовнішнього packet чи register; це задає відповідна специфікація.

Матеріал LearnCpp про розміри об'єктів дає додатковий контекст щодо representation bytes,[^learncpp-object-sizes] а дорожня карта aCode пропонує ширший український шлях подальшого вивчення C і C++.[^acode-cpp-next]
