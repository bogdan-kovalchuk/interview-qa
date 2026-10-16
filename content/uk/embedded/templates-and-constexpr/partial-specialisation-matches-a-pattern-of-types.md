---
id: emb-tmplcx-0010
title: "Що таке partial specialization шаблону?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
---

## Question code

```cpp
template<typename T>
class Buffer<T*> {
  // для всіх вказівникових типів
};
```

## Short answer

**Спеціалізація за патерном (напр., усі вказівники), а не одним типом.**

`Buffer<T*>` застосовується до будь-якого типу вигляду `T*` і замінює primary template лише для таких аргументів.[^cpp-draft-temp-spec-partial-general] Правило: partial specialization – коли поведінка спільна для цілого класу типів, заданого патерном.

## Detailed explanation

Primary template описує загальний випадок, а partial specialization – альтернативне визначення для аргументів, що збігаються з патерном. Для `Buffer<int*>` патерн `T*` збігається з `T = int`, тож використовується спеціалізація. Для `Buffer<int>` патерн не збігається, і діє primary template.[^cpp-draft-temp-spec-partial-general] Параметр `T` у патерні визначається самим збігом: для `Buffer<const char*>` він дорівнює `const char`.

Практичний сенс – одна назва класу з різною реалізацією для цілого сімейства типів. У прикладі `Buffer<T>` зберігає значення, а `Buffer<T*>` зберігає сам вказівник і не розіменовує його. Виклик `put(...)` виглядає однаково, але код різний, і тип аргументу вирішує, яку версію буде вибрано.

```cpp
template <typename T>
class Buffer {                       // primary template: any T
public:
    void put(T value) { last_ = value; }
private:
    T last_{};
};

template <typename T>
class Buffer<T*> {                   // partial specialization: any pointer type T*
public:
    void put(T* p) { last_ptr_ = p; }
private:
    T* last_ptr_ = nullptr;
};

void use() {
    Buffer<int> a;      a.put(1);    // primary
    int x = 0;
    Buffer<int*> b;     b.put(&x);   // Buffer<T*> with T = int
    Buffer<const char*> c;           // Buffer<T*> with T = const char
    (void)c;
}
```

**Типові помилки:**

- Вважати, що `Buffer<T*>` стосується й посилань (`int&`), і масивів (`int[4]`): це інші типи, для них діє primary template або окрема спеціалізація.
- Змінити primary template і очікувати, що спеціалізація теж зміниться: вона є окремим визначенням і правиться окремо.
- Плутати `template<> class Buffer<int*>` з partial specialization: перша задає визначення лише для `int*`, а друга – для всіх вказівників.[^cpp-draft-temp-expl-spec]
