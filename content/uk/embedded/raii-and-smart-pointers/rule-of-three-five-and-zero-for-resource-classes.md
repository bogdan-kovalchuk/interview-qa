---
id: emb-raii-0025
title: "Що таке rule of three / five / zero?"
description: "Якщо клас керує ресурсом – визнач (або видали) усі спецфункції разом."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
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
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що неявний move constructor не оголошується, якщо в класі є user-declared деструктор, а неявний copy constructor за такого деструктора deprecated. Про оптимізацію й згенерований код не йдеться."
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що copy-конструктор і copy-присвоєння unique_ptr видалені, а переміщення дозволені; деструктор викликає deleter лише для ненульового вказівника. Розміру не задає."
---

## Short answer

**Якщо клас керує ресурсом – визнач (або видали) усі спецфункції разом.**

Rule of three: dtor, copy ctor, copy assign; rule of five (C++11) додає move ctor і move assign. Rule of zero: не керуй ресурсами вручну – нехай члени-RAII (smart pointers, guards) роблять це, і не пиши жодної спецфункції. Оголошений деструктор не дає неявного move constructor, тож переміщення піде через copy.[^cpp-draft-class-copy-ctor]

Правило: прагни rule of zero; якщо керуєш ресурсом сам – не лишай дефолтні copy, що можуть призвести до double-free.

## Detailed explanation

Деструктор, copy constructor і copy assignment разом описують володіння ресурсом. Якщо клас тримає сирий хендл і цих функцій не пише, компілятор згенерує copy-операції, які копіюють члени поелементно. Два об’єкти тоді вказують на один ресурс, і обидва звільнять його у своєму деструкторі. Неявний copy constructor за наявності user-declared деструктора лишається, але вже deprecated.[^cpp-draft-class-copy-ctor]

C++11 додав move-операції, тож правило п’яти вимагає визначити і їх. Важлива деталь: оголошений деструктор не дає неявного move constructor, тож `std::move` тихо переходить до copy constructor.[^cpp-draft-class-copy-ctor] Нижче клас, що визначає всі п’ять операцій: copy видалено, move реалізовано.

```cpp
// Illustrative: Handle, open_h and close_h stand in for a vendor driver API.
class SpiChannel {
public:
    explicit SpiChannel(int id) : h_(open_h(id)) {}
    ~SpiChannel() { if (h_) close_h(h_); }

    SpiChannel(const SpiChannel&) = delete;
    SpiChannel& operator=(const SpiChannel&) = delete;

    SpiChannel(SpiChannel&& o) noexcept : h_(o.h_) { o.h_ = nullptr; }
    SpiChannel& operator=(SpiChannel&& o) noexcept {
        if (this != &o) {
            if (h_) close_h(h_);
            h_ = o.h_;
            o.h_ = nullptr;
        }
        return *this;
    }
private:
    Handle* h_;
};
```

Найкраще взагалі не писати спецфункцій. Член `std::unique_ptr<Handle, decltype(&close_h)> h_;` сам викликає `close_h`, не копіюється, але переміщується.[^cpp-draft-unique-ptr-single] Оскільки клас не оголошує жодної спецфункції, move-операції він отримує неявно, а copy стає видаленою через член.[^cpp-draft-class-copy-ctor]

Rule of zero лишається доступним і зі stateful deleter (його зберігає сам `unique_ptr`; росте лише `sizeof`). До правила п’яти повертаються, коли ресурс не вкладається в готовий RAII-тип: наприклад, потрібен нестандартний протокол перенесення чи звільнення. Сирий `Handle*` як член без деструктора веде до витоку ресурсу, бо нічого його не закриє.

**Типові помилки:**

- Визначити деструктор і не визначити move: переміщення мовчки стає копіюванням, і два об’єкти закривають один хендл.[^cpp-draft-class-copy-ctor]
- Видалити copy-операції і забути про move: клас стає непереміщуваним, і повернення його локальної змінної з функції не компілюється.[^cpp-draft-class-copy-ctor]
- Тримати сирий `Handle*` як член без деструктора: ресурс протікає.

## Sources

<!-- generated from frontmatter -->
