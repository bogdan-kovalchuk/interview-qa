---
id: emb-fund-0027
title: "Linux-контролер не може запускати нові процеси, хоча df показує вільне місце. Як перевірити inodes, tmpfs, file descriptors і logs?"
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
    title: "fork(2) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-man-getrlimit
    title: "getrlimit(2) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
  - source_id: linux-man-proc-sys-kernel
    title: "proc_sys_kernel(5) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man5/proc_sys_kernel.5.html
  - source_id: linux-man-proc-sys-fs
    title: "proc_sys_fs(5) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man5/proc_sys_fs.5.html
  - source_id: linux-man-open
    title: "open(2) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-man-df
    title: "df(1) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man1/df.1.html
  - source_id: linux-tmpfs
    title: "The Linux Kernel: Tmpfs"
    url: https://docs.kernel.org/filesystems/tmpfs.html
  - source_id: linux-man-unlink
    title: "unlink(2) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man2/unlink.2.html
  - source_id: linux-man-proc-pid-fd
    title: "proc_pid_fd(5) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
  - source_id: linux-man-wait
    title: "wait(2) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man2/wait.2.html
  - source_id: linux-cgroup-v2
    title: "The Linux Kernel: Control Group v2"
    url: https://docs.kernel.org/admin-guide/cgroup-v2.html
  - source_id: linux-ext4-admin
    title: "The Linux Kernel: ext4 General Information"
    url: https://docs.kernel.org/admin-guide/ext4.html
  - source_id: linux-man-mke2fs
    title: "mke2fs(8) – сторінка man Linux"
    url: https://man7.org/linux/man-pages/man8/mke2fs.8.html
---

## Short answer

Перевір `df -i` для inodes, `df -h` для `/tmp`/`/run` tmpfs, `ulimit -n` і `lsof` для file descriptors. Подивись `dmesg`, `journalctl`, OOM messages, read-only remount і errors filesystem. <span class="warn">Вільні bytes на rootfs не допоможуть, якщо закінчились inodes, PID limit, fd limit або tmpfs.</span>[^dou-embedded-interview]

## Detailed explanation

`df` показує лише вільні блоки файлових систем. Щоб запустити новий процес, ядру потрібні PID і task-структури, процесу-батьку – вільні file descriptors, а новому процесу часто ще й можливість створити файл у `/tmp`, `/run` чи `/var`. Кожен із цих ресурсів має власний ліміт, і будь-який із них може закінчитися при «вільних» гігабайтах на rootfs. Тому діагностику починають не з гіпотези, а з точного тексту помилки.

### Крок 0: який саме errno

Повідомлення в журналі чи shell зазвичай однозначно вказує напрям:

- `fork: Resource temporarily unavailable` – це `EAGAIN` від `fork()`. Man-сторінка перелічує причини: досягнуто `RLIMIT_NPROC` для real UID, системний ліміт `threads-max`, вичерпано діапазон `pid_max` або ліміт `pids.max` cgroup-контролера PIDs. `ENOMEM` означає, що ядру забракло пам’яті на структури нового процесу.[^linux-man-fork]
- `Too many open files` – це `EMFILE` (досягнуто per-process ліміт `RLIMIT_NOFILE`) або `ENFILE` (системний ліміт відкритих файлів).[^linux-man-open]
- `No space left on device` – `ENOSPC`: на пристрої немає місця для нового файлу.[^linux-man-open] На ext2/3/4 це стосується і блоків, і inodes.
- `Read-only file system` – файлову систему перемонтовано тільки на читання, і місце тут ні до чого.

### Inodes

Кожен файл займає inode, а кількість inodes на ext2/3/4 визначається під час створення файлової системи співвідношенням bytes-per-inode, яке згодом змінити не можна; лише зміна розміру файлової системи пропорційно змінює кількість inodes.[^linux-man-mke2fs] Мільйони дрібних файлів (лог-фрагменти, кеші, файли сесій, черги) вичерпують inodes задовго до блоків. Перевірка – `df -i`, яка показує використання inodes замість блоків.[^linux-man-df] Далі шукають каталог-винуватець, наприклад рахуючи файли по підкаталогах `/var` командою `find`.

### tmpfs: `/tmp`, `/run`, `/dev/shm`

tmpfs зберігає файли у virtual memory, тобто фактично в RAM і, якщо для монтування дозволено swap, у swap. Розмір за замовчуванням – половина фізичної RAM, ліміт inodes за замовчуванням – половина кількості сторінок RAM (або lowmem-сторінок, якщо їх менше), і обидва параметри змінюються під час remount.[^linux-tmpfs] Звідси два наслідки для embedded:

