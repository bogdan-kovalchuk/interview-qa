---
id: emb-cppoop-0017
title: "Навіщо base-класу з virtual-методами потрібен virtual destructor?"
description: "Без virtual-деструктора видалення похідного через Base* – undefined behavior."
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-draft-expr-delete
    title: "C++ working draft: Delete ([expr.delete])"
    url: https://eel.is/c++draft/expr.delete
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 3: у single-object delete-expression, якщо static type не схожий на dynamic type, static type має бути базою dynamic type і мати virtual destructor, інакше поведінка не визначена. Не описує, що саме станеться на конкретному компіляторі."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 15: для virtual destructor deallocation function визначається так, ніби `delete this` стоїть у non-virtual destructor цього класу, що гарантує наявність deallocation function, яка відповідає dynamic type об’єкта. Не стосується non-virtual destructor-ів."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-06
    kind: spec
    version: null
    applicability: "У розділі 2.5.2 каже, що virtual destructor займає пару entries у vtable: complete object destructor (без delete) і deleting destructor (знищує об’єкт і викликає delete). Це ABI, а не стандарт мови."
  - source_id: cpp-core-guidelines-c35
    title: "C++ Core Guidelines: C.35 (base class destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c35-a-base-class-destructor-should-be-either-public-and-virtual-or-protected-and-non-virtual
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.35: деструктор базового класу має бути або public і virtual, або protected і non-virtual; protected забороняє видалення через вказівник на базу. Це рекомендація стилю, а не вимога мови."
  - source_id: cpp-core-guidelines-c127
    title: "C++ Core Guidelines: C.127 (virtual or protected destructor)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c127-a-class-with-a-virtual-function-should-have-a-virtual-or-protected-destructor
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.127: клас із virtual-функцією має мати virtual або protected destructor; приклад із `unique_ptr<B>` для `D` без такого деструктора названо undefined behavior. Це рекомендація стилю, а не вимога мови."
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

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
