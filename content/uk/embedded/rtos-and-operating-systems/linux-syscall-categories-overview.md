---
id: emb-fund-0001
title: "Які системні виклики ви знаєте?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-syscalls
    title: "Linux manual page: syscalls(2)"
    url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - source_id: linux-man-malloc
    title: "Linux manual page: malloc(3)"
    url: https://man7.org/linux/man-pages/man3/malloc.3.html
  - source_id: linux-man-fork
    title: "Linux manual page: fork(2)"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-man-open
    title: "Linux manual page: open(2)"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-x86-64-syscall-table
    title: "Linux kernel source: arch/x86/entry/syscalls/syscall_64.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/arch/x86/entry/syscalls/syscall_64.tbl
  - source_id: linux-generic-syscall-table
    title: "Linux kernel source: scripts/syscall.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/scripts/syscall.tbl
  - source_id: linux-adding-syscalls
    title: "Linux kernel documentation: Adding a New System Call"
    url: https://docs.kernel.org/process/adding-syscalls.html
  - source_id: linux-man-vdso
    title: "Linux manual page: vdso(7)"
    url: https://man7.org/linux/man-pages/man7/vdso.7.html
  - source_id: linux-man-strace
    title: "Linux manual page: strace(1)"
    url: https://man7.org/linux/man-pages/man1/strace.1.html
---

## Short answer

Основні категорії:[^dou-embedded-interview]

- **Файлова система**: `open()`, `read()`, `write()`, `close()`, `lseek()`, `stat()`, `unlink()`
- **Процеси**: `fork()`, `exec()`, `wait()`, `exit()`, `getpid()`
- **Пам’ять**: `mmap()`, `munmap()`, `brk()`
- **Мережа**: `socket()`, `bind()`, `connect()`, `send()`, `recv()`
- **Синхронізація**: `futex()`
- **Пристрої**: `ioctl()`.

Переглянути всі: `man 2 syscalls` або файл `arch/x86/entry/syscalls/syscall_64.tbl` у ядрі.

## Detailed explanation

### Бібліотечна функція, обгортка і сам системний виклик

Системний виклик – фундаментальний інтерфейс між застосунком і ядром Linux. Програма зазвичай звертається до нього не напряму, а через функцію-обгортку в glibc або іншій C-бібліотеці: обгортка розкладає аргументи по регістрах, виконує виклик і, якщо ядро повернуло від’ємний номер помилки, записує його в `errno` та повертає `-1`.[^linux-man-syscalls] Тому, відповідаючи на питання «які системні виклики ви знаєте», корисно одразу розвести три рівні:

- функції стандартної бібліотеки, які самі не є системними викликами: `printf`, `fopen`, `malloc`. Наприклад, `malloc` у glibc розширює heap через `sbrk`, а блоки, більші за `MMAP_THRESHOLD` (типово 128 kB), виділяє окремим анонімним відображенням через `mmap`;[^linux-man-malloc]
- обгортки з тим самим ім’ям, що й виклик ядра (`read`, `write`, `close`);
- обгортки, які викликають зовсім інший системний виклик (про це нижче).

### Основні категорії з прикладами

Нижче – групування, яке зручно назвати на співбесіді; усі імена взято з офіційного списку системних викликів Linux.[^linux-man-syscalls]

- **Процеси й потоки**: `clone`, `clone3`, `fork`, `vfork`, `execve`, `exit_group`, `wait4`, `waitid`, `getpid`, `gettid`.
- **Файлові дескриптори та введення-виведення**: `openat`, `read`, `write`, `pread64`, `close`, `lseek`, `dup3`, `fcntl`, `newfstatat`, `statx`.
- **Файлова система**: `mkdirat`, `unlinkat`, `renameat2`, `mount`, `chdir`.
- **Пам’ять**: `brk`, `mmap`, `munmap`, `mprotect`, `madvise`, `mlockall`.
- **Синхронізація та IPC**: `futex`, `pipe2`, `eventfd2`, `memfd_create`, `mq_open`, а також System V `msgget`, `semop`, `shmget`.
- **Мережа**: `socket`, `bind`, `listen`, `accept4`, `connect`, `sendmsg`, `recvmsg`.
- **Очікування подій**: `ppoll`, `epoll_ctl`, `epoll_pwait`, `io_uring_setup`.
- **Час і таймери**: `clock_gettime`, `clock_nanosleep`, `timer_create`, `timerfd_create`.
- **Сигнали**: `rt_sigaction`, `rt_sigprocmask`, `tgkill`.
- **Планування**: `sched_setscheduler`, `sched_setaffinity`.
- **Ресурси й безпека**: `prlimit64`, `capset`, `seccomp`, `getrandom`.
- **Пристрої та модулі**: `ioctl` для специфічних для драйвера команд, `finit_module` для завантаження модуля ядра.

### Типові пастки

**Ім’я обгортки не дорівнює імені виклику.** Починаючи з glibc 2.3.3, функція `fork()` викликає не системний виклик `fork`, а `clone` із прапорцями, що дають той самий ефект.[^linux-man-fork] Починаючи з glibc 2.26, обгортка `open()` використовує системний виклик `openat`.[^linux-man-open] Тому в трасі реальної програми ви побачите `openat`, а не `open`. Найнадійніший спосіб дізнатися, які виклики насправді виконує процес, – запустити його під `strace`, який перехоплює кожен системний виклик і друкує його ім’я, аргументи та результат.[^linux-man-strace]

**Номери викликів залежать від архітектури.** Файл `arch/x86/entry/syscalls/syscall_64.tbl` описує лише x86-64: там `read` має номер 0, `write` – 1, `open` – 2, `fork` – 57.[^linux-x86-64-syscall-table] Для Embedded Linux на ARM це не той файл. Починаючи з Linux 6.11, arm64, riscv, loongarch та ще кілька архітектур описуються спільною таблицею `scripts/syscall.tbl`.[^linux-adding-syscalls] У ній `openat` має номер 56, `read` – 63, `write` – 64, а рядків для `open` і `fork` немає зовсім: заголовок таблиці прямо каже, що функціональність не дублюється, а менш гнучкі виклики нові архітектури мають реалізовувати в user space.[^linux-generic-syscall-table]

**Не кожен «системний» виклик заходить у ядро.** Деякі виклики, як-от `clock_gettime`, програма робить дуже часто, тож ядро відображає в кожен процес vDSO – код, який C-бібліотека використовує, щоб уникнути переходу в ядро і пов’язаних із ним накладних витрат.[^linux-man-vdso] У `strace` такі виклики не з’являються.

**Набір викликів неоднаковий на різних архітектурах.** На x86-32 мережеві виклики історично мультиплексуються через один виклик `socketcall`, а System V IPC – через `ipc`; у списку є й виклики, що існують лише на окремих архітектурах.[^linux-man-syscalls]

### Що хоче почути інтерв’юер

Достатньо назвати 4–6 категорій із реальними прикладами, пояснити різницю між бібліотечною функцією та системним викликом, згадати `errno` і `strace`. Сильна відповідь для embedded додає, що на ARM-платі номери й навіть набір викликів інші, ніж у `syscall_64.tbl`, а на мікроконтролері без MMU/MPU код застосунку і ядра RTOS виконується в одному спільному адресному просторі[^zephyr-introduction], тож виклик API ядра там зазвичай є звичайним викликом функції, без переходу між режимами. Механізм переходу з user mode в kernel mode розібрано в qid:emb-fund-0003.
