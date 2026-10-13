---
id: emb-raii-0019
title: "Як RAII вирішує проблему early return між lock і unlock?"
description: "RAII-guard звільняє mutex на кожному виході зі scope, включно з early return."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Пункт 2, примітка 1: при виході зі scope будь-яким способом автоматичні об’єкти знищуються у зворотному порядку конструювання; при std::exit чи std::abort вони можуть не знищуватися. Не описує mutex й RTOS."
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Настанова: замість ручних lock() і unlock() використовувати RAII-обгортку, бо unlock() легко забути, пропустити через return чи exception. Про переривання чи bare-metal не каже."
  - source_id: cppcg-cp44
    title: "C++ Core Guidelines: CP.44 – Remember to name your lock_guards and unique_locks"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp44-remember-to-name-your-lock_guards-and-unique_locks
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Настанова CP.44: безіменний локальний об’єкт – це temporary, що одразу виходить зі scope. У прикладі (A) unique_lock<mutex>(m1) є локальною змінною m1, що затінює глобальний m1 і нічого не блокує; (B) lock_guard<mutex> {m2} блокує і одразу розблоковує. Приклади – std::lock_guard і std::unique_lock, а не RTOS guard."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Пункти 1–2: при винятку, перехопленому обробником, автоматичні об’єкти, побудовані після входу в try-блок, знищуються (stack unwinding). Не описує випадок, коли винятки вимкнено компілятором."
  - source_id: cpp-draft-csetjmp-syn
    title: "C++ working draft: C library setjmp/longjmp header ([csetjmp.syn])"
    url: https://eel.is/c++draft/csetjmp.syn
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Пункт 2: пара setjmp/longjmp має undefined behavior, якщо заміна на catch і throw викликала б нетривіальні деструктори автоматичних об’єктів. Не описує exit чи abort."
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

## Sources

<!-- generated from frontmatter -->
