---
id: emb-cppoop-0031
title: "Trap: чому методи інлайняться у bare-metal доступ лише з оптимізацією (наприклад `-O2`), а не на `-O0`?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
  - source_id: cpp-draft-class-mfct
    title: "C++ working draft: Member functions ([class.mfct])"
    url: https://eel.is/c++draft/class.mfct
  - source_id: cpp-draft-dcl-inline
    title: "C++ working draft: The inline specifier ([dcl.inline])"
    url: https://eel.is/c++draft/dcl.inline
---

## Short answer

<span class="warn">На `-O0` GCC за замовчуванням не розгортає функції inline, окрім позначених `always_inline`, тож кожен `set()` лишається реальним викликом.</span>[^gcc-optimize-options]

Тобто «нульовий оверхед» обгортки проявляється лише з оптимізацією: `-finline-small-functions` вмикається на `-O2`, `-O3` і `-Os`,[^gcc-optimize-options] а в debug-збірці клас-обгортка коштує виклику з прологом і епілогом.

Захист: оцінюй розмір і швидкість C++-абстракцій на release-прапорцях (`-O2`/`-Os`), не на `-O0`, і перевіряй асемблер.

## Detailed explanation

Метод, визначений у тілі класу, неявно `inline`,[^cpp-draft-class-mfct] але `inline` лише висловлює перевагу підстановки, а реалізація не зобов’язана її виконувати.[^cpp-draft-dcl-inline] Тож «обгортка нічого не коштує» – не правило мови, а результат роботи оптимізатора: тіло методу підставляється в місце виклику лише тоді, коли компілятор це вирішує.

GCC без оптимізації не розгортає жодної функції inline, крім тих, що мають атрибут `always_inline`; це поведінка за замовчуванням, коли оптимізація вимкнена.[^gcc-optimize-options] Тому на `-O0` кожен `set()` лишається окремою функцією: виклик, пролог, тіло, епілог, повернення. На `-O2`, `-O3` і `-Os` GCC вмикає `-finline-small-functions`, який евристично підставляє функції, чиє тіло менше за код виклику, навіть без слова `inline`.[^gcc-optimize-options] Наскільки це спрацює для конкретного `set()`, залежить від коду й версії компілятора.

Ілюстративний приклад: на x86-64 з GCC 13.3 `blink()` на `-O0` містить `call` на `Gpio::set()`, а на `-O2` виклику немає, і read-modify-write через вказівник, збережений у `g`, згортається в load, `bts` і store. У цьому експерименті підстановка була й на `-O1` та `-Og`, але документація цього не гарантує: вона гарантує лише відсутність підстановки без оптимізації.

```cpp
#include <cstdint>

class Gpio {
  volatile std::uint32_t *const odr_;
  const std::uint8_t pin_;
public:
  Gpio(volatile std::uint32_t *odr, std::uint8_t pin) : odr_{odr}, pin_{pin} {}
  void set() const { *odr_ |= (UINT32_C(1) << pin_); }
};

void blink(const Gpio &g) { g.set(); }
// -O0: у blink() є call на Gpio::set()
// -O2: call немає, тіло set() підставлене в blink()
```

На MCU це має практичні наслідки: кожен зайвий виклик коштує тактів, стека й місця у flash, тож розмір і таймінги debug-збірки можуть помітно відрізнятися від release. Тому вимірюй абстракцію на тих прапорцях, з якими вона виходить у продукт, і дивись асемблер чи map file.

**Типові помилки:**

- Робити висновок про вартість C++-абстракції за збіркою на `-O0`.
- Вважати, що `inline` чи визначення методу в тілі класу гарантує підстановку.[^cpp-draft-dcl-inline]
- Налагоджувати timing-critical код (bit-banging, ISR) лише в debug-збірці й переносити виміряні таймінги на release.
- Узагальнювати результат одного компілятора чи його версії на всі інші.
