---
id: emb-tmplcx-0001
title: "Що таке function template і чим він кращий за макрос?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-cpp-replace
    title: "C++ working draft: Replacement of macros ([cpp.replace])"
    url: https://eel.is/c++draft/cpp.replace
  - source_id: cpp-draft-expr-call
    title: "C++ working draft: Function call ([expr.call])"
    url: https://eel.is/c++draft/expr.call
  - source_id: cpp-draft-temp-deduct-call
    title: "C++ working draft: Deducing template arguments from a function call ([temp.deduct.call])"
    url: https://eel.is/c++draft/temp.deduct.call
---

## Question code

```cpp
template<typename T>
T clamp(T v, T lo, T hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}
```

## Short answer

**Одне визначення, що працює для будь-якого типу, який підтримує операції з тіла, – з повним type checking.**

На відміну від макроса, який лише підставляє текст аргументів,[^cpp-draft-cpp-replace] шаблон обчислює кожен аргумент рівно один раз, без double evaluation.[^cpp-draft-expr-call] Якщо аргументи дають різні виводи для T, виклик відхиляється.[^cpp-draft-temp-deduct-call]

Правило: function template зазвичай кращий за function-like макрос, але макроси лишаються для stringizing (`#`) і склеювання токенів (`##`).[^cpp-draft-cpp-replace][^embeddedinterviewlab]

## Detailed explanation

Function template – це опис функції з параметром типу. Компілятор виводить T з аргументів виклику і створює конкретну функцію для цього типу. Якщо аргументи дають різні виводи для T, виведення не вдається і компіляція зупиняється з помилкою, тобто перевірка типів спрацьовує саме на виклику.[^cpp-draft-temp-deduct-call]

Макрос працює інакше. Препроцесор підставляє в список заміни послідовність токенів аргументу, а не його значення, і типів не знає.[^cpp-draft-cpp-replace] Тому аргумент із побічним ефектом, як `x++`, виконується стільки разів, скільки параметр зустрічається в тілі. Ілюстративний приклад (використовує `clamp` із Question code):

```cpp
#define CLAMP_MACRO(v, lo, hi) ((v) < (lo) ? (lo) : ((v) > (hi) ? (hi) : (v)))

void demo() {
  int x = 5;
  int a = CLAMP_MACRO(x++, 0, 10);  // a == 7, x == 8: x++ ran three times
  int y = 5;
  int b = clamp(y++, 0, 10);        // b == 5, y == 6: argument used once
  // clamp(1, 2, 3.0);              // error: conflicting deduction for T
}
```

Макрос дає `a == 7` і `x == 8`, бо `x++` виконався тричі. Шаблон дає `b == 5` і `y == 6`: його параметр `v` ініціалізується значенням аргументу один раз.[^cpp-draft-expr-call] Той самий `clamp` відхиляє виклик `clamp(1, 2, 3.0)`, тоді як макрос з такими аргументами компілюється без помилки.

Шаблон не робить функцію безтиповою. Тіло має підтримувати операції, які використовує: `clamp` вимагає `<` і `>` для T, тож тип без них не пройде компіляцію під час інстанціації. Макроси лишаються потрібними там, де потрібні `#` або `##`; шаблон цього не вміє.[^cpp-draft-cpp-replace]

**Типові помилки:**

- Вважати, що шаблон працює з будь-яким типом без вимог до операцій у тілі.
- Замінювати макрос шаблоном там, де потрібні `#` (stringizing) або `##` (склеювання токенів).
- Очікувати, що `clamp(1, 2, 3.0)` неявно узгодить `int` і `double`: T має вивестися однаково з усіх параметрів, інакше виклик відхиляється.
