---
id: emb-conn-0012
title: "Що стоїть між network interface і MCU: PHY, MAC, transceiver, controller, DMA і driver stack?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-phy-abstraction
    title: "Linux kernel documentation: PHY Abstraction Layer"
    url: https://docs.kernel.org/networking/phy.html
  - source_id: linux-dma-api-howto
    title: "Linux kernel documentation: Dynamic DMA mapping Guide"
    url: https://docs.kernel.org/core-api/dma-api-howto.html
  - source_id: ti-dp83848c-datasheet
    title: "TI DP83848C PHYTER Single Port 10/100 Mb/s Ethernet Physical Layer Transceiver"
    url: https://www.ti.com/lit/ds/symlink/dp83848c.pdf
  - source_id: ti-sloa101-can
    title: "TI SLOA101B: Introduction to the Controller Area Network (CAN)"
    url: https://www.ti.com/lit/an/sloa101b/sloa101b.pdf
---

## Short answer

Physical medium обслуговує **PHY/transceiver**, який перетворює electrical/radio signals у digital link signals. **MAC/controller** формує frames, filters, interrupts і часто працює з DMA descriptors у RAM. Driver stack ініціалізує hardware, керує buffers/cache coherency, обробляє IRQ і передає packets у TCP/IP або fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

### Шари від дроту до мережевого стеку

Між кабелем і кодом застосунку стоїть кілька апаратних і програмних блоків, і на співбесіді важливо чітко розділяти їхні відповідальності.

| Блок | Що робить | Типовий приклад |
|---|---|---|
| PHY / transceiver | електричні рівні, кодування на лінії, узгодження параметрів link | окремий Ethernet PHY, CAN transceiver |
| MAC / controller | кадри, CRC, фільтрація адрес, доступ до середовища, DMA | Ethernet MAC або CAN controller усередині MCU |
| DMA і дескриптори | переносять кадри між MAC і RAM без участі CPU | кільце дескрипторів у RAM |
| driver | ініціалізація, IRQ, буфери, стан link | Ethernet driver RTOS або Linux |
| network stack | IP, ARP, TCP/UDP, сокети | lwIP, Zephyr net, Linux |

Документація ядра Linux описує це розділення так: мережевий пристрій – це набір регістрів, що дає інтерфейс до рівня MAC, а MAC спілкується з фізичним з’єднанням через PHY. PHY узгоджує параметри link з партнером на іншому кінці кабелю і через регістри показує драйверу, що саме узгоджено.[^linux-phy-abstraction]

Для CAN поділ аналогічний: протокол ISO 11898 описує data-link і physical signaling, які реалізує CAN controller (кадри, арбітраж, лічильники помилок), а підключення до фізичної лінії CANH/CANL виконує окремий line transceiver. Приклад TI – DSP із вбудованим CAN controller плюс transceiver SN65HVD230.[^ti-sloa101-can] Тобто "transceiver" у CAN, RS-485 чи Ethernet – це аналогова частина, яка не знає про кадри, а "controller" – цифрова логіка протоколу.

### Інтерфейс MAC–PHY і шина керування

У Ethernet між MAC і PHY є два окремі інтерфейси:

- **Дані: MII, RMII, RGMII.** Наприклад, PHY DP83848C у режимі MII передає дані по 4 біти (nibble) синхронно з тактом 25 МГц для 100 Мбіт/с, а в RMII – по 2 біти синхронно з опорним тактом 50 МГц; у RMII такт MII не використовується.[^ti-dp83848c-datasheet] Арифметика сходиться: 4 біти × 25 МГц = 2 біти × 50 МГц = 100 Мбіт/с. RGMII для гігабіта – це 12-контактний інтерфейс із тактом 125 МГц, і між тактом та даними потрібна затримка 1,5–2 нс, яку вносить PHY, MAC або трасування на платі.[^linux-phy-abstraction]
- **Керування: MDC/MDIO.** Через цю послідовну шину драйвер читає й пише регістри PHY: ID, стан link, результат auto-negotiation. У DP83848C максимальна частота MDC – 25 МГц, а auto-negotiation відповідає IEEE 802.3.[^ti-dp83848c-datasheet] Адреса PHY на шині та частина режимів задаються strap-виводами, значення яких PHY зчитує під час reset; ці виводи після reset мають іншу функцію, тому їх підтягують резисторами, а не підключають напряму до живлення.[^ti-dp83848c-datasheet]

