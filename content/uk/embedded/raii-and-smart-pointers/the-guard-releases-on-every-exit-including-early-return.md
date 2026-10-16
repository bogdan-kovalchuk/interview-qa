---
id: emb-raii-0019
title: "Як RAII вирішує проблему early return між lock і unlock?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
  - source_id: cpp-draft-csetjmp-syn
    title: "C++ working draft: C library setjmp/longjmp header ([csetjmp.syn])"
    url: https://eel.is/c++draft/csetjmp.syn
---

## Question code

```c
// C: баг на error-шляху
mutex_lock(&m);
if (error) return -1; // забули unlock!
mutex_unlock(&m);
```

## Short answer

**RAII-guard звільняє mutex на кожному виході зі scope, включно з early return і винятком (якщо винятки увімкнені).**[^cpp-draft-stmt-jump][^cpp-draft-except-ctor] При exit, abort чи longjmp це не гарантовано: `longjmp` через об’єкт з нетривіальним деструктором – undefined behavior.[^cpp-draft-csetjmp-syn]

```cpp
{ LockGuard lock(m);
  if (error) return -1; } // dtor unlocks
```

Типовий failure mode: early return між lock і unlock може дати deadlock через забутий unlock на error path.

Правило: RAII перетворює дисципліну (пам’ятати unlock) на структурну гарантію.[^cppcg-cp20]

## Detailed explanation

У C ручний unlock мусить стояти перед кожним `return`, і один пропущений шлях лишає mutex захопленим. У C++ з RAII unlock переноситься в dtor локального об’єкта. Стандарт говорить, що при виході зі scope будь-яким способом автоматичні об’єкти, побудовані в ньому, знищуються у зворотному порядку конструювання; це стосується й `return`.[^cpp-draft-stmt-jump]

Ілюстративний приклад, де `LockGuard` – RAII-обгортка навколо mutex:

```cpp
int update(int v) {
  LockGuard lock(m);
  if (v < 0) return -1;  // dtor releases the mutex
  shared = v;
  return 0;              // dtor releases the mutex here too
}
```

Обидва виходи звільняють mutex, а ручного unlock у коді немає.

Важлива деталь – форма запису. Тимчасовий guard пишеться з фігурними дужками: `LockGuard{m};`. Він знищується в кінці повного виразу, тож lock одразу знімається.[^cppcg-cp44] А `LockGuard(m);` для non-template типу оголошує змінну з іменем `m`: вона затінює глобальний mutex і нічого не блокує. Без конструктора за замовчуванням така форма не компілюється, з ним компілюється, а `-Wshadow` попереджає.

Межі гарантії: вона діє при виході зі scope. При `std::exit` або `std::abort` автоматичні об’єкти можуть не знищуватися, а `longjmp` через об’єкт з нетривіальним деструктором – undefined behavior, тож mutex може лишитися захопленим.[^cpp-draft-stmt-jump][^cpp-draft-csetjmp-syn]

**Типові помилки:**

- Записати `LockGuard(m);` замість `LockGuard{m};`: це оголошення змінної `m`, а не тимчасовий guard, і mutex не захоплюється.
- Викликати `unlock()` вручну поряд із guard-ом: подвійне звільнення.
- Тримати guard на всю функцію, хоча критична секція коротша: mutex зайнятий довше, ніж потрібно.
