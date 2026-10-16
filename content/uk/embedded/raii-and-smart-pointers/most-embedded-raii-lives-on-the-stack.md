---
id: emb-raii-0014
title: "Чи потребує RAII heap-алокації?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r5
    title: "C++ Core Guidelines: R.5 – Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cpp-draft-basic-start-term
    title: "C++ working draft: Termination ([basic.start.term])"
    url: https://eel.is/c++draft/basic.start.term
---

## Short answer

**Ні – RAII не вимагає купи.**

RAII-об’єкт може бути локальною змінною, членом класу чи глобальним об’єктом, тож окремої алокації не потребує: scoped-об’єкт не додає alloc/dealloc понад ті, що вже має охоплюючий scope.[^cppcg-r5] Типові embedded-RAII – lock guards і scope handles – обгортають ресурси, що існують незалежно (mutex, маска переривань), а `std::lock_guard` за специфікацією зберігає лише посилання на mutex.[^cpp-draft-thread-lock-guard]

Правило: stack-allocated guard – найпоширеніший і повністю heap-free RAII.

## Detailed explanation

Питання змішує дві різні речі: де живе сам RAII-об’єкт і який ресурс він тримає. Guard – звичайна змінна: локальна, глобальна чи член іншого об’єкта. Core Guidelines називають такий об’єкт scoped і зазначають, що він не має окремої вартості алокації та деалокації понад ту, що вже є в охоплюючого scope чи об’єкта.[^cppcg-r5] А ресурс, який guard тримає, може не бути пам’яттю взагалі: mutex, маска переривань, chip select, дескриптор периферії. `std::lock_guard` показує це наочно: за специфікацією його єдиний член – посилання на mutex, а конструктор і деструктор викликають `lock()` та `unlock()`.[^cpp-draft-thread-lock-guard]

Автоматичне звільнення забезпечує сама мова: при виході зі scope будь-яким способом об’єкти з automatic storage duration, сконструйовані в ньому, знищуються у зворотному порядку.[^cpp-draft-stmt-jump-general] Allocator тут не потрібен, а вартість зводиться до місця в stack frame і викликів конструктора та деструктора. Heap з’являється лише тоді, коли сам ресурс – динамічна пам’ять, як у `unique_ptr`; це властивість ресурсу, а не RAII.

```cpp
// Ілюстративно: chip select як RAII без жодної алокації.
class ChipSelect {
public:
    explicit ChipSelect(Gpio& pin) : pin_(pin) { pin_.low(); }
    ~ChipSelect() { pin_.high(); }
    ChipSelect(const ChipSelect&) = delete;
    ChipSelect& operator=(const ChipSelect&) = delete;
private:
    Gpio& pin_;
};

void read_id(Gpio& cs, Spi& spi) {
    ChipSelect sel(cs);   // CS низький
    spi.transfer();
}                         // CS знову високий на будь-якому виході
```

**Межі.** Стек зазвичай обмежений, тож великий об’єкт не варто класти на нього: Core Guidelines допускають у такому разі локальний `const unique_ptr` на об’єкт у heap.[^cppcg-r5] Об’єкти зі static storage duration знищуються як частина `std::exit`, а повернення з `main` його викликає.[^cpp-draft-basic-start-term] Якщо `main` у firmware не повертається, деструктор такого глобального об’єкта не спрацює, тож для нього RAII означає лише ініціалізацію при старті, а не guard. Об’єкти, які треба створювати динамічно без heap, можна будувати через placement new у заздалегідь виділеному буфері: qid:emb-raii-0015.

**Типові помилки:**

- Ототожнювати RAII з `unique_ptr` і вважати, що без heap RAII неможливий.
- Створювати сам guard через `new`: це додає алокацію й відповідальність за `delete`, тобто повертає проблему, яку RAII мав прибрати.[^cppcg-r5]
- Покладатися на деструктор глобального об’єкта в прошивці з нескінченним `main`.[^cpp-draft-basic-start-term]
- Класти великий буфер у guard на стеку без перевірки розміру stack-а.
