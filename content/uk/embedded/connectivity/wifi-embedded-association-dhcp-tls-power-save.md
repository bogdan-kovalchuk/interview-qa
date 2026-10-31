---
id: emb-conn-0007
title: "Як працює Wi-Fi на embedded-пристрої і які наслідки мають association, DHCP, TLS і power save modes?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: esp-idf-wifi-station
    title: "ESP-IDF Programming Guide: Wi-Fi Driver, Station Scenarios"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/wifi-driver/station-scenarios.html
  - source_id: rfc-2131-dhcp
    title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: https://www.rfc-editor.org/rfc/rfc2131.html
  - source_id: rfc-8446-tls13
    title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: https://www.rfc-editor.org/rfc/rfc8446.html
  - source_id: rfc-5280-x509
    title: "RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile"
    url: https://www.rfc-editor.org/rfc/rfc5280.html
  - source_id: rfc-8449-record-size-limit
    title: "RFC 8449: Record Size Limit Extension for TLS"
    url: https://www.rfc-editor.org/rfc/rfc8449.html
  - source_id: esp-idf-wifi-power
    title: "ESP-IDF Programming Guide: Wi-Fi Driver, Performance and Power Save"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/wifi-driver/wifi-performance-and-power-save.html
  - source_id: rfc-826-arp
    title: "RFC 826: An Ethernet Address Resolution Protocol"
    url: https://www.rfc-editor.org/rfc/rfc826.html
---

## Short answer

Embedded Wi-Fi проходить scan/auth/association з AP, потім отримує IP через DHCP або static config. TLS додає CPU/RAM cost, certificates, entropy і довгі handshakes, що важливо для small MCU. Power save modes зменшують споживання, але додають latency, buffering у AP і складніші reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

### Від увімкнення до першого сокета

Шлях Wi-Fi-станції до робочої мережі складається з кількох послідовних фаз, і кожна може завершитися помилкою зі своєю причиною. ESP-IDF документує цей шлях детально, тому зручно розглянути його як конкретний приклад:[^esp-idf-wifi-station]

1. **Scan.** Драйвер переходить по каналах; при активному скануванні надсилає probe request, при пасивному чекає beacon. Кількість каналів залежить від налаштованого country code. Для явного скану через `esp_wifi_scan_start()` час на канал за замовчуванням 120 ms, а поля SSID, BSSID і channel дозволяють звузити скан до однієї точки доступу або одного каналу.
2. **Authentication.** Станція надсилає authentication request і запускає таймер; без відповіді виникає `WIFI_EVENT_STA_DISCONNECTED` з причиною `WIFI_REASON_AUTH_EXPIRE`, при відмові – `WIFI_REASON_AUTH_FAIL`.
3. **Association.** Аналогічно: запит, таймер, відповідь точки доступу.
4. **Four-way handshake.** Обмін EAPOL-повідомленнями 1/4–4/4, у якому узгоджуються ключі шифрування; якщо чергове повідомлення не прийшло вчасно, причина відключення – `WIFI_REASON_HANDSHAKE_TIMEOUT`. Лише після цього генерується `WIFI_EVENT_STA_CONNECTED`.
5. **DHCP.** Після `STA_CONNECTED` запускається DHCP-клієнт, і лише після отримання адреси приходить `IP_EVENT_STA_GOT_IP`. Документація окремо називає типовою помилкою створення сокетів до цієї події.

Умовний приклад бюджету: повний активний скан 13 каналів по 120 ms – це вже близько 1,56 s до першого кадру автентифікації. Тому пристрої, що часто прокидаються, зберігають канал і BSSID останньої точки доступу.

Не менш важливий зворотний шлях. Коли з’єднання рветься (точку доступу вимкнули, сигнал впав), драйвер повідомляє lwIP, і той прибирає всі UDP/TCP-з’єднання, тож усі сокети застосунку стають непрацездатними. Рекомендовані дії: знову викликати `esp_wifi_connect()`, закрити всі сокети і створити їх заново. Якщо змінилася IP-адреса, `IP_EVENT_STA_GOT_IP` приходить із прапорцем `ip_change`, і сокети теж слід перестворити.[^esp-idf-wifi-station] Firmware, яка вміє лише «підключитися при старті», у полі довго не проживе: потрібна явна машина станів reconnect.

