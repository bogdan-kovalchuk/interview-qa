---
id: emb-rtos-0002
title: "Що таке mutex?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: posix-2024-definitions
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 3. Definitions"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: posix-2024-general-concepts
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 4. General Concepts"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html
  - source_id: linux-man-futex7
    title: "Linux manual page: futex(7)"
    url: https://man7.org/linux/man-pages/man7/futex.7.html
  - source_id: linux-mutex-design
    title: "Linux kernel documentation: Generic Mutex Subsystem"
    url: https://docs.kernel.org/locking/mutex-design.html
---

## Short answer

**Mutex** – примітив синхронізації для взаємовиключного доступу до shared resource.[^dou-embedded-interview] Тільки один потік може володіти mutex одночасно; інші потоки мають чекати.

Якщо mutex зайнятий, потік зазвичай блокується і переходить у sleep, тому CPU не витрачається на активне очікування. Це головна відмінність від spinlock, який крутиться в циклі.

Використовується для захисту shared data, наприклад списків, черг, counters або структур стану; Важливо брати й відпускати mutex у зрозумілому порядку, щоб не створити deadlock.

## Detailed explanation

### Визначення: взаємне виключення плюс власник

POSIX визначає mutex як об’єкт синхронізації, що дозволяє кільком потокам серіалізувати доступ до спільних даних; назва походить від mutual exclusion. Потік, який захопив mutex, стає його власником і лишається ним, доки **цей самий** потік не звільнить mutex.[^posix-2024-definitions] Саме власність відрізняє mutex від семафора й уможливлює перевірку помилок і priority inheritance (детальніше – qid:emb-rtos-0009).

FreeRTOS пояснює mutex як токен, пов’язаний зі спільним ресурсом: задача, що хоче звернутися до ресурсу, мусить спершу взяти токен, а закінчивши, обов’язково повернути. Важливо, що механізм тримається лише на дисципліні програміста: апаратно ресурс нічим не захищений, кожна задача просто домовляється не чіпати його без токена.[^freertos-kernel-book] Код, що звертається до даних в обхід mutex, повертає race condition (qid:emb-rtos-0001).

### Семантика lock і unlock

Якщо mutex уже захоплений іншим потоком, `pthread_mutex_lock()` блокує викликача, доки mutex не звільниться, і повертається з mutex у захопленому стані та з викликачем як власником. Коли `pthread_mutex_unlock()` звільняє mutex, на якому чекають потоки, хто з них отримає його, визначає політика планування.[^posix-pthread-mutex-lock]

Друга, менш очевидна гарантія – синхронізація пам’яті: захоплення mutex і його звільнення синхронізують пам’ять відносно інших потоків.[^posix-2024-general-concepts] Тому дані, записані всередині критичної секції, гарантовано видно наступному власнику, і додатково ставити бар’єри чи `volatile` не потрібно.

```c
#include <pthread.h>

static pthread_mutex_t stats_lock = PTHREAD_MUTEX_INITIALIZER;
static unsigned long rx_bytes, rx_packets;   /* invariant: updated together */

void stats_add(unsigned long len)
{
    pthread_mutex_lock(&stats_lock);
    rx_bytes += len;
    rx_packets++;
    pthread_mutex_unlock(&stats_lock);
}
```

Тут mutex захищає не одну змінну, а інваріант між двома: читач, що теж бере `stats_lock`, ніколи не побачить оновлений `rx_bytes` без оновленого `rx_packets`. Окремі атомарні змінні такого не гарантують.

### Типи POSIX mutex

Поведінка при повторному захопленні власником і при звільненні не власником залежить від типу:[^posix-pthread-mutex-lock]

- `PTHREAD_MUTEX_NORMAL`: повторний `lock` – deadlock; `unlock` не власником – undefined behavior (для robust mutex – помилка);
- `PTHREAD_MUTEX_ERRORCHECK`: в обох випадках повертається помилка – зручно під час налагодження;
- `PTHREAD_MUTEX_RECURSIVE`: власник може захопити mutex повторно, ведеться лічильник, і mutex звільняється, коли лічильник повернеться до нуля; `unlock` не власником – помилка;
- `PTHREAD_MUTEX_DEFAULT`: для non-robust варіанта поведінка в обох випадках не визначена, якщо реалізація не відображає цей тип на один із трьох інших; переносимий код не повинен покладатися ні на повторне захоплення, ні на звільнення не власником.

