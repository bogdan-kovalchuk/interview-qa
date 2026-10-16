---
id: emb-cppoop-0032
title: "Який порядок ініціалізації членів у конструкторі?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-base-init
    title: "C++ working draft: Initializing bases and members ([class.base.init])"
    url: https://eel.is/c++draft/class.base.init
  - source_id: cpp-draft-basic-indet
    title: "C++ working draft: Indeterminate and erroneous values ([basic.indet])"
    url: https://eel.is/c++draft/basic.indet
  - source_id: cppcg-c47-member-init-order
    title: "C++ Core Guidelines: C.47 – Define and initialize data members in the order of member declaration"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c47-define-and-initialize-data-members-in-the-order-of-member-declaration
  - source_id: gcc-cpp-dialect-options
    title: "GCC 16.1.0: Options Controlling C++ Dialect (-Wreorder)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/C_002b_002b-Dialect-Options.html#index-Wreorder
---

## Short answer

**Нестатичні члени ініціалізуються в порядку оголошення в класі, а не в порядку запису в списку ініціалізації.**[^cpp-draft-class-base-init] Тому якщо `a_` оголошено перед `b_`, а список має вигляд `: b_{x}, a_{b_ + 1}`, першим ініціалізується `a_` і читає ще не ініціалізований `b_` – це помилка, зазвичай undefined behavior. Захист: пиши список у порядку оголошення; GCC попередить через `-Wreorder`, який вмикає `-Wall`.[^gcc-cpp-dialect-options]

## Detailed explanation

Конструктор створює об’єкт у фіксованому порядку: спочатку бази, потім нестатичні члени в порядку, у якому їх оголошено в класі, і лише тоді виконується тіло конструктора. Стандарт прямо каже, що для членів це діє незалежно від порядку mem-initializer.[^cpp-draft-class-base-init] Причина в знищенні: деструктор в класу один, і він має знищувати підоб’єкти у зворотному порядку ініціалізації, а списки в різних конструкторах одного класу можуть відрізнятися. Тому порядок береться з оголошення, а не зі списку.[^cpp-draft-class-base-init]

Пастка виникає, коли один член використовує інший. Список ініціалізації читається як послідовність кроків, але такою не є: компілятор лише підставляє кожному члену його ініціалізатор у порядку оголошення. Якщо `a_` оголошено першим, а його ініціалізатор читає `b_`, то `b_` ще не ініціалізований, і читання його значення – indeterminate value. Загалом це undefined behavior;[^cpp-draft-basic-indet] для об’єктів з automatic storage чернетка C++26 натомість вводить erroneous behavior з визначеним реалізацією значенням, але й тоді це помилка програми.[^cpp-draft-basic-indet]

Ілюстративний приклад:

```cpp
#include <cstdint>

class Dev {
  std::uint32_t a_;   // оголошено першим, тож ініціалізується першим
  std::uint32_t b_;

public:
  // BUG: a_ читає b_ до його ініціалізації
  explicit Dev(std::uint32_t x) : b_{x}, a_{b_ + 1} {}
};

class DevFixed {
  std::uint32_t a_;
  std::uint32_t b_;

public:
  // порядок збігається з оголошенням, a_ не залежить від b_
  explicit DevFixed(std::uint32_t x) : a_{x + 1}, b_{x} {}
};
```

GCC попереджає, коли порядок mem-initializer не збігається з порядком виконання; це `-Wreorder`, який входить до `-Wall`.[^gcc-cpp-dialect-options] Він перевіряє лише збіг порядку, а не залежності: якщо список збігається з оголошенням, але `a_{b_}` оголошено раніше за `b_`, розбіжності порядку немає, і `-Wreorder` мовчить, хоч `b_` усе ще не ініціалізований. Core Guidelines радять оголошувати й ініціалізувати члени в одному порядку.[^cppcg-c47-member-init-order]

**Типові помилки:**

- Вважати, що порядок у списку ініціалізації визначає порядок виконання.
- Ігнорувати або вимикати `-Wreorder`: попередження вказує саме на цю пастку.
- Вважати, що `-Wreorder` знайде кожну залежність між членами: він порівнює лише порядок списку й оголошення.
- Змінити порядок оголошення членів під час рефакторингу, не перевіривши залежностей між ними: це змінює порядок ініціалізації.
