---
id: emb-conn-0001
title: "Як TCP/IP стек використовується в IoT-пристрої і де проходить межа між firmware, OS і network stack?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: zephyr-net-stack-architecture
    title: "Zephyr Project documentation: Network Stack Architecture"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/net-stack-architecture.html
  - source_id: lwip-overview
    title: "lwIP 2.1.0: Overview"
    url: https://www.nongnu.org/lwip/2_1_x/index.html
  - source_id: lwip-pitfalls
    title: "lwIP 2.1.0: Common pitfalls"
    url: https://www.nongnu.org/lwip/2_1_x/pitfalls.html
  - source_id: lwip-multithreading
    title: "lwIP 2.1.0: Multithreading"
    url: https://www.nongnu.org/lwip/2_1_x/multithreading.html
  - source_id: esp-idf-lwip
    title: "ESP-IDF Programming Guide: lwIP"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/lwip.html
  - source_id: linux-napi
    title: "Linux kernel documentation: NAPI"
    url: https://docs.kernel.org/networking/napi.html
  - source_id: linux-man-tcp
    title: "tcp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/tcp.7.html
  - source_id: esp-at-overview
    title: "ESP-AT User Guide: What is ESP-AT"
    url: https://docs.espressif.com/projects/esp-at/en/latest/esp32/Get_Started/What_is_ESP-AT.html
  - source_id: zephyr-net-offload
    title: "Zephyr Project documentation: Network Traffic Offloading"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/net_offload.html
---

## Short answer

На bare-metal MCU TCP/IP часто дає бібліотека типу lwIP, а firmware напряму керує Ethernet/Wi-Fi driver і sockets-like API. В Embedded Linux kernel містить network stack і drivers, а application працює через socket API. Межа проходить там, де frame від hardware driver стає packet-ом stack-а, а далі application protocol типу MQTT/HTTP працює поверх TCP/TLS.[^dou-embedded-interview]

## Detailed explanation

### Шари і питання власності

Мережевий стек IoT-пристрою зручно читати знизу вгору: PHY або радіо, MAC із DMA-дескрипторами, драйвер, мережевий інтерфейс із L2-логікою (Ethernet з ARP, Wi-Fi, PPP), IP/ICMP/UDP/TCP, програмний інтерфейс (BSD sockets або власний API стека), прикладні протоколи (DHCP, DNS, TLS, MQTT, HTTP, CoAP) і нарешті логіка застосунку. Zephyr описує саме таку структуру: застосунок працює через BSD socket API або готові бібліотеки CoAP, LwM2M і MQTT; під ними core-протоколи IPv4/IPv6/UDP/TCP/ICMP, абстракція мережевого інтерфейсу, L2-технології (Ethernet, IEEE 802.15.4, Bluetooth, CAN) і драйвери пристроїв; ARP для IPv4 виконує саме Ethernet-компонент L2.[^zephyr-net-stack-architecture]

Питання «де проходить межа» насправді складається з трьох: хто володіє кодом кожного шару, у якому контексті виконання (ISR, окремий потік стека, потік застосунку, kernel чи userspace) він працює і хто володіє буфером пакета в кожен момент. Відповідь залежить від того, яка з трьох архітектур використана.

### Bare-metal або RTOS із lwIP

lwIP – невелика незалежна реалізація TCP/IP, розрахована на системи з десятками кілобайт вільної RAM і приблизно 40 KB коду; вона містить IPv4/IPv6, UDP, TCP, DHCP, DNS, raw/native API, необов’язковий Berkeley-подібний socket API, шар `altcp` для TLS поверх TCP (портований на mbedTLS) і MQTT-клієнт.[^lwip-overview] Тут немає апаратної межі kernel/userspace: драйвер, стек і застосунок зібрані в один образ і ділять один адресний простір. Межа – суто програмний контракт, і порушити його дуже легко.

