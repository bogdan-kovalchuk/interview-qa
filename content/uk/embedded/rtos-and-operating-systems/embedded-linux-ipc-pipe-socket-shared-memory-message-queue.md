---
id: emb-fund-0014
title: "Які IPC-механізми доречні в Embedded Linux і які trade-offs мають pipe, socket, shared memory та message queue?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-pipe
    title: "Linux manual page: pipe(7)"
    url: https://man7.org/linux/man-pages/man7/pipe.7.html
  - source_id: linux-man-unix
    title: "Linux manual page: unix(7)"
    url: https://man7.org/linux/man-pages/man7/unix.7.html
  - source_id: linux-man-shm-overview
    title: "Linux manual page: shm_overview(7)"
    url: https://man7.org/linux/man-pages/man7/shm_overview.7.html
  - source_id: linux-man-mmap
    title: "Linux manual page: mmap(2)"
    url: https://man7.org/linux/man-pages/man2/mmap.2.html
  - source_id: linux-man-mq-overview
    title: "Linux manual page: mq_overview(7)"
    url: https://man7.org/linux/man-pages/man7/mq_overview.7.html
  - source_id: linux-man-sem-overview
    title: "Linux manual page: sem_overview(7)"
    url: https://man7.org/linux/man-pages/man7/sem_overview.7.html
---

## Short answer

`pipe` простий для stream між related processes, але локальний і односторонній. `socket` гнучкий: Unix domain для local IPC або TCP/UDP для network, але має overhead. `shared memory` найшвидша для великих даних, проте потребує synchronization; `message queue` дає message boundaries і priority, але обмежена розмірами/лімітами system.[^dou-embedded-interview]

## Detailed explanation

Embedded Linux-пристрій рідко складається з одного процесу: є daemon, що працює з датчиками, сервіс зв’язку, вебінтерфейс, watchdog. Вибір IPC визначається трьома питаннями: чи потрібні межі повідомлень, скільки даних передається і хто відповідає за синхронізацію.

### Pipe і FIFO

Pipe – односпрямований канал із кінцями для читання й запису. Його створює `pipe(2)`, тому він зручний між спорідненими процесами, які успадкували descriptors через `fork()`. FIFO (named pipe) має ім’я у файловій системі, і його може відкрити будь-який процес, якому дозволяють права доступу.[^linux-man-pipe]

Ключова властивість: pipe – це byte stream без меж повідомлень. Два `write()` по 10 байтів можуть бути прочитані одним `read()` на 20 байтів, тож формат кадру (довжина, роздільник) задає застосунок. Ємність pipe обмежена; у Linux з версії 2.6.11 вона за замовчуванням становить 16 сторінок, тобто 65 536 байтів при сторінці 4096 байтів. Коли pipe заповнений, `write()` блокується або повертає помилку з `O_NONBLOCK`. POSIX гарантує атомарність запису не більше `PIPE_BUF` байтів (мінімум 512, у Linux 4096), тому кілька записувачів не перемішають короткі повідомлення, а довші можуть перемішатися.[^linux-man-pipe]

### Unix domain socket

`AF_UNIX` socket призначений для ефективного обміну між процесами на одній машині. Він підтримує три типи: `SOCK_STREAM` (потік, як TCP), `SOCK_DGRAM`, що зберігає межі повідомлень і в Linux не губить і не переставляє datagrams, та `SOCK_SEQPACKET` – з’єднання з межами повідомлень і порядком доставки.[^linux-man-unix] На відміну від pipe, сокет двонаправлений і природно лягає на архітектуру «один сервер – багато клієнтів».

Є і можливості, яких немає в інших механізмах: через `SCM_RIGHTS` можна передати іншому процесу відкриті file descriptors, а `SO_PEERCRED` повертає облікові дані процесу на іншому кінці з’єднання.[^linux-man-unix] Для embedded-сервісу це спосіб перевірити, хто саме надсилає команду. Ціна – кожне повідомлення копіюється через ядро, тому для великих обсягів сокет програє shared memory.

### Shared memory

POSIX shared memory складається з `shm_open()`, `ftruncate()` (новий об’єкт має нульовий розмір) і `mmap()`. У Linux об’єкти лежать у `tmpfs`, зазвичай у `/dev/shm`, і мають kernel persistence: об’єкт існує, доки його не видалили `shm_unlink()` і всі процеси не зняли mapping, або до перезавантаження.[^linux-man-shm-overview]

```c
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

struct frame {
    unsigned seq;
    unsigned char pixels[640 * 480];
};

struct frame *map_frame(void)
{
    int fd = shm_open("/cam_frame", O_CREAT | O_RDWR, 0600);
    if (fd < 0) {
        return NULL;
    }
    if (ftruncate(fd, sizeof(struct frame)) < 0) {
        close(fd);
        return NULL;
    }
    void *p = mmap(NULL, sizeof(struct frame), PROT_READ | PROT_WRITE,
                   MAP_SHARED, fd, 0);
    close(fd);
    return p == MAP_FAILED ? NULL : p;
}
```

Descriptor можна закрити одразу після `mmap()`, mapping від цього не зникає.[^linux-man-mmap] Після відображення дані передаються без копіювання через ядро, і саме тому shared memory – найшвидший варіант для великих буферів (кадри камери, аудіо). Але ядро більше не впорядковує доступ: процеси мають синхронізуватися самі, наприклад POSIX semaphores.[^linux-man-shm-overview] Unnamed semaphore, що використовується між процесами, має лежати саме в такій спільній пам’яті.[^linux-man-sem-overview] Типова помилка – прапорець «кадр готовий» у спільній структурі без жодної синхронізації: це data race з усіма наслідками (див. qid:emb-rtos-0001).

### POSIX message queue

`mq_open()`, `mq_send()`, `mq_receive()` передають окремі повідомлення; кожне має пріоритет, і отримувач завжди бере повідомлення з найвищим пріоритетом першим. У Linux доступно 32 768 рівнів пріоритету, хоча POSIX вимагає лише 0–31. Процес може запросити асинхронне сповіщення через `mq_notify()`, а оскільки в Linux дескриптор черги є file descriptor, чергу можна чекати через `poll()`/`epoll()`, хоча це непортабельно.[^linux-man-mq-overview]

Обмеження задані системними лімітами: за замовчуванням `msg_max` дорівнює 10 повідомленням, а `msgsize_max` – 8192 байтам; обидва змінюються через `/proc/sys/fs/mqueue/`.[^linux-man-mq-overview] Тому черга підходить для команд і подій, а не для потоку даних. Черга теж має kernel persistence: без `mq_unlink()` вона існує до перезавантаження.[^linux-man-mq-overview]

### Підсумкове порівняння

| Механізм | Межі повідомлень | Напрям | Найкраще підходить для |
|---|---|---|---|
| pipe / FIFO | ні, byte stream | один | лог, потік між батьком і нащадком |
| `AF_UNIX` socket | залежно від типу | обидва | client-server, передача descriptors |
| shared memory | немає, це пам’ять | обидва | великі буфери з окремою синхронізацією |
| message queue | так, з пріоритетом | будь-який | короткі команди й події |

На співбесіді важливо показати, що «найшвидший» механізм не автоматично найкращий: shared memory переносить усю складність синхронізації в застосунок, а сокет чи черга дають готову модель повідомлень ціною копіювання.
