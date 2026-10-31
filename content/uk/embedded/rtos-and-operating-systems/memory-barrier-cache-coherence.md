---
id: emb-rtos-0007
title: "Що таке memory barrier і cache coherence?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: linux-memory-barriers
    title: "Linux kernel memory barriers"
    url: https://docs.kernel.org/core-api/wrappers/memory-barriers.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cmsis-core-intrinsics
    title: "CMSIS-Core (Cortex-M): Intrinsic Functions for CPU Instructions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__intrinsic__CPU__gr.html
  - source_id: cmsis-core-cache
    title: "CMSIS-Core (Cortex-M): Cache Functions (Level-1)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__cache__functions__m7.html
  - source_id: cmsis-core-dcache
    title: "CMSIS-Core (Cortex-M): D-Cache Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Dcache__functions__m7.html
  - source_id: linux-dma-api-howto
    title: "Linux kernel: Dynamic DMA mapping Guide"
    url: https://docs.kernel.org/core-api/dma-api-howto.html
---

## Short answer

**Memory barrier** – інструкція або compiler primitive, яка обмежує переупорядкування операцій пам’яті компілятором або CPU. Вона потрібна, коли порядок доступів важливий: lock-free код, MMIO-регістри, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** – узгодженість копій даних у кешах різних CPU/core або між cache і пам’яттю, з якою працює DMA. Якщо DMA записав буфер у RAM, CPU може все ще бачити стару copy в cache без invalidate/clean.

Практично: для shared memory використовують atomics/barriers, а для DMA – cache clean/invalidate або non-cacheable buffers залежно від MCU/MPU.

## Detailed explanation

Memory barrier і cache coherence часто плутають, хоча вони відповідають на різні запитання. Barrier задає **порядок**, у якому доступи до пам’яті стають видимими іншим учасникам. Coherence визначає, чи бачать ці учасники **однаковий вміст** тієї самої адреси. Одне не замінює інше.

### Хто переставляє доступи

Переставляти можуть двоє: компілятор і процесор. Компілятор має право змінювати порядок незалежних load/store і тримати значення в регістрі, бо в однопотоковому коді результат від цього не змінюється. Linux kernel має для цього `barrier()` – compiler barrier, який не дає перенести доступи через себе й змушує в циклі перечитувати змінні з умови. Документація прямо застерігає, що compiler barrier не має прямого впливу на CPU, а `READ_ONCE()`/`WRITE_ONCE()` реалізовані як volatile-доступи і є лише слабкою формою того самого `barrier()`.[^linux-memory-barriers] Тому `volatile` сам по собі не впорядковує доступи для іншого ядра чи пристрою.

CPU може виконувати інструкції й ставити load/store у чергу доступів у зручному йому порядку, якщо для самого ядра причинність програми зберігається. Усередині одного CPU barrier не потрібен: ядро завжди бачить власні доступи в програмному порядку. Barrier потрібен там, де є інший спостерігач – інше ядро або пристрій.[^linux-memory-barriers]

У C11 цю різницю видно в API: `atomic_thread_fence()` – повноцінний fence, а `atomic_signal_fence()` обмежує компілятор так само, але не генерує апаратних fence-інструкцій і впорядковує лише потік і обробник сигналу в тому самому потоці.[^iso-c-n1570]

### Barrier працює в парі

Barrier на одному боці нічого не гарантує, якщо другий бік читає без упорядкування. Linux вимагає парувати barriers: write barrier у того, хто публікує дані, і read, acquire або address-dependency barrier у того, хто їх читає; відсутність пари майже напевно є помилкою.[^linux-memory-barriers] У C11 типовий спосіб – release-запис прапорця і acquire-читання: release synchronizes with acquire, яке прочитало записане значення, тож дані, записані до прапорця, видно після його читання.[^iso-c-n1570]

