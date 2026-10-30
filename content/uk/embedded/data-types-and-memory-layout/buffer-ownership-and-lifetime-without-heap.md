---
id: emb-memlink-0014
title: "Як реалізувати ownership і lifetime для буферів без heap у embedded C?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Виділити буфери статично або в pool і явно визначити owner: driver, task, queue чи caller. Передавати не «сирий ресурс назавжди», а handle або descriptor зі станом `free/in_use/done`. Для ISR/DMA добре працюють ring buffer, double buffer і callback/queue, де lifetime завершується після явного release.[^dou-embedded-interview]

## Detailed explanation

### Чому heap уникають у надійних embedded-системах

У критично важливих вбудованих системах використання динамічного розподілу пам’яті (`malloc`, `free`) суворо обмежується або повністю забороняється стандартами функціональної безпеки (наприклад, MISRA C:2012 Rule 21.3). Головними причинами є недетермінований час виконання алокації, ризик фрагментації heap (heap fragmentation), коли вільна пам’ять є, але неможливо знайти неперервний блок, та відсутність гарантій успішного виділення пам’яті під час тривалої роботи пристрою.[^freertos-heap]

Без віртуальної пам’яті та MMU пам’ять розподіляється статично ще на етапі лінкування у секціях `.bss` або `.data`.[^gnu-ld-manual] Проте обробка мережевих пакетів, кадрів протоколів зв’язку (CAN, UART, Ethernet) чи буферизація даних сенсорів вимагають чіткої дисципліни володіння ресурсами (buffer ownership) та контролю часу їхнього життя (lifetime).

### Статичні пули фіксованих блоків (buffer pools)

Класичним підходом для заміни динамічної пам’яті є пул буферів однакового фіксованого розміру (fixed-block pool). Структурно такий механізм реалізується у вигляді статичного масиву буферів та відповідного пулу дескрипторів:

```c
#define POOL_SIZE   8
#define BUFFER_SIZE 128

typedef enum {
    BUF_STATE_FREE = 0,
    BUF_STATE_ACQUIRED,
    BUF_STATE_PENDING_TX
} buf_state_t;

typedef struct {
    uint8_t raw_data[BUFFER_SIZE];
    uint16_t length;
    buf_state_t state;
} packet_desc_t;

static packet_desc_t g_packet_pool[POOL_SIZE];
```

Виділення та повернення буфера в такому пулі здійснюється за постійний час O(1) через однозв’язний список вільних індексів або бітову маску (bitmask). Оскільки розмір кожного блоку зафіксований, явище зовнішньої фрагментації принципово виключається.

### Моделі передачі власності (ownership transfer)

Для уникнення race conditions та memory leaks у багатозадачному середовищі застосовують декілька шаблонів володіння:

1. **Caller-allocated buffer:** функція-споживач ніколи не володіє пам’яттю. Викликаюча сторона передає покажчик на вже виділений буфер та його максимальну місткість (`int uart_read(uint8_t *dest, size_t max_len)`). Lifetime буфера прив’язаний до області видимості caller-а.[^iso-c-n1570]
2. **Transfer ownership via queue:** задача-генератор (наприклад, парсер протоколу) бере дескриптор із пулу, заповнює корисним навантаженням і відправляє покажчик або індекс у чергу повідомлень RTOS (FreeRTOS `xQueueSend`). У момент надсилання генератор вважає буфер відчуженим і більше не має права звертатися до нього. Задача-обробник вичитує дескриптор з черги, стає його ексклюзивним власником, виконує обробку і після завершення повертає блок назад у пул (`buffer_release(desc)`).
3. **Borrowing (позичання):** власник тимчасово передає константний покажчик на дані іншому модулю для читання без права збереження посилання на майбутнє.

### Подвійна буферизація та кільцеві буфери для ISR і DMA

Для безперервної взаємодії апаратних периферійних модулів (DMA, ADC, SPI) з обчислювальними задачами використовуються спеціалізовані структури:

- **Подвійна буферизація (Ping-Pong / Double Buffering):** два статичні буфери чергують свої ролі. Поки DMA контролер наповнює перший буфер у фоновому режимі, процесорне ядро обробляє раніше отримані дані у другому буфері. Після виникнення переривання DMA Transfer Complete буфери міняються ролями. Це гарантує нульове копіювання і повну відсутність конфліктів доступу між ядром та DMA.
- **Кільцевий буфер (Ring Buffer / FIFO):** lock-free структура на основі статичного масиву з двома покажчиками або індексами `head` та `tail`. Переривання (ISR) записує байти за індексом `head`, а фоновий потік вичитує їх за індексом `tail`. Завдяки атомарному оновленню індексів передача байтів відбувається без блокування переривань та без залучення динамічної пам’яті.
