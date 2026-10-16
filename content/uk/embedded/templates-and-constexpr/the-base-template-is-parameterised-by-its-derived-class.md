---
id: emb-tmplcx-0011
title: "Що таке CRTP і навіщо він у шаблонах?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-static-cast
    title: "C++ working draft: Static cast ([expr.static.cast])"
    url: https://eel.is/c++draft/expr.static.cast
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
---

## Question code

```cpp
template<typename D>
class SensorBase {
public:
  int read_filtered() {
    int raw = static_cast<D*>(this)->read_raw();
    return (raw + last_) / 2;
  }
private:
  int last_ = 0;
};
```

## Short answer

**CRTP (curiously recurring template pattern): base – шаблон, параметризований похідним: `class Derived : public Base<Derived>`.**

Base викликає методи похідного через `static_cast<D*>(this)`; такий downcast коректний лише тоді, коли base є підоб’єктом справжнього `D`.[^cpp-draft-expr-static-cast] Клас без virtual-функцій не має vptr.[^itanium-cxx-abi] Тому vtable для нього немає, а тип `D` відомий уже на етапі компіляції.

Правило: CRTP дає статичний поліморфізм без virtual dispatch, але не підходить, коли тип обирається в runtime.

## Detailed explanation

У прикладі `SensorBase<D>` не має virtual-функцій і викликає `read_raw()` через `static_cast<D*>(this)`. Для кожного `D` є окремий клас `SensorBase<D>`, де тип уже відомий, тож виклик має конкретну ціль. Але `static_cast` тут не перевіряє тип під час виконання: якщо `this` не є підоб’єктом об’єкта `D`, поведінка undefined.[^cpp-draft-expr-static-cast] Тому база має бути базою саме того класу, який її параметризує: `class Temp : public SensorBase<Temp>`, а не `SensorBase<Pressure>`.

Перевірено на GCC 13.3 (x86-64): без оптимізації (`-O0`) виклики `read_filtered` і `read_raw` лишаються, але vtable немає. З `-O2` обидва виклики вбудовано, і від `read_filtered` лишаються читання `last_` і арифметика; так само поводиться Clang. Вбудовування – рішення оптимізатора, стандарт його не гарантує.

Головне обмеження: `SensorBase<Temp>` і `SensorBase<Pressure>` – різні класи без спільної бази, тож їх не покласти в один масив і не передати як один `SensorBase&`. Коли тип обирається в runtime (за конфігурацією чи протоколом), потрібні virtual-функції або спільний інтерфейс. Помилка в `read_raw` з’являється лише тоді, коли `read_filtered` буде використано, бо визначення member-функцій шаблону інстанціюються за потреби.[^cpp-draft-temp-inst]

```cpp
template <typename D>
class SensorBase {
public:
  int read_filtered() {
    int raw = static_cast<D*>(this)->read_raw();
    return (raw + last_) / 2;
  }
private:
  int last_ = 0;
};

// Illustrative: a real driver would read a register here.
class Temp : public SensorBase<Temp> {
public:
  int read_raw() { return 100; }
};

int use_temp(Temp& t) { return t.read_filtered(); }
```

**Типові помилки:**

- Вважати CRTP повною заміною virtual: коли тип відомий лише в runtime, спільної бази немає, і потрібен інший механізм.
- Написати `class Temp : public SensorBase<Pressure>`: якщо `Pressure` не походить від `SensorBase<Pressure>`, `static_cast` не скомпілюється; якщо походить, це undefined behavior.[^cpp-draft-expr-static-cast]
- Не реалізувати `read_raw` і не викликати `read_filtered`: помилки компіляції не буде.[^cpp-draft-temp-inst]
