---
id: emb-raii-0018
title: "Trap: чим небезпечний RAII-деструктор усередині ISR?"
description: "Деструктор виконується в тому ж контексті, що й вихід зі scope – тобто в ISR (interrupt service routine)."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
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
    applicability: "Пункт 2, примітка 1: при виході зі scope будь-яким способом, зокрема через return, автоматичні об’єкти знищуються у зворотному порядку конструювання, тож dtor guard-а виконується всередині обробника. Не каже, які дії в деструкторі допустимі в ISR."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Каже, що функції mutex CMSIS-RTOS2 не можна викликати з ISR: osMutexRelease повертає osErrorISR, а osMutexAcquire також недоступна з ISR. Не описує інші RTOS і не визначає поведінку деструкторів."
---

## Question code

```c
void isr() {
  LockGuard lock(m); // dtor викличе release В ISR!
  // ...
}
```

## Short answer

<span class="warn">Деструктор виконується в тому ж контексті, що й вихід зі scope – тобто в ISR (interrupt service routine).</span>[^cpp-draft-stmt-jump]

Якщо dtor викликає RTOS-API, заборонений в ISR, наприклад release mutex, це в ISR неприпустимо: CMSIS-RTOS2 забороняє `osMutexRelease` з ISR і повертає `osErrorISR`.[^cmsis-rtos2-mutex] Безпечніший варіант – guard, dtor якого відновлює стан переривань без блокуючих дій.

## Detailed explanation

ISR – це функція, яку викликає апаратне переривання, і автоматичні об’єкти в ній живуть за звичайними правилами. Коли керування виходить зі scope будь-яким способом, зокрема через `return`, об’єкти знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-jump] Тому dtor guard-а, створеного на початку ISR, виконується всередині обробника, безпосередньо перед поверненням із переривання.

Проблема в тому, що RTOS-примітиви не призначені для переривань. CMSIS-RTOS2 описує mutex-функції як недоступні з ISR: `osMutexRelease` повертає `osErrorISR`, а `osMutexAcquire` також не можна викликати з ISR.[^cmsis-rtos2-mutex] Отже ISR не може ні захопити, ні звільнити такий mutex: виклики повертають помилку, а не чекають. Якщо ж задача тримає той самий mutex, а ISR намагається його дочекатися спін-циклом, задача не виконається, поки ISR не завершиться, і може виникнути deadlock.

Навіть короткий блокуючий dtor, наприклад із UART TX, затримує обробку інших переривань і дає jitter. Тому правило «dtor короткий, отже безпечний» тут не працює: виконується сам dtor, і його дії мають бути неблокуючими.

Безпечний шаблон – guard, який не чекає ресурсу: у ctor він запам’ятовує поточний стан переривань і вимикає їх, а в dtor відновлює збережений стан. Такий guard не має блокуючого teardown, тож його можна використовувати в ISR, якщо критична секція коротка.

**Типові помилки:**

- Брати в ISR звичайний RAII-guard RTOS-mutex, навіть якщо dtor «тільки» його звільняє.
- Вважати dtor безпечним лише тому, що він короткий: він виконується, і його дії теж мають бути неблокуючими.
- Викликати в dtor, який може спрацювати в ISR, `malloc`, `printf` або UART TX з очікуванням завершення.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
