---
id: emb-cppoop-0017
title: "Навіщо base-класу з virtual-методами потрібен virtual destructor?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
  - source_id: cpp-core-guidelines-c127
    title: "C++ Core Guidelines: C.127 (virtual or protected destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c127-a-class-with-a-virtual-function-should-have-a-virtual-or-protected-destructor
---

## Short answer

<span class="warn">Без virtual-деструктора видалення похідного об’єкта через `Base*` – undefined behavior.</span>[^cpp-draft-expr-delete]

`Base* p = new Derived; delete p;` на практиці зазвичай викличе лише `~Base()`, а не `~Derived()`, тож ресурси нащадка не звільняться, але стандарт навіть цього не гарантує. Захист: якщо клас має virtual-функції й може видалятися через вказівник на базу – оголоси `virtual ~Base()`, а якщо такого видалення не передбачено – зроби деструктор protected і non-virtual.[^cpp-core-guidelines-c35]

## Detailed explanation

Вираз `delete p` знищує об’єкт і звільняє пам’ять. Якщо деструктор virtual, виклик іде через vtable до деструктора найпохіднішого класу, тож спрацьовує тіло `~Derived()`, а потім деструктори членів і баз. В Itanium C++ ABI virtual destructor займає пару entries: complete object destructor і deleting destructor, який після знищення об’єкта ще й викликає `delete`.[^itanium-cxx-abi] Для non-virtual деструктора компілятор бачить лише static type `Base` і викликає тільки `~Base()`.

Стандарт формулює це жорсткіше за «може бути витік»: якщо static type у `delete` не збігається з dynamic type, він має бути базою й мати virtual destructor, інакше поведінка не визначена.[^cpp-draft-expr-delete] Отже, «лише `~Base()`» – типовий, але не гарантований результат; компілятор вправі зробити що завгодно. Ця вимога стосується будь-якого delete через базу, зокрема й `std::unique_ptr<Base>`, який у Core Guidelines наведено як приклад undefined behavior.[^cpp-core-guidelines-c127]

Ще одна причина, чому virtual потрібен не лише для деструкторів членів: deallocation function. Для virtual destructor стандарт гарантує, що вибрана `operator delete` відповідає dynamic type об’єкта.[^cpp-draft-class-dtor] Якщо в похідного класу є свій `operator delete`, наприклад для пулу пам’яті, а деструктор базового non-virtual, вибір deallocation function за dynamic type не гарантований, а загалом поведінка вже не визначена. Для embedded це важливіше, ніж виглядає: пули й власні алокатори там звичайна річ.

Правило не означає «завжди додавай virtual». Якщо базу ніколи не видаляють через вказівник на неї (об’єкти статичні чи на стеку, або `delete` у проєкті заборонений), UB не виникає; тоді Core Guidelines радять protected non-virtual destructor, і `delete` через базу просто не скомпілюється.[^cpp-core-guidelines-c35] Для вже polymorphic класу vptr і так є, а virtual destructor додає лише пару слотів у vtable.[^itanium-cxx-abi]

```cpp
// Illustrative
struct Base {
  virtual void tick();
  virtual ~Base() = default;   // видалення через Base* безпечне
};
struct Derived : Base { ~Derived() override; };

struct Iface {
  virtual void tick() = 0;
protected:
  ~Iface() = default;          // delete через Iface* не скомпілюється
};
```

**Типові помилки:**

- Вважати наслідком лише витік пам’яті: за стандартом поведінка взагалі не визначена.
- Додати virtual-функції в базу й забути virtual destructor, а потім тримати об’єкти в `unique_ptr<Base>`.
- Ставити деструктор інтерфейсу public і non-virtual: він має бути або public virtual, або protected non-virtual.
