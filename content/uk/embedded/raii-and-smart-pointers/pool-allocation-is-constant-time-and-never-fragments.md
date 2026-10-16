---
id: emb-raii-0017
title: "Що таке arena/pool алокація в контексті RAII?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: zephyr-memory-slabs
    title: "Zephyr Project documentation: Memory Slabs"
    url: https://docs.zephyrproject.org/latest/kernel/memory_management/slabs.html
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
---

## Short answer

**Виділення з масиву блоків фіксованого розміру: між блоками немає зовнішньої фрагментації, а lifetime контрольований.**

Zephyr slab тримає вільні блоки в зв’язному списку.[^zephyr-memory-slabs] За такої структури виділення бере перший вільний блок, і його час не залежить від кількості блоків; пул, що шукає вільний блок циклом, такої гарантії не має.

Trivial-об’єкти можна просто відкинути reset-ом арени; для non-trivial destructors їх треба викликати перед reset, бо при повторному використанні пам’яті деструктор неявно не викликається.[^cpp-draft-basic-life]

Правило: пул дає відсутність зовнішньої фрагментації, але не нульові витрати: кожен об’єкт займає цілий блок.[^zephyr-memory-slabs]

## Detailed explanation

Arena (bump-allocator) і pool – різні механізми. Arena виділяє пам’ять, просуваючи вказівник, і звільняє все разом reset-ом. Pool тримає масив однакових блоків і видає та повертає їх окремо. RAII зв’язує lifetime із цим: handle у деструкторі повертає блок у пул, наприклад `unique_ptr` з власним deleter-ом, який викликає функцію звільнення пулу.

Відсутність зовнішньої фрагментації має конкретну причину: блоки однакового розміру лежать один за одним без зайвого місця між ними.[^zephyr-memory-slabs] Але це не безкоштовно. Об’єкт меншого розміру займає весь блок, тож розмір блока має бути не меншим за найбільший об’єкт, а залишок блока пропадає.

Вартість залежить від реалізації. Zephyr slab тримає вільні блоки в зв’язному списку.[^zephyr-memory-slabs] Зі структури списку випливає, що виділення бере перший блок і його час не залежить від кількості блоків; це висновок із такої структури, а не твердження Zephyr, який часу не оцінює. Пул, що шукає вільний блок у бітовій карті, у найгіршому випадку проходить усі блоки, тож O(1) тут не гарантується.

Арена не знає, які об’єкти в ній живуть, тому перед reset їх треба знищити вручну. Стандарт каже, що при повторному використанні storage деструктор неявно не викликається, а коректність програми часто залежить від його виклику.[^cpp-draft-basic-life] Для non-trivial типів викликай деструктори перед reset у зворотному порядку конструювання, як це робить компілятор для автоматичних об’єктів при виході зі scope.[^cpp-draft-stmt-jump]

**Типові помилки:**

- Reset арени з живими non-trivial об’єктами: їхні ресурси не звільняться.
- Вважати O(1) властивістю самого пулу, а не конкретної реалізації.
- Виділяти блок менший за потрібний об’єкт: запис за межі блока.
- Повернути той самий блок у пул двічі.
