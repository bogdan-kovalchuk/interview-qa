---
id: emb-cppoop-0020
title: "Що таке CRTP і яку проблему він вирішує?"
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
---

## Question code

```cpp
template <typename D>
class SensorBase {
public:
  int16_t read() {
    return static_cast<D*>(this)->read_impl();
  }
};
```

## Short answer

**Curiously Recurring Template Pattern – поліморфізм на етапі компіляції** через `static_cast` до похідного типу.

Похідний клас успадковує `SensorBase<Derived>`, а `read()` викликає `read_impl()` як звичайну (не virtual) функцію, тож vptr і vtable для цього не потрібні.[^itanium-cxx-abi] Оптимізатор може інлайнити такий виклик, але без оптимізації (`-O0`) GCC функції не інлайнить.[^gcc-optimize-options] `static_cast` коректний, лише коли об’єкт справді має тип `Derived`, інакше це undefined behavior.[^cpp-draft-expr-static-cast]

Правило: CRTP прибирає вартість dispatch (vptr, непрямий виклик), але не гарантує нульового оверхеду в цілому.

## Detailed explanation

CRTP розв’язує таку задачу: кілька типів (наприклад, датчиків) мають спільний інтерфейс і спільний код, скажімо `read()` з масштабуванням чи логуванням, але без вартості runtime-поліморфізму. Базовий клас стає шаблоном, параметризованим похідним типом: `class Temp : public SensorBase<Temp>`. Метод `read()` базового шаблону «знає», що `this` насправді вказує на `Temp`, і через `static_cast<D*>(this)` викликає `read_impl()` похідного класу. Усе вирішується під час компіляції, без таблиці.

`static_cast` тут допустимий, бо перетворення вказівника на base у вказівник на похідний клас визначене лише тоді, коли цей base справді є підоб’єктом об’єкта похідного типу; інакше undefined behavior.[^cpp-draft-expr-static-cast] У CRTP це правда за побудовою, але компілятор не перевіряє, що `D` – той самий тип, що успадкував базу: `class Pressure : public SensorBase<Temp>` скомпілюється, а виклик `read()` на об’єкті `Pressure` буде undefined behavior. Типовий захист – приватний конструктор бази й `friend D`: тоді `Pressure` не зможе створити свою базу, і помилка стане помилкою компіляції.

Щодо вартості: у Itanium C++ ABI vptr потрібен лише dynamic class, тобто класу з virtual-функціями чи virtual-базами,[^itanium-cxx-abi] а `SensorBase<D>` їх не має. Тому об’єкт не росте, а `read_impl()` викликається прямо, і ціль відома компілятору. Це дозволяє інлайнінг, але не гарантує його: без оптимізації GCC не розгортає функції inline, а `-finline-small-functions` вмикається на `-O2`, `-O3` і `-Os`.[^gcc-optimize-options] Отже, «нульовий оверхед» означає відсутність вартості dispatch, а не відсутність коду: кожен використаний метод шаблону інстанціюється окремо для кожного похідного типу.[^cpp-draft-temp-inst]

Ілюстративний приклад:

```cpp
#include <cstdint>

template <typename D>
class SensorBase {
public:
    std::int16_t read() { return static_cast<D*>(this)->read_impl(); }
};

class Temp : public SensorBase<Temp> {
    friend class SensorBase<Temp>;                    // база викликає приватний read_impl
    std::int16_t read_impl() { return 25; }
};

std::int16_t poll(Temp& t) { return t.read(); }       // прямий виклик, vtable немає
```

**Типові помилки:**

- Вважати CRTP безкоштовним за визначенням: на `-O0` GCC не інлайнить функції, тож виклик лишається call,[^gcc-optimize-options] а код base-методів дублюється для кожного похідного типу (див. qid:emb-cppoop-0022).
- Успадкувати від `SensorBase<Інший>`: `static_cast` на неправильний тип – undefined behavior.[^cpp-draft-expr-static-cast]
- Очікувати runtime-поліморфізм: `SensorBase<Temp>` і `SensorBase<Pressure>` – різні класи без спільного base, їх не покласти в один масив; для цього потрібен virtual (див. qid:emb-cppoop-0019).
- Зробити `read_impl` приватним без `friend`: база не зможе його викликати.
