---
id: emb-raii-0026
title: "Trap: чому забути `= delete` copy ctor у класі-обгортці ресурсу – критична помилка?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: [class.copy.ctor]"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: cpp-draft-new-delete-single
    title: "C++ working draft: [new.delete.single]"
    url: https://eel.is/c++draft/new.delete.single
  - source_id: cpp-draft-structure-specifications
    title: "C++ working draft: [structure.specifications]"
    url: https://eel.is/c++draft/structure.specifications
---

## Short answer

<span class="warn">Дефолтний copy ctor зробить поверхневу копію handle -> два об’єкти «володіють» одним ресурсом -> подвійне звільнення.</span>[^cpp-draft-class-copy-ctor]

При знищенні обох dtor ресурс звільняється двічі. Для `new`/`delete` це undefined behavior, бо порушено передумову `operator delete`,[^cpp-draft-new-delete-single][^cpp-draft-structure-specifications] а для RTOS-handle наслідки залежать від API: помилка, corruption або закриття вже закритого ресурсу.

Захист: зазвичай або `= delete` copy, або move semantics з обнуленням джерела.[^embeddedinterviewlab]

## Detailed explanation

Клас-обгортка тримає handle (м’ютекс, дескриптор периферійного каналу) і звільняє його в деструкторі. Якщо copy-конструктор не оголошено, компілятор генерує неявний, і він за стандартом виконує memberwise copy баз і членів.[^cpp-draft-class-copy-ctor] Для покажчика чи числового ідентифікатора це означає просте копіювання значення без жодної логіки власника, тож після `ResourceGuard b = a;` обидва об’єкти містять той самий handle.

Коли обидва об’єкти виходять зі scope, їхні деструктори звільняють один і той самий handle двічі. Для пам’яті, отриманої через `new`, повторний `delete` того самого вказівника порушує передумову `operator delete`, а порушення передумов бібліотечної функції дає undefined behavior.[^cpp-draft-new-delete-single][^cpp-draft-structure-specifications] Для RTOS-handle стандарт C++ нічого не визначає: API може повернути помилку, пошкодити внутрішній стан або звільнити ресурс, який уже належить іншому коду.

```cpp
// Illustrative: Handle stands in for an RTOS resource handle.
using Handle = void*;
Handle acquire_resource();
void release_resource(Handle h);

class ResourceGuard {
public:
    ResourceGuard(Handle h) : h_(h) {}
    ~ResourceGuard() { release_resource(h_); }
    // Without the next two lines the implicit copy below compiles,
    // and both objects release the same handle.
    ResourceGuard(const ResourceGuard&) = delete;
    ResourceGuard& operator=(const ResourceGuard&) = delete;
private:
    Handle h_;
};

void example() {
    ResourceGuard a{acquire_resource()};
    ResourceGuard b = a;   // compile error while the copy constructor is deleted
}
```

Правило: копіювання треба заборонити або замінити передачею власності. `= delete` для copy-конструктора та copy-присвоєння робить спробу копіювання помилкою компіляції, як у прикладі. Move-конструктор переносить handle і обнуляє джерело, тож звільнення відбувається один раз. Спільне володіння через лічильник посилань можливе, але це явний механізм, а не поведінка за замовчуванням.

**Типові помилки:**

- Заборонити копіювання лише в коментарі чи документації, а не через `= delete`.
- Заборонити copy і не реалізувати move, через що власність не можна передати іншій функції.
- Розраховувати, що RTOS мовчки проігнорує повторне звільнення handle; це залежить від конкретного API.
