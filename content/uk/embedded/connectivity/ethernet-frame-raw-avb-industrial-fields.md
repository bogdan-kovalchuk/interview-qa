---
id: emb-conn-0010
title: "Що таке Ethernet frame і які поля важливі при роботі з raw Ethernet, AVB або industrial Ethernet?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-if-ether-h
    title: "Linux kernel source: include/uapi/linux/if_ether.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/if_ether.h
  - source_id: rfc-894-ip-over-ethernet
    title: "RFC 894: A Standard for the Transmission of IP Datagrams over Ethernet Networks"
    url: https://www.rfc-editor.org/rfc/rfc894.html
  - source_id: rfc-9542-ieee802-params
    title: "RFC 9542: IANA Considerations and IETF Protocol and Documentation Usage for IEEE 802 Parameters"
    url: https://www.rfc-editor.org/rfc/rfc9542.html
  - source_id: linux-if-vlan-h
    title: "Linux kernel source: include/linux/if_vlan.h"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/linux/if_vlan.h
  - source_id: linux-man-packet
    title: "packet(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/packet.7.html
  - source_id: lwip-opts-arp
    title: "lwIP 2.1.0: ARP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__arp.html
  - source_id: linux-man-tc-cbs
    title: "tc-cbs(8) – Linux manual page"
    url: https://man7.org/linux/man-pages/man8/tc-cbs.8.html
  - source_id: linux-man-tc-taprio
    title: "tc-taprio(8) – Linux manual page"
    url: https://man7.org/linux/man-pages/man8/tc-taprio.8.html
  - source_id: linux-timestamping
    title: "Linux kernel documentation: Timestamping"
    url: https://docs.kernel.org/networking/timestamping.html
---

## Short answer

**Ethernet frame** містить destination/source MAC, EtherType або length, payload і FCS; VLAN tag може додати priority/VID. Для raw Ethernet важливі MAC filtering, MTU, padding і EtherType. Для AVB/industrial Ethernet критичні timestamping, priority/QoS, deterministic latency і взаємодія MAC/PHY/driver.[^dou-embedded-interview]

## Detailed explanation

### Структура кадру в числах

Заголовок Ethernet-кадру – 14 байтів: MAC-адреса отримувача (6), MAC-адреса відправника (6) і поле типу (2), яке в Linux описане структурою `struct ethhdr`. Корисне навантаження – до 1500 байтів, мінімальний кадр без FCS – 60 байтів, максимальний без FCS – 1514, сама FCS (контрольна сума кадру) – 4 байти.[^linux-if-ether-h] Отже, на рівні MAC кадр має від 64 до 1518 байтів разом із FCS. Мінімальне поле даних – 46 байтів; коротший IP-пакет доповнюється нулями, і це доповнення не входить у довжину IP-пакета.[^rfc-894-ip-over-ethernet]

Поле типу має подвійне значення: число від 0x0600 і більше – це EtherType (ідентифікатор протоколу у payload), значення, менше за 0x05DD (тобто до 1500), означає довжину кадру IEEE 802.3 з LLC-заголовком.[^rfc-9542-ieee802-params] Для власних експериментальних протоколів IEEE виділяє EtherType 0x88B5 і 0x88B6.[^rfc-9542-ieee802-params] Поле типу передається в мережевому порядку байтів (у Linux воно оголошене як `__be16`).[^linux-if-ether-h]

У MAC-адресі важливі два біти першого октету. Наймолодший – Group bit: якщо він 1, адреса групова (multicast або broadcast). Наступний – universal/local bit: 0 означає глобально унікальну адресу виробника.[^rfc-9542-ieee802-params] Для raw-протоколів це практично важливо: адресу призначення часто роблять multicast, і MAC-фільтр контролера треба налаштувати, щоб такі кадри взагалі доходили до драйвера.

### VLAN-тег і пріоритет

Тег IEEE 802.1Q (EtherType 0x8100) вставляється після MAC-адрес і додає 4 байти; заголовок стає 18-байтовим, максимальний кадр без FCS – 1518 байтів, корисне навантаження так і лишається 1500. Двобайтове поле TCI містить 3-бітний Priority Code Point, біт DEI (раніше CFI) і 12-бітний VLAN ID, тобто 4096 значень.[^linux-if-vlan-h] Подвійне тегування 802.1ad використовує EtherType 0x88A8.[^linux-if-ether-h] Саме PCP переносить пріоритет кадру в AVB/TSN і промислових мережах, тож драйвер, який губить або не виставляє тег, ламає всю схему QoS.

### Raw Ethernet на практиці

