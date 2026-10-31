---
id: emb-rtos-0001
title: "Що таке race condition?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: ostep-concurrency-intro
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 26: Concurrency: An Introduction"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf
  - source_id: ostep-concurrency-bugs
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 32: Common Concurrency Problems"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/threads-bugs.pdf
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: posix-2024-general-concepts
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 4. General Concepts"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html
---

## Short answer

**Race condition** – ситуація, коли результат залежить від порядку виконання потоків, процесів або ISR.[^dou-embedded-interview] Якщо порядок змінюється, програма може іноді працювати правильно, а іноді давати помилку.

Класичний приклад: `counter++` – це не одна атомарна дія, а послідовність read, modify, write; якщо два потоки одночасно читають старе значення, один інкремент може загубитися.

Захист: `mutex`, spinlock, atomic operations, critical section або вимкнення interrupt-ів на короткий час в embedded-коді.

## Detailed explanation

### Визначення й пов’язані терміни

Race condition виникає, коли результат залежить від того, як саме в часі переплелося виконання кількох потоків: за невдалого моменту перемикання контексту програма дає хибний результат, і від запуску до запуску він може бути різним. Такий результат називають indeterminate. Ділянку коду, що звертається до спільного ресурсу і не повинна виконуватися кількома потоками одночасно, називають критичною секцією; властивість, яка гарантує, що в ній перебуває лише один потік, – mutual exclusion.[^ostep-concurrency-intro]

### Класичний приклад: втрачений інкремент

`counter++` для процесора – три кроки: прочитати значення в регістр, додати одиницю, записати назад. Нехай `counter` дорівнює 50:[^ostep-concurrency-intro]

1. Потік 1 читає 50 у свій регістр і додає 1 (у регістрі 51). Спрацьовує переривання таймера, і ОС зберігає його регістри.
2. Потік 2 читає з пам’яті все ще 50, додає 1 і записує 51.
3. Потік 1 відновлюється і записує свої 51.

Інкремент виконано двічі, а лічильник замість 52 дорівнює 51. Ту саму помилку видно в простій програмі з двома потоками, що збільшують спільний лічильник у циклі: іноді результат правильний, а іноді менший за очікуваний і різний від запуску до запуску, навіть на одному процесорі.[^ostep-concurrency-intro]

```c
#include <pthread.h>
#include <stdio.h>

static volatile long counter;        /* volatile keeps every access, not atomicity */

static void *worker(void *arg)
{
    (void)arg;
    for (int i = 0; i < 1000000; i++)
        counter++;                   /* read, modify, write */
    return NULL;
}

int main(void)
{
    pthread_t a, b;
    pthread_create(&a, NULL, worker, NULL);
    pthread_create(&b, NULL, worker, NULL);
    pthread_join(a, NULL);
    pthread_join(b, NULL);
    printf("%ld\n", counter);        /* expected 2000000 */
    return 0;
}
```

Строго кажучи, у C11 така програма має undefined behavior, тож «менше значення» – лише типовий прояв, а не гарантована поведінка (див. наступний розділ).

### Варіанти, характерні для embedded

FreeRTOS описує ті самі проблеми на рівні задач і переривань:[^freertos-kernel-book]

- **Read-modify-write регістра периферії.** `PORTA |= 0x01;` компілюється в читання, OR і запис. Якщо задачу A витиснуть між читанням і записом, а задача B тим часом змінить `PORTA`, A запише застаріле значення і зітре зміну B.
- **Неатомарний доступ до змінних.** Оновлення кількох полів структури або змінної, ширшої за природне слово архітектури (32-бітна змінна на 16-бітному процесорі), може бути перерване посередині.
- **Нереентерабельні функції.** Функція зі `static` станом чи глобальними даними небезпечна при виклику з кількох задач або із задачі й переривання; функція, що працює лише з аргументами й локальними змінними, реентерабельна, бо кожна задача має власний стек і регістри.
- **Переплетення виводу.** Задача A почала писати на LCD «Hello world», її витиснула задача B зі своїм рядком, і на екрані з’явилося «Hello wAbort, Retry, Fail?orld».

### Race condition і data race – не одне й те саме

У мові C це точний термін. Дві операції конфліктують, якщо одна змінює комірку пам’яті, а інша читає або змінює ту саму комірку. Data race – це два конфліктні доступи з різних потоків, хоча б один із яких не атомарний і жоден із яких не happens before іншого; будь-який data race – undefined behavior.[^iso-c-n1570] `volatile` від цього не рятує: він лише вимагає, щоб кожен вираз із таким об’єктом обчислювався строго за правилами абстрактної машини[^iso-c-n1570], але не робить доступ атомарним і не впорядковує його відносно інших потоків. POSIX формулює вимогу до застосунку прямо: доступ кількох потоків до комірки пам’яті, не реалізований як lock-free, треба обмежити так, щоб жоден потік не читав і не змінював її, поки інший може її змінювати; для цього використовують функції, що синхронізують і виконання, і пам’ять, як-от `pthread_mutex_lock()`, `sem_wait()`, `pthread_join()`.[^posix-2024-general-concepts]

Race condition – ширше поняття: помилка в логіці порядку, яка може залишитися, навіть коли кожен окремий доступ атомарний. Дослідження реальних багів виділяють два типи:[^ostep-concurrency-bugs]

- **atomicity violation** – ділянку, яка мала бути неподільною, такою не зробили: один потік перевіряє `if (thd->proc_info)` і потім викликає `fputs(thd->proc_info, ...)`, а інший між цими кроками записує `NULL`;
- **order violation** – код припускає порядок, який ніхто не гарантує: потік використовує `mThread->State` до того, як інший потік встиг ініціалізувати `mThread`. Виправлення – явна сигналізація (умовна змінна, семафор), а не «затримка про всяк випадок».

### Захист

- **Mutex** навколо всієї критичної секції, включно з перевіркою й дією (qid:emb-rtos-0002).
- **Атомарні операції** для одиночних лічильників і прапорців (qid:emb-rtos-0003); для інваріантів між кількома змінними їх недостатньо.
- **Критична секція RTOS.** У FreeRTOS `taskENTER_CRITICAL()` вимикає переривання повністю або до рівня `configMAX_SYSCALL_INTERRUPT_PRIORITY` залежно від порту; такі секції мають бути дуже короткими, інакше погіршиться час реакції на переривання. Призупинення планувальника (`vTaskSuspendAll()`) захищає лише від інших задач, бо переривання лишаються ввімкненими.[^freertos-kernel-book]
- **Проєктування без спільного ресурсу.** Найкращий спосіб, коли це практично, – щоб до ресурсу звертався лише один потік або задача.[^freertos-kernel-book]

### Чому їх важко знайти

Результат indeterminate: помилка проявляється лише за певного переплетення і може не відтворюватися довго.[^ostep-concurrency-intro] Тому на співбесіді добре звучить відповідь, яка не обмежується «додати mutex»: визначити спільні дані, межі критичних секцій, контексти доступу (потік, ISR, інше ядро) і вибрати примітив відповідно до контексту.
