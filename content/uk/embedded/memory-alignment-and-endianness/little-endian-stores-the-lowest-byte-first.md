---
id: emb-align-0012
title: "Як у пам'яті little-endian машини ляже `0xDEADBEEF`?"
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

## Short answer

**`EF BE AD DE`** (від нижчої адреси до вищої).

Little-endian розміщує найменш значущий байт за найнижчою адресою: `0xEF` за offset 0, `0xBE` за 1, `0xAD` за 2 та `0xDE` за 3.

Правило: інтерпретуй dump за показаним напрямком адрес, а не просто розвертай надрукований текст.[^embeddedinterviewlab]

## Detailed explanation

Розділи `0xDEADBEEF` на байти за значущістю: `DE`, `AD`, `BE`, `EF`. Байт `EF` містить біти від 0 до 7, тому little-endian представлення розміщує його за найнижчою адресою об'єкта. Наступні адреси містять дедалі значущіші байти:

```text
Lower address                         Higher address
base + 0   base + 1   base + 2   base + 3
0xEF       0xBE       0xAD       0xDE
```

Якщо debugger показує пам'ять від нижчих адрес ліворуч, рядок матиме вигляд `EF BE AD DE`. Деякі інструменти групують байти у слова або обирають інший напрямок показу, тому перед інтерпретацією завжди перевіряй підписи адрес.

Твердження передбачає 32-бітний unsigned-об'єкт зі значенням `0xDEADBEEF` і little-endian цільову платформу. C визначає object representation як `sizeof` байтів, але залишає порядок байтів звичайних цілих чисел implementation-defined.[^iso-c-n1570] Саме шістнадцяткове значення не розвертається: завантаження всіх чотирьох байтів через належно вирівняний об'єкт `uint32_t` на тій самій платформі дає `0xDEADBEEF`.

Коли байти належать зовнішньому формату, декодуй їх за правилами цього формату, а не перетворюй buffer на `uint32_t *`. Явне декодування усуває припущення і про alignment, і про host endianness. Матеріал LearnCpp про розміри об'єктів дає базове пояснення байтового зберігання,[^learncpp-object-sizes] а aCode пропонує ширшу українську дорожню карту подальшого вивчення C і C++.[^acode-cpp-next]
