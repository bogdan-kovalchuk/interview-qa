---
id: emb-raii-0002
title: "Чому RAII критичний саме в embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
  - source_id: linux-man-exit
    title: "Linux man-pages: _exit(2)"
    url: https://man7.org/linux/man-pages/man2/_exit.2.html
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
---

## Short answer

**Немає OS-страховки й garbage collector – забутий ресурс може лишитися зайнятим до reset.**

Mutex, який потік не відпустив, у CMSIS-RTOS2 сам не звільняється: автоматично це робить лише robust mutex, і лише коли власник завершується.[^cmsis-rtos2-mutex] У Linux ядро закриває відкриті файлові дескриптори процесу, коли той завершується,[^linux-man-exit] а прошивка на MCU зазвичай є однією програмою без такого прибирання.

Правило: RAII повертає ресурс на кожному виході зі scope, тож забути звільнення складніше.[^cppcg-r1-raii]

## Detailed explanation

На десктопі процес – одиниця ізоляції: коли він завершується, ядро забирає частину його ресурсів. У Linux, наприклад, `_exit` закриває всі відкриті файлові дескриптори процесу.[^linux-man-exit] Прошивка на MCU зазвичай працює як одна програма, яка не завершується, і такого шару прибирання під нею немає. Пропущене звільнення тому не зникає саме: воно блокує інші частини системи або накопичується, доки не станеться reset чи спрацює watchdog.

Найпростіший приклад – mutex у RTOS. Потік бере mutex, на error-шляху виходить із функції без `osMutexRelease`, і mutex лишається у власності цього потоку. Потоки, що чекають на нього з `osWaitForever`, блокуються. За замовчуванням mutex у CMSIS-RTOS2 не рекурсивний (потік не може взяти його повторно), тож навіть наступний `osMutexAcquire` самого власника не пройде. Robust mutex звільняється автоматично, але лише коли власник завершується через `osThreadExit` чи `osThreadTerminate`; потік, що просто працює далі із забутим lock, цим не рятується, а non-robust mutex автоматично не звільняється, тож звільняти його має сам код.[^cmsis-rtos2-mutex]

Те саме стосується й інших ресурсів. Канал DMA, SPI-шина чи GPIO, взяті через HAL, зазвичай позначені в драйвері як «зайняті», а чи можна їх звільнити без участі коду, який їх узяв, залежить від конкретного драйвера. Стан переривань – ще один ресурс: `__disable_irq()` встановлює PRIMASK, а PRIMASK блокує всі переривання й винятки з конфігурованим пріоритетом, крім NMI і hard fault.[^cmsis-core-register] Забутий restore на error-шляху лишає ці переривання вимкненими.

RAII прибирає саму можливість забути. Шляхів виходу з функції в драйверах багато (таймаут, NACK, помилка CRC), і кожен новий `return` – шанс пропустити release. Деструктор прив’язує звільнення до виходу зі scope, тому воно не залежить від кількості шляхів.[^cpp-draft-stmt-dcl] Межі такі: RAII не діє, якщо програма завершується через `std::abort` чи `std::exit`,[^cpp-draft-support-start-term] або зависає чи перезапускається посередині – тому watchdog і діагностика потрібні й далі.

**Типові помилки:**

- Сподіватися, що RTOS «прибере» mutex за потоком: це робить лише robust mutex і лише при завершенні потоку.
- Загортати в RAII тільки пам’ять (`unique_ptr`), а mutex, chip select і канали DMA лишати на ручні виклики.
- Брати RTOS-guard в ISR: mutex API CMSIS-RTOS2 звідти викликати не можна.[^cmsis-rtos2-mutex]
