---
id: emb-fund-0004
title: "Що таке файловий дескриптор?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: posix-2024-definitions
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 3. Definitions"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html
  - source_id: linux-man-open
    title: "Linux manual page: open(2)"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-man-dup
    title: "Linux manual page: dup(2)"
    url: https://man7.org/linux/man-pages/man2/dup.2.html
  - source_id: linux-man-close
    title: "Linux manual page: close(2)"
    url: https://man7.org/linux/man-pages/man2/close.2.html
  - source_id: linux-man-getrlimit
    title: "Linux manual page: getrlimit(2)"
    url: https://man7.org/linux/man-pages/man2/getrlimit.2.html
  - source_id: linux-man-proc-pid-fd
    title: "Linux manual page: proc_pid_fd(5)"
    url: https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
  - source_id: linux-adding-syscalls
    title: "Linux kernel documentation: Adding a New System Call"
    url: https://docs.kernel.org/process/adding-syscalls.html
  - source_id: linux-gpio-chardev
    title: "Linux kernel documentation: GPIO Character Device Userspace API"
    url: https://docs.kernel.org/userspace-api/gpio/chardev.html
  - source_id: linux-gpio-v2-get-line-ioctl
    title: "Linux kernel documentation: GPIO_V2_GET_LINE_IOCTL"
    url: https://docs.kernel.org/userspace-api/gpio/gpio-v2-get-line-ioctl.html
---

## Short answer

**File descriptor (fd)** – невід’ємне ціле число, що ідентифікує відкритий ресурс у процесі: файл, сокет, pipe, пристрій.[^dou-embedded-interview] Ядро зберігає таблицю fd для кожного процесу.

Стандартні: `0` = stdin, `1` = stdout, `2` = stderr.

Цикл: `fd = open("file", O_RDONLY);`, потім `read(fd, buf, n);`, потім `close(fd);`. В Linux «все є файлом» – через fd можна працювати з пристроями (`/dev/gpiochip0`), sysfs, і навіть таймерами (`timerfd`).

## Detailed explanation

### Три рівні: дескриптор, відкритий опис файлу, сам об’єкт

POSIX визначає файловий дескриптор як унікальне в межах процесу невід’ємне ціле число, яке ідентифікує відкритий файл для доступу до нього; значення 0, 1 і 2 мають умовне призначення – standard input, standard output і standard error.[^posix-2024-definitions] Але саме число – лише верхній рівень. Щоб правильно відповідати на питання про `dup`, `fork` і спільний offset, треба знати всю ланку:

1. **Дескриптор** – індекс у таблиці відкритих дескрипторів процесу. `open()` повертає найменший номер, який зараз не відкритий у цьому процесі.[^linux-man-open]
2. **Відкритий опис файлу (open file description)** – запис у системній таблиці відкритих файлів; у ядрі Linux це `struct file`. Саме він зберігає поточний offset і прапорці стану файлу (`O_APPEND`, `O_NONBLOCK` тощо). Кожен виклик `open()` створює новий опис.[^linux-man-open] Один дескриптор завжди посилається рівно на один опис, але на один опис може посилатися кілька дескрипторів.[^posix-2024-definitions]
3. **Об’єкт** – файл на диску (inode), pipe, сокет, пристрій. Посилання дескриптора не зміниться, навіть якщо шлях потім видалять або перейменують.[^linux-man-open]

Прапорці самого дескриптора (зараз це фактично лише close-on-exec, `FD_CLOEXEC`) належать дескриптору, а не опису.[^linux-man-dup]

### Що з цього випливає на практиці

- **`dup()`/`dup2()`** створюють новий дескриптор на той самий опис, тож обидва поділяють offset: `lseek()` через один змінює позицію і для другого. Close-on-exec у копії вимкнений.[^linux-man-dup]
- **`fork()`**: дочірній процес успадковує копії дескрипторів батька, які посилаються на ті самі описи. Батько й дитина, що пишуть в один успадкований файл, рухають спільний offset.[^linux-man-open]
- **Два незалежні `open()`** одного файлу дають два різні описи з незалежними offset-ами.[^linux-man-open]
- **Правило найменшого вільного номера** пояснює класичне перенаправлення виводу. Надійніше робити його явно через `dup2()`:

