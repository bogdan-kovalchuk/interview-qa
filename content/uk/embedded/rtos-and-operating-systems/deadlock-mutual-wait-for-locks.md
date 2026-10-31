---
id: emb-rtos-0004
title: "Що таке deadlock?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: ostep-concurrency-bugs
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 32: Common Concurrency Problems"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: linux-spinlocks
    title: "Linux kernel documentation: Locking lessons (spinlocks)"
    url: https://docs.kernel.org/locking/spinlocks.html
  - source_id: linux-lockdep-design
    title: "Linux kernel documentation: Runtime locking correctness validator"
    url: https://docs.kernel.org/locking/lockdep-design.html
---

## Short answer

**Deadlock** – ситуація, коли два або більше потоки взаємно чекають ресурси один одного і ніхто не може продовжити виконання.[^dou-embedded-interview]

Приклад: Thread A взяв `m1` і чекає `m2`, а Thread B взяв `m2` і чекає `m1`. Обидва заблоковані назавжди.

Запобігання: фіксований порядок взяття locks, короткі критичні секції, timeout, lock hierarchy, уникання вкладених locks або використання higher-level primitives.

## Detailed explanation

### Як виникає

Документація FreeRTOS описує deadlock (також deadly embrace) як ситуацію, коли дві задачі не можуть продовжити роботу, бо кожна чекає на ресурс, який тримає інша. Типовий сценарій: задачам A і B для дії потрібні обидва mutex X і Y. A бере X, після чого її витісняє B; B бере Y і намагається взяти X, але X зайнятий, тож B блокується. A продовжує, намагається взяти Y і теж блокується. Тепер кожна чекає на іншу, і жодна не просунеться.[^freertos-kernel-book]

```c
#include <pthread.h>

static pthread_mutex_t m1 = PTHREAD_MUTEX_INITIALIZER;
static pthread_mutex_t m2 = PTHREAD_MUTEX_INITIALIZER;

static void *thread_a(void *arg)
{
    (void)arg;
    pthread_mutex_lock(&m1);
    pthread_mutex_lock(&m2);   /* blocks forever if B already holds m2 */
    /* ... use both resources ... */
    pthread_mutex_unlock(&m2);
    pthread_mutex_unlock(&m1);
    return NULL;
}

static void *thread_b(void *arg)
{
    (void)arg;
    pthread_mutex_lock(&m2);   /* opposite order: the bug */
    pthread_mutex_lock(&m1);
    /* ... */
    pthread_mutex_unlock(&m1);
    pthread_mutex_unlock(&m2);
    return NULL;
}
```

Такий код може місяцями працювати на стенді й зависнути в полі: deadlock проявляється лише тоді, коли перемикання станеться точно між двома `lock`.

### Чотири необхідні умови

Deadlock можливий лише тоді, коли одночасно виконуються чотири умови, класично сформульовані в статті Коффмана та співавторів 1971 року:[^ostep-concurrency-bugs]

1. **Mutual exclusion** – потоки отримують ексклюзивний контроль над ресурсами (наприклад, захоплюють lock).
2. **Hold-and-wait** – потік тримає вже отримані ресурси, поки чекає на додаткові.
3. **No preemption** – ресурс не можна примусово забрати в потоку, що його тримає.
4. **Circular wait** – існує кільцевий ланцюжок потоків, де кожен тримає ресурс, потрібний наступному.

Якщо хоча б одна умова не виконується, deadlock неможливий. Тому кожен метод запобігання – це спосіб зламати одну з них.[^ostep-concurrency-bugs] Зверніть увагу: це необхідні умови, а не достатні – наявність усіх чотирьох лише робить deadlock можливим за певного переплетення.

### Як запобігти

