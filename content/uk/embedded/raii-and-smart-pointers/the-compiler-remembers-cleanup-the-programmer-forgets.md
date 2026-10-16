---
id: emb-raii-0020
title: "Чим RAII кращий за ручний init/deinit (список відмінностей)?"
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
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-cp20
    title: "C++ Core Guidelines: CP.20 – Use RAII, never plain lock()/unlock()"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#cp20-use-raii-never-plain-lockunlock
---

## Short answer

- **Гарантія очищення:** при виході зі scope компілятор викликає dtor, а вручну це мусить пам’ятати програміст;
- **Error-шлях:** early return безпечний vs кожен вихід – шанс на баг;
- **Дублювання:** dtor написаний раз vs повтор на кожному виході;
- **Порядок:** автоматичне знищення у зворотному порядку vs ручні виклики, які треба записати самому;
- **Runtime:** у GCC з `-O2` зазвичай той самий виклик unlock, що й у ручному коді; порожній dtor не дає інструкцій, але перевіряй asm.

Правило: RAII не додає нових можливостей, він прибирає помилки забутого очищення на виходах зі scope.[^cpp-draft-stmt-jump]

## Detailed explanation

Ручний init/deinit вимагає, щоб cleanup повторювався на кожному виході з функції. Кожен новий `return` або `break` – це новий шанс його пропустити, як у прикладі з C у питанні. Для mutex це прямий шлях до deadlock. RAII переносить cleanup у dtor: стандарт гарантує, що при виході зі scope будь-яким способом, зокрема через `return`, автоматичні об’єкти знищуються.[^cpp-draft-stmt-jump] Настанова CP.20 пояснює те саме: unlock легко забути, пропустити через return чи exception.[^cppcg-cp20]

Порядок: якщо функція володіє кількома ресурсами, ручний cleanup має відтворювати зворотний порядок створення. RAII робить це автоматично, бо автоматичні об’єкти знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-jump]

Межі: автоматичні об’єкти не знищуються, коли програма завершується через `std::exit`, а `std::abort` не виконує жодних деструкторів.[^cpp-draft-support-start-term] Тому RAII не замінює очищення при аварійному завершенні.

Про runtime. Порожній dtor без побічних ефектів не створює коду: у перевірці GCC з `-O2` він зник повністю. Dtor, що викликає unlock, після inlining дає той самий виклик unlock, що й ручний код, на кожному шляху виходу. Точні інструкції залежать від компілятора та прапорців, тому їх варто перевіряти в асемблері цільової збірки.

**Типові помилки:**

- Вважати, що RAII завжди дає нульовий runtime: dtor з unlock все одно виконує unlock, і його вартість – це вартість самого unlock.
- Очікувати, що dtor спрацює після `exit()` або `abort()`: автоматичні об’єкти в цих випадках не знищуються.
- Викликати `unlock()` вручну разом із guard-ом: подвійне звільнення.
