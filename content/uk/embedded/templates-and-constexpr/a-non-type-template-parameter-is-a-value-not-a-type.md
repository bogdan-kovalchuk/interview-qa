---
id: emb-tmplcx-0004
title: "Що таке non-type template parameter (NTTP)?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-param
    title: "C++ working draft: Template parameters ([temp.param])"
    url: https://eel.is/c++draft/temp.param
  - source_id: cpp-draft-temp-arg-nontype
    title: "C++ working draft: Constant template arguments ([temp.arg.nontype])"
    url: https://eel.is/c++draft/temp.arg.nontype
  - source_id: cpp-draft-expr-add
    title: "C++ working draft: Additive operators ([expr.add])"
    url: https://eel.is/c++draft/expr.add
---

## Short answer

**Параметр шаблону, який є значенням, а не типом, – напр. `size_t N`.**[^cpp-draft-temp-param]

У `CircularBuffer<T, N>` розмір `N` є NTTP: його аргумент має бути константним виразом, тож розмір масиву `buf_[N]` відомий на етапі компіляції.[^cpp-draft-temp-arg-nontype] Правило: NTTP записує розмір або конфігурацію в тип, тому `CircularBuffer<uint8_t, 64>` і `CircularBuffer<uint8_t, 128>` – різні типи.[^iso-cpp-n4861]

## Detailed explanation

Шаблон може мати параметри двох видів: параметр-тип (`typename T`) і параметр-значення, який оголошується як звичайна змінна в списку шаблону, наприклад `std::size_t N`. У поточному стандарті параметр-значення називається constant template parameter; термін NTTP означає те саме.[^cpp-draft-temp-param]

Аргумент для такого параметра має бути константним виразом, тобто значенням, відомим компілятору під час компіляції. Для `CircularBuffer<std::uint8_t, 64>` це `64`. Якщо ж `n` отримано з `read_config()` під час роботи, компілятор видасть помилку: значення `n` не можна використати в константному виразі.[^cpp-draft-temp-arg-nontype]

Значення впливає на тип. `CircularBuffer<std::uint8_t, 64>` і `CircularBuffer<std::uint8_t, 128>` – різні класи, тож і інстанціації різні, як у питанні qid:emb-tmplcx-0002. Розмір масиву `buf_[N]` відомий під час збирання, без жодного параметра, що обчислюється під час роботи.

Ілюстративний приклад:

```cpp
#include <cstddef>
#include <cstdint>

template <typename T, std::size_t N>
class CircularBuffer { T buf_[N]; };

CircularBuffer<std::uint8_t, 64> rx;    // N is 64: a constant expression
CircularBuffer<std::uint8_t, 128> tx;   // another type, another instantiation

// int n = read_config();
// CircularBuffer<std::uint8_t, n> bad; // error: n is not a constant expression
```

NTTP не додає перевірки індексів. Арифметика вказівників за межі масиву з `N` елементів дає undefined behavior, тож `buf_[i]` з `i >= N` не стає безпечним через те, що `N` є параметром шаблону.[^cpp-draft-expr-add]

**Типові помилки:**

- Передавати в NTTP значення, відоме лише під час роботи, і очікувати, що компілятор його прийме.
- Вважати, що NTTP сама перевіряє межі масиву: вихід за межі – undefined behavior, і компілятор не зобов’язаний його зупинити.
