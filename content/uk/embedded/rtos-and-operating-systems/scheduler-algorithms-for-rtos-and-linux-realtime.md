---
id: emb-rtos-0011
title: "Які scheduler algorithms важливі для RTOS і Linux real-time workloads?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: liu-layland-1973
    title: "Liu, Layland: Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment (JACM, 1973)"
    url: https://www.cs.ru.nl/~hooman/DES/liu-layland.pdf
  - source_id: linux-man-sched
    title: "sched(7) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man7/sched.7.html
  - source_id: linux-sched-deadline
    title: "The Linux Kernel: Deadline Task Scheduling"
    url: https://docs.kernel.org/scheduler/sched-deadline.html
  - source_id: linux-rt-mutex
    title: "The Linux Kernel: RT-mutex subsystem with PI support"
    url: https://docs.kernel.org/locking/rt-mutex.html
  - source_id: posix-mutexattr-protocol
    title: "POSIX.1-2024: pthread_mutexattr_getprotocol, pthread_mutexattr_setprotocol"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutexattr_getprotocol.html
  - source_id: linux-preempt-rt-theory
    title: "The Linux Kernel: Real-time preemption, theory of operation"
    url: https://docs.kernel.org/core-api/real-time/theory.html
---

## Short answer

В RTOS типово важливий **fixed-priority preemptive scheduling**, інколи round-robin для tasks одного priority. Для Linux real-time важливі `SCHED_FIFO`, `SCHED_RR`, пріоритетне успадкування (priority inheritance) і PREEMPT_RT поведінка latency. <span class="warn">Алгоритм scheduler треба оцінювати разом з interrupt latency, locks і worst-case execution time.</span>[^dou-embedded-interview]

## Detailed explanation

Для real-time системи важливо не те, наскільки «справедливо» розподілено CPU, а чи встигне кожна задача до свого дедлайну в найгіршому випадку. Тому розмова про scheduler algorithms має три частини: як вибирається наступна задача, як перевірити, що набір задач планований, і що відбувається, коли задачі ділять ресурси.

### Fixed-priority preemptive scheduling у RTOS

Більшість малих RTOS використовують fixed-priority preemptive scheduling: завжди виконується задача з найвищим пріоритетом серед готових, а задача вищого пріоритету, що стала готовою, негайно витісняє поточну, і не лише на tick. У FreeRTOS цей режим з time slicing є типовим. Задачі однакового пріоритету чергуються (round robin) на кожному tick, але FreeRTOS прямо застерігає, що round robin гарантує лише чергування, а не рівний розподіл часу. Time slicing можна вимкнути, а `configUSE_PREEMPTION = 0` вмикає cooperative scheduling, де перемикання відбувається лише при блокуванні чи явному `taskYIELD()`.[^freertos-kernel-book] Деталі станів задач, tick і context switch – у qid:emb-rtos-0012.

Сам алгоритм вибору тривіальний; складність у тому, **як призначити пріоритети**.

### Rate-monotonic scheduling і тест утилізації

Liu і Layland (1973) розглянули періодичні незалежні задачі з постійним часом виконання `C` і дедлайном, що дорівнює періоду `T`, на одному процесорі з витісненням. Для такої моделі вони довели, що **rate-monotonic** призначення (вищий пріоритет у задачі з коротшим періодом) оптимальне серед фіксованих пріоритетів: якщо набір планований хоч якимось фіксованим призначенням, він планований і rate-monotonic. Для `m` задач найменша верхня межа утилізації становить `U = m * (2^(1/m) - 1)`; для великих `m` вона прямує до приблизно 70 %.[^liu-layland-1973]

Це **достатня**, а не необхідна умова. Приклад з трьома задачами `(C, T)` = (1 мс, 4 мс), (2 мс, 8 мс), (3 мс, 12 мс): `U = 0.25 + 0.25 + 0.25 = 0.75`, межа для `m = 3` дорівнює `3 * (1.2599 - 1) ≈ 0.780`, отже планованість гарантовано. Натомість для двох задач (1, 2) і (2, 5) `U = 0.5 + 0.4 = 0.9` перевищує межу `2 * (1.4142 - 1) ≈ 0.828`, але в тій самій статті показано, що цей набір усе одно виконується вчасно: у критичний момент друга задача отримує інтервали [1, 2] і [3, 4] і завершується в момент 4, до дедлайну 5.[^liu-layland-1973] Для точної перевірки використовують аналіз часу відгуку в критичний момент, коли задача стартує разом з усіма задачами вищого пріоритету: якщо в цей момент кожна задача встигає до дедлайну, набір планований.[^liu-layland-1973]

