---
id: emb-raii-0031
title: "Як move semantics дозволяє повертати RAII-об’єкт із функції?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-copy-elision
    title: "C++ working draft: Copy elision ([class.copy.elision])"
    url: https://eel.is/c++draft/class.copy.elision
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
---

## Short answer

**Move ctor переносить власність ресурсу без копіювання й без подвійного звільнення.**

`return guard;` для move-only типу передає handle викликачу.[^cpp-draft-class-copy-elision] Move-конструктор має залишити джерело з null handle, тож dtor джерела нічого не звільняє. Це дозволяє factory-функціям віддавати готові RAII-ресурси.

Правило: move-only RAII можна повертати з функцій; копіювання вимкнено (`= delete`), щоб уникнути подвійного звільнення.[^embeddedinterviewlab]

## Detailed explanation

Для `return guard;` з іменованим локальним об’єктом береться move-конструктор, а не copy-конструктор, і це видно навіть тоді, коли copy-конструктор недоступний. Стандарт дозволяє опустити і сам перенос: тоді об’єкт будується безпосередньо в місці призначення. Тому код має бути коректним з обома варіантами, а не покладатися на елізію, яка для іменованого об’єкта не обов’язкова.[^cpp-draft-class-copy-elision]

Move-конструктор – це конструктор, перший параметр якого має тип `X&&`.[^cpp-draft-class-copy-ctor] Його задача – перенести handle і залишити джерело в стані, з яким деструктор нічого не звільняє. У прикладі нижче це `other.p_ = nullptr` і перевірка `if (p_)` у деструкторі. Так само поводиться `unique_ptr`: після переміщення його `get()` дорівнює `nullptr`.[^cpp-draft-unique-ptr-single] Тепер володіє лише один об’єкт, тож подвійного звільнення немає.

Явний `= delete` робить намір видимим. Без нього клас, який оголошує деструктор, але не move-конструктор, отримав би неявний copy-конструктор, що копіює вказівник поверхнево; такий конструктор є застарілим. Два об’єкти з одним `p_` двічі викликали б `free_buffer`. Помилку `DmaBuffer c = b;` компілятор показує вже під час компіляції.

```cpp
#include <cstddef>
#include <cstdint>

// Illustrative: alloc_buffer and free_buffer stand for a HAL or pool API.
uint8_t* alloc_buffer(std::size_t n);
void free_buffer(uint8_t* p);

class DmaBuffer {
public:
  explicit DmaBuffer(std::size_t n) : p_(alloc_buffer(n)) {}
  ~DmaBuffer() { if (p_) free_buffer(p_); }

  DmaBuffer(const DmaBuffer&) = delete;
  DmaBuffer& operator=(const DmaBuffer&) = delete;

  DmaBuffer(DmaBuffer&& other) noexcept : p_(other.p_) { other.p_ = nullptr; }
  // move assignment omitted for brevity

private:
  uint8_t* p_;
};

DmaBuffer make_buffer() {
  DmaBuffer buf(256);
  return buf;  // NRVO or move ctor; the deleted copy ctor is never selected
}
```

У `DmaBuffer b = make_buffer();` функція `free_buffer` викликається рівно один раз, коли `b` виходить зі scope. Перенос не робить ресурс спільним: якщо кільком частинам коду потрібен буфер, потрібне спільне володіння, а не move.

**Типові помилки:**

- Не обнулити джерело в move-конструкторі (`other.p_ = nullptr`): обидва об’єкти звільнять один handle.
- Вважати, що елізія гарантована для іменованого локального об’єкта; код має працювати з move-конструктором.
- Залишити copy-конструктор неявним у класі, що володіє ресурсом, замість явного `= delete`.
