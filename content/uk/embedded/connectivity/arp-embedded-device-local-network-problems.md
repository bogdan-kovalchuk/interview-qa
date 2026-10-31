---
id: emb-conn-0008
title: "Що таке ARP і коли embedded-пристрій реально стикається з ARP-проблемами у локальній мережі?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: rfc-826-arp
    title: "RFC 826: An Ethernet Address Resolution Protocol"
    url: https://www.rfc-editor.org/rfc/rfc826.html
  - source_id: rfc-1122-host-requirements
    title: "RFC 1122: Requirements for Internet Hosts – Communication Layers"
    url: https://www.rfc-editor.org/rfc/rfc1122.html
  - source_id: lwip-opts-arp
    title: "lwIP 2.1.0: ARP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__arp.html
  - source_id: linux-man-arp
    title: "arp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/arp.7.html
  - source_id: rfc-5227-ipv4-acd
    title: "RFC 5227: IPv4 Address Conflict Detection"
    url: https://www.rfc-editor.org/rfc/rfc5227.html
  - source_id: esp-idf-kconfig-lwip
    title: "ESP-IDF Programming Guide: Project Configuration (LWIP options)"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html
  - source_id: rfc-2131-dhcp
    title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: https://www.rfc-editor.org/rfc/rfc2131.html
---

## Short answer

**ARP** зіставляє IPv4 address з MAC address у локальному Ethernet/Wi-Fi сегменті. Embedded device стикається з ARP при першому connect до gateway/peer, IP conflict, stale ARP cache, link flap або sleep/wake сценаріях. Симптоми: ping не проходить у LAN, перший packet губиться, після зміни IP/MAC потрібен gratuitous ARP.[^dou-embedded-interview]

## Detailed explanation

### Механізм

Щоб передати IPv4-пакет у Ethernet або Wi-Fi, стек мусить знати MAC-адресу наступного вузла на тому самому сегменті. Якщо адресат поза підмережею, наступний вузол – шлюз, тож пристрій, що говорить із хмарою, розв’язує через ARP адресу роутера, а не сервера. ARP request розсилається широкомовно і містить шукану protocol address; вузол, що впізнав свою адресу, міняє місцями поля відправника й адресата, ставить код REPLY і надсилає відповідь прямо запитувачу. Алгоритм прийому RFC 826 також оновлює наявний запис, якщо відправник уже є в таблиці, і додає новий, якщо отримувач сам є адресатом запиту.[^rfc-826-arp] Ніякої автентифікації в цьому алгоритмі немає: будь-хто в сегменті може надіслати пакет, який перепише запис у таблиці, і на цьому побудовано ARP spoofing.

### Кеш і його правила

RFC 1122 вимагає від хоста механізму видалення застарілих записів (бажано з налаштовуваним тайм-аутом) і захисту від ARP flooding: рекомендовано не більше одного запиту на секунду для однієї адреси. Він також рекомендує (SHOULD) зберігати щонайменше один, останній, пакет для кожної ще не розв’язаної адреси й відправляти його після відповіді; інакше губиться перший пакет кожного обміну, що особливо боляче для UDP-протоколів на кшталт DNS.[^rfc-1122-host-requirements]

Конкретні стеки реалізують це по-різному:

- **lwIP** за замовчуванням має таблицю на 10 записів (`ARP_TABLE_SIZE`), запис живе 300 тиків таймера ARP, тобто 5 хвилин при інтервалі 1 s (`ARP_MAXAGE`), а з `ARP_QUEUEING = 0` у черзі на розв’язання тримається лише найсвіжіший пакет для кожної IP-адреси. Статичні записи доступні лише з `ETHARP_SUPPORT_STATIC_ENTRIES`.[^lwip-opts-arp]
- **Linux** вважає запис дійсним випадковий час між половиною і півтора `base_reachable_time` (за замовчуванням 30 s); позитивний сигнал від вищих рівнів, наприклад TCP ACK, подовжує його. Застарілий запис перевіряється спочатку unicast-запитами (`ucast_solicit`, 3), а потім широкомовним запитом; для нерозв’язаної адреси в черзі чекають до 3 пакетів (`unres_qlen`).[^linux-man-arp]

### Де embedded-пристрій справді натрапляє на ARP

**Втрата першого пакета.** Пристрій прокинувся, кеш порожній, firmware швидко надсилає кілька UDP-датаграм на той самий адресат. Поки ARP не розв’язаний, lwIP із налаштуваннями за замовчуванням тримає лише останній пакет, тож попередні зникають.[^lwip-opts-arp] Симптом: «після старту перше повідомлення губиться, далі все працює». Ліки: прикладне підтвердження, увімкнений `ARP_QUEUEING` або попереднє розв’язання адреси шлюзу.

**Мала таблиця.** Шлюз Modbus TCP, що опитує 20 пристроїв у локальній мережі, при таблиці на 10 записів постійно витісняє записи, і частина опитувань щоразу починається з ARP-обміну. Це виглядає як нерегулярні стрибки латентності без жодних помилок у логах.

**Застарілий запис після заміни обладнання.** Контролер замінили новим із тією самою IP-адресою, але іншим MAC. Сусіди продовжують слати кадри на старий MAC, доки запис не застаріє; у lwIP це до 5 хвилин. Рішення описує RFC 5227: після перевірки адреси хост зобов’язаний розіслати дві ARP Announcement (`ANNOUNCE_NUM = 2`), у яких і sender, і target IP дорівнюють його новій адресі, саме для того, щоб в інших хостів не лишилося застарілих записів.[^rfc-5227-ipv4-acd]

**Застарілий запис у точці доступу.** ESP-IDF за замовчуванням періодично (раз на 60 s) надсилає gratuitous ARP. Документація пояснює причину: якщо ARP-таблиця точки доступу застаріла, а сама точка не надсилає ARP-запит для оновлення, пакети станції перестають доходити.[^esp-idf-kconfig-lwip]

**Конфлікт адрес.** Два пристрої з однаковою статичною адресою дають «плаваючі» відмови: відповідає то один, то інший. RFC 5227 вимагає ARP Probe (з нульовою sender IP, щоб не забруднити чужі кеші) при старті інтерфейсу, після пробудження зі сну, при зміні стану лінку і після асоціації Wi-Fi з новою точкою доступу, але забороняє робити це періодично.[^rfc-5227-ipv4-acd] DHCP-клієнт теж повинен (SHOULD) перевірити отриману адресу через ARP.[^rfc-2131-dhcp]

**Енергоощадний Wi-Fi.** ARP request – широкомовний кадр. Станція в режимі глибокого енергозбереження, що прокидається рідше за DTIM, може пропускати broadcast, і тоді сусіди не можуть розв’язати її адресу, хоча сама вона назовні надсилає дані без проблем (див. qid:emb-conn-0007).

### Як діагностувати

- Захопити трафік і відфільтрувати ARP: чи є відповідь, чи не відповідають на одну IP два різні MAC.
- Подивитися таблицю на самому пристрої (у lwIP – через статистику та налагоджувальний вивід etharp) і на сусідньому Linux-хості.
- Перевірити, чи збігається симптом із пробудженням, зміною точки доступу або заміною обладнання.

Інтерв’юер очікує почути не визначення ARP, а саме ці сценарії: перший пакет, розмір і тайм-аут кешу, gratuitous ARP і ARP Probe, broadcast у режимах енергозбереження і відсутність автентифікації.