Якщо дедлайни коротші за період, пріоритети призначають за відносним дедлайном (deadline-monotonic); автори зазначають, що за таких умов фіксований порядок має бути монотонним за інтервалом між запитом і дедлайном.[^liu-layland-1973]

### EDF і SCHED_DEADLINE

Earliest Deadline First призначає пріоритети динамічно: виконується задача з найближчим абсолютним дедлайном. У моделі Liu і Layland EDF планує набір тоді й лише тоді, коли сумарна утилізація не перевищує 1, тобто приклад з `U = 0.9` для EDF гарантовано планований.[^liu-layland-1973]

У Linux EDF доступний як `SCHED_DEADLINE` (з Linux 3.14[^linux-man-sched]): задача задає `runtime`, `deadline` і `period`, а ядро поєднує EDF з Constant Bandwidth Server, який не дає задачі спожити більше `runtime` за `period` і так ізолює задачі одна від одної. Нові задачі проходять admission control.[^linux-sched-deadline] На багатоядерних системах політика реалізована як global EDF (GEDF), а налаштовується через `sched_setattr()`.[^linux-man-sched] Документація ядра нагадує, що для багатьох CPU і для `D != P` прості тести за утилізацією вже лише достатні або взагалі неточні.[^linux-sched-deadline]

### Linux: SCHED_FIFO і SCHED_RR

Для більшості real-time застосунків у Linux використовують POSIX-політики:[^linux-man-sched]

- `SCHED_FIFO` – статичні пріоритети 1–99, які завжди вищі за звичайні (`SCHED_OTHER`) задачі; time slicing немає, задача виконується, доки не заблокується, не поступиться CPU або не буде витіснена вищим пріоритетом.
- `SCHED_RR` – те саме, але з квантом часу для задач однакового пріоритету.
- За замовчуванням ядро резервує 5 % CPU для не-real-time задач: `sched_rt_runtime_us = 950000` на `sched_rt_period_us = 1000000`. Нескінченний цикл у `SCHED_FIFO` без цього обмеження повністю заблокував би CPU.
- Real-time процесу зазвичай потрібно зафіксувати пам’ять через `mlock()` або `mlockall()`, щоб уникнути затримок через paging.

Призначення пріоритетів для `SCHED_FIFO` підпорядковується тій самій теорії: rate- чи deadline-monotonic порядок і аналіз найгіршого часу виконання (WCET).

### Спільні ресурси: priority inversion і inheritance

Будь-який алгоритм ламається, якщо високопріоритетна задача чекає mutex, який тримає низькопріоритетна, а середня тим часом виконується. FreeRTOS описує це як unbounded priority inversion; його mutex-и мають базовий механізм priority inheritance, що обмежує інверсію в часі, але ускладнює аналіз таймінгів, тому покладатися на нього як на виправлення дизайну не рекомендується.[^freertos-kernel-book] POSIX визначає для mutex протоколи `PTHREAD_PRIO_INHERIT` (власник отримує пріоритет найвищого очікувача) і `PTHREAD_PRIO_PROTECT` (власник отримує priority ceiling mutex-а незалежно від наявності очікувачів).[^posix-mutexattr-protocol] У Linux `PTHREAD_PRIO_INHERIT` реалізовано через PI-futex на базі rt-mutex, де підвищення пріоритету передається ланцюжком, якщо власник сам заблокований на іншому rt-mutex.[^linux-rt-mutex]

### PREEMPT_RT

Сама політика планування не допоможе, якщо ядро довго виконується з вимкненим витісненням. PREEMPT_RT замінює `spinlock_t` на sleeping lock на основі rtmutex з priority inheritance і примусово переводить обробники переривань у потоки ядра, які за замовчуванням працюють як `SCHED_FIFO` з пріоритетом 50. Ядро стає витіснюваним майже скрізь, і затримка між пробудженням високопріоритетної задачі та її запуском зменшується.[^linux-preempt-rt-theory] Пріоритети threaded IRQ стають частиною загальної схеми пріоритетів: застосунок, вищий за 50, може витісняти обробку переривань, і це треба планувати свідомо.

### Що хоче почути інтерв’юер

Fixed-priority preemptive як основа RTOS; rate- і deadline-monotonic призначення; тест Liu і Layland як достатню умову; EDF і `SCHED_DEADLINE`; `SCHED_FIFO`/`SCHED_RR` і RT throttling; priority inheritance і ceiling; PREEMPT_RT. І головне: жоден алгоритм не компенсує невідомий WCET, довгі критичні секції чи interrupt latency, тому планованість перевіряють разом із вимірюванням найгірших затримок на реальному залізі.
