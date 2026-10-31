---
id: emb-conn-0005
title: "Як працює BLE з погляду embedded firmware: advertising interval, connection parameters, GATT і power budget?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-core-hci
    title: "Bluetooth Core Specification 6.0, Vol 4 Part E: Host Controller Interface Functional Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host-controller-interface/host-controller-interface-functional-specification.html
  - source_id: bt-core-gap
    title: "Bluetooth Core Specification 6.0, Vol 3 Part C: Generic Access Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-access-profile.html
  - source_id: bt-core-att
    title: "Bluetooth Core Specification 6.0, Vol 3 Part F: Attribute Protocol"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/attribute-protocol--att-.html
  - source_id: bt-core-architecture
    title: "Bluetooth Core Specification 6.0, Vol 1 Part A: Architecture"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/architecture,-change-history,-and-conventions/architecture.html
  - source_id: bt-core-gatt
    title: "Bluetooth Core Specification 6.0, Vol 3 Part G: Generic Attribute Profile"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/host/generic-attribute-profile--gatt-.html
---

## Short answer

У BLE device рекламується з **advertising interval**, після connection працює з negotiated connection interval, latency і supervision timeout. **GATT** описує services/characteristics для даних і команд. Power budget сильно залежить від radio wakeups, payload size, connection parameters, sleep states і того, чи firmware вчасно повертає MCU у low power.[^dou-embedded-interview]

## Detailed explanation

### Модель споживання

BLE економний не тому, що радіо споживає мало під час роботи, а тому, що воно працює короткими подіями: advertising event або connection event, а між ними радіо і, в ідеалі, MCU сплять. Тому середній струм пристрою з достатньою точністю описується так:

```text
I_avg ≈ I_sleep + Q_event / T_event + (робота MCU поза радіоподіями)
```

де `Q_event` – заряд, витрачений на одну подію (пробудження, стабілізація генератора, прийом і передавання), а `T_event` – фактичний період подій. Умовний приклад: якщо подія коштує 10 µC, а відбувається кожні 100 ms, це додає 100 µA до струму сну; якщо та сама подія відбувається раз на 500 ms – лише 20 µA. Реальне значення `Q_event` треба брати з документації конкретного чипа або вимірювати, але сама формула показує головне: firmware керує енергією насамперед через частоту подій, а не через розмір пакета.

### Advertising interval

Між початками advertising events минає `advInterval + advDelay`: `advInterval` кратний 0,625 ms і не менший за 20 ms, а `advDelay` – псевдовипадкові 0–10 ms для кожної події.[^bt-core-link-layer] Для legacy advertising HCI дозволяє інтервал 20 ms – 10,24 s (за замовчуванням 1,28 s), а карта каналів за замовчуванням вмикає всі три advertising-канали 37, 38 і 39, тобто одна подія – це до трьох передавань.[^bt-core-hci]

Компроміс простий: короткий інтервал дає швидке виявлення і з’єднання, довгий – менше споживання. Поширена тактика – часто рекламуватися короткий час після увімкнення або натискання кнопки, а потім переходити на рідкісний advertising. Якщо пристрій лише транслює значення (маячок, датчик), з’єднання може взагалі не знадобитися: дані йдуть у non-connectable advertising, але для legacy advertising їх не більше 31 байта, і доставка не підтверджується.[^bt-core-hci][^bt-core-gap]

### Параметри з’єднання

Після з’єднання ритм задають три параметри Link Layer:[^bt-core-link-layer]

- `connInterval` – кратний 1,25 ms, у межах 7,5 ms – 4,0 s;
- `connPeripheralLatency` – скільки connection events Peripheral має право пропустити, якщо їй нічого надсилати; при цьому `connSubrateFactor × (latency + 1)` не більше 500, а `connInterval × connSubrateFactor × (latency + 1)` менше за половину supervision timeout;
- `connSupervisionTimeout` – кратний 10 ms, у межах 100 ms – 32 s, і більший за `(1 + latency) × connSubrateFactor × connInterval × 2`; якщо за цей час не прийшов жоден коректний пакет, з’єднання вважається втраченим.