Звідси класичні апаратно-програмні помилки. Неправильна адреса PHY або неініціалізований MDIO дає "PHY не знайдено". Невідповідність затримки RGMII, за документацією ядра, проявляється підступно: обмін частково працює з втратами пакетів, MAC фіксує помилки FCS/CRC або відкидає кадри, а на 10/100 Мбіт/с проблема зникає, бо там запас setup/hold більший.[^linux-phy-abstraction]

### DMA, дескриптори і когерентність кешу

MAC зазвичай не віддає кадри через регістр даних, а сам читає і пише RAM через вбудований DMA. Драйвер готує кільце дескрипторів: кожен містить адресу буфера, довжину, статус і ознаку того, кому зараз належить дескриптор – CPU чи DMA. Апаратура обробляє дескриптор, змінює статус, повертає його CPU і генерує переривання.

Linux Dynamic DMA mapping Guide дає дві моделі, які корисно знати і на bare-metal MCU:[^linux-dma-api-howto]

- **Coherent mapping** – для структур, де CPU і пристрій мають бачити записи одне одного без явного flush; перший приклад у документації – саме кільця DMA-дескрипторів мережевої карти. Навіть тут потрібні memory barriers: якщо пристрій має побачити адресу в дескрипторі раніше за прапорець "валідний", між записами ставлять `wmb()`.
- **Streaming mapping** – для мережевих буферів, які передаються пристрою на одну транзакцію. Між передачами буфер синхронізують явно: `dma_sync_single_for_cpu()` перед читанням CPU і `dma_sync_single_for_device()` перед поверненням пристрою.
- На системах, де кеш не когерентний з DMA, буфер, що ділить cache line з іншими даними, може бути пошкоджений.

```c
/* Linux driver: order of descriptor writes matters even in coherent memory */
desc->addr = buf_dma;
wmb();                    /* device must see addr before the valid flag */
desc->ctrl = DESC_VALID;
```

На MCU з data cache (наприклад, Cortex-M7) та сама проблема розв’язується вручну: clean кешу перед передачею TX-буфера, invalidate перед читанням RX-буфера, буфери вирівняні на розмір cache line, або дескриптори та буфери розміщені в некешованій області пам’яті. Симптом помилки – пакет "приходить", але CPU бачить у буфері старі дані.

### Driver stack і порядок ініціалізації

Типова послідовність: увімкнути тактування і pin mux, зняти reset з PHY і дочекатися стабілізації, знайти PHY на MDIO за адресою, запустити auto-negotiation, а після встановлення link налаштувати MAC на ту саму швидкість і duplex. У Linux це оформлено як PHY Abstraction Layer: драйвер MAC передає в `phy_connect()` callback `adjust_link`, який викликається при зміні стану link, а PAL запускає власну state machine і реєструє переривання PHY, якщо воно є.[^linux-phy-abstraction] У RTOS це часто робиться опитуванням регістра стану PHY з окремої задачі.

Далі драйвер обробляє IRQ завершення RX/TX і помилок, переносить основну роботу з ISR у task або bottom half, поповнює RX-кільце порожніми буферами і передає кадри в стек (lwIP, Zephyr net, Linux). Важливе рішення – копіювати кадр у буфер стеку чи передавати буфер без копіювання: zero-copy економить CPU, але прив’язує час життя буфера DMA до стеку.

### Що очікують почути на співбесіді

Кандидат має пояснити, де в конкретній системі проходять межі: MAC у SoC, PHY зовнішній; CAN controller у MCU, transceiver окремо; Wi-Fi-модуль часто має власний MAC і firmware, і MCU бачить лише командний інтерфейс. І вміти локалізувати симптом: немає link – PHY, живлення, магнітні елементи, strap; link є, але немає кадрів – режим MII/RMII/RGMII, такти, налаштування MAC; кадри з CRC-помилками – затримки RGMII або цілісність сигналу; кадри приходять, але дані старі – когерентність кешу і DMA.