- **Зламати circular wait – фіксований порядок захоплення.** Найпрактичніший і найпоширеніший спосіб: якщо всі завжди беруть `L1` перед `L2`, кільце не утвориться. У великих системах достатньо часткового порядку; приклад – код відображення пам’яті в Linux, де коментар на початку файлу описує десяток груп порядку захоплення. Коли функція отримує два lock як аргументи, порядок можна визначати за адресами: завжди брати спершу lock із більшою адресою (за умови, що це різні lock).[^ostep-concurrency-bugs]
- **Зламати hold-and-wait – брати все одразу.** Усі потрібні lock захоплюються атомарно під одним глобальним lock. Вада: треба заздалегідь знати всі lock, що порушує інкапсуляцію, і паралелізм падає, бо lock тримаються довше, ніж потрібно.[^ostep-concurrency-bugs]
- **Зламати no preemption – `trylock` з відкатом.** Якщо другий lock недоступний (`pthread_mutex_trylock()`), звільнити перший і почати спочатку. Новий ризик – livelock: два потоки нескінченно повторюють спробу і не просуваються; допомагає випадкова затримка перед повтором.[^ostep-concurrency-bugs]
- **Зламати mutual exclusion – lock-free структури** на атомарних інструкціях на кшталт compare-and-swap.[^ostep-concurrency-bugs]
- **Таймаут як детектор помилки проєктування.** FreeRTOS радить не чекати на mutex нескінченно, а ставити таймаут трохи більший за максимальний очікуваний час очікування: неотримання mutex за цей час – симптом помилки проєктування, можливо deadlock. Найкраще ж – розглянути можливість deadlock ще на етапі проєктування й виключити її.[^freertos-kernel-book]

Окремий підхід – дозволити deadlock і відновлюватися: детектор періодично будує граф ресурсів і шукає цикли, так роблять, наприклад, СУБД.[^ostep-concurrency-bugs] Для embedded аналогом часто є watchdog, але це вже відновлення, а не запобігання.

### Варіанти, які легко пропустити

- **Deadlock із самим собою.** Задача, що тримає mutex, викликає бібліотечну функцію, яка намагається взяти той самий mutex, і блокується, чекаючи сама на себе. Рішення у FreeRTOS – рекурсивний mutex.[^freertos-kernel-book] У POSIX повторне захоплення `PTHREAD_MUTEX_NORMAL` – deadlock, а `PTHREAD_MUTEX_ERRORCHECK` замість цього повертає `EDEADLK`, що зручно під час налагодження.[^posix-pthread-mutex-lock]
- **Lock і переривання на одному ядрі.** Якщо код у контексті процесу взяв spinlock, а на тому самому CPU приходить переривання, обробник якого бере той самий lock, обробник крутиться вічно: власник не продовжить, поки переривання не завершиться. На іншому CPU це безпечно. Тому дані, спільні з обробником переривань, захищають варіантами `spin_lock_irqsave()`, що вимикають переривання.[^linux-spinlocks] На MCU це той самий сценарій: ISR ніколи не повинен чекати на ресурс, який може тримати перерваний ним код.
- **Не плутати з priority inversion.** Задача високого пріоритету, що чекає на mutex низькопріоритетної задачі, не в deadlock: власник рано чи пізно звільнить mutex. Небезпечний випадок – коли середньопріоритетна задача не дає власнику виконуватися; FreeRTOS називає це unbounded priority inversion.[^freertos-kernel-book] Механізми – у qid:emb-rtos-0009.

### Інструменти

У ядрі Linux lockdep відстежує класи lock і всі порядки, в яких їх колись захоплювали, і знаходить кільцеві залежності будь-якої складності; також він забороняє залежність hardirq-safe lock від hardirq-unsafe.[^linux-lockdep-design] Головна перевага: достатньо, щоб кожен простий ланцюжок захоплень трапився хоча б раз, і валідатор доведе можливість deadlock, навіть якщо складний сценарій із кількома CPU і перериваннями на практиці не відтворився.[^linux-lockdep-design]

### Що хоче почути інтерв’юер

Визначення через взаємне очікування, приклад із двома lock у різному порядку, чотири умови Коффмана і те, яку з них ламає кожен метод, фіксований порядок захоплення як основне рішення, а також відмінність від livelock і priority inversion.
