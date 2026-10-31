---
id: emb-safety-0002
title: "Що таке TLS для embedded-пристрою і які проблеми дають certificates, RAM і entropy source?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 – Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
  - source_id: rfc-8446-tls13
    title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: https://www.rfc-editor.org/rfc/rfc8446
  - source_id: rfc-5280-x509
    title: "RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile"
    url: https://www.rfc-editor.org/rfc/rfc5280
  - source_id: rfc-9525-service-identity
    title: "RFC 9525: Service Identity in TLS"
    url: https://www.rfc-editor.org/rfc/rfc9525
  - source_id: rfc-8449-record-size-limit
    title: "RFC 8449: Record Size Limit Extension for TLS"
    url: https://www.rfc-editor.org/rfc/rfc8449
  - source_id: rfc-6066-tls-extensions
    title: "RFC 6066: Transport Layer Security (TLS) Extensions: Extension Definitions"
    url: https://www.rfc-editor.org/rfc/rfc6066
  - source_id: esp-idf-mbedtls
    title: "ESP-IDF Programming Guide (ESP32): Mbed TLS"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/protocols/mbedtls.html
  - source_id: rfc-4086-randomness
    title: "RFC 4086: Randomness Requirements for Security"
    url: https://www.rfc-editor.org/rfc/rfc4086
  - source_id: esp-idf-random
    title: "ESP-IDF Programming Guide (ESP32): Random Number Generation"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/random.html
---

## Short answer

**TLS** шифрує transport, автентифікує server/client і захищає telemetry або firmware update від MITM. Проблеми embedded: certificate chain займає flash/RAM, handshake потребує buffers і crypto time, а ключі вимагають якісного entropy source/TRNG. <span class="warn">Без правильного time/certificate validation TLS може виглядати увімкненим, але не давати реальної автентифікації</span>.[^dou-embedded-interview]

## Detailed explanation

TLS (Transport Layer Security) – протокол, що дає клієнту й серверу змогу обмінюватися даними так, щоб запобігти підслуховуванню, зміні та підробці повідомлень; актуальна версія – TLS 1.3.[^rfc-8446-tls13] Для embedded-пристрою це стандартний спосіб захистити telemetry, команди керування й завантаження firmware update поверх TCP. Сам протокол той самий, що й на сервері; відрізняються обмеження: мало RAM і flash, повільна асиметрична криптографія, немає годинника реального часу і не завжди є якісне джерело випадковості.

### Що саме автентифікує TLS

Сервер надсилає ланцюжок сертифікатів (`certificate_list` у повідомленні Certificate).[^rfc-8446-tls13] Пристрій має перевірити, що ланцюжок веде до trust anchor, який зберігається в його flash (кореневий або проміжний CA), що жоден сертифікат не прострочений і що сертифікат виданий саме тому серверу, до якого пристрій підключається. Без цих перевірок шифрування є, а автентифікації немає: будь-хто посередині (MITM) може підставити власний сертифікат.

**Час.** Алгоритм перевірки шляху в RFC 5280 вимагає, щоб період дії сертифіката включав поточний час.[^rfc-5280-x509] Пристрій без RTC з батарейкою після увімкнення не знає дати. Варіанти: синхронізувати час до перевірки (але тоді й джерело часу має бути довіреним), зберігати останній відомий час у flash як нижню межу, мати RTC. Вимкнення перевірки дати – свідоме послаблення, яке треба задокументувати, а не тихий workaround.

**Ім’я сервера.** RFC 9525 описує перевірку ідентичності сервісу: клієнт порівнює очікуване DNS-ім’я з записами `subjectAltName` у сертифікаті.[^rfc-9525-service-identity] Типова помилка в embedded-коді – не передати бібліотеці ім’я хоста або залишити режим «не перевіряти сертифікат» після налагодження.

**Ротація.** Кореневі сертифікати мають строк дії і можуть бути відкликані. Якщо trust store вшитий у firmware без можливості оновлення, пристрій через кілька років не зможе підключитися. Тому оновлення списку CA має бути частиною процесу OTA, а pinning конкретного серверного сертифіката вимагає плану заміни.

### RAM

Запис TLS переносить до `2^14` (16384) байтів даних.[^rfc-8446-tls13] RFC 8449 нагадує, що для TLS 1.2 і раніше до цього додається до 2048 байтів розширення на стиснення й захист, у TLS 1.3 – до 256 байтів, і виділити до 18 KB лише на вхідний шифротекст для деяких реалізацій неможливо; AEAD-шифр до того ж вимагає мати весь запис у пам’яті, щоб його розшифрувати й автентифікувати.[^rfc-8449-record-size-limit]

Зменшити буфер можна лише за домовленістю з сервером. Старе розширення `max_fragment_length` з RFC 6066 дозволяє значення `2^9`, `2^10`, `2^11` і `2^12` байтів,[^rfc-6066-tls-extensions] а RFC 8449 замінює його розширенням `record_size_limit`. Важлива деталь: якщо розширення не узгоджене, сторони можуть надсилати записи будь-якого розміру, дозволеного протоколом.[^rfc-8449-record-size-limit] Тобто зменшений вхідний буфер безпечний лише тоді, коли сервер гарантовано підтримує це розширення.

Масштаб для орієнтиру: в ESP-IDF приклад `https_request` з перевіркою сервера з Mbed TLS використовує близько 42 KB heap у конфігурації за замовчуванням і близько 22 KB з динамічними TX/RX-буферами та опціями динамічного звільнення конфігураційних даних і CA-сертифіката; документація попереджає, що ці числа змінюються з версіями.[^esp-idf-mbedtls] До цього додаються stack для криптографії, сам ланцюжок сертифікатів під час перевірки і час handshake: асиметричні операції на MCU без апаратного прискорювача можуть тривати помітно довго.

### Entropy

TLS вимагає криптографічно стійкого генератора псевдовипадкових чисел (CSPRNG): випадкові значення йдуть у поля Random у ClientHello і ServerHello та на генерацію ключового матеріалу.[^rfc-8446-tls13] CSPRNG стійкий лише настільки, наскільки непередбачуване його початкове значення (seed). RFC 4086 наводить приклад: якщо 128-бітні ключі виводять з генератора, ініціалізованого 8-бітним seed, атакувальнику достатньо перебрати 256 варіантів, а не `2^128`.[^rfc-4086-randomness] Типові embedded-помилки – seed з лічильника часу від старту (після кожного reset він однаковий), з серійного номера або з константи.

Апаратний TRNG теж має умови роботи. Наприклад, на ESP32 `esp_random()` дає справжні випадкові числа лише тоді, коли ввімкнено RF-підсистему (Wi-Fi або Bluetooth), коли застосунок увімкнув внутрішнє джерело ентропії SAR ADC через `bootloader_random_enable()`, або поки працює second stage bootloader; інакше вихід слід вважати лише псевдовипадковим.[^esp-idf-random] Документація прямо зазначає, що після старту застосунку зазвичай доступні лише псевдовипадкові числа, доки не ініціалізовано Wi-Fi або Bluetooth.[^esp-idf-random] Звідси практичне правило: ключ, згенерований застосунком на першому старті до ініціалізації радіо й без увімкненого джерела ентропії, може виявитися слабким.

### Що хоче почути інтерв’юер

Що TLS на пристрої – це не лише «увімкнути шифрування», а повна перевірка сертифіката (ланцюжок, строк дії, ім’я хоста), розв’язана проблема часу, бюджет RAM з урахуванням розміру записів і поведінки сервера, план оновлення trust store і надійне джерело ентропії до першої генерації ключів.
