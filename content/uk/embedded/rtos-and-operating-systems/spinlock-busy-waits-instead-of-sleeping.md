---
id: emb-rtos-0006
title: "Що таке spinlock?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: posix-pthread-spin-lock
    title: "POSIX.1-2024: pthread_spin_lock, pthread_spin_trylock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_spin_lock.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-kernel-locking-guide
    title: "Linux kernel: Unreliable Guide To Locking"
    url: https://docs.kernel.org/kernel-hacking/locking.html
  - source_id: linux-locking-lessons
    title: "Linux kernel: Locking lessons (spin locks)"
    url: https://docs.kernel.org/locking/spinlocks.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
  - source_id: linux-man-sched
    title: "Linux manual page: sched(7)"
    url: https://man7.org/linux/man-pages/man7/sched.7.html
---

## Short answer

**Spinlock** – примітив синхронізації, при якому потік, що не може отримати lock, **крутиться (spin) у циклі**, постійно перевіряючи доступність, замість того щоб засипати.[^dou-embedded-interview]

Перевага: низька латентність, якщо очікування дуже коротке. У kernel-space spinlock використовують там, де sleep заборонений; залежно від типу lock і контексту він може вимикати preemption або IRQ. У user-space spinlock – це просто busy waiting primitive.

Правило: <span class="warn">не можна спати, тримаючи spinlock</span>; Якщо критична секція довга або код може блокуватися – краще mutex.

## Detailed explanation

### Механізм

Spinlock – це lock, у якого потік, що не зміг його захопити, не передає процесор планувальнику, а циклічно повторює спробу. POSIX формулює це прямо: `pthread_spin_lock()` захоплює lock, якщо його ніхто не тримає; інакше потік «крутиться», тобто не повертається з виклику, доки lock не звільниться. Повторне захоплення тим самим потоком дає undefined behavior, а `pthread_spin_trylock()` замість очікування повертає `EBUSY`.[^posix-pthread-spin-lock]

Основа будь-якого spinlock – атомарна операція read-modify-write. У C11 найпростіший такий тип – `atomic_flag`: `atomic_flag_test_and_set` атомарно встановлює прапорець і повертає його попереднє значення, а операції над `atomic_flag` стандарт зобов’язує бути lock-free.[^iso-c-n1570] Мінімальна реалізація:

```c
#include <stdatomic.h>

static atomic_flag lock = ATOMIC_FLAG_INIT;

void spin_lock(void)
{
    while (atomic_flag_test_and_set_explicit(&lock, memory_order_acquire)) {
        /* busy wait: the CPU keeps executing this loop */
    }
}

void spin_unlock(void)
{
    atomic_flag_clear_explicit(&lock, memory_order_release);
}
```

Порядок пам’яті тут не декоративний. Release-операція над об’єктом synchronizes with acquire-операцією, яка прочитала записане нею значення, тож усе, що власник записав у критичній секції, видно наступному власнику.[^iso-c-n1570] Spinlock без acquire/release захищає лише сам прапорець, але не дані.

### Чому не засинати

Mutex при зайнятому lock переводить задачу в очікування, і процесор виконує іншу роботу. Spinlock натомість спалює процесорний час, зате не платить за context switch і може використовуватися там, де засинати не можна. У Linux kernel саме так розділені два основні типи lock: spinlock малий, швидкий і придатний будь-де, а mutex дозволяє блокуватися, тому в контексті переривання, де спати не можна, лишається spinlock.[^linux-kernel-locking-guide]

Звідси головне правило: функції, які можуть заснути (прямо чи опосередковано викликати `schedule()`), не можна викликати, тримаючи spinlock або з вимкненим preemption. Kernel-документація називає типові приклади: `copy_from_user()`, `copy_to_user()`, `kmalloc(GFP_KERNEL)`, `mutex_lock()`.[^linux-kernel-locking-guide] Інтерв’юер очікує, що кандидат пов’яже це правило з наслідком: якщо власник spinlock заснув, кожен, хто намагається захопити lock, крутиться весь час цього сну й марно спалює процесор.

### Spinlock і переривання

Якщо ті самі дані змінює обробник переривання, звичайного `spin_lock()` недостатньо. Код задачі захопив lock, на тому ж CPU приходить переривання, обробник намагається захопити той самий lock і крутиться вічно, бо власник не продовжить роботу, доки обробник не завершиться. На іншому CPU така ситуація безпечна. Тому існує `spin_lock_irqsave()`: він вимикає переривання лише локально, а взаємне виключення між CPU забезпечує сам lock.[^linux-locking-lessons] Варіанти `_bh()`, `_irq()` і `_irqsave()/_irqrestore()` додатково вимикають softirq або апаратні переривання.[^linux-lock-types]

### Одне ядро і PREEMPT_RT

На одноядерній системі крутитися немає сенсу: власник lock не може виконуватися одночасно з тим, хто чекає. Linux це враховує: у ядрі без `CONFIG_SMP` і без `CONFIG_PREEMPT` spinlock не існує взагалі, а з `CONFIG_PREEMPT` він просто вимикає preemption.[^linux-kernel-locking-guide] Аналог на одноядерному MCU під RTOS – не busy wait, а критична секція: у FreeRTOS між `taskENTER_CRITICAL()` і `taskEXIT_CRITICAL()` перемикання задач неможливе, а на портах із вкладеними перериваннями можуть виконуватися лише переривання з логічним пріоритетом вище `configMAX_SYSCALL_INTERRUPT_PRIORITY`, і їм заборонено викликати FreeRTOS API.[^freertos-kernel-book]

У ядрі з `PREEMPT_RT` семантика змінюється: `spinlock_t` і `rwlock_t` реалізовані через `rt_mutex`, preemption не вимикається, а суфікси `_irq`/`_irqsave` не змінюють стан переривань CPU. Справжнім spinning lock у всіх конфігураціях лишається `raw_spinlock_t`, і його рекомендують лише для дуже короткого низькорівневого коду, де справді потрібно вимкнути preemption або переривання.[^linux-lock-types]

### Пастки в user space

У user space spinlock не вимикає ні preemption, ні переривання. Власника можуть витіснити посеред критичної секції, і тоді всі, хто чекає, марно витрачають свої кванти. POSIX попереджає, що spin lock схильний до priority inversion.[^posix-pthread-spin-lock] На одному ядрі з політикою `SCHED_FIFO` це може стати повною зупинкою: потік `SCHED_FIFO` виконується, доки не заблокується, не викличе `sched_yield()` або не буде витіснений потоком з вищим пріоритетом.[^linux-man-sched] Якщо крутиться потік із вищим пріоритетом, ніж власник lock, власник не отримує процесор і не звільнить lock.

Практичний висновок: spinlock виправданий, коли є кілька ядер, критична секція коротка й обмежена в часі та в ній немає блокувальних викликів. Якщо секція довга, може заснути або система одноядерна, правильний вибір – mutex (у RTOS – із priority inheritance) або критична секція RTOS.
