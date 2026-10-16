---
id: emb-cppoop-0003
title: "Що таке неявний вказівник `this`?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-prim-this
    title: "C++ working draft: This ([expr.prim.this])"
    url: https://eel.is/c++draft/expr.prim.this
  - source_id: cpp-draft-over-match-funcs
    title: "C++ working draft: Candidate functions and argument lists ([over.match.funcs.general])"
    url: https://eel.is/c++draft/over.match.funcs.general
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
---

## Short answer

**`this` – вказівник на об’єкт, для якого викликано нестатичну member-функцію.**[^cpp-draft-expr-prim-this] Для overload resolution стандарт моделює його як додатковий перший параметр, тому `obj.set()` працює приблизно як виклик, що отримує `&obj`.[^cpp-draft-over-match-funcs] Тип `this` – `X*`, а в `const`-методі `const X*`; у `static`-функції `this` немає. Для не-`virtual` методу це близько до C-функції з явним вказівником на структуру, і оптимізатор часто прибирає різницю, але стандарт цього не гарантує.

## Detailed explanation

Нестатична member-функція працює над конкретним об’єктом, тож їй треба якось знати, над яким саме. Кожне звернення до поля в тілі методу – наприклад `odr_` – означає `this->odr_`; префікс компілятор підставляє сам. Стандарт визначає `this` як prvalue типу «вказівник на `X`» (з cv-кваліфікацією методу), значення якого – адреса об’єкта, для якого функцію викликано.[^cpp-draft-expr-prim-this] Оскільки це prvalue, `this` не змінна: йому не можна присвоїти інше значення, а `static`-функція, що не прив’язана до об’єкта, його не має.

Щоб описати overload resolution, стандарт вважає, що implicit object member function має додатковий перший параметр, який представляє об’єкт виклику; для `const`-методу це «lvalue reference to `const X`». Водночас сам текст зазначає, що ці перетворення існують лише для опису й реалізація не зобов’язана їх виконувати.[^cpp-draft-over-match-funcs] Тому «прихований перший параметр» – слушна модель для розуміння, а не гарантія кодогенерації. На практиці її зручно перевіряти в асемблері цільового компілятора.

Ось ілюстративна еквівалентність; це концептуальна модель, а не те, що буквально робить компілятор:

```cpp
struct Gpio {
  volatile uint32_t *odr_;
  uint8_t pin_;
  void set() const { *odr_ |= (UINT32_C(1) << pin_); }  // this: const Gpio*
};

// Концептуально те саме, що вільна функція з явним вказівником:
void gpio_set(const Gpio *self) {
  *self->odr_ |= (UINT32_C(1) << self->pin_);
}
```

Порівняння з C-функцією найточніше для не-`virtual` методів, де ціль виклику відома на етапі компіляції, тож оптимізатор може обробити їх так само, як звичайну функцію. Для `virtual`-функції реальний виклик залежить ще й від динамічного типу об’єкта (dynamic binding),[^cpp-draft-class-virtual] тому «нульової різниці» з C-функцією там чекати не варто.

**Типові помилки:**

- Вважати, що `const`-метод робить незмінним усе, на що вказує об’єкт: `this` стає `const X*`, але через вказівник-член, як `odr_`, пишуть далі (див. qid:emb-cppoop-0005).
- Намагатися використати `this` у `static`-функції чи думати, що його можна змінити.
- Обіцяти «нульовий оверхед» методу без перевірки: це залежить від компілятора, прапорців оптимізації та `virtual`.
