---
id: emb-rtos-0009
title: "Чим mutex відрізняється від semaphore у потоках і RTOS tasks?"
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
  - source_id: posix-pthread-mutexattr-protocol
    title: "POSIX.1-2024: pthread_mutexattr_getprotocol, pthread_mutexattr_setprotocol"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutexattr_getprotocol.html
  - source_id: posix-sem-post
    title: "POSIX.1-2024: sem_post"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html
  - source_id: linux-mutex-design
    title: "Linux kernel: Generic Mutex Subsystem"
    url: https://docs.kernel.org/locking/mutex-design.html
  - source_id: linux-lock-types
    title: "Linux kernel: Lock types and their rules"
    url: https://docs.kernel.org/locking/locktypes.html
---

## Short answer

`mutex` має ownership: той task/thread, що lock-нув, має unlock-нути, і часто підтримує priority inheritance (успадкування пріоритету). `semaphore` – лічильник permits/events без такого ownership, тому його можна give/take для ресурсів або сигналізації. Для захисту shared data вибирають mutex; для producer-consumer сигналу або pool count – semaphore.[^dou-embedded-interview]

## Detailed explanation

Зовні mutex і binary semaphore схожі: обидва мають два стани й операції «взяти» і «віддати». У FreeRTOS mutex навіть описаний як особливий тип binary semaphore.[^freertos-kernel-book] Різниця не в лічильнику, а у **власнику**, і з неї випливає все інше: priority inheritance, заборона в ISR, рекурсивне захоплення, виявлення помилок.

### Власник

Mutex завжди має власника – задачу чи потік, що його захопив. POSIX фіксує це в семантиці: після успішного `pthread_mutex_lock()` mutex заблокований, а власником є викликач. Спроба розблокувати mutex не власником для типів `PTHREAD_MUTEX_ERRORCHECK` і `PTHREAD_MUTEX_RECURSIVE`, а також для robust mutex повертає `EPERM`; для звичайного неробастного mutex це undefined behavior.[^posix-pthread-mutex-lock] Linux kernel формулює правила ще жорсткіше: mutex одночасно тримає лише одна задача, звільнити його може лише власник, рекурсивне захоплення заборонене, а використовувати mutex у контексті апаратних чи програмних переривань не можна.[^linux-mutex-design]

Semaphore власника не має. `sem_post()` збільшує лічильник або будить одного з потоків, що чекають, і нікого не цікавить, хто раніше робив `sem_wait()`.[^posix-sem-post] Саме тому semaphore придатний для сигналізації між різними контекстами: у FreeRTOS ISR «дає» binary semaphore, ніколи його не взявши, а задача «бере» його і не повертає. Книга FreeRTOS прямо застерігає, що в такому сценарії правило «хто взяв, той і повертає» не діє, на відміну від використання для взаємного виключення.[^freertos-kernel-book]

### Priority inversion і priority inheritance

Власник потрібен, щоб планувальник знав, кому підняти пріоритет. Класичний сценарій із трьома задачами: L (низький пріоритет) захоплює mutex, H (високий) хоче той самий mutex і блокується, а M (середній), якому mutex не потрібен, витісняє L. Тепер H чекає на L, а L не може виконуватися через M. FreeRTOS називає це unbounded priority inversion, бо M може затримувати обидві задачі необмежено довго.[^freertos-kernel-book]

Priority inheritance тимчасово піднімає пріоритет власника mutex до пріоритету найвищої задачі, що чекає на нього, а після звільнення mutex повертає вихідний. L виконується з пріоритетом H, M не може її витіснити, і інверсія стає обмеженою в часі. Це не усуває інверсію, а лише обмежує її, і FreeRTOS не радить покладатися на inheritance для коректної роботи системи. Через вплив на пріоритети задач mutex у FreeRTOS не можна використовувати з ISR. Реалізація спрощена: задача, що тримає кілька mutex, залишається на найвищому успадкованому пріоритеті, доки не звільнить їх усі.[^freertos-kernel-book]

Binary semaphore у FreeRTOS такого механізму не має.[^freertos-kernel-book] У Linux те саме має принциповий характер: `PREEMPT_RT` не може дати priority inheritance для semaphore, бо невідомого власника неможливо «підняти», тому блокування на semaphore може спричинити priority inversion.[^linux-lock-types]

У POSIX протокол задається атрибутом mutex. За замовчуванням це `PTHREAD_PRIO_NONE`, тобто володіння mutex не впливає на пріоритет. З `PTHREAD_PRIO_INHERIT` власник виконується з вищим із власного пріоритету і пріоритету найвищого потоку, що чекає, причому ефект поширюється ланцюжком, якщо власник сам заблокований на іншому такому mutex. `PTHREAD_PRIO_PROTECT` реалізує priority ceiling: власник отримує пріоритет-стелю mutex незалежно від того, чи хтось чекає.[^posix-pthread-mutexattr-protocol]

```c
#include <pthread.h>

int init_pi_mutex(pthread_mutex_t *m)
{
    pthread_mutexattr_t attr;
    int rc = pthread_mutexattr_init(&attr);

    if (rc != 0) {
        return rc;
    }
    rc = pthread_mutexattr_setprotocol(&attr, PTHREAD_PRIO_INHERIT);
    if (rc == 0) {
        rc = pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_ERRORCHECK);
    }
    if (rc == 0) {
        rc = pthread_mutex_init(m, &attr);
    }
    pthread_mutexattr_destroy(&attr);
    return rc;
}
```

`pthread_mutexattr_setprotocol()` повертає `ENOTSUP`, якщо реалізація не підтримує вказаний протокол, тому результат треба перевіряти, а не припускати.[^posix-pthread-mutexattr-protocol] Тип `ERRORCHECK` тут доданий, щоб розблокування не власником давало помилку, а не undefined behavior.

### Рекурсія і смерть власника

Ще дві речі, можливі лише завдяки власнику. Рекурсивний mutex дозволяє тій самій задачі захопити його повторно й веде лічильник: mutex звільняється, коли кількість «віддати» зрівняється з кількістю «взяти». У FreeRTOS для цього є окремий recursive mutex, бо повторне захоплення звичайного mutex тією ж задачею – deadlock із самою собою.[^freertos-kernel-book] POSIX робить так само для `PTHREAD_MUTEX_RECURSIVE`.[^posix-pthread-mutex-lock] Robust mutex у POSIX повідомляє наступному власнику через `EOWNERDEAD`, що попередній завершився, тримаючи lock, і стан даних треба відновити.[^posix-pthread-mutex-lock] Для semaphore жоден із цих механізмів неможливий.

### Підсумок

| Властивість | Mutex | Semaphore |
|---|---|---|
| Власник | є, звільняє лише він | немає |
| Priority inheritance | можлива (FreeRTOS, `PTHREAD_PRIO_INHERIT`) | немає |
| Виклик «віддати» з ISR | ні | так (`xSemaphoreGiveFromISR`) |
| Типове призначення | взаємне виключення | сигналізація, лічильник ресурсів |

Відповідь, яку чекає інтерв’юер: mutex – для захисту спільних даних, бо має власника і завдяки цьому підтримує priority inheritance; semaphore – для сигналізації між задачами чи з ISR і для обліку однакових ресурсів. Якщо захищати критичну секцію binary semaphore замість mutex, система втрачає priority inheritance і лишається вразливою до unbounded priority inversion.