Приклад без subrating (`connSubrateFactor = 1`): `connInterval` 100 ms і latency 4 дозволяють Peripheral слухати лише кожну п’яту подію, тобто раз на 500 ms, коли вона простоює. Supervision timeout тоді мусить бути більшим за `5 × 100 ms × 2 = 1000 ms`; 2 s – розумне значення із запасом. Ціна – затримка команд від Central: до 500 ms, поки Peripheral не прокинеться. Пропускати події – це право, а не обов’язок Peripheral, тож щойно в неї з’являються дані, вона може вийти на найближчу подію.[^bt-core-link-layer]

Хто вирішує: параметри першим обирає Central у `CONNECT_IND` у межах, заданих її host, а змінюються вони процедурами Connection Update або Connection Parameters Request.[^bt-core-link-layer] Peripheral може повідомити бажані значення через характеристику Peripheral Preferred Connection Parameters, доступну лише для читання, і запросити оновлення, але Central не зобов’язана погодитися.[^bt-core-gap] Firmware має працювати коректно з будь-якими параметрами, які їй нав’язали.

### Скільки даних за одну подію

- Корисне навантаження LL data PDU – щонайменше 27 октетів і до 251 октету, якщо обидва боки домовилися про більшу довжину.[^bt-core-link-layer]
- ATT_MTU за замовчуванням 23, тож одна notification несе до 20 байтів значення (`ATT_MTU - 3`); більший MTU погоджується обміном `ATT_EXCHANGE_MTU`.[^bt-core-att]
- Біт MD дозволяє передати кілька пакетів в одній connection event, не чекаючи наступної.[^bt-core-link-layer]
- LE 2M PHY має бітову швидкість 2 Mb/s проти 1 Mb/s у LE 1M, тобто той самий пакет займає ефір приблизно вдвічі коротше; LE Coded PHY (500 або 125 kb/s) додає кодування з корекцією помилок, що підвищує стійкість зв’язку ціною приблизно у 2–8 разів довшого (2 або 8 символів на біт) ефірного часу.[^bt-core-architecture]

Звідси практичне правило для телеметрії: накопичувати вимірювання в буфері і надсилати рідше, але більшими порціями. Кожне пробудження має фіксовану вартість, а додаткові байти в тій самій події коштують відносно мало.

### GATT-рішення, що впливають на енергію

- **Notify чи Indicate.** Для notifications немає flow control, їх можна надсилати будь-коли. Indications послідовні: наступну можна надіслати тому самому клієнту лише після confirmation попередньої, тож їхній темп обмежений часом повного обміну indication-confirmation.[^bt-core-att] Для потокової телеметрії – notify, для рідкісних критичних подій – indicate.
- **CCCD для bonded-пристроїв** має зберігатися між з’єднаннями, а для не-bonded скидається до значення за замовчуванням при кожному з’єднанні.[^bt-core-gatt] Firmware, яка забуває підписку після перезавантаження, змушує телефон зайвий раз виконувати discovery і запис.
- **Розмір характеристики** узгоджують із MTU, щоб уникати довгих операцій читання частинами.

### Що робить сама firmware

Контролер BLE сам планує події, але середній струм часто зіпсовано не радіо, а MCU: опитування в циклі замість очікування подій, таймери, що прокидаються частіше за connection interval, увімкнений UART для логів, периферія, яка не дає зайти в глибокий сон, довга обробка в callback-ах стека. На співбесіді сильна відповідь закінчується методикою: виміряти середній струм за довгий інтервал (наприклад, профайлером живлення), розкласти його на сон, advertising, connection events і активну роботу MCU, і тільки потім змінювати параметри. Протокольні основи – ролі, advertising PDU, ATT і GATT – розібрано в qid:emb-conn-0003.