Окремо є robust mutex: якщо процес власника завершився, поки той тримав mutex, наступний `pthread_mutex_lock()` повертає `EOWNERDEAD` (якщо завершився лише потік-власник, а процес живий, стандарт дозволяє, але не вимагає цієї помилки); mutex при цьому вже захоплений викликачем, а застосунок має відновити узгодженість даних і викликати `pthread_mutex_consistent()`.[^posix-pthread-mutex-lock]

### Чи справді mutex «засинає», а не крутиться

Спрощення «mutex блокує потік, spinlock крутиться в циклі» правильне за суттю, але реалізації гібридні:

- **user space Linux.** Примітиви NPTL побудовані на futex. Якщо конкуренції немає, операція повністю виконується в user space атомарною інструкцією над цілим числом, і ядро залучається лише для арбітражу, коли потрібно заснути або розбудити.[^linux-man-futex7] Тобто незайнятий mutex зазвичай захоплюється без системного виклику.
- **ядро Linux.** `struct mutex` має три шляхи: fastpath – атомарний `cmpxchg()` поля власника; midpath – optimistic spinning, поки власник виконується на іншому CPU і немає задач із вищим пріоритетом; slowpath – постановка в чергу очікування і сон. Документація прямо називає це гібридом.[^linux-mutex-design]

Правила для mutex ядра Linux варто знати й поза ядром: тримати mutex може лише одна задача; звільнити – лише власник; повторне й рекурсивне захоплення заборонені; задача не може завершитися, тримаючи mutex; mutex не можна використовувати в контексті апаратних чи програмних переривань.[^linux-mutex-design] Варіант для контексту переривань – spinlock (qid:emb-rtos-0006).

### Mutex у FreeRTOS

- Mutex – особливий тип бінарного семафора з механізмом priority inheritance; потребує `configUSE_MUTEXES` = 1, створюється `xSemaphoreCreateMutex()`, береться `xSemaphoreTake()`, повертається `xSemaphoreGive()`.[^freertos-kernel-book]
- **Не з ISR.** Оскільки priority inheritance змінює пріоритет задач-власників, mutex не можна використовувати з обробників переривань.[^freertos-kernel-book]
- **Priority inheritance обмежує, але не усуває інверсію.** Власник тимчасово отримує пріоритет найпріоритетнішої задачі, що чекає на mutex, тож інверсія стає обмеженою в часі; покладатися на цей механізм для коректності системи не рекомендовано.[^freertos-kernel-book]
- **Таймаут замість вічного очікування.** Нескінченний таймаут не рекомендовано для production-коду; краще брати таймаут трохи більший за найдовше очікуване утримання, тоді його спрацювання сигналізує про помилку проєктування, можливо deadlock.[^freertos-kernel-book]
- **Рекурсивний mutex** (`xSemaphoreCreateRecursiveMutex()`, `xSemaphoreTakeRecursive()`) потрібен, якщо задача під mutex викликає бібліотечну функцію, що бере той самий mutex; звичайний mutex у такій ситуації заблокує задачу на самій собі.[^freertos-kernel-book]
- **Однакові пріоритети.** Якщо задача, що чекає на mutex, має той самий пріоритет, що й власник, вона не витісняє власника в момент `xSemaphoreGive()`, а лише переходить у стан Ready. Дві задачі, які в тісному циклі довго тримають mutex, можуть отримувати процесорний час дуже нерівно; книга радить викликати `taskYIELD()` після звільнення, якщо за час утримання змінився tick count.[^freertos-kernel-book]

### Типові помилки

Забутий `unlock` у гілці помилки; повільні операції (I/O, логування, очікування іншої черги) під mutex; використання mutex з ISR; захоплення кількох mutex у різному порядку в різних потоках – класичний deadlock (qid:emb-rtos-0004). На співбесіді очікують почути: взаємне виключення, власність, блокування замість активного очікування, синхронізацію пам’яті, priority inheritance і правила використання.
