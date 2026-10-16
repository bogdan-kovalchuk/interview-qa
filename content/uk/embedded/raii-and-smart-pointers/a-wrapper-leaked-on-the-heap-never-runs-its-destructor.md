---
id: emb-raii-0029
title: "Trap: що станеться з ресурсом, якщо об’єкт-обгортку створити на heap і забути `delete`?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-basic-stc-dynamic
    title: "C++ working draft: [basic.stc.dynamic.general]"
    url: https://eel.is/c++draft/basic.stc.dynamic.general
  - source_id: cpp-draft-unique-ptr-dtor
    title: "C++ working draft: [unique.ptr.single.dtor]"
    url: https://eel.is/c++draft/unique.ptr.single.dtor
  - source_id: cpp-core-guidelines-r5
    title: "C++ Core Guidelines, R.5: Prefer scoped objects, don’t heap-allocate unnecessarily"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r5-prefer-scoped-objects-dont-heap-allocate-unnecessarily
---

## Short answer

<span class="warn">Деструктор не викличеться -> ресурс не звільниться (leak), попри те що це «RAII-клас».</span>[^cpp-draft-basic-stc-dynamic]

Об’єкт, створений через `new`, знищується лише delete-виразом, тож `new LockGuard(...)` без delete – той самий забутий unlock.

Захист: тримай RAII-об’єкти на стеку, як радять C++ Core Guidelines (R.5),[^cpp-core-guidelines-r5] або під `unique_ptr`, який у деструкторі викликає свій deleter (за замовчуванням delete).[^cpp-draft-unique-ptr-dtor]

## Detailed explanation

RAII прив’язує очищення до часу життя об’єкта. Для динамічного об’єкта час життя закінчується delete-виразом,[^cpp-draft-basic-stc-dynamic] тож guard, створений через `new` і ніколи не видалений, тримає захоплений lock і не викликає свій деструктор. Це не залежить від того, чи є в класі деструктор: він просто не має шансу спрацювати.

```cpp
#include <memory>

// Illustrative: LockGuard locks in the constructor and unlocks in the destructor.
using osMutexId_t = void*;
void osMutexAcquire(osMutexId_t m);
void osMutexRelease(osMutexId_t m);

class LockGuard {
public:
    explicit LockGuard(osMutexId_t m) : m_(m) { osMutexAcquire(m_); }
    ~LockGuard() { osMutexRelease(m_); }
private:
    osMutexId_t m_;
};

void leaky(osMutexId_t m) {
    LockGuard* g = new LockGuard{m};  // mutex acquired
    // no delete g: ~LockGuard never runs, m stays locked
}

void scoped(osMutexId_t m) {
    LockGuard g{m};                   // automatic storage duration
}                                     // ~LockGuard releases m here

void owned(osMutexId_t m) {
    std::unique_ptr<LockGuard> g = std::make_unique<LockGuard>(m);
}                                     // unique_ptr calls delete, so ~LockGuard runs
```

Heap тут зайвий: щоб захопити lock на час функції, досить локального об’єкта, і саме так радять C++ Core Guidelines (R.5).[^cpp-core-guidelines-r5] Якщо об’єкт справді мусить жити довше за блок, `std::unique_ptr` тримає власність і в деструкторі викликає свій deleter, за замовчуванням delete, тож очищення відбувається автоматично.[^cpp-draft-unique-ptr-dtor]

**Типові помилки:**

- Вважати, що RAII-клас очищує ресурс незалежно від того, як створено об’єкт.
- Тримати сирий вказівник від `new` без власника, тобто без `unique_ptr` чи гарантованого `delete`.
- Вважати, що `unique_ptr` потрібен для кожного RAII-об’єкта, хоча для локальної змінної досить стека.
