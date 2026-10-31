---
id: emb-fund-0002
title: "Що таке POSIX?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-standards
    title: "Linux manual page: standards(7)"
    url: https://man7.org/linux/man-pages/man7/standards.7.html
  - source_id: posix-2024-introduction
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 1. Introduction"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap01.html
  - source_id: posix-2024-unistd-h
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024): <unistd.h>"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/unistd.h.html
  - source_id: zephyr-posix-overview
    title: "Zephyr Project documentation: POSIX Overview"
    url: https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html
---

## Short answer

**POSIX** (Portable Operating System Interface) – стандарт IEEE, що визначає API для сумісності між Unix-подібними ОС.[^dou-embedded-interview] Описує: файловий API (`open`/`read`/`write`/`close`), процеси (`fork`/`exec`), потоки (`pthread`), сигнали, IPC, регулярні вирази.

Мета: код, написаний під POSIX, компілюється і працює на Linux, macOS, FreeBSD, QNX без змін. В Embedded Linux – основа для portability. RTOS-и (Zephyr, FreeRTOS) реалізують підмножини POSIX (pthreads, semaphores) для переносимості коду.

## Detailed explanation

### Стандарт і його історія

POSIX – це сімейство стандартів IEEE 1003. Перший, POSIX.1 (IEEE Std 1003.1-1988), описував інтерфейс операційної системи; згодом окремими частинами додалися POSIX.1b (real-time, 1993), POSIX.1c (потоки `pthread`, 1995) та POSIX.1g (мережевий API, зокрема сокети, 2000). У 2001 році POSIX.1, POSIX.2 і Single UNIX Specification об’єднали в один документ під егідою Austin Group; чинна редакція – POSIX.1-2024 (IEEE Std 1003.1-2024), узгоджена з C17.[^linux-man-standards]

Стандарт складається з чотирьох томів: Base Definitions (терміни, концепції, заголовні файли C), System Interfaces (функції), Shell and Utilities (командний інтерпретатор і утиліти) та Rationale (пояснення рішень).[^posix-2024-introduction]

### Сумісність на рівні вихідного коду, а не бінарних файлів

Головна думка, яку варто чітко сформулювати: мета POSIX – переносимість застосунків **на рівні вихідного коду**. Переносимість об’єктного чи бінарного коду прямо винесена за межі стандарту, як і графічні інтерфейси та СУБД. Крім того, POSIX описує зовнішню поведінку інтерфейсів, а не те, як їх реалізовано всередині.[^posix-2024-introduction]

Практичні наслідки:

- програму під POSIX треба **перезібрати** для кожної цільової системи й архітектури; виконуваний файл для x86-64 Linux не запуститься на ARM-платі лише тому, що обидві системи «POSIX-сумісні»;
- стандарт не каже, що є системним викликом, а що – бібліотечною функцією. Наприклад, `pthread_mutex_lock()` може бути реалізована переважно в C-бібліотеці, і код від цього не залежить;
- номери системних викликів, розміри структур та ABI стандарт не фіксує – це деталі реалізації.

### Обов’язкове та опційне

POSIX не монолітний. Частину функціональності позначено як опції (наприклад, TPI – priority inheritance для mutex, SHM – об’єкти спільної пам’яті), і для максимальної переносимості застосунку слід або уникати опційних можливостей, або перевіряти їх наявність.[^posix-2024-introduction] Реалізація повідомляє про підтримку через константи в `<unistd.h>`: якщо константу не визначено або вона дорівнює `-1`, опція недоступна для компіляції; якщо вона більша за нуль – опція завжди доступна під час виконання; значення `0` означає, що компілювати можна, але підтримку під час виконання треба перевірити через `sysconf()`. Для POSIX.1-2024 `_POSIX_VERSION` дорівнює `202405L`, а `_POSIX_THREADS` і `_POSIX_TIMERS` завжди мають значення `202405L`, тобто потоки й таймери в цій редакції обов’язкові.[^posix-2024-unistd-h]

```c
#include <stdio.h>
#include <unistd.h>

int main(void)
{
#if defined(_POSIX_THREAD_PRIO_INHERIT) && _POSIX_THREAD_PRIO_INHERIT > 0
    puts("priority inheritance: always supported");
#elif defined(_POSIX_THREAD_PRIO_INHERIT) && _POSIX_THREAD_PRIO_INHERIT == 0
    long v = sysconf(_SC_THREAD_PRIO_INHERIT);
    puts(v > 0 ? "priority inheritance: supported at run time"
               : "priority inheritance: not supported at run time");
#else
    puts("priority inheritance: not supported for compilation");
#endif
    return 0;
}
```

Окремо існує рівень XSI Conformance: система, що його заявляє, зобов’язана надавати додатковий набір інтерфейсів, які для базової POSIX-сумісності є лише опційними.[^linux-man-standards]

### POSIX у вбудованих системах

В Embedded Linux POSIX – це звична мова прикладного коду: файли, сокети, `pthread`, сигнали, таймери. Для RTOS повна відповідність стандарту здебільшого непрактична й непотрібна: такі системи мають фіксоване призначення й обмежені ресурси. Тому ще стандарт POSIX.13-2003 визначив профілі прикладного середовища (AEP) – від Minimal Realtime System Profile (PSE51) до Multi-Purpose Realtime System (PSE54); нині цей стандарт неактивний, але його ідею передають опції та групи опцій POSIX.1-2017.[^zephyr-posix-overview]

Zephyr реалізує підмножину IEEE 1003.1-2017. POSIX-функції там вимкнені за замовчуванням і вмикаються через Kconfig, зокрема готовими профілями на кшталт `CONFIG_POSIX_AEP_CHOICE_PSE51`. Документація Zephyr прямо зазначає, що код ядра й застосунку зазвичай збираються в один бінарний образ і застосунок можна розглядати як один процес; також вона називає POSIX популярним шаром абстракції ОС (OSAL) для IoT, який використовують Zephyr, AWS FreeRTOS, TI-RTOS і NuttX.[^zephyr-posix-overview] Звідси типова пастка: бібліотека з `pthread`, `nanosleep` і сокетами переноситься на RTOS відносно легко, а код, що покладається на `fork()`, окремі адресні простори процесів чи повну файлову систему, без переробки не перенесеться.

### Що хоче почути інтерв’юер

Розшифрування абревіатури й зв’язок з IEEE 1003.1; що стандарт визначає API та поведінку, а не реалізацію; що переносимість – на рівні вихідного коду; що є обов’язкові й опційні частини; і що RTOS реалізують підмножини POSIX для перевикористання коду. Бонус – знати, як перевірити опцію через `<unistd.h>` і `sysconf()`.