У Linux кадри без IP надсилають і приймають через `AF_PACKET`. Для цього процесу потрібна capability `CAP_NET_RAW`. З `SOCK_RAW` кадр проходить до драйвера без змін, і буфер користувача має містити заголовок фізичного рівня; `SOCK_DGRAM` знімає заголовок на прийомі і будує його сам на передаванні. Опції `PACKET_MR_PROMISC` і `PACKET_MR_MULTICAST` вмикають promiscuous mode і приймання конкретної multicast-групи.[^linux-man-packet]

Мінімальна збірка кадру для `SOCK_RAW` виглядає так (буфер щонайменше `ETH_FRAME_LEN` байтів, `len` не більше `ETH_DATA_LEN`):

```c
#include <arpa/inet.h>      /* htons */
#include <linux/if_ether.h> /* struct ethhdr, ETH_ALEN, ETH_HLEN, ETH_ZLEN */
#include <stddef.h>
#include <string.h>

/* Builds a frame without FCS; returns the number of bytes to pass to send(). */
size_t build_frame(unsigned char *buf, const unsigned char dst[ETH_ALEN],
                   const unsigned char src[ETH_ALEN], unsigned short ethertype,
                   const void *payload, size_t len)
{
    struct ethhdr *h = (struct ethhdr *)buf;
    size_t total = ETH_HLEN + len;

    memcpy(h->h_dest, dst, ETH_ALEN);
    memcpy(h->h_source, src, ETH_ALEN);
    h->h_proto = htons(ethertype);
    memcpy(buf + ETH_HLEN, payload, len);
    if (total < ETH_ZLEN) {             /* pad up to the 60-byte minimum */
        memset(buf + total, 0, ETH_ZLEN - total);
        total = ETH_ZLEN;
    }
    return total;
}
```

На MCU без Linux ті самі поля обробляє драйвер MAC разом із DMA-дескрипторами. Корисна деталь з lwIP: через 14-байтовий заголовок IP-заголовок після нього не вирівняний на 32 біти, тому опція `ETH_PAD_SIZE = 2` додає два байти перед кадром у буфері і прискорює роботу на 32-бітних платформах.[^lwip-opts-arp] Перелік того, що перевіряють для raw Ethernet на MCU: хто доповнює короткі кадри (MAC апаратно чи драйвер), хто обчислює і знімає FCS, які адреси пропускає фільтр (точний чи hash-фільтр), чи драйвер не відкидає кадри з невідомим EtherType.

### AVB, TSN і промислові протоколи

Багато промислових і медійних протоколів працюють прямо поверх Ethernet, без IP, і розрізняються саме EtherType. У заголовку Linux, наприклад, зареєстровані: 0x22F0 – TSN (IEEE 1722), 0x88F7 – IEEE 1588 (PTP), 0x8892 – PROFINET, 0x88A4 – EtherCAT, 0x88FB і 0x892F – резервування PRP і HSR (IEC 62439-3), 0x88CC – LLDP.[^linux-if-ether-h] Для них критичні три речі.

**Пріоритети і формування трафіку.** Кадри з PCP відображаються на класи трафіку і апаратні черги. Credit-based shaper з IEEE 802.1Q у Linux реалізує qdisc `cbs`, призначений саме для TSN-застосунків; він встановлюється під qdisc, що відображає потоки на класи трафіку (наприклад, `mqprio`), і може бути винесений в апаратуру через параметр `offload`.[^linux-man-tc-cbs] Time-aware shaper реалізує qdisc `taprio`: циклічний розклад станів «воріт», кожен з яких дозволяє передавання лише певним класам трафіку, з прив’язкою до `base-time`.[^linux-man-tc-taprio] Обидва механізми мають сенс, лише якщо драйвер і MAC справді мають кілька черг.

**Мітки часу.** Синхронізація часу через PTP вимагає знати момент передавання і прийому кадру. Linux розрізняє програмні мітки, які драйвер ставить якомога ближче до передачі пакета мережевому інтерфейсу, і апаратні, які генерує сам мережевий адаптер; апаратні вмикаються окремою конфігурацією інтерфейсу з правами адміністратора.[^linux-timestamping] Програмна мітка включає джиттер стека і драйвера, тому для точної синхронізації потрібна апаратна підтримка в MAC або PHY.

**Детермінованість.** Затримку кадру формують черги, розміри DMA-кілець, групування переривань і затримка самого PHY. На співбесіді добре звучить відповідь, яка пов’язує поля кадру з апаратурою: EtherType визначає, кому драйвер віддасть кадр; PCP і VID визначають чергу і шейпер; адреса призначення визначає, чи пропустить кадр фільтр; а мітка часу має бути взята якомога ближче до дроту.
