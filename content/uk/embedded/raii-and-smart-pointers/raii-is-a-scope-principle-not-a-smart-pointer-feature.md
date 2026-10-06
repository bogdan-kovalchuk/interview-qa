---
id: emb-raii-0013
title: "Trap: «RAII працює лише зі smart pointers» – у чому помилка?"
description: "RAII – це принцип прив’язки ресурсу до lifetime об’єкта у scope, а не фіча smart pointers."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-stmt-jump-general
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "У примітці каже, що при виході зі scope (будь-яким способом) об’єкти з automatic storage duration, сконструйовані в ньому, знищуються у зворотному порядку конструювання, а програма може завершитися через std::exit чи std::abort без знищення таких об’єктів. Про конкретні embedded-ресурси не каже."
  - source_id: cpp-draft-thread-lock-guard
    title: "C++ working draft: Class template lock_guard ([thread.lock.guard])"
    url: https://eel.is/c++draft/thread.lock.guard
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що lock_guard керує володінням lockable-об’єктом у межах scope і тримає його протягом свого lifetime; конструктор викликає lock(), деструктор – unlock(); копіювання й присвоєння видалено; член – лише посилання на mutex. Не описує interrupt guard чи інші embedded-ресурси."
  - source_id: cppcg-r1
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: ресурс, що потребує парних викликів acquire/release (fopen/fclose, lock/unlock, new/delete), слід загорнути в об’єкт, який бере ресурс у конструкторі й віддає в деструкторі. Не обмежує RAII вказівниками."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: замість ручних lock() і unlock() використовувати RAII-обгортку, бо unlock() легко забути, пропустити через return чи exception. Про переривання чи bare-metal не каже."
---

## Short answer

<span class="warn">RAII – це принцип прив’язки ресурсу до lifetime об’єкта у scope, а не фіча smart pointers.</span>

Конструктор бере ресурс, деструктор віддає: так працюють `std::lock_guard`, що тримає mutex протягом свого lifetime,[^cpp-draft-thread-lock-guard] власний interrupt guard чи scoped handle на периферію – без жодного heap-pointer-а. Smart pointer – лише одне із застосувань цієї ідеї, для пари `new`/`delete`.[^cppcg-r1]

Захист: думай про RAII як «ctor бере / dtor віддає», а не як про `unique_ptr`.

## Detailed explanation

RAII спирається не на smart pointers, а на гарантію мови: при виході зі scope будь-яким способом об’єкти з automatic storage duration, сконструйовані в ньому, знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-jump-general] Тому пару «взяти / віддати» можна доручити парі конструктор/деструктор. Core Guidelines формулюють це так: коли ресурс потребує парних викликів на кшталт `fopen`/`fclose`, `lock`/`unlock` чи `new`/`delete`, його загортають в об’єкт, що бере ресурс у конструкторі й віддає в деструкторі.[^cppcg-r1] Звідси видно, що `new`/`delete` – лише один із трьох прикладів.

`std::lock_guard` – стандартний RAII-об’єкт без жодного власного вказівника на пам’ять: він керує володінням lockable-об’єктом протягом свого lifetime, конструктор викликає `lock()`, деструктор – `unlock()`.[^cpp-draft-thread-lock-guard] Core Guidelines радять саме так замість ручних `lock()` і `unlock()`, бо `unlock()` легко забути, пропустити через `return` чи exception.[^cppcg-cp20] В embedded те саме застосовне до будь-якої пари «захопити / повернути», наприклад до вимкнення переривань.

```cpp
// Ілюстративно: read_primask, disable_irq і enable_irq – умовні
// обгортки над інструкціями конкретного ядра.
class IrqGuard {
public:
    IrqGuard() : saved_(read_primask()) { disable_irq(); }
    ~IrqGuard() { if (saved_ == 0) { enable_irq(); } }  // відновлює попередній стан
    IrqGuard(const IrqGuard&) = delete;
    IrqGuard& operator=(const IrqGuard&) = delete;
private:
    std::uint32_t saved_;
};

void tick() {
    IrqGuard guard;   // переривання вимкнено
    ++counter;
}                     // деструктор відновлює стан на будь-якому виході зі scope
```

Guard запам’ятовує попередній стан, тож вкладені guard-и не вмикають переривання передчасно. Копіювання заборонено, як і в `lock_guard`,[^cpp-draft-thread-lock-guard] щоб один ресурс не віддали двічі. Smart pointer – це той самий шаблон, застосований до ресурсу «динамічна пам’ять».

**Межі.** Гарантія стосується знищення об’єктів при виході зі scope. Програма може завершитися через `std::exit` чи `std::abort` без знищення об’єктів з automatic storage duration,[^cpp-draft-stmt-jump-general] а guard, оголошений у функції, яка ніколи не повертається, ресурс не віддасть.

**Типові помилки:**

- Ототожнювати RAII з `unique_ptr` і через це писати ручні `disable_irq()` / `enable_irq()` з кількома `return` між ними.[^cppcg-cp20]
- Робити guard копіюваним без продуманої семантики: копія віддасть той самий ресурс удруге.
- Тримати guard довше, ніж потрібно: переривання лишаються вимкненими на весь scope, а не на критичну ділянку.
- Чекати, що деструктор спрацює при `std::exit`, `std::abort` або виході з нескінченного циклу.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
