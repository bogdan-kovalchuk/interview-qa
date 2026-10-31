---
id: emb-rtos-0008
title: "Які способи синхронізації потоків застосовують у POSIX/RTOS і коли вибрати mutex, semaphore або condition variable?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: posix-pthread-mutex-lock
    title: "POSIX.1-2024: pthread_mutex_lock, pthread_mutex_trylock, pthread_mutex_unlock"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html
  - source_id: posix-sem-post
    title: "POSIX.1-2024: sem_post"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html
  - source_id: posix-pthread-cond-wait
    title: "POSIX.1-2024: pthread_cond_clockwait, pthread_cond_timedwait, pthread_cond_wait"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_wait.html
  - source_id: posix-pthread-cond-signal
    title: "POSIX.1-2024: pthread_cond_broadcast, pthread_cond_signal"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_signal.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
---

## Short answer

`mutex` захищає shared state з одним owner у критичній секції. `semaphore` рахує ресурси або сигналізує event між ISR/task у RTOS-стилі, якщо це дозволено API. `condition variable` будить потоки, які чекають на predicate під mutex; вона не зберігає подію сама по собі.[^dou-embedded-interview]

## Detailed explanation

Вибір примітива починається не з API, а з питання, яку задачу синхронізації розв’язують. Їх три: **взаємне виключення** (лише один потік змінює дані), **очікування події чи стану** (потік чекає, доки щось станеться) і **облік ресурсів** (скільки одиниць вільно). Mutex, semaphore і condition variable відповідають саме цим трьом задачам, і більшість помилок – це використання примітива не за призначенням.

### Mutex: захист спільного стану

Mutex має власника. Успішний `pthread_mutex_lock()` повертається з mutex у заблокованому стані й потоком-викликачем як власником; якщо mutex зайнятий, потік блокується. Розблокування не власником для `PTHREAD_MUTEX_ERRORCHECK` чи `PTHREAD_MUTEX_RECURSIVE` повертає `EPERM`, а для звичайного неробастного mutex це undefined behavior.[^posix-pthread-mutex-lock] Отже, mutex – інструмент для критичної секції: захопив, змінив дані, звільнив той самий потік.

У FreeRTOS mutex – це особливий binary semaphore з механізмом priority inheritance. Саме через вплив на пріоритети задач його не можна використовувати з ISR.[^freertos-kernel-book] Детально відмінності mutex і semaphore розібрано в qid:emb-rtos-0009.

### Semaphore: лічильник подій або ресурсів

Semaphore – лічильник без власника. `sem_post()` або будить один заблокований потік, або, якщо ніхто не чекає, просто збільшує значення, тобто подія «запам’ятовується». До того ж `sem_post()` є async-signal-safe і може викликатися з обробника сигналу.[^posix-sem-post]

У RTOS це основний спосіб розбудити задачу з переривання. FreeRTOS описує два сценарії: binary semaphore для відкладеної обробки переривання (ISR робить `xSemaphoreGiveFromISR()`, задача блокується в `xSemaphoreTake()`) і counting semaphore для підрахунку подій або для пулу однакових ресурсів, коли початкове значення дорівнює кількості ресурсів.[^freertos-kernel-book] FreeRTOS також прямо зазначає, що розблокувати задачу з переривання ефективніше через direct-to-task notification, ніж через binary semaphore, а рахувати події – ефективніше через notification, ніж через counting semaphore.[^freertos-kernel-book]

Одним semaphore часто намагаються робити і серіалізацію, і очікування. Linux kernel-документація радить для нового коду розділяти ці ролі: для серіалізації – mutex, для очікування – окремий механізм, наприклад completion.[^linux-lock-types]

### Condition variable: очікування предиката

Condition variable не зберігає подію. `pthread_cond_signal()` і `pthread_cond_broadcast()` не мають жодного ефекту, якщо на condition variable ніхто не заблокований.[^posix-pthread-cond-signal] Тому подія повинна жити в спільних даних – у предикаті, захищеному mutex, а condition variable лише будить тих, хто чекає на зміну цього предиката.

`pthread_cond_wait()` викликають із захопленим mutex. Функція атомарно звільняє mutex і блокує потік, а після повернення mutex знову належить потоку. Можливі spurious wakeups, і повернення з функції нічого не каже про значення предиката, тож його треба перевіряти повторно.[^posix-pthread-cond-wait] Звідси канонічний шаблон із циклом `while`:

```c
#include <pthread.h>
#include <stdbool.h>

static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t ready_cv = PTHREAD_COND_INITIALIZER;
static bool frame_ready = false;

void wait_frame(void)
{
    pthread_mutex_lock(&lock);
    while (!frame_ready) {          /* check the predicate, not the wakeup */
        pthread_cond_wait(&ready_cv, &lock);
    }
    frame_ready = false;
    pthread_mutex_unlock(&lock);
}

void publish_frame(void)
{
    pthread_mutex_lock(&lock);
    frame_ready = true;
    pthread_cond_signal(&ready_cv);
    pthread_mutex_unlock(&lock);
}
```

Якщо `publish_frame()` виконається раніше, ніж споживач почне чекати, сигнал пропаде, але `frame_ready` уже `true`, і споживач не заблокується. `if` замість `while` або прапорець поза mutex ламають цю гарантію. Викликати `pthread_cond_signal()` можна й без mutex, але POSIX вимагає тримати його, якщо потрібна передбачувана поведінка планування.[^posix-pthread-cond-signal] Condition variable доречна, коли умова складніша за лічильник: «черга не порожня і не встановлено прапорець зупинки», «буфер має щонайменше N байтів».

### Як вибирати

| Задача | Примітив |
|---|---|
| Захистити структуру даних між потоками | mutex |
| Розбудити задачу з ISR або обробника сигналу | semaphore або task notification |
| Обмежити доступ до N однакових ресурсів | counting semaphore |
| Чекати складну умову над спільним станом | condition variable + mutex |

На співбесіді очікують почути три речі: mutex має власника і не викликається з ISR; semaphore пам’ятає кількість подій, а condition variable – ні, тому вона завжди працює в парі з предикатом під mutex; перевірка предиката робиться в циклі через spurious wakeups. У RTOS-коді для очікування подій частіше використовують черги, event groups і task notifications; їхнє порівняння – у qid:emb-rtos-0014.