### DHCP: оренда, а не назавжди

DHCP видає адресу в оренду. Клієнт має два таймери: T1 (за замовчуванням половина терміну оренди), після якого він просить продовження в сервера, що видав адресу, і T2 (0,875 терміну), після якого звертається до будь-якого сервера. Після отримання адреси клієнт за RFC повинен (SHOULD) перевірити її ARP-запитом, щоб виявити конфлікт. Пристрій, що вже мав адресу, може в стані INIT-REBOOT попросити ту саму адресу знову, що скорочує обмін після перезавантаження.[^rfc-2131-dhcp]

Для embedded це означає: таймери оренди мають працювати і під час енергоощадних режимів; пристрій, що спав довше за термін оренди, мусить пройти DHCP повністю; статична адреса прибирає DHCP із шляху підключення, але переносить відповідальність за унікальність адреси на конфігурацію мережі.

### TLS: дорогий не трафік, а підготовка

- **Випадковість.** TLS вимагає криптографічно стійкого генератора псевдовипадкових чисел (CSPRNG).[^rfc-8446-tls13] На MCU це означає апаратне джерело ентропії і правильно засіяний DRBG, а не `rand()`.
- **Час.** Сертифікат має період дійсності між датами notBefore і notAfter.[^rfc-5280-x509] Пристрій без RTC після холодного старту не знає дати, тож перевірка сертифіката або неможлива, або тихо вимкнена. Типове рішення – SNTP до TLS і продумана поведінка, якщо час ще невідомий.
- **Пам’ять.** Запис TLS може нести до 2^14 байтів відкритих даних.[^rfc-8446-tls13] AEAD-шифр вимагає наявності всього запису, щоб розшифрувати й автентифікувати його, а до 18K пам’яті під шифротекст – більше, ніж можуть собі дозволити деякі реалізації. Для обмежених пристроїв призначене розширення `record_size_limit`, яке замінює застаріле `max_fragment_length`.[^rfc-8449-record-size-limit] Без нього RAM потрібно планувати під повний запис.
- **Handshake.** TLS 1.3 виконує повний handshake за один round trip, а з PSK-відновленням сесії дозволяє 0-RTT early data. Але 0-RTT дані не мають forward secrecy і не захищені від повторення між з’єднаннями[^rfc-8446-tls13], тож команди керування в 0-RTT надсилати не можна. Відновлення сесії через PSK корисне і без 0-RTT, бо дозволяє уникнути частини асиметричної криптографії при кожному перепідключенні.

### Power save: споживання проти затримки

У ESP-IDF станція, з’єднана з точкою доступу, може працювати в Modem-sleep. У мінімальному режимі (`WIFI_PS_MIN_MODEM`, за замовчуванням) вона прокидається на кожен DTIM, щоб прийняти beacon; broadcast-дані не губляться, бо точка доступу надсилає їх після DTIM. У максимальному режимі (`WIFI_PS_MAX_MODEM`) станція прокидається раз на listen interval, який може бути довшим за період DTIM, тож broadcast-дані можуть губитися. `WIFI_PS_NONE` вимикає Modem-sleep: споживання вище, затримка прийому мінімальна. З увімкненим Modem-sleep затримка прийому може сягати періоду DTIM або listen interval.[^esp-idf-wifi-power]

Наслідки, які варто назвати: команди з хмари приходять із додатковою затримкою до періоду DTIM або listen interval; втрата broadcast у максимальному режимі зачіпає ARP-запити, які надсилаються широкомовно[^rfc-826-arp], тож пристрій може періодично ставати «невидимим» у локальній мережі (див. qid:emb-conn-0008). Для пристрою, що надсилає дані раз на години, альтернатива – deep sleep між сеансами, але тоді кожен сеанс оплачує повний цикл: скан, автентифікацію, асоціацію, four-way handshake, DHCP і TLS. Що вигідніше – тримати з’єднання в Modem-sleep чи щоразу підключатися заново – вирішує лише вимірювання енергії одного повного сеансу проти струму в режимі утримання з’єднання.
