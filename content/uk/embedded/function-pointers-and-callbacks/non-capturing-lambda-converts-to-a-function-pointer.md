---
id: emb-fnptr-0037
title: "Чи можна передати C++ non-capturing lambda у C-style callback?"
description: "Так, якщо lambda не має captures і сигнатура сумісна."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: cpp-lambda-closure
    title: "C++ working draft: Closure types"
    url: https://eel.is/c++draft/expr.prim.lambda.closure
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Правила conversion для non-capturing lambdas і closure type; не визначає конкретні ABI чи вимоги C HAL."
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

## Sources

<!-- generated from frontmatter -->