- переповнений tmpfs дає `ENOSPC`, хоча `df /` показує вільне місце, тож перевіряти треба `df -h` і `df -i` саме для `/tmp`, `/run`, `/dev/shm`;
- дані в tmpfs займають RAM. Документація попереджає, що завеликий tmpfs може довести систему до deadlock, бо OOM handler не здатен звільнити цю пам’ять.[^linux-tmpfs] На пристрої без swap «логи в `/run`» поступово з’їдають пам’ять для нових процесів.

### Видалені, але відкриті файли

Якщо `df` показує зайняте місце, а `du` його не знаходить, типова причина – файл видалили (наприклад, logrotate), але процес досі тримає його відкритим. Після `unlink()` файл існує, доки не закрито останній descriptor, що на нього посилається.[^linux-man-unlink] Знайти такий файл можна через `/proc/<pid>/fd/`: там на кожен відкритий descriptor є symlink на реальний файл.[^linux-man-proc-pid-fd] Місце повертає перезапуск процесу або закриття descriptor, а не повторне видалення.

### File descriptors

- **Per-process:** `RLIMIT_NOFILE` – на одиницю більше за найбільший номер descriptor, який процес може відкрити; перевищення дає `EMFILE` у `open()`, `pipe()`, `dup()`.[^linux-man-getrlimit] Поточний ліміт показує `ulimit -n` або `/proc/<pid>/limits`, а кількість відкритих – `ls /proc/<pid>/fd | wc -l`. Якщо число в daemon-а постійно росте, це leak descriptors (незакриті сокети, файли, `eventfd`).
- **Системний:** `/proc/sys/fs/file-max` задає загальний ліміт, при досягненні якого виклики повертають `ENFILE`, а в журналі ядра з’являється `VFS: file-max limit <number> reached`. `/proc/sys/fs/file-nr` показує кількість виділених file handles поруч із максимумом.[^linux-man-proc-sys-fs]

### Процеси, потоки й PID

- `/proc/sys/kernel/pid_max` на одиницю більший за максимальний PID і тому є системним лімітом на сумарну кількість процесів і потоків; значення за замовчуванням – 32768.[^linux-man-proc-sys-kernel]
- `/proc/sys/kernel/threads-max` – системний ліміт на кількість потоків (tasks).[^linux-man-proc-sys-kernel]
- `RLIMIT_NPROC` обмежує кількість процесів (точніше, потоків) одного real UID, але не діє для root і процесів з `CAP_SYS_ADMIN` чи `CAP_SYS_RESOURCE`.[^linux-man-getrlimit] Якщо сервіс працює від окремого користувача, саме цей ліміт часто першим спрацьовує.
- **Zombie-процеси.** Дочірній процес, який завершився, але на який батько не викликав `wait()`, залишається zombie і займає слот у таблиці процесів; якщо таблиця заповниться, нові процеси створити неможливо.[^linux-man-wait] У `ps` вони видні зі станом `Z`, а лікувати треба батька, який не обробляє `SIGCHLD`.
- **cgroup v2.** Контролер PIDs зупиняє `fork()`/`clone()` після досягнення `pids.max`; поточне значення видно в `pids.current`, а відмови рахує `pids.events`.[^linux-cgroup-v2] systemd-сервіс може мати власний ліміт задач, навіть коли система загалом має вільні PID.

### Журнали й стан файлової системи

`dmesg` і `journalctl` показують те, що не видно з `df`: повідомлення OOM killer, помилки файлової системи, `VFS: file-max limit reached`. Окремо варто перевірити `/proc/mounts`: ext4 з опцією `errors=remount-ro` при помилці перемонтовує файлову систему тільки на читання.[^linux-ext4-admin] На flash-носіях після зносу чи раптового зникнення живлення це типовий сценарій, і тоді запис будь-якого файлу падає, хоча вільних блоків багато.

### Компактний чекліст

```sh
df -h; df -i                          # blocks and inodes, including tmpfs mounts
grep ' ro,' /proc/mounts              # anything remounted read-only?
cat /proc/sys/fs/file-nr              # allocated / free / max file handles
cat /proc/sys/kernel/pid_max /proc/sys/kernel/threads-max
ps -eo stat= | grep -c '^Z'           # zombie count
ls /proc/<pid>/fd | wc -l             # fds of a suspect daemon
grep 'open files\|processes' /proc/<pid>/limits
dmesg | tail -n 50                    # OOM, I/O and filesystem errors
```

Сильна відповідь на співбесіді не просто перелічує команди, а пояснює, як від тексту помилки перейти до конкретного ліміту, і пропонує системне виправлення: ротацію логів з обмеженням розміру, окремий розділ або квоту для даних, ліміти в unit-файлах сервісів, моніторинг кількості inodes, descriptors і процесів.
