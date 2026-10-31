---
id: emb-conn-0006
title: "Чим Bluetooth Classic відрізняється від BLE за профілями, throughput, latency і power consumption?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: bt-core-architecture
    title: "Bluetooth Core Specification 6.0, Vol 1 Part A: Architecture"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/architecture,-change-history,-and-conventions/architecture.html
  - source_id: esp-idf-bt-overview
    title: "ESP-IDF Programming Guide: Bluetooth Architecture Overview"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/bt-architecture/overview.html
  - source_id: bt-core-link-layer
    title: "Bluetooth Core Specification 6.0, Vol 6 Part B: Link Layer Specification"
    url: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-60/out/en/low-energy-controller/link-layer-specification.html
  - source_id: bt-spp
    title: "Bluetooth SIG: Serial Port Profile 1.2"
    url: https://www.bluetooth.com/specifications/specs/serial-port-profile-1-2/
  - source_id: bt-a2dp
    title: "Bluetooth SIG: Advanced Audio Distribution Profile 1.4"
    url: https://www.bluetooth.com/specifications/specs/advanced-audio-distribution-profile-1-4/
  - source_id: bt-le-audio
    title: "Bluetooth SIG: LE Audio"
    url: https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/
---

## Short answer

**Bluetooth Classic** орієнтований на постійніші з’єднання і профілі на кшталт audio/serial, часто з вищим throughput і більшим power cost. **BLE** оптимізований для коротких подій, advertising, GATT data model і низьке споживання. Для sensors/control BLE зазвичай кращий, для audio або legacy SPP частіше потрібен Classic.[^dou-embedded-interview]

## Detailed explanation

### Дві радіосистеми в одній специфікації

Специфікація Bluetooth Core описує дві окремі системи: Basic Rate з необов’язковим розширенням Enhanced Data Rate (BR/EDR, у побуті «Bluetooth Classic») і Low Energy (LE). Вони працюють в одному діапазоні 2,4 GHz, але мають різні фізичні рівні, канали, процедури з’єднання і протоколи верхнього рівня. Пристрій, що реалізує обидві системи (dual-mode), може спілкуватися і з такими самими пристроями, і з пристроями лише однієї системи; деякі профілі та сценарії підтримує тільки одна з систем.[^bt-core-architecture] Звідси практичний наслідок: LE-only пристрій не з’єднається з BR/EDR-only пристроєм, і сумісність між ними можлива лише через dual-mode пристрій.

Це видно і на рівні чипів. В ESP-IDF, наприклад, оригінальний ESP32 підтримує обидва режими, а ESP32-S3, ESP32-C3, ESP32-C6, ESP32-H2 та інші нові серії – лише Bluetooth LE.[^esp-idf-bt-overview] Вимога «потрібен SPP або A2DP» одразу звужує вибір мікроконтролера.

### Фізичний рівень і доступ до каналу

BR/EDR стрибає по 79 радіоканалах (або меншому набору при Adaptive Frequency Hopping) зі стандартною швидкістю 1600 стрибків на секунду; пристрої утворюють piconet, у якому Central задає годинник і послідовність стрибків, а Peripherals синхронізуються з нею.[^bt-core-architecture] Символьна швидкість 1 Msym/s дає 1 Mb/s у режимі Basic Rate, а EDR підвищує валову ефірну швидкість до 2 або 3 Mb/s.[^bt-core-architecture]

LE використовує 40 каналів: три primary advertising-канали для виявлення і legacy advertising і 37 каналів загального призначення для даних.[^bt-core-link-layer] Обов’язковий PHY – LE 1M (1 Mb/s); необов’язкові – LE 2M (2 Mb/s) і LE Coded з корекцією помилок (500 або 125 kb/s).[^bt-core-architecture] Виявлення в LE – це advertising і scanning, а не процедури inquiry і page, як у BR/EDR.

### Профілі

У Classic дані йдуть через профілі, побудовані поверх L2CAP, RFCOMM і SDP. Serial Port Profile емулює послідовний кабель поверх RFCOMM[^bt-spp], A2DP описує розподіл високоякісного аудіо[^bt-a2dp].

LE майже всі прикладні дані описує через GATT: сервіси, характеристики і дескриптори поверх ATT. Аудіо в LE теж є: LE Audio працює на радіо Bluetooth Low Energy, використовує кодек LC3, додає підтримку слухових апаратів і широкомовне аудіо Auracast; аудіо на радіо Classic Bluetooth SIG називає Classic Audio.[^bt-le-audio] Специфікація LE включає для цього ізохронний транспорт, як зі з’єднанням, так і без нього.[^bt-core-architecture] Отже, «аудіо – тільки Classic» вже неточно: Classic потрібен там, де протилежний бік підтримує лише Classic Audio, а LE Audio вимагає підтримки з обох боків.

### Throughput

Специфікація наводить для BR/EDR швидкості передавання даних 721,2 kb/s для Basic Rate і 2,1 Mb/s для EDR.[^bt-core-architecture] Для LE ефірна швидкість 1 або 2 Mb/s, але корисна пропускна здатність застосунку помітно нижча: вона залежить від розміру LL-пакета (корисне навантаження до 251 октету замість мінімальних 27)[^bt-core-link-layer], ATT_MTU, кількості пакетів у connection event, connection interval і того, чи підтримує це все другий бік. Тому на співбесіді краще не називати одне число для BLE, а пояснити, від чого воно залежить.

### Latency

У LE затримка даних визначається connection interval (від 7,5 ms до 4 s) і Peripheral latency, а затримка встановлення з’єднання – advertising interval і вікном сканування Central.[^bt-core-link-layer] Обидва параметри firmware обирає під задачу. Для потокового аудіо в Classic є синхронні з’єднання, а в LE – ізохронні канали; обидва механізми передають дані за регулярним розкладом, а не за принципом «надіслати, коли є дані».[^bt-core-architecture]

### Power consumption

Специфікація прямо формулює мету LE: продукти з нижчим споживанням, меншою складністю і вартістю, ніж BR/EDR, для сценаріїв із нижчими швидкостями даних і нижчим duty cycle.[^bt-core-architecture] Енергоощадність LE походить із короткого ефірного часу: радіо прокидається лише на advertising і connection events, а connection interval може бути секундами. У BR/EDR теж є режими зниження активності, наприклад sniff mode, але саме LE специфікація позиціонує для сценаріїв із низьким duty cycle.

### Як обирати

| Задача | Вибір |
|---|---|
| Датчик, носимий пристрій, керування з телефону, маячок | BLE (GATT, advertising) |
| Аудіо до гарнітур і автомобілів, що підтримують лише Classic Audio | Classic (A2DP і голосові профілі) |
| Нове аудіо, слухові апарати, broadcast | LE Audio, якщо обидва боки підтримують |
| Заміна кабелю для старого обладнання з SPP | Classic SPP |
| Пристрій мусить працювати з обома світами | dual-mode контролер |

Сильна відповідь на співбесіді не зводиться до «BLE повільніший, але економніший»: це дві різні системи з різними профілями, а вибір визначається тим, які профілі підтримує протилежний бік, який профіль трафіку (потік чи рідкісні пакети) і який чип узагалі доступний.
