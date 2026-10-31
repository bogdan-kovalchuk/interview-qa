---
id: emb-irq-0009
title: "Як передаються дані між ISR і main loop або RTOS task без race condition?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
  - source_id: freertos-isr-comms
    title: "FreeRTOS xTaskNotifyFromISR API reference"
    url: https://www.freertos.org/Documentation/02-Kernel/04-API-references/05-Direct-to-task-notifications/07-xTaskNotifyFromISR
  - source_id: freertos-semphr-h
    title: "FreeRTOS-Kernel: include/semphr.h (опис API семафорів і м’ютексів)"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/include/semphr.h
---

## Short answer

Використовують **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores або direct task notification. Shared multi-byte state захищають interrupt disable, mutex у task context або atomic operations, залежно від платформи. <span class="warn">Сам по собі `volatile` не робить операцію atomic і не вирішує race condition.</span>[^dou-embedded-interview]

## Detailed explanation

Передача даних між асинхронним обробником переривання (ISR) та основним потоком виконання (main loop або задачею RTOS) є однією з найвідповідальніших операцій у низькорівневому програмуванні. Стан гонитви (Race Condition) виникає, коли один потік зчитує або модифікує спільні дані одночасно з тим, як ISR асинхронно перериває його виконання і змінює той самий стан.

### Природа стану гонитви та міф про volatile

Кваліфікатор типу `volatile` інструктує компілятор C/C++ не викидати операції доступу до змінної та не кешувати її значення в регістрах процесора між викликами.[^iso-c-n1570] Проте `volatile` не надає жодних гарантій атомарності:
- **Операції Read-Modify-Write:** Вираз `counter++` над `volatile`-змінною на Cortex-M зазвичай компілюється в три послідовні машинні інструкції: завантаження значення з пам’яті в регістр (`LDR`), інкремент регістра (`ADD`) і запис результату назад у пам’ять (`STR`). Якщо переривання спрацює між `LDR` та `STR`, обробник змінить значення в пам’яті, але після повернення основний потік запише свій старий інкрементований результат, безповоротно стерши оновлення від ISR.
- **Розрив багатобайтних даних (Torn Reads/Writes):** Якщо розмір змінної (наприклад, 64-бітне ціле `uint64_t` або складна структура) перевищує розрядність шини даних або регістрів процесора (32 біти на Cortex-M), процесор оновлює її кількома інструкціями пам’яті. Спрацьовування ISR посеред цього процесу призведе до того, що одна половина даних належатиме новому значенню, а друга – старому.

### Архітектурні підходи до безпечної передачі даних

1. **Критичні секції на основі маскування переривань:**
   - На рівні фонового потоку (task або main loop) читання або запис спільного стану захищається тимчасовим відключенням переривань.
   - Важливо зберігати попередній стан регістра маски (наприклад, `PRIMASK` або `BASEPRI` в ARM), а не безумовно вмикати переривання назад, щоб коректно підтримувати вкладені критичні секції:
     ```c
     uint32_t mask = __get_PRIMASK();
     __disable_irq();
     /* Безпечний доступ до спільних даних */
     shared_data = new_value;
     __set_PRIMASK(mask);
     ```
   - Тривалість перебування в критичній секції повинна бути зведена до абсолютного мінімуму (кілька машинних слів копіювання), щоб не збільшувати системну латентність переривань.

2. **Кільцевий буфер типу Single-Producer Single-Consumer (Lock-Free FIFO):**
   - Для безперервного потоку даних (байтів UART, відліків АЦП) найефективнішим є кільцевий буфер без блокувань (lock-free ring buffer).[^linux-circular-buffers]
   - Один учасник є виключним автором індексу запису (`head`), а інший – індексу читання (`tail`).
   - Якщо змінні `head` і `tail` мають тип із розміром машинного слова (наприклад, `uint32_t`) і вирівняні в пам’яті, читання та запис індексів є апаратно атомарними.
   - Виробник (ISR) записує байт за адресою `buffer[head]`, після чого виконує бар’єр пам’яті `__DMB()` і публікує нове значення `head = (head + 1) & MASK`. Споживач бачить новий індекс лише після того, як самі дані вже надійно збережені в пам’яті.

3. **Апаратні атомарні операції та інструкції ексклюзивного доступу:**
   - Ядра ARM Cortex-M3/M4/M7 підтримують пару інструкцій `LDREX` та `STREX` (Load/Store Exclusive).
   - Вони дозволяють реалізувати безпечні операції Compare-and-Swap (CAS) або атомарні лічильники стандарту C11 (`<stdatomic.h>`) без повного блокування контролера переривань.

4. **Механізми операційних систем реального часу (RTOS):**
   - **FromISR API:** В операційних системах типу FreeRTOS функції синхронізації розділені на виклики з потоків та виклики з обробників переривань (наприклад, `xQueueSendToBackFromISR`, `xSemaphoreGiveFromISR`, `xTaskNotifyFromISR`).[^freertos-semphr-h][^freertos-isr-comms]
   - **Direct Task Notifications:** Швидкий спосіб передачі сигналу або 32-бітного лічильника/маски подій напряму в задачу (`xTaskNotifyFromISR`). Задача очікує подію у заблокованому стані без споживання процесорного часу.
   - **Спеціальний параметр `pxHigherPriorityTaskWoken`:** дозволяє визначити, чи має розблокована задача вищий пріоритет за перерваний потік, і запросити перемикання контексту прямо на виході з ISR.

### Неприпустимі операції та помилки

- **Використання м’ютексів всередині ISR:** у FreeRTOS м’ютекси не можна використовувати з обробників переривань.[^freertos-semphr-h] Вони реалізують успадкування пріоритетів, яке має сенс лише між задачами, а `xSemaphoreTake` може перевести викликача в стан очікування (Blocked), тоді як обробник переривання не має власного контексту задачі для блокування. Наслідок такого виклику – не гарантована діагностика, а спрацювання перевірки (`configASSERT`, якщо її ввімкнено) або непередбачувана поведінка ядра.
- **Ігнорування когерентності кешу (D-Cache Coherency):** Якщо передача даних виконується контролером DMA, а ISR лише встановлює прапорець завершення, ядро із увімкненим кешем даних (Cortex-M7), якщо буфер лежить у кешованій області пам’яті, зобов’язане виконати інвалідацію рядків кешу пам’яті буфера перед його читанням.
