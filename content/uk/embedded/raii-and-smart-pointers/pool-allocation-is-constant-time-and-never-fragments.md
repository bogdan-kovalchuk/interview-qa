---
id: emb-raii-0017
title: "Що таке arena/pool алокація в контексті RAII?"
description: "Виділення блоків фіксованого розміру з масиву: без зовнішньої фрагментації між блоками, lifetime контрольований."
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
  - source_id: zephyr-memory-slabs
    title: "Zephyr Project documentation: Memory Slabs"
    url: https://docs.zephyrproject.org/latest/kernel/memory_management/slabs.html
    accessed: 2026-10-13
    kind: official
    version: "latest"
    applicability: "Каже, що блоки slab мають один фіксований розмір без зайвого місця між ними, що знімає проблеми фрагментації, і що вільні блоки ведуться зв’язним списком. Не дає оцінки часу виділення і не описує інші пули."
  - source_id: cpp-draft-basic-life
    title: "C++ working draft: Object lifetime ([basic.life])"
    url: https://eel.is/c++draft/basic.life
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Пункт 6: програма може завершити lifetime об’єкта класу без виклику деструктора, повторно використавши storage; тоді деструктор неявно не викликається, а коректність часто залежить від його виклику. Не описує арени й пули."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Пункт 2, примітка 1: при виході зі scope будь-яким способом автоматичні об’єкти знищуються у зворотному порядку конструювання; при std::exit чи std::abort їх знищення може не відбутися. Не описує пули й арени."
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

## Sources

<!-- generated from frontmatter -->
