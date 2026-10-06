---
id: emb-patterns-0035
title: "Чому ISR пише дані у слот ДО оновлення `head` (порядок операцій)?"
description: "Щоб consumer ніколи не побачив просунутий head, який вказує на ще не записаний байт."
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
    applicability: "Підтверджує семантику release/acquire для atomic-операцій (5.1.2.4, 7.17.3) і правила для звичайних та volatile-доступів (5.1.2.3); не описує переривання, апаратні core чи конкретні пристрої."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує протокол single-producer/single-consumer: елемент записують до публікації `head` через release-store, consumer читає `head` через acquire-load і звільняє слот через `tail`; це документація ядра Linux, тож для MCU вона слугує зразком протоколу, а не специфікацією."
  - source_id: gcc-volatiles
    title: "GCC 16.1.0: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Volatiles.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Підтверджує, що доступи до non-volatile об’єктів не впорядковані щодо volatile-доступів і що volatile-об’єкт не можна використати як memory barrier; не стосується апаратного впорядкування між core."
---

## Short answer

**Щоб consumer ніколи не побачив просунутий `head`, який вказує на ще не записаний байт.**

`head` публікує запис: consumer вважає готовими всі слоти до нього, тож дані мають бути записані й видимі першими. Це важливо, коли consumer може виконатися «посередині» (інший core, вкладене переривання, витіснена задача), а також проти переупорядкування компілятором чи CPU – тому `head` публікують release-store, а читають acquire-load.[^linux-circular-buffers][^iso-c-n1570]

Правило: producer: дані -> `head`; consumer: дані -> `tail`.

## Detailed explanation

У кільцевому буфері з одним producer-ом і одним consumer-ом індекс `head` працює як **публікація запису**: consumer, побачивши `head != tail`, вважає слот `tail` готовим і читає його без додаткових перевірок. Тому producer мусить спершу повністю записати дані в слот і лише потім просунути `head`. Симетрично consumer спершу дочитує слот, а тоді просуває `tail`, бо саме `tail` повідомляє producer-у, що слот можна перезаписувати.[^linux-circular-buffers]

Пояснення «між двома кроками можуть перервати» правильне лише тоді, коли consumer справді може виконатися посередині: producer – задача, яку витісняє ISR-consumer; consumer працює на іншому core; або його запускає вкладене переривання з вищим пріоритетом. Коли ISR на одному core пише, а `main`-цикл читає, `main` не може вклинитися в тіло ISR, і проблема виникає з іншого боку: порядок записів у вихідному коді ще не означає такий самий порядок виконання. Компілятор вправі поміняти місцями два записи в різні об’єкти, якщо однопотокова поведінка не змінюється, а `volatile` тут не допомагає: доступи до non-volatile об’єктів не впорядковані щодо volatile-доступів.[^gcc-volatiles]

Переносне рішення – пара release/acquire з C11. Producer публікує `head` через `memory_order_release`, consumer читає його через `memory_order_acquire`; release-операція синхронізується з acquire-операцією, що прочитала записане значення, тож усе записане до `head` стає видимим consumer-у після цього читання.[^iso-c-n1570] Ядро Linux робить те саме через `smp_store_release()` і `smp_load_acquire()`, а сам протокол безпечний лише для одного producer-а й одного consumer-а.[^linux-circular-buffers] Приклад ілюстративний:

```c
#include <stdatomic.h>
#include <stdint.h>

#define RB_SIZE 8u                       /* степінь двійки */
static uint8_t buf[RB_SIZE];
static _Atomic uint32_t head, tail;

int rb_push(uint8_t byte)                /* producer, напр. ISR */
{
    uint32_t h = atomic_load_explicit(&head, memory_order_relaxed);
    uint32_t t = atomic_load_explicit(&tail, memory_order_acquire);
    uint32_t next = (h + 1u) & (RB_SIZE - 1u);
    if (next == t) return -1;            /* буфер повний */
    buf[h] = byte;                       /* 1: дані */
    atomic_store_explicit(&head, next, memory_order_release); /* 2: публікація */
    return 0;
}
```

**Типові помилки:**

- Просувати `head` до запису або писати `buf[head++] = byte`: порядок побічного ефекту `++` відносно запису в слот не гарантований.[^iso-c-n1570]
- Вважати `volatile head` бар’єром для даних у слоті.[^gcc-volatiles]
- Застосовувати цю схему з кількома producer-ами або consumer-ами без окремого серіалізування.[^linux-circular-buffers]
- Читати `head` у consumer без acquire (або з кешованим значенням) і потім читати слот.

## Sources

<!-- generated from frontmatter -->
