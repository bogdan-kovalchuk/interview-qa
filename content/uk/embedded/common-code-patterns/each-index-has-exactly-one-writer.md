---
id: emb-patterns-0041
title: "Який спільний інваріант робить SPSC ring buffer безпечним без локів?"
description: "Кожен індекс має рівно одного writer-а: producer пише тільки head, consumer – тільки tail."
track: embedded
section: common-code-patterns
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Підтверджує, що data race на не-атомарних об’єктах є undefined behavior (5.1.2.4 п. 25), що `volatile` лише вимагає виконання доступів за правилами abstract machine (6.7.3 п. 7), і описує _Atomic, memory_order (7.17.3) та atomic_signal_fence (7.17.4.2); вибір примітивів для конкретного MCU залежить від тулчейна."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (Linux kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: "7.3.0-rc6"
    applicability: "Описує схему з одним producer і одним consumer без спільного локу, маску для буфера розміром у степінь двійки, завжди вільний один елемент та release/acquire-порядок запису даних і індексів. Це документація ядра Linux (SMP), а не bare-metal MCU: ідею можна переносити, а конкретні макроси й бар’єри – ні."
---

## Short answer

**Кожен індекс має рівно одного writer-а: producer пише тільки `head`, consumer – тільки `tail`.**

Оскільки немає спільної змінної, яку обидві сторони змінюють (як `count`), немає й read-modify-write гонки.[^linux-circular-buffers] Чужий індекс сторона лише читає, і це безпечно тільки тоді, коли доступ до нього атомарний і впорядкований щодо даних буфера (release/acquire або еквівалентний barrier), а не просто `volatile`.[^iso-c-n1570]

Правило: «один writer на змінну» – основа lock-free SPSC (single-producer / single-consumer) черг, але лише для рівно одного producer і одного consumer.[^linux-circular-buffers]

## Detailed explanation

Кільцевий буфер має два індекси: `head` – куди producer кладе наступний елемент, `tail` – звідки consumer бере наступний. Якщо `head` змінює тільки producer, а `tail` – тільки consumer, то жодна змінна не має двох writer-ів, і не потрібен ні лок, ні атомарний `count`.[^linux-circular-buffers] Спільний лічильник `count++` у producer і `count--` у consumer – це два read-modify-write над однією змінною: ISR може перервати main між читанням і записом, і одне з оновлень загубиться. Один writer на змінну цю проблему знімає.

Але «один writer» – ще не вся безпека. Кожна сторона читає чужий індекс, а порядок має значення. Producer мусить спочатку записати дані в елемент і лише потім опублікувати новий `head`; consumer мусить спочатку прочитати `head`, і лише потім дані за ним. Для цього використовують запис з release і читання з acquire.[^linux-circular-buffers] У C11 це `_Atomic` індекси з `memory_order_release` та `memory_order_acquire`; `volatile` тут недостатній, бо він не робить доступ атомарним і не впорядковує звичайні записи даних відносно індексу, а data race на не-атомарному об’єкті – undefined behavior.[^iso-c-n1570] Якщо producer і consumer – це main та ISR на одному ядрі, зазвичай достатньо заборонити компілятору переставляти доступи (наприклад, `atomic_signal_fence`), бо апаратні fence-інструкції тоді не потрібні;[^iso-c-n1570] на багатоядерному чипі або при DMA потрібен справжній hardware ordering. Індекс має читатися й писатися однією інструкцією: 16-бітний індекс на 8-бітному MCU можна «розірвати» ISR посередині.

Ще дві деталі: розмір буфера зручно брати степенем двійки, тоді обгортання індексу – це `& (SIZE - 1)` замість ділення; а щоб відрізнити повний буфер від порожнього, один елемент залишають вільним.[^linux-circular-buffers]

```c
#include <stdatomic.h>
#include <stdbool.h>
#include <stdint.h>

#define SIZE 64u                       /* степінь двійки */

typedef struct {
    uint8_t buf[SIZE];
    _Atomic uint32_t head;             /* пише лише producer */
    _Atomic uint32_t tail;             /* пише лише consumer */
} spsc_t;

bool spsc_push(spsc_t *q, uint8_t v)   /* ілюстративно */
{
    uint32_t head = atomic_load_explicit(&q->head, memory_order_relaxed);
    uint32_t tail = atomic_load_explicit(&q->tail, memory_order_acquire);
    uint32_t next = (head + 1u) & (SIZE - 1u);
    if (next == tail) return false;    /* повний */
    q->buf[head] = v;
    atomic_store_explicit(&q->head, next, memory_order_release);
    return true;
}

bool spsc_pop(spsc_t *q, uint8_t *v)
{
    uint32_t tail = atomic_load_explicit(&q->tail, memory_order_relaxed);
    uint32_t head = atomic_load_explicit(&q->head, memory_order_acquire);
    if (tail == head) return false;    /* порожній */
    *v = q->buf[tail];
    atomic_store_explicit(&q->tail, (tail + 1u) & (SIZE - 1u), memory_order_release);
    return true;
}
```

**Типові помилки:**

- Тримати спільний `count`, який змінюють обидві сторони.
- Вважати, що `volatile` індекс замінює atomic і порядок записів: дані можуть стати видимими після індексу.
- Додати другого producer (наприклад, два ISR або ISR і main): інваріант «один writer» зникає, і потрібен лок або критична секція.
- Використати розмір, що не є степенем двійки, з маскою `& (SIZE - 1)`, або забути вільний елемент і не відрізняти повний буфер від порожнього.

## Sources

<!-- generated from frontmatter -->
