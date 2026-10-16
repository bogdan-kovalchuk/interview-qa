---
id: emb-cppoop-0029
title: "Чим static member function відрізняється від звичайної?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-static
    title: "C++ working draft: Static members ([class.static])"
    url: https://eel.is/c++draft/class.static
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
  - source_id: cpp-draft-expr-unary-op
    title: "C++ working draft: Unary operators ([expr.unary.op])"
    url: https://eel.is/c++draft/expr.unary.op
  - source_id: cpp-draft-dcl-link
    title: "C++ working draft: Linkage specifications ([dcl.link])"
    url: https://eel.is/c++draft/dcl.link
---

## Short answer

**Static member function не має `this`** – вона не прив’язана до екземпляра.[^cpp-draft-class-static] Тому її можна викликати як `Class::func()` без об’єкта, але вона не може напряму звертатися до нестатичних членів. Адреса такої функції – звичайний вказівник на функцію, а не pointer-to-member,[^cpp-draft-expr-unary-op] тож її часто використовують як callback-thunk для C API (application programming interface), передаючи об’єкт через `void*`-контекст. Типи функцій мають language linkage, тож для строгої C-сумісності інколи потрібна окрема `extern "C"` wrapper-функція.[^cpp-draft-dcl-link]

## Detailed explanation

Нестатична member function завжди викликається для якогось об’єкта, і `this` – вказівник саме на нього.[^cpp-draft-expr-prim-this] Static member function з жодним об’єктом не пов’язана: `this` у ній немає, і вона не може бути `const`, `volatile` чи `virtual`.[^cpp-draft-class-static] Викликати її можна як `Class::func()`, не маючи екземпляра; запис `obj.func()` теж дозволений, але тоді об’єктний вираз лише обчислюється й до функції не передається.[^cpp-draft-class-static] Звідси головне обмеження: щоб звернутися до нестатичного члена, їй потрібен явний об’єкт (вказівник чи посилання), отриманий інакше.

Це й робить static member function придатною як callback для C API. Бібліотека, RTOS чи драйвер таймера очікує вільну функцію на кшталт `void (*)(void *ctx)`. Адреса static member function – звичайний «pointer to T» на функцію, а `&Class::method` для нестатичного методу дає pointer to member function – інший тип, ніж звичайний вказівник на функцію.[^cpp-draft-expr-unary-op] Тому типовий патерн такий: static-функція приймає `void *ctx`, перетворює його назад на вказівник на об’єкт і викликає звичайний метод.

Ілюстративний приклад (компілюється з `-std=c++17`; `timer_set_callback` – вигадане C API):

```cpp
extern "C" {
using irq_cb_t = void (*)(void *ctx);
void timer_set_callback(irq_cb_t cb, void *ctx);
}

class Led {
public:
  void toggle() { on_ = !on_; }
  void attach() { timer_set_callback(&Led::thunk, this); }

private:
  static void thunk(void *ctx) { static_cast<Led *>(ctx)->toggle(); }
  bool on_ = false;
};
```

Лишається тонкість із linkage. За стандартом функції й типи функцій за замовчуванням мають C++ language linkage, а типи функцій з різним language linkage – різні типи, навіть якщо вони в іншому однакові.[^cpp-draft-dcl-link] Тож тип, який C-заголовок описує як `extern "C"`-вказівник на функцію, формально не те саме, що тип static member function. Для суворої відповідності пишуть вільну `extern "C"` функцію-обгортку, що викликає static member. На практиці GCC 13 і Clang компілюють приклад вище без помилок і попереджень, але це поведінка компілятора, а не гарантія стандарту.

**Типові помилки:**

- Передати `&Led::toggle` (нестатичний метод) як C callback: це pointer to member function, а не вказівник на функцію.[^cpp-draft-expr-unary-op]
- Перетворити `void *ctx` на інший тип, ніж той, з якого його отримали: це помилка, зазвичай undefined behavior.
- Знищити об’єкт, поки callback ще зареєстрований: `ctx` стає висячим вказівником.
- Покладатися на те, що компілятор прийме static member замість `extern "C"` callback скрізь: стандарт цього не гарантує.[^cpp-draft-dcl-link]
