---
id: emb-conn-0003
title: "Як працює BLE на рівні advertising, connection, GATT service і characteristic?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-gap
    title: "Bluetooth Core Specification 6.0, Vol 3 Part C: Generic Access Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-access-profile.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-core-hci
    title: "Bluetooth Core Specification 6.0, Vol 4 Part E: Host Controller Interface Functional Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host-controller-interface/host-controller-interface-functional-specification.html
  - source_id: bt-core-att
    title: "Bluetooth Core Specification 6.0, Vol 3 Part F: Attribute Protocol"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/attribute-protocol--att-.html
  - source_id: bt-core-gatt
    title: "Bluetooth Core Specification 6.0, Vol 3 Part G: Generic Attribute Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-attribute-profile--gatt-.html
---

## Short answer

BLE peripheral рекламує advertising packets з address, flags і optional service data, а central сканує й ініціює connection. Після connection data model зазвичай GATT: services групують characteristics, а characteristic має value і properties типу read/write/notify. Для low-power telemetry важливі connection interval, MTU, notification rate і sleep між events.[^dou-embedded-interview]

## Detailed explanation

### Ролі та радіоканали

GAP визначає для LE чотири ролі. Broadcaster лише надсилає advertising events (передавач обов’язковий, приймач – ні), Observer їх приймає, Peripheral приймає з’єднання, а Central ініціює встановлення LE-з’єднання.[^bt-core-gap] Діапазон 2,4 GHz поділено на 40 радіоканалів: три «primary advertising channels» використовуються для початкового advertising і всього legacy advertising, а решта 37 «general-purpose channels» – для більшості обміну, зокрема для даних у з’єднанні.[^bt-core-link-layer]

### Advertising

Пристрій в advertising state періодично виконує advertising event: у кожній події він передає PDU на primary-каналах. Інтервал між початками подій дорівнює `T_advEvent = advInterval + advDelay`, де `advInterval` кратний 0,625 ms і не менший за 20 ms, а `advDelay` – псевдовипадкова добавка 0–10 ms, яку Link Layer генерує заново для кожної події, щоб два пристрої з однаковим інтервалом не зіткнулися назавжди.[^bt-core-link-layer] Через HCI legacy-інтервал задається в діапазоні 20 ms – 10,24 s, за замовчуванням 1,28 s.[^bt-core-hci]

Legacy advertising PDU – це `ADV_IND` (connectable і scannable undirected), `ADV_DIRECT_IND`, `ADV_NONCONN_IND` і `ADV_SCAN_IND`; extended advertising (Bluetooth 5) додає `ADV_EXT_IND` на primary-каналі з вказівником на `AUX_ADV_IND` на secondary-каналі.[^bt-core-link-layer] Сканер в active scanning може надіслати `SCAN_REQ` на scannable advertising і отримати `SCAN_RSP` з додатковими даними. Для legacy advertising і advertising data, і scan response data обмежені 31 октетом кожне.[^bt-core-hci] Дані кодуються як послідовність AD-структур (Flags, імена, UUID сервісів, manufacturer data). У Broadcast mode пристрій не встановлює прапорці discoverable, а всі передані так дані вважаються ненадійними: підтвердження прийому немає.[^bt-core-gap]

### Встановлення з’єднання

Central, що перебуває в initiating state, відповідає на connectable advertising пакетом `CONNECT_IND` (або `AUX_CONNECT_REQ` для extended advertising). У ньому вже лежать параметри з’єднання: `connInterval = Interval × 1,25 ms`, `connPeripheralLatency = Latency`, `connSupervisionTimeout = Timeout × 10 ms`, а також карта каналів ChM, що позначає дозволені data-канали.[^bt-core-link-layer] Отже, параметри першим обирає Central; Peripheral може лише попросити інші значення пізніше.

Після цього обидва пристрої стрибають по data-каналах і зустрічаються в connection events. Початок події – anchor point; Central передає першим, Peripheral відповідає. Біт MD у заголовку пакета означає «маю ще дані»: якщо його не встановив жоден бік, подію закриває пакет Peripheral, інакше Central може продовжити обмін у тій самій події.[^bt-core-link-layer] Між подіями радіо обох пристроїв може спати – звідси енергоефективність BLE (детальніше про параметри та бюджет живлення – qid:emb-conn-0005).

### ATT: плоска база атрибутів

Над з’єднанням працює L2CAP, а над ним – Attribute Protocol. ATT-сервер експонує атрибути, кожен з яких має тип (UUID), handle і набір permissions, визначених вищим рівнем.[^bt-core-att] ATT_MTU – максимальний розмір ATT-пакета; для LE значення за замовчуванням 23 октети.[^bt-core-gatt] Клієнт може запропонувати більший MTU через `ATT_EXCHANGE_MTU_REQ`, і далі обидва боки використовують менше з двох значень.[^bt-core-att] Notification несе до `ATT_MTU-3` октетів значення, тобто 20 байтів при MTU 23; довше значення обрізається.[^bt-core-att] Максимальна довжина значення атрибута – 512 октетів.[^bt-core-att]

### GATT: сервіси, характеристики, дескриптори

GATT накладає ієрархію на плоский список атрибутів. Service – набір даних і пов’язаної поведінки для певної функції; він містить характеристики та, можливо, включені сервіси.[^bt-core-gatt] Characteristic складається з декларації, properties, значення і необов’язкових descriptors, що описують значення або налаштовують сервер.[^bt-core-gatt]

Основні properties: Read, Write Without Response, Write (з відповіддю), Notify і Indicate. Notify надсилає значення без підтвердження, Indicate – з підтвердженням; для обох сервер зобов’язаний мати Client Characteristic Configuration Descriptor (CCCD), і саме записом у нього (біт 0 – notification, біт 1 – indication) клієнт підписується.[^bt-core-gatt]

Важлива деталь, яку часто плутають: ролі GATT client і server не прив’язані до ролей GAP. Вони визначаються тим, хто ініціює процедуру, і пристрій може одночасно бути обома.[^bt-core-gatt] Типовий сенсор – GAP Peripheral і GATT server, але Peripheral цілком може бути й GATT client, наприклад читаючи час із телефону.

### Повний сценарій на прикладі сенсора

1. Сенсор надсилає `ADV_IND` з Flags і UUID свого сервісу.
2. Телефон (Central) сканує, знаходить UUID і відповідає `CONNECT_IND` зі своїми параметрами.
3. Клієнт обмінюється MTU, виконує service discovery і знаходить характеристику вимірювання з property Notify.
4. Клієнт записує біт notification у CCCD цієї характеристики.
5. Сенсор надсилає notification з новим значенням у найближчих connection events, а між ними спить.

На співбесіді очікують, що кандидат розрізнить рівні (Link Layer, ATT, GATT, GAP), пояснить, хто обирає параметри з’єднання, і чим Notify відрізняється від Indicate з погляду пропускної здатності та надійності.
