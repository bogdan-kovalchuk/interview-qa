---
id: emb-raii-0002
title: "Чому RAII критичний саме в embedded?"
description: "Немає OS (operating system) страхувальної сітки й garbage collector – забутий ресурс може лишитися зайнятим до reset."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує mutex API CMSIS-RTOS2: osMutexAcquire і osMutexRelease (коди повернення, зокрема osErrorResource при release без acquire чи не власником; недоступні з ISR), атрибути osMutexRecursive та osMutexRobust. Конкретна RTOS-реалізація поза специфікацією може поводитися інакше."
  - source_id: linux-man-exit
    title: "Linux man-pages: _exit(2)"
    url: https://man7.org/linux/man-pages/man2/_exit.2.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Каже, що _exit() завершує процес і закриває всі його відкриті файлові дескриптори. Стосується Linux-процесів; про bare-metal MCU і про не-файлові ресурси нічого не каже."
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує __disable_irq, __enable_irq, __get_PRIMASK, __set_PRIMASK: PRIMASK, коли встановлений, блокує всі винятки з конфігурованим пріоритетом; __disable_irq і __enable_irq виконуються лише в privileged mode. Сторінка позначає __get_PRIMASK як доступний лише для Armv8-M, тож доступність для конкретного ядра треба перевіряти в його документації."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: при кожній передачі керування в межах функції (зокрема при поверненні з неї) automatic-змінні блоку, активні в точці відправлення й неактивні в точці призначення, знищуються у зворотному порядку конструювання. Не охоплює завершення програми через exit чи abort і не описує винятки."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що std::abort завершує програму без виконання деструкторів, а std::exit не знищує automatic-об’єкти; freestanding-реалізації можуть не мати цих функцій."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: обгортати ресурс із парними acquire/release в об’єкт, що захоплює в конструкторі й звільняє в деструкторі; приклади – файли, mutex, пам’ять, не апаратна периферія."
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

## Sources

<!-- generated from frontmatter -->
