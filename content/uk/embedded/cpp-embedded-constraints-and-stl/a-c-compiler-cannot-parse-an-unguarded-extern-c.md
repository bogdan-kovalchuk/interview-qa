---
id: emb-cppstl-0018
title: "Trap: що станеться зі спільним header без `#ifdef __cplusplus` guard?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">C-компілятор зустріне `extern "C"` і впаде з syntax error</span> – це C++-конструкція, невідома C.

Header, призначений для обох мов, без guard-обгортки зламає C-збірку.

Захист: завжди обгортай `extern "C" { ... }` у `#ifdef __cplusplus ... #endif` з обох боків.[^embeddedinterviewlab]

## Detailed explanation

### Чому C-компілятор зазнає збою при обробці `extern "C"`

Специфікація мовного зв’язування `extern "C"` є фундаментальною частиною граматики мови C++ ([dcl.link])[^iso-cpp-n4861]. Вона повідомляє C++ компілятору, що оголошені функції повинні мати C linkage, тобто не піддаватися декоруванню імен (name mangling).

У мові C граматика абсолютно інша: стандарт ISO C[^iso-c-n1570] не передбачає наявності строкового літерала після специфікатора класу зберігання `extern`. Коли чистий C-компілятор (наприклад `arm-none-eabi-gcc` або `clang` у режимі трансляції файлів `.c`) зустрічає рядок:
```c
extern "C" {
```
він розпізнає ключове слово `extern`, але очікує після нього тип даних або ідентифікатор змінної/функції. Отримавши строковий літерал `"C"`, препроцесор і парсер завершують роботу з фатальною синтаксичною помилкою:
```text
error: expected identifier or '(' before string constant
```
або
```text
error: unknown type name 'extern'
```

### Стандартне вирішення: ідіома `#ifdef __cplusplus`

Згідно зі стандартом C++[^iso-cpp-n4861], будь-який сумісний компілятор C++ автоматично визначає макрос препроцесора `__cplusplus` (значення якого відповідає версії стандарту, наприклад `201703L` для C++17). У компіляторах мови C цей макрос гарантовано не визначений.

Тому будь-який спільний заголовний файл (наприклад, драйвер периферії HAL, API RTOS або бібліотека математичних функцій), призначений для використання як у модулях `.c`, так і в `.cpp`, обов’язково повинен обгортати блок зв’язування в умовну компіляцію:
```c
#ifndef SENSOR_API_H
#define SENSOR_API_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

void sensor_init(void);
bool sensor_read_data(int16_t* out_temp, int16_t* out_humidity);

#ifdef __cplusplus
}
#endif

#endif /* SENSOR_API_H */
```

### Підводні камені та типові помилки у спільних заголовках

1. **Включення директив `#include` всередині блоку `extern "C"`**:
   Якщо помістити директиви `#include` всередину відкритої дужки `extern "C" {`, усі оголошення з підключених заголовних файлів (включно зі стандартними C++ заголовками на кшталт `<algorithm>` чи шаблонами) отримають зв’язування C linkage, що призведе до помилок компіляції (`template with C linkage`). Усі директиви `#include` повинні передувати директиві `extern "C"`.
2. **Невідповідність типів між C та C++**:
   У C дозволене неявне приведення `void*` до інших покажчиків, тоді як у C++ це заборонено. Якщо спільний заголовок містить inline-функції, вони повинні містити явне приведення типів або макроси приведення, сумісні з обома стандартами.
3. **Забута закриваюча фігурна дужка**:
   Якщо блок `#ifdef __cplusplus` відкриває дужку `{`, але наприкінці файлу забуто симетричний блок закриття, компілятор C++ видасть неочевидну помилку про несподіваний кінець файлу (`expected '}' at end of input`), а C-компілятор збірки взагалі не помітить проблеми, що ускладнює діагностику.
