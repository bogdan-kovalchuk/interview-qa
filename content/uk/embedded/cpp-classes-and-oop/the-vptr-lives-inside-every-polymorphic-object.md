---
id: emb-cppoop-0015
title: "Що таке vptr і де він зберігається?"
track: embedded
section: cpp-classes-and-oop
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-class-virtual
    title: "C++ working draft: Virtual functions ([class.virtual])"
    url: https://eel.is/c++draft/class.virtual
  - source_id: cpp-draft-class-cdtor
    title: "C++ working draft: Construction and destruction ([class.cdtor])"
    url: https://eel.is/c++draft/class.cdtor
  - source_id: cpp-draft-class-copy-ctor
    title: "C++ working draft: Copy/move constructors ([class.copy.ctor])"
    url: https://eel.is/c++draft/class.copy.ctor
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
---

## Short answer

**vptr – прихований pointer усередині кожного об’єкта з virtual-функціями, що вказує на vtable його dynamic type.**

Зазвичай він додається компілятором як прихований член об’єкта, тому `sizeof` зростає приблизно на розмір pointer-а (4 байти на 32-bit, з урахуванням вирівнювання). Точна позиція vptr – ABI-dependent, не частина стандарту C++; в Itanium C++ ABI це offset 0, якщо в класу немає primary base.[^itanium-cxx-abi]

Правило: перша virtual-функція в ієрархії зазвичай додає кожному екземпляру vptr, а наступні virtual-функції розмір об’єкта вже не збільшують.[^itanium-cxx-abi]

## Detailed explanation

Стандарт C++ описує лише наслідок: виклик virtual-функції залежить від dynamic type об’єкта, а non-virtual – від static type вказівника чи посилання.[^cpp-draft-class-virtual] Щоб знайти потрібну функцію під час виконання, компілятор має зберігати щось в самому об’єкті. Типове рішення – vptr: перед викликом код читає vptr з об’єкта, далі читає слот у vtable, на яку той вказує, і робить непрямий виклик за цією адресою. Те, що це саме vptr на vtable, – деталь ABI, а не вимога мови.

В Itanium C++ ABI vptr потрібен кожному dynamic class, тобто класу з virtual-функціями або virtual-базами (тож vptr може мати й клас без жодної virtual-функції). Якщо primary base є, похідний клас використовує її vptr; якщо немає – vptr розміщується на offset 0, і `sizeof` починається з розміру pointer-а.[^itanium-cxx-abi] Тому додавання другої й наступних virtual-функцій розмір об’єкта не змінює: росте лише vtable в ROM, а кожен екземпляр у RAM має по одному vptr.

Цікава деталь – vptr не постійний за час життя. Під час конструювання об’єкт по черзі «стає» кожною своєю базою, і конструктор кожного класу виставляє vptr на таблицю саме цього класу.[^itanium-cxx-abi] Саме тому virtual-виклик усередині конструктора чи деструктора обирає final overrider у класі цього конструктора, а не в похідному.[^cpp-draft-class-cdtor] Для `static` об’єкта це означає: доки його конструктор не відпрацював, vptr може бути ще не виставлений.

Для embedded важливо, що vptr – звичайні байти об’єкта. Обнулений через `memset` поліморфний об’єкт має нульовий vptr, і наступний virtual-виклик піде за довільною адресою; `memcpy` з об’єкта іншого динамічного типу чи з буфера підміняє vptr, а навіть для того самого типу це undefined behavior, бо клас не є trivially copyable. Тому такі об’єкти слід копіювати через copy constructor чи assignment, а не побайтово; недарма copy constructor класу з virtual-функціями стандарт не вважає trivial.[^cpp-draft-class-copy-ctor]

```cpp
// Illustrative: не роби так з поліморфним об’єктом
struct Driver { virtual void tick(); int state; };
void run(Driver& x);      // визначено в іншому .cpp

Driver d;
memset(&d, 0, sizeof d);  // обнулив і vptr
run(d);                   // x.tick() усередині – справжній virtual-виклик через обнулений vptr
```

**Типові помилки:**

- Вважати, що позиція й розмір vptr визначені стандартом C++: це ABI і target.
- Думати, що кожна нова virtual-функція додає ще один vptr в об’єкт: додається лише слот у vtable.
- Заповнювати чи копіювати поліморфні об’єкти як сирі байти (`memset`, `memcpy`).