lwIP має два режими. У mainloop-режимі (`NO_SYS`) доступний лише raw API, і є два способи гарантувати, що в стеку одночасно працює лише один контекст: або ISR драйвера викликає `netif->input` напряму (тоді всі callback-и стека виконуються в контексті переривання), або ISR кладе прийняті кадри в чергу, яку опитує головний цикл. Документація прямо забороняє викликати lwIP з переривання, наприклад `udp_send()` чи `tcp_write()` з ISR SPI.[^lwip-pitfalls] В OS-режимі ядро стека виконує один потік `tcpip_thread`; raw API можна викликати лише з нього або, якщо ввімкнено `LWIP_TCPIP_CORE_LOCKING`, з потоку, що захопив core lock через `LOCK_TCPIP_CORE()` (але не з ISR)[^lwip-pitfalls], а потоки застосунку, що користуються netconn або sockets, спілкуються з ним передаванням повідомлень. Потокобезпечні лише функції з `api.h`, `sockets.h`, `netifapi.h` та ще кількох заголовків, і навіть socket-функції не можна викликати для одного TCP/UDP control block з кількох потоків без власного блокування.[^lwip-multithreading]

Практичний наслідок: ISR драйвера лише забирає дескриптор і сигналізує, кадр передається в стек у контексті стека, а застосунок працює у власній задачі через sockets. ESP-IDF використовує модифікований lwIP, офіційно підтримує саме BSD Sockets API і для інших API радить вмикати `CONFIG_LWIP_CHECK_THREAD_SAFETY`, щоб стек сам перевіряв контекст виклику.[^esp-idf-lwip]

### Zephyr: межі у вигляді черг

У нативному стеку Zephyr драйвер у контексті переривання виділяє мережеві буфери й кладе пакет у RX-чергу на `k_fifo`; ця черга відокремлює подальшу обробку (bottom half), бо драйвер має завершитися якомога швидше. Далі L2 перевіряє пакет і знімає заголовок та FCS, інтерфейс збирає статистику, L3 перевіряє IPv4/IPv6, а socket handler кладе дані в чергу конкретного сокета. Застосунок зазвичай працює в userspace-контексті, стек – у kernel-контексті. На передаванні шлях симетричний, а черги `k_fifo` в обох напрямках є точками, де дані переходять між потоками з різними контекстами і пріоритетами.[^zephyr-net-stack-architecture]

### Embedded Linux

Тут межа апаратно захищена: драйвер і весь TCP/IP стек належать ядру, а застосунок бачить лише сокети через системні виклики, тож кожен `send()`/`recv()` – це перехід user/kernel і копіювання даних. Усередині ядра пристрій повідомляє про нові події перериванням, після чого ядро планує NAPI-екземпляр, який обробляє пакети, зазвичай у контексті software interrupt або в окремих kernel-потоках.[^linux-napi] Поведінку TCP застосунок налаштовує лише через socket options і sysctl: наприклад, `TCP_NODELAY` вимикає алгоритм Nagle.[^linux-man-tcp]

### Винесений стек: TCP/IP поза основним MCU

Третій варіант – TCP/IP виконує окремий чип, а основний MCU керує ним командами. ESP-AT, наприклад, перетворює ESP32 на slave-пристрій, якому host MCU надсилає AT-команди (зокрема Wi-Fi, TCP/IP і MQTT) та отримує відповіді.[^esp-at-overview] Zephyr для таких випадків має network offloading API, через який вендорський HAL підставляє власну реалізацію IP-стека, і socket offloading, коли вендорський стек експортує socket API.[^zephyr-net-offload] Межа тут переміщується найдалі: firmware основного MCU не бачить пакетів зовсім, а працює з абстракцією «з’єднання» через послідовний протокол. За це платять меншим контролем над параметрами TCP, питанням, де виконується TLS, і необхідністю обробляти скидання модуля та ресинхронізацію його стану.

### Що зазвичай хоче почути інтерв’юер

- Назвати шари і власника кожного: драйвер, стек, прикладний протокол, застосунок.
- Пояснити контексти виконання: ISR робить мінімум, стек живе в одному контексті, застосунок не викликає raw API з чужого потоку.
- Пояснити власність буферів: хто виділяє `pbuf` чи `net_buf`, хто звільняє, що відбувається при вичерпанні пулу.
- Розміщення TLS: між TCP і прикладним протоколом; у lwIP це шар `altcp`, що прозоро обгортає TCP.[^lwip-overview]
- Типові дефекти: виклик `tcp_write()` з ISR, один control block у кількох потоках без блокування, робота з сокетами до отримання IP-адреси.