```c
#include <stdatomic.h>
#include <stdint.h>

static uint32_t payload;
static atomic_int ready;

void producer(void)            /* core 0 */
{
    payload = 42;
    atomic_store_explicit(&ready, 1, memory_order_release);
}

int consumer(uint32_t *out)    /* core 1 */
{
    if (atomic_load_explicit(&ready, memory_order_acquire) == 0) {
        return 0;
    }
    *out = payload;            /* guaranteed to see 42 */
    return 1;
}
```

На Cortex-M відповідні інструкції доступні через CMSIS: `__DMB()` гарантує видимий порядок явних доступів до і після інструкції, не чекаючи їхнього завершення, а `__DSB()` завершується лише тоді, коли завершилися всі попередні явні доступи.[^cmsis-core-intrinsics] У Linux SMP barriers (`smp_mb()`, `smp_wmb()`, `smp_rmb()`) на однопроцесорній збірці зводяться до compiler barrier, а mandatory barriers (`mb()`, `wmb()`, `rmb()`) потрібні навіть без SMP, коли порядок має побачити пристрій.[^linux-memory-barriers]

### Cache coherence між ядрами і з DMA

Між ядрами одного coherent-домену апаратний протокол переносить cache line туди, де до неї звертаються, тож кожен load чи store для інших CPU виглядає так, ніби доступ дійшов до пам’яті.[^linux-memory-barriers] Це не скасовує barriers: coherence гарантує узгоджений вміст однієї адреси, а порядок між різними адресами задають barriers або atomics (детальніше – qid:emb-dtypes-0106 і qid:emb-rtos-0003).

З DMA ситуація інша: не кожна система підтримує coherence з пристроями. Тоді пристрій може прочитати з RAM застарілі дані, бо dirty-рядки ще в кеші CPU, – потрібен clean (flush). У зворотному напрямку CPU може бачити стару копію в кеші або навіть затерти щойно записані DMA дані, коли dirty-рядок буде витіснено в RAM, – потрібен invalidate. Доступи MMIO зазвичай обходять кеш, тому можуть «обігнати» раніший запис у кешовану пам’ять; barrier тут недостатній, потрібен flush.[^linux-memory-barriers]

Linux DMA API розрізняє coherent mappings, де апаратура гарантує взаємну видимість без явного flush, і streaming mappings, які перебувають «поза coherency domain» і потребують явної синхронізації. Coherent-пам’ять не скасовує barriers: якщо пристрій має побачити перше слово descriptor раніше за прапорець валідності, між записами потрібен `wmb()`.[^linux-dma-api-howto] Для такого обміну з descriptor є і спеціальні `dma_rmb()`/`dma_wmb()`, але вони не впорядковують доступи до MMIO.[^linux-memory-barriers]

### Що це означає на MCU

Деякі ядра Cortex-M, наприклад M7 і M55, мають опційний L1 instruction і data cache.[^cmsis-core-cache] Для них CMSIS дає `SCB_CleanDCache_by_Addr()`, `SCB_InvalidateDCache_by_Addr()` і `SCB_CleanInvalidateDCache_by_Addr()`, де адреса має бути вирівняна на межу 32 байти.[^cmsis-core-dcache] Типова послідовність: перед TX-DMA – clean буфера, після RX-DMA – invalidate перед читанням.[^linux-memory-barriers] Буфер DMA не повинен ділити cache line з іншими змінними: Linux-документація описує саме цей сценарій, коли CPU пише одне слово, DMA – інше в тому самому рядку, і один із записів губиться.[^linux-dma-api-howto] Альтернатива – розмістити буфери в non-cacheable регіоні, якщо це дозволяє конфігурація пам’яті конкретного MCU.

### Що хоче почути інтерв’юер

- Barrier задає порядок, а не очищає кеш; cache maintenance задає вміст, а не порядок.
- Compiler barrier і `volatile` не впливають на перестановки в CPU.
- Barriers працюють парами: публікація з release, читання з acquire.
- Coherence між ядрами ще не означає coherence з DMA, а MMIO має окремі правила.
