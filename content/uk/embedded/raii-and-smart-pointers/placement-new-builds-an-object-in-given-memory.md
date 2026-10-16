---
id: emb-raii-0015
title: "Як конструювати об’єкт без `malloc` у заздалегідь виділеному буфері?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-new-delete-placement
    title: "C++ working draft: Non-allocating forms ([new.delete.placement])"
    url: https://eel.is/c++draft/new.delete.placement
  - source_id: cpp-draft-new-syn
    title: "C++ working draft: Header <new> synopsis ([new.syn])"
    url: https://eel.is/c++draft/new.syn
  - source_id: cpp-draft-expr-new
    title: "C++ working draft: New ([expr.new])"
    url: https://eel.is/c++draft/expr.new
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: cpp-draft-optional-general
    title: "C++ working draft: Class template optional, general ([optional.optional.general])"
    url: https://eel.is/c++draft/optional.optional.general
---

## Question code

```cpp
alignas(T) std::byte storage[sizeof(T)];
T* obj = new (storage) T(args); // placement new
obj->~T(); // явний виклик dtor
```

## Short answer

**Placement new будує об’єкт у наданій пам’яті без алокації.**

Бібліотечний `operator new(size_t, void*)` лише повертає переданий pointer і більше нічого не робить.[^cpp-draft-new-delete-placement] Пам’ять може бути static-масивом чи memory pool; стандарт виходить з того, що вона має потрібні розмір і alignment, тож це відповідальність програміста.[^cpp-draft-expr-new] Деструктор треба викликати явно (`obj->~T()`), бо `delete` тут не застосовний.[^cpp-draft-class-dtor]

Правило: placement new + явний dtor = динамічне конструювання без heap.

## Detailed explanation

Вираз `new (storage) T(args)` – це new-expression з placement-аргументами: вони передаються в allocation function, яку вибирає overload resolution.[^cpp-draft-expr-new] Для `void*` це non-allocating форма з `<new>`: вона повертає переданий pointer і навмисно не виконує жодної іншої дії.[^cpp-draft-new-delete-placement] [^cpp-draft-new-syn] Тому пам’ять не виділяється, а конструктор `T` просто виконується за цією адресою. Саме це робить placement new придатним для static-буферів, memory pool-ів і відображених адрес периферії.

**Вимоги до буфера.** Пам’ять має вміщувати `sizeof(T)` байтів і бути вирівняною для `T`. Масив `unsigned char` або `std::byte` може надавати storage для створеного в ньому об’єкта, якщо об’єкт повністю вміщується в масив.[^cpp-draft-intro-object] Але вирівнювання така умова не гарантує: new-expression вважає повернутий блок відповідно вирівняним,[^cpp-draft-expr-new] і програма має виконати це припущення сама, звідси `alignas(T)` у коді запитання. Без нього масив байтів може опинитися за адресою, невідповідною для `T`; це порушує припущення стандарту, а на деяких ядрах невирівняний доступ ще й дає апаратний fault.

**Завершення lifetime.** Об’єкт, збудований у чужій пам’яті, треба знищити явним `obj->~T()`. Стандарт окремо зазначає, що така пара розміщення й знищення буває потрібна для роботи з апаратними ресурсами та в memory management.[^cpp-draft-class-dtor] Звичайний `delete` не підходить: delete-expression не лише викликає деструктор, а й звільняє storage,[^cpp-draft-basic-life] а наш буфер не отримано від allocation function. Після виклику деструктора lifetime завершено, і повторний виклик для того самого об’єкта – undefined behavior.[^cpp-draft-class-dtor] Пропустити деструктор формально можна, бо програма може завершити lifetime, повторно використавши storage, але коректність програми часто залежить саме від цього виклику.[^cpp-draft-basic-life] Якщо конструктор кидає exception, викликається placement `operator delete`, який нічого не робить, тож буфер лишається вашим.[^cpp-draft-new-delete-placement]

```cpp
// Ілюстративно: слот для одного об’єкта з явним життєвим циклом.
template <class T>
class Slot {
public:
    Slot() = default;
    Slot(const Slot&) = delete;
    Slot& operator=(const Slot&) = delete;
    ~Slot() { reset(); }

    template <class... Args>
    T* emplace(Args&&... args) {
        reset();                                   // не накладаємо об’єкт на об’єкт
        p_ = new (buf_) T(std::forward<Args>(args)...);
        return p_;
    }
    void reset() {
        if (p_ != nullptr) { p_->~T(); p_ = nullptr; }
    }
private:
    alignas(T) std::byte buf_[sizeof(T)];
    T* p_ = nullptr;
};
```

Такий клас сам стає RAII-обгорткою: деструктор `Slot` викликає деструктор об’єкта, тож явний `~T()` не розсипається по коду (див. qid:emb-raii-0014). Для готового рішення без heap існує `std::optional<T>`: значення, яке він містить, вкладене в сам об’єкт `optional`.[^cpp-draft-optional-general]

**Типові помилки:**

- Брати `char buf[sizeof(T)]` без `alignas(T)`: розмір збігається, а вирівнювання – ні.[^cpp-draft-expr-new]
- Викликати `delete obj` чи `free(obj)` для об’єкта в статичному буфері: delete-expression звільняє storage, якого ми не виділяли.[^cpp-draft-basic-life]
- Побудувати новий об’єкт у зайнятому слоті, не знищивши попередній: втрачається його деструктор, а разом з ним і ресурси, які він тримав.
- Викликати деструктор двічі або користуватися `obj` після `obj->~T()`.[^cpp-draft-class-dtor]
