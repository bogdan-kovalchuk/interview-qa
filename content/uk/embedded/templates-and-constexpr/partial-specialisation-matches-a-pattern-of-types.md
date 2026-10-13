---
id: emb-tmplcx-0010
title: "Що таке partial specialization шаблону?"
description: "Спеціалізація за патерном (напр., усі вказівники), а не одним типом."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що partial specialization є альтернативним визначенням шаблону, яке використовується замість primary template, коли аргументи збігаються з її патерном. Не описує вибір між кількома відповідними спеціалізаціями."
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що template<> задає explicit specialization для одного набору аргументів, як у прикладі з stream<char>, а не для цілого сімейства типів."
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

## Sources

<!-- generated from frontmatter -->
