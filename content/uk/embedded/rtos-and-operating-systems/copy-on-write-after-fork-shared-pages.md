---
id: emb-fund-0016
title: "Що таке copy-on-write і де воно проявляється в Linux fork або memory mapping?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-fork
    title: "Linux manual page: fork(2)"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-page-tables
    title: "Linux kernel: Page Tables"
    url: https://docs.kernel.org/mm/page_tables.html
  - source_id: linux-man-mmap
    title: "Linux manual page: mmap(2)"
    url: https://man7.org/linux/man-pages/man2/mmap.2.html
  - source_id: linux-overcommit-accounting
    title: "Linux kernel: Overcommit Accounting"
    url: https://docs.kernel.org/mm/overcommit-accounting.html
  - source_id: linux-man-mlock
    title: "Linux manual page: mlock(2)"
    url: https://man7.org/linux/man-pages/man2/mlock.2.html
  - source_id: linux-man-vfork
    title: "Linux manual page: vfork(2)"
    url: https://man7.org/linux/man-pages/man2/vfork.2.html
  - source_id: linux-nommu-mmap
    title: "Linux kernel: No-MMU memory mapping support"
    url: https://docs.kernel.org/admin-guide/mm/nommu-mmap.html
---

## Short answer

**Copy-on-write** дозволяє кільком mappings спільно читати одні physical pages, доки хтось не спробує записати. Після `fork` parent і child спочатку ділять pages, а при write kernel створює приватну копію сторінки. Це економить RAM і пришвидшує fork, але перший write може мати page fault latency.[^dou-embedded-interview]

## Detailed explanation

### Семантика і реалізація

Після `fork()` батьківський і дочірній процеси працюють в окремих адресних просторах, які в момент виклику мають однаковий вміст; записи в пам’ять, нові mappings і `munmap()` в одному процесі не впливають на інший.[^linux-man-fork] Це вимога семантики, а не опис реалізації. Копіювати весь адресний простір одразу було б дорого, тому Linux реалізує `fork()` через copy-on-write сторінки: безпосередня вартість виклику – дублювання таблиць сторінок батька і створення структури задачі для нащадка.[^linux-man-fork]

Ідея copy-on-write: після `fork()` обидва процеси посилаються на ті самі фізичні сторінки, а копія створюється лише тоді, коли хтось у сторінку пише. Спроба запису спричиняє page fault – kernel-документація прямо називає Copy-on-Write серед звичайних, очікуваних причин page fault, – і обробник дає процесу приватну копію сторінки.[^linux-page-tables] Сторінки, які ніхто не змінює (код, константи, більшість бібліотек), так і залишаються спільними.

```c
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

static int counter = 1;

int main(void)
{
    pid_t pid = fork();
    if (pid < 0) {
        return 1;
    }
    if (pid == 0) {
        counter = 100;    /* first write: the child gets a private copy of the page */
        _exit(0);
    }
    waitpid(pid, NULL, 0);
    printf("%d\n", counter);    /* prints 1 */
    return 0;
}
```

Нащадок змінює `counter`, але батько друкує `1`: адресні простори окремі, хоча до першого запису сторінка з `counter` була спільною.

### Copy-on-write у memory mapping

Той самий механізм лежить в основі `mmap()` з `MAP_PRIVATE`: це приватний copy-on-write mapping, зміни в якому не видно іншим процесам, що відобразили той самий файл, і які не потрапляють у файл.[^linux-man-mmap] Для порівняння, з `MAP_SHARED` оновлення видно іншим процесам, що відобразили той самий регіон, а для файлового mapping вони потрапляють і у файл.[^linux-man-mmap] Анонімний `MAP_PRIVATE` у системі з MMU – це сторінки, що стають copy-on-write після `fork()`, а анонімний `MAP_SHARED` після `fork()` залишається спільним.[^linux-nommu-mmap]

`fork()` дозволяє керувати цим і для окремих регіонів: mappings, позначені через `madvise(2)` як `MADV_DONTFORK`, нащадок не успадковує, а регіон із `MADV_WIPEONFORK` у нащадка заповнюється нулями.[^linux-man-fork]

### Що це означає для embedded

**Пам’ять, якої фізично ще немає.** Відразу після `fork()` споживання RAM майже не росте, але кожна приватна сторінка, яку змінять, потребуватиме нового фрейму. У механізмі overcommit accounting приватний writable mapping коштує свій розмір на кожен екземпляр; режим 0 (евристичний) за замовчуванням дозволяє overcommit, а режим 2 обмежує сумарний commit і повертає помилку вже під час виділення.[^linux-overcommit-accounting] Якщо ж ядро не може знайти фізичний фрейм, воно запускає OOM killer.[^linux-page-tables] На пристрої з 64–128 МБ RAM великий процес, що робить `fork()` і потім активно пише в пам’ять, може несподівано вичерпати RAM уже після успішного виклику.

**Затримка першого запису.** Перший запис у кожну спільну сторінку – це page fault з виділенням і копіюванням сторінки. Для real-time процесу це неконтрольована затримка. Блокування пам’яті через `mlock()`/`mlockall()` тут не допоможе нащадку: memory locks не успадковуються при `fork()`.[^linux-man-mlock]

**Багатопотоковий процес.** Нащадок отримує лише той потік, що викликав `fork()`, але повну копію адресного простору, включно зі станом mutex і condition variables. До `execve()` у нащадку багатопотокової програми можна безпечно викликати лише async-signal-safe функції.[^linux-man-fork] Mutex, захоплений іншим потоком у момент `fork()`, у нащадку не звільнить ніхто, бо цього потоку там немає; для таких випадків fork(2) радить `pthread_atfork(3)`.[^linux-man-fork]

**Запуск програм.** Якщо нащадок одразу викликає `execve()`, навіть дублювання таблиць сторінок – зайва робота. `vfork()` створює процес без копіювання таблиць сторінок батька: батьківський потік призупинено, доки нащадок не завершиться або не викличе `execve()`, а до того нащадок ділить з батьком усю пам’ять, включно зі стеком.[^linux-man-vfork] Через це в нащадку після `vfork()` майже нічого не можна робити, крім `exec` або `_exit()`.

**Системи без MMU.** Copy-on-write потребує апаратного захисту сторінок. На no-MMU Linux (uClinux) `fork()` немає взагалі, а `clone()` треба викликати з `CLONE_VM`.[^linux-nommu-mmap] Код, що покладається на `fork()`, на таких MCU-класу процесорах доведеться переписати на `vfork()` + `exec` або на потоки.

На співбесіді очікують почути, що copy-on-write – оптимізація реалізації, яка не змінює семантики `fork()`, але змінює профіль пам’яті й затримок: економія RAM під час виклику, page faults і можливий OOM пізніше.
