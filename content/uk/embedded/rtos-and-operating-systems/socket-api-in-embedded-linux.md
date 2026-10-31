---
id: emb-fund-0015
title: "Що таке socket у Linux і коли embedded-пристрій реально потребує socket API?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-socket
    title: "Linux manual page: socket(2)"
    url: https://man7.org/linux/man-pages/man2/socket.2.html
  - source_id: linux-man-socket-7
    title: "Linux manual page: socket(7)"
    url: https://man7.org/linux/man-pages/man7/socket.7.html
  - source_id: linux-man-unix
    title: "Linux manual page: unix(7)"
    url: https://man7.org/linux/man-pages/man7/unix.7.html
  - source_id: linux-socketcan
    title: "Linux kernel: SocketCAN - Controller Area Network"
    url: https://docs.kernel.org/networking/can.html
  - source_id: zephyr-bsd-sockets
    title: "Zephyr Project documentation: BSD Sockets"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/sockets.html
---

## Short answer

**Socket** – file descriptor для endpoint-у network або local IPC. Embedded-пристрій потребує socket API, коли говорить TCP/UDP, Unix domain IPC, Bluetooth sockets або має daemon/client архітектуру. Для простого sensor-to-MCU без OS socket не потрібен; там буде UART/SPI/I2C або lightweight network stack API.[^dou-embedded-interview]

## Detailed explanation

### Що таке socket

`socket()` створює endpoint для обміну й повертає file descriptor, що на нього посилається. Виклик приймає три аргументи: domain (сімейство протоколів), type (семантика обміну) і protocol.[^linux-man-socket] Socket layer у Linux – уніфікований інтерфейс між процесом і мережевими стеками ядра.[^linux-man-socket-7] Тобто socket – це не «мережеве з’єднання», а загальна абстракція: той самий API обслуговує TCP, локальний IPC, CAN-шину чи інтерфейс до ядра.

Типи визначають поведінку. `SOCK_STREAM` – надійний двонаправлений потік байтів зі з’єднанням; `SOCK_DGRAM` – datagrams без з’єднання, ненадійні й обмеженої довжини; `SOCK_SEQPACKET` – надійний упорядкований канал для datagrams, де кожен виклик читання забирає пакет цілком.[^linux-man-socket] Для сімейства `AF_UNIX` Linux додатково гарантує, що datagrams не губляться і не переставляються.[^linux-man-unix]

### Життєвий цикл і робота з descriptor

Сервер викликає `socket()`, `bind()` для локальної адреси, `listen()` і `accept()`, який повертає новий socket для кожного вхідного з’єднання; клієнт робить `connect()`. Дані передаються через `send()`/`recv()` і їхні варіанти, а оскільки socket – це file descriptor, працюють і звичайні `read()`/`write()`, а очікування готовності – через `poll()` або `select()`.[^linux-man-socket-7] Саме це робить socket зручним для embedded daemon: один цикл `poll()` може одночасно чекати на мережу, локальних клієнтів і, наприклад, character device. Таймаути блокувальних операцій задають опції `SO_RCVTIMEO` і `SO_SNDTIMEO`.[^linux-man-socket-7]

Найчастіша помилка – вважати, що один `send()` або `recv()` передає весь буфер. Для `SOCK_STREAM` POSIX дозволяє обробити менше даних, ніж запитано: `recv` на 1000 байтів може повернути 100, і решту треба дочитати наступними викликами.[^zephyr-bsd-sockets] Тому запис у потоковий socket роблять циклом:

```c
#include <errno.h>
#include <stddef.h>
#include <sys/socket.h>
#include <sys/types.h>

int send_all(int fd, const void *buf, size_t len)
{
    const char *p = buf;

    while (len > 0) {
        ssize_t n = send(fd, p, len, 0);
        if (n < 0) {
            if (errno == EINTR) {
                continue;
            }
            return -1;
        }
        p += n;
        len -= (size_t)n;
    }
    return 0;
}
```

З тієї ж причини протокол поверх TCP повинен сам задавати межі повідомлень (поле довжини чи роздільник): потік байтів їх не зберігає.

### Коли embedded-пристрою справді потрібен socket API

- **IP-мережа.** Будь-який TCP чи UDP обмін: MQTT, HTTP, Modbus TCP, NTP, власна телеметрія. Сімейства `AF_INET` і `AF_INET6` – найочевидніший випадок.[^linux-man-socket]
- **Локальний IPC між сервісами.** `AF_UNIX` створений для ефективного обміну між процесами на одній машині, вміє передавати file descriptors через `SCM_RIGHTS` і повідомляти облікові дані співрозмовника через `SO_PEERCRED`.[^linux-man-unix] Це типова схема «daemon володіє обладнанням, клієнти надсилають команди».
- **CAN.** SocketCAN реалізує CAN-драйвери як мережеві інтерфейси й надає до них Berkeley socket API, наближений до роботи з TCP/IP; раніше існували реалізації на character devices.[^linux-socketcan] На Linux-контролері з CAN socket – стандартний шлях.
- **Інші сімейства.** `AF_BLUETOOTH` для низькорівневих Bluetooth-протоколів, `AF_PACKET` для сирих кадрів, `AF_NETLINK` як інтерфейс до ядра.[^linux-man-socket]

### Коли він не потрібен

Обмін із датчиком через I2C, SPI чи UART не вимагає socket API: у Linux це character device, а на bare-metal MCU – драйвер периферії без операційної системи. Socket з’являється там, де є мережевий стек або локальні процеси, що обмінюються повідомленнями.

Наявність socket API також не прив’язана до Linux. У Zephyr є сумісний із BSD Sockets API (вмикається `CONFIG_NET_SOCKETS`), функції за замовчуванням мають префікс `zsock_`, а з `CONFIG_POSIX_API` доступні і стандартні імена. Таблицю file descriptors цей API використовує навіть тоді, коли решту POSIX-підсистеми вимкнено.[^zephyr-bsd-sockets] Тому код мережевого клієнта можна відносно легко переносити між Linux і RTOS, якщо не покладатися на специфічні для Linux опції.

Інтерв’юер, ставлячи це питання, зазвичай перевіряє дві речі: чи розуміє кандидат, що socket – це file descriptor з усіма наслідками (`poll`, неблокувальний режим, закриття), і чи знає він про часткові `send`/`recv` у потокових сокетах.
