---
id: emb-tmplcx-0016
title: "Що робить `extern template`?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-temp-explicit
    title: "C++ working draft: Explicit instantiation ([temp.explicit])"
    url: https://eel.is/c++draft/temp.explicit
  - source_id: cpp-draft-temp-inst
    title: "C++ working draft: Implicit instantiation ([temp.inst])"
    url: https://eel.is/c++draft/temp.inst
---

## Question code

```cpp
extern template class Buffer<uint8_t>;
```

## Short answer

**Дозволяє компілятору не інстанціювати члени шаблону в цьому translation unit.**[^cpp-draft-temp-explicit] Визначення має існувати десь у програмі як явна інстанціація-визначення, інакше програма некоректна.[^cpp-draft-temp-explicit] Правило: `extern template` у заголовку і одна явна інстанціація в одному `.cpp` дозволяють уникнути копій у кожному TU для не-inline членів.

## Detailed explanation

Якщо визначення членів видно в заголовку, компілятор інстанціює їх у кожному translation unit, який їх викликає, і може випустити власну копію в кожному `.o`-файлі. Саме таке повторення і намагається прибрати `extern template`.[^cpp-draft-temp-inst]

Нижче ілюстративний поділ на заголовок і `.cpp`; він компілюється з `g++ -std=c++17`, а `main.cpp` тут не наведено:

```cpp
// buffer.h (illustrative)
#include <cstddef>
#include <cstdint>

template <typename T>
class Buffer {
public:
    void push(T value);            // defined in buffer.cpp
    T pop();
private:
    T data_[64];
    std::size_t n_ = 0;
};

extern template class Buffer<std::uint8_t>;   // other TUs do not instantiate uint8_t members

// buffer.cpp (illustrative)
#include "buffer.h"

template <typename T>
void Buffer<T>::push(T value) { data_[n_ % 64] = value; ++n_; }

template <typename T>
T Buffer<T>::pop() { --n_; return data_[n_ % 64]; }

template class Buffer<std::uint8_t>;   // the one explicit instantiation definition
```

У `nm -C` видно: `main.o`, що викликає `push`, має `U` (undefined), а визначення лежить у `buffer.o`. Для випадку, коли визначення членів стоять у заголовку, перевірено на GCC з `-O0`: без `extern template` кожен TU, що викликає `push`, створює власну слабку копію (`W`), а з ним лише посилається на символ (`U`).

Легко пропустити дві умови. По-перше, явна інстанціація-визначення має бути в програмі: без неї виклик лишається без визначення, і лінкер зазвичай повідомляє `undefined reference`. Стандарт вважає таку програму некоректною, без обов’язкової діагностики.[^cpp-draft-temp-explicit] По-друге, явна інстанціація класу інстанціює його прямі не-шаблонні члени, тож якщо якийсь член не компілюється для `T`, помилка з’явиться навіть без його виклику.[^cpp-draft-temp-explicit]

Межа: правило явної декларації стосується і inline-функцій, але декларація не робить inline-функцію «оголошеною» спеціалізацією, тож компілятор може інстанціювати її для inline-підстановки в кожному TU.[^cpp-draft-temp-inst] Тому економія від `extern template` найпередбачуваніша для не-inline членів. Для inline-членів, зокрема визначених у тілі класу, розмір прошивки залежить від компілятора і лінкера.

**Типові помилки:**

- Поставити `extern template` у заголовку без явної інстанціації-визначення в `.cpp`: з’являється помилка лінкера.
- Очікувати, що `extern template` прибере копії inline-членів у прошивці.
- Явно інстанціювати клас для типу, з яким один із не-шаблонних членів не компілюється.
