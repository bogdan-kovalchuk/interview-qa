---
id: emb-raii-0018
title: "Trap: чим небезпечний RAII-деструктор усередині ISR?"
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
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
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
