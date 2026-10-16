---
id: emb-fnptr-0037
title: "Чи можна передати C++ non-capturing lambda у C-style callback?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cpp-lambda-closure
    title: "C++ working draft: Closure types"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
---

## Short answer

**Так, якщо lambda не має captures і сигнатура сумісна.**

Звичайна non-generic lambda без captures має conversion function до pointer to function із сумісними параметрами й типом повернення. Capturing lambda такої conversion function не має; для стану передавай context окремо або використовуй C++ callback abstraction.[^cpp-lambda-closure]

Для C HAL callback перевір також calling convention та точну сигнатуру, визначені API.[^cpp-lambda-closure]

## Detailed explanation

Lambda-вираз створює closure object з окремим типом, а його виклик описує `operator()`. Якщо lambda не має capture і є non-generic, стандарт C++ задає conversion function до pointer to function з тими самими типами параметрів і повернення, що й у call operator. Тому її можна використати там, де очікується сумісний function pointer.[^cpp-lambda-closure]

Це перетворення не означає, що будь-яку lambda можна передати будь-якому C callback. Наприклад, `void (*)(int)` вимагає один `int`-параметр і `void` результат; lambda з іншою сигнатурою не підходить. Generic lambda теж має окрему conversion function template, тож конкретний function pointer має визначити сумісну спеціалізацію.[^cpp-lambda-closure]

Практична користь у C++-обгортках над C HAL: коротку дію без стану можна записати поруч із місцем реєстрації callback. Якщо код має доступ до об’єкта, локальної змінної чи іншого стану через capture, ця lambda вже не конвертується у звичайний function pointer. Тоді потрібен API з context pointer або callback-об’єкт, який зберігає стан.[^cpp-lambda-closure]

**Типова помилка:** вважати, що відсутність квадратних дужок у виклику функції якось додає доступ до локальних змінних. Capture визначається самим lambda expression; порожній список `[]` означає, що захопленого стану немає.

Приклад:

```cpp
static void handle(int code) { (void)code; }
void (*callback)(int) = [](int code) { handle(code); };
```

Такий приклад ілюструє перетворення лише за умови, що `handle` видимий і виклик сумісний з обмеженнями callback API. Якщо API має C linkage boundary, передавання C++ function pointer не змінює автоматично calling convention чи ABI домовленості API.[^cpp-lambda-closure]