```c
#include <fcntl.h>
#include <unistd.h>

int redirect_stdout(const char *path)
{
    int fd = open(path, O_WRONLY | O_CREAT | O_APPEND | O_CLOEXEC, 0644);
    if (fd < 0)
        return -1;
    if (fd == STDOUT_FILENO)            /* stdout was closed: open() reused 1 */
        return fcntl(fd, F_SETFD, 0);   /* keep it, just clear close-on-exec */
    if (dup2(fd, STDOUT_FILENO) < 0) {  /* fd 1 now refers to the same description */
        close(fd);
        return -1;
    }
    return close(fd);                   /* fd 1 stays open */
}
```

Тут `O_CLOEXEC` закриває вихідний дескриптор при `execve()`, а копія на номері 1 цей прапорець не успадковує, тому перенаправлений stdout переживе запуск нової програми. Окремо оброблено випадок, коли stdout уже був закритий: тоді `open()` сама поверне номер 1, `dup2()` з однаковими номерами нічого не робить, і без цієї перевірки фінальний `close()` закрив би щойно відкритий stdout.[^linux-man-dup]

### Типові пастки

- **Витік дескрипторів.** Ліміт `RLIMIT_NOFILE` на одиницю більший за максимальний номер дескриптора, який процес може відкрити; спроба перевищити його через `open()`, `pipe()`, `dup()` дає `EMFILE`.[^linux-man-getrlimit] На пристрої, що працює місяцями, забутий `close()` у гілці помилки рано чи пізно вичерпає ліміт.
- **Ігнорування результату `close()`.** Помилка попереднього `write()` може проявитися лише на фінальному `close()`, що звільняє опис; неперевірений результат означає ризик тихої втрати даних. Повторювати `close()` після помилки не слід: ядро Linux звільняє номер ще на початку операції, і повторний виклик може закрити дескриптор, який уже встиг отримати інший потік.[^linux-man-close]
- **Закриття дескриптора, яким користується інший потік.** Номер одразу може бути перевикористаний наступним `open()`, а на Linux заблокований у цей момент `read()` чи `write()` тримає посилання на опис і може успішно завершитися вже після `close()` в іншому потоці.[^linux-man-close]
- **Витік у дочірні програми.** За замовчуванням дескриптор лишається відкритим через `execve()`; `O_CLOEXEC` змінює це під час відкриття.[^linux-man-open] Встановлювати `FD_CLOEXEC` окремим `fcntl()` пізніше ризиковано: між двома викликами інший потік може зробити `fork()` і `execve()`, і дескриптор потрапить у чужу програму.[^linux-adding-syscalls]

Для діагностики корисний `/proc/<pid>/fd/`: там кожен відкритий дескриптор – символьне посилання на файл, а для pipe і сокетів – рядок вигляду `socket:[2248868]`.[^linux-man-proc-pid-fd]

### «Усе є файлом» в Embedded Linux

Розробникам ядра прямо рекомендовано: якщо новий системний виклик дає user space посилання на об’єкт ядра, це має бути файловий дескриптор, а не новий тип handle; готовність дескриптора до читання чи запису – звичайний спосіб повідомити user space про подію.[^linux-adding-syscalls] Завдяки цьому таймери (`timerfd`), події (`eventfd`), сокети, pipe і пристрої можна чекати одним `poll()` чи `epoll` в одному циклі подій.

Приклад із реальної плати – GPIO. Сучасний інтерфейс – символьний пристрій `/dev/gpiochipX`: `open()` дає дескриптор чипа, а лінії запитуються через `ioctl` `GPIO_V2_GET_LINE_IOCTL`.[^linux-gpio-chardev] Результат запиту – ще один дескриптор: стан ліній, зокрема значення виходів, гарантовано зберігається, поки цей дескриптор відкритий; після закриття лінія може повернутися до стану за замовчуванням.[^linux-gpio-v2-get-line-ioctl] Тобто час життя дескриптора тут прямо визначає, хто керує фізичним виводом.

### Що хоче почути інтерв’юер

Що fd – це індекс у таблиці процесу, а не сам файл; що між fd і файлом є open file description зі спільним offset; як поводяться `dup` і `fork`; що таке 0/1/2 і `O_CLOEXEC`; і що через дескриптори в Linux працюють не лише файли, а й сокети, пристрої та таймери.
