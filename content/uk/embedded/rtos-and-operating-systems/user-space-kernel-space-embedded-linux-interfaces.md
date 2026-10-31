---
id: emb-fund-0012
title: "Як user space спілкується з kernel space в Embedded Linux через syscalls, ioctl, procfs або sysfs?"
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
  - source_id: linux-man-ioctl
    title: "Linux manual page: ioctl(2)"
    url: https://man7.org/linux/man-pages/man2/ioctl.2.html
  - source_id: linux-ioctl-guide
    title: "Linux kernel: ioctl based interfaces"
    url: https://docs.kernel.org/driver-api/ioctl.html
  - source_id: linux-sysfs
    title: "Linux kernel: sysfs - The filesystem for exporting kernel objects"
    url: https://docs.kernel.org/filesystems/sysfs.html
  - source_id: linux-sysfs-rules
    title: "Linux kernel: Rules on how to access information in sysfs"
    url: https://docs.kernel.org/admin-guide/sysfs-rules.html
  - source_id: linux-man-proc
    title: "Linux manual page: proc(5)"
    url: https://man7.org/linux/man-pages/man5/proc.5.html
  - source_id: linux-debugfs
    title: "Linux kernel: DebugFS"
    url: https://docs.kernel.org/filesystems/debugfs.html
  - source_id: linux-gpio-sysfs
    title: "Linux kernel: GPIO Sysfs Interface for Userspace"
    url: https://docs.kernel.org/userspace-api/gpio/sysfs.html
  - source_id: linux-man-socket
    title: "Linux manual page: socket(2)"
    url: https://man7.org/linux/man-pages/man2/socket.2.html
---

## Short answer

User space входить у kernel через `syscall`: `read`, `write`, `open`, `mmap` тощо. Для device-specific control часто використовують `ioctl`, для простих атрибутів driver-а – `sysfs`, а `procfs` переважно для process/kernel diagnostic info. <span class="warn">Не варто робити нестабільний binary protocol у sysfs</span>; там очікуються прості текстові атрибути.[^dou-embedded-interview]

## Detailed explanation

### Одна межа, кілька форм

Користувацька програма не має прямого доступу до пам’яті ядра чи регістрів пристроїв, тому кожна взаємодія з ядром іде через system call – фундаментальний інтерфейс між застосунком і Linux kernel. Зазвичай syscall викликають не напряму, а через обгортку libc (glibc, musl): вона розкладає аргументи по регістрах, виконує перехід у ядро, а від’ємний код помилки перетворює на `errno` і повертає `-1`.[^linux-man-syscalls] Сам механізм переходу розібрано в qid:emb-fund-0003.

`ioctl`, `procfs` і `sysfs` – не альтернатива syscalls, а різні способи використати ті самі syscalls. До `sysfs` чи `/proc` звертаються звичайними `open()`/`read()`/`write()`, а `ioctl()` – це окремий syscall над уже відкритим file descriptor. Тому питання насправді про те, яку форму інтерфейсу драйвер надає user space.

### Character device і ioctl

Основний шлях для даних – вузол пристрою в `/dev`: `open()`, далі `read()`/`write()` для потоку даних. Усе, що не вкладається в модель потокового вводу-виводу (налаштування режиму, запуск калібрування, читання статусу структурою), традиційно йде через `ioctl()`. Він змінює параметри пристрою спеціального файла, першим аргументом приймає відкритий file descriptor, другим – залежний від пристрою код операції, третім – вказівник на дані; семантика аргументів і результату визначається конкретним драйвером.[^linux-man-ioctl]

Код операції має структуру. Для нових команд kernel-документація вимагає макроси `_IO`, `_IOR`, `_IOW`, `_IOWR`: вони кодують напрямок передачі, 8-бітний тип драйвера, 8-бітний номер команди і розмір аргументу. На розмір відведено 13 або 14 біт, тож аргумент не може перевищувати 8191 байт.[^linux-ioctl-guide]

```c
#include <linux/ioctl.h>
#include <linux/types.h>

struct adc_cfg {
    __u32 channel;
    __u32 sample_rate_hz;
};

#define ADC_IOC_MAGIC   'a'
#define ADC_IOC_SET_CFG _IOW(ADC_IOC_MAGIC, 1, struct adc_cfg)
#define ADC_IOC_GET_CFG _IOR(ADC_IOC_MAGIC, 2, struct adc_cfg)
```

Тут треба передати сам тип структури, а не `sizeof` від нього: інакше макрос закодує `sizeof(size_t)`. Версіонувати структуру аргументу під тим самим номером – погана ідея; правильніше додати нову команду, а стару лишити для сумісності. На невідому команду драйвер повертає `-ENOTTY`. Поля структури варто оголошувати типами фіксованої ширини (`__u32`, `__u64`), а не `long`: розмір `long` залежить від архітектури, а 32-бітний user space на 64-бітному ядрі має бачити той самий layout.[^linux-ioctl-guide]

### sysfs: один атрибут – одне значення

`sysfs` відображає об’єкти device model у файлову систему. Атрибути мають бути текстовими ASCII-файлами, бажано з одним значенням на файл; допускається масив однотипних значень, а змішані типи, багаторядкові дані й складне форматування документація прямо засуджує. Ядро виділяє для `show()` буфер розміром `PAGE_SIZE` і викликає метод один раз на кожне читання.[^linux-sysfs] Тому `sysfs` підходить для параметрів на кшталт режиму, порогу чи стану, але не для потоку семплів і не для бінарного протоколу.

Ще один нюанс: структура `sysfs` відображає внутрішню будову ядра, а стабільного внутрішнього API ядро не обіцяє, тож окремі аспекти `sysfs` можуть змінюватися між версіями.[^linux-sysfs-rules] Показовий приклад для embedded – GPIO: старий інтерфейс `/sys/class/gpio` оголошено застарілим, нові розробки мають використовувати GPIO character device API, а sysfs-варіант буде видалено.[^linux-gpio-sysfs]

### procfs і debugfs

`procfs` – псевдофайлова система з інформацією про процеси та ядро, зазвичай змонтована в `/proc`. Більшість її файлів доступні лише для читання, але частина дозволяє змінювати змінні ядра, як-от параметри в `/proc/sys`.[^linux-man-proc] Документація debugfs підсумовує різницю так: `/proc` призначений лише для інформації про процес, `sysfs` має суворе правило одного значення на файл, а `debugfs` не має правил узагалі й не вважається стабільним ABI.[^linux-debugfs] Отже, `debugfs` – місце для налагоджувальної інформації, від якої не повинен залежати продакшн-софт.

### Інші канали

Ще один канал – netlink: окреме сімейство сокетів `AF_NETLINK`, яке socket(2) описує як інтерфейс між ядром і user space.[^linux-man-socket]

### Як вибирати

- Потік даних (семпли АЦП, кадри) – `read()`/`write()` на character device, за потреби `mmap()`.
- Команди й структуровані налаштування – `ioctl()` з коректно закодованими номерами.
- Прості текстові параметри драйвера – `sysfs`.
- Стан процесів і системні налаштування – `/proc`; налагоджувальні дані – `debugfs`.

Інтерв’юер зазвичай перевіряє не перелік механізмів, а розуміння ABI: інтерфейс, який побачив user space, стає контрактом, і його важко змінити, не зламавши наявні програми. Порівняння драйвера в ядрі з user space драйвером – у qid:emb-linemb-0001.
