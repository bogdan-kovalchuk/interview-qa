---
id: emb-conn-0002
title: "Як вибрати між MQTT, RabbitMQ і WebSocket для передачі telemetry з IoT-пристрою у хмару?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: mqtt-v5
    title: "MQTT Version 5.0, OASIS Standard"
    url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html
  - source_id: lwip-overview
    title: "lwIP 2.1.0: Overview"
    url: https://www.nongnu.org/lwip/2_1_x/index.html
  - source_id: zephyr-net-stack-architecture
    title: "Zephyr Project documentation: Network Stack Architecture"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/net-stack-architecture.html
  - source_id: rfc-6455-websocket
    title: "RFC 6455: The WebSocket Protocol"
    url: https://www.rfc-editor.org/rfc/rfc6455.html
  - source_id: rabbitmq-mqtt-plugin
    title: "RabbitMQ documentation: MQTT Plugin"
    url: https://www.rabbitmq.com/docs/mqtt
---

## Short answer

**MQTT** найчастіше підходить device-to-cloud: легкий publish/subscribe, QoS і reconnect model. **WebSocket** доречний, коли потрібен bidirectional channel із web/backend через HTTP infrastructure. **RabbitMQ** – broker для backend messaging; напряму на малий device його зазвичай не ставлять, але device може говорити з gateway, який уже публікує в RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

### Три різні категорії, а не три альтернативи

Перше, що варто сказати на співбесіді: MQTT, WebSocket і RabbitMQ лежать на різних рівнях. MQTT – прикладний протокол обміну повідомленнями за моделлю publish/subscribe. WebSocket – транспортне кадрування поверх TCP без жодної семантики повідомлень. RabbitMQ – конкретний брокер (продукт), ядро якого реалізує AMQP 0-9-1, а MQTT підтримує через плагін. Тому коректне питання звучить так: яким протоколом говорить пристрій і що стоїть по той бік з’єднання.

### MQTT: протокол, придуманий для пристроїв

Специфікація MQTT 5.0 описує його як легкий client-server протокол publish/subscribe, розрахований зокрема на обмежені середовища M2M та IoT. Він працює поверх TCP/IP або іншого транспорту з упорядкованою, безвтратною і двонапрямленою доставкою; UDP сам по собі не годиться, бо може губити й переставляти дані. Ключові властивості: три рівні QoS, мінімальний транспортний overhead і механізм сповіщення інших клієнтів про аварійне від’єднання.[^mqtt-v5]

Що з цього важливо для firmware:

- **QoS 0** – «не більше одного разу», підходить для сенсорних даних, де наступне вимірювання однаково прийде скоро. **QoS 1** – «щонайменше один раз», доставку гарантовано, але дублікати можливі, тож приймач має бути ідемпотентним. **QoS 2** – «рівно один раз» ціною двоетапного підтвердження (PUBREC, PUBREL, PUBCOMP) і додаткового стану на обох боках.[^mqtt-v5]
- QoS діє між одним відправником і одним отримувачем. Видавець і брокер, брокер і кожен підписник – окремі ділянки, і рівень QoS на виході до підписника може відрізнятися від вхідного.[^mqtt-v5] «QoS 1 від пристрою» ще не означає end-to-end гарантію до бази даних.
- **Keep Alive**: якщо сервер не отримав жодного пакета від клієнта протягом півтора інтервалу Keep Alive, він зобов’язаний закрити з’єднання.[^mqtt-v5] Це дає брокеру швидке виявлення мертвого пристрою незалежно від TCP keepalive.
- **Will Message** публікує сервер, коли з’єднання закрилося не штатно: так бекенд дізнається, що пристрій зник.[^mqtt-v5]
- **Retained message**: сервер зберігає останнє повідомлення з прапорцем RETAIN для топіка й одразу віддає його новим підписникам – зручно для «останнього відомого стану».[^mqtt-v5]
- **Сесії**: з `Clean Start = 0` сервер відновлює стан існуючої сесії для того самого Client Identifier – підписки і непідтверджені QoS 1/2 повідомлення переживають розрив зв’язку. Але в MQTT 5.0 сесія зберігається після закриття з’єднання лише тоді, коли Session Expiry Interval більший за нуль; відсутнє поле означає 0, і сесія зникає разом із з’єднанням. Повторне надсилання непідтверджених PUBLISH вимагається саме при такому перепідключенні, з тими самими Packet Identifier і прапорцем DUP.[^mqtt-v5]

MQTT-клієнт уже є в типових embedded-стеках: lwIP постачає його з підтримкою TLS через `altcp`, а Zephyr – серед прикладних протоколів поряд із CoAP і LwM2M.[^lwip-overview][^zephyr-net-stack-architecture]

### WebSocket: тунель через HTTP-інфраструктуру

WebSocket (RFC 6455) – це opening handshake у вигляді HTTP Upgrade-запиту, після якого йде базове кадрування повідомлень поверх TCP; стандартні порти 80 і 443 (через TLS). Клієнт зобов’язаний маскувати всі кадри, які надсилає серверу, а для перевірки живості є керувальні кадри Ping і Pong.[^rfc-6455-websocket] Топіків, QoS, retained-повідомлень, сесій і повідомлення про аварійне від’єднання WebSocket не визначає: усе це доведеться винайти поверх нього.

Тому «чистий» WebSocket для телеметрії доречний, коли бекенд уже має власний протокол повідомлень поверх нього або коли пристрій має пройти через проксі й мережі, де відкрито лише 443. Компроміс – MQTT over WebSocket: специфікація MQTT дозволяє такий транспорт, вимагаючи передавати пакети в бінарних кадрах і не припускати, що межі MQTT-пакетів збігаються з межами WebSocket-кадрів.[^mqtt-v5] Пристрій зберігає всю семантику MQTT, а мережа бачить звичайний HTTPS-трафік.

### RabbitMQ: брокер на боці бекенду

RabbitMQ підтримує MQTT 3.1, 3.1.1 і 5.0 через плагін із базової поставки, а також MQTT over WebSocket через Web MQTT plugin. Плагін побудований на сутностях AMQP 0-9-1: повідомлення з MQTT-топіків маршрутизуються через topic exchange (за замовчуванням `amq.topic`), роздільник `/` перекладається в `.`, і споживачі AMQP 0-9-1, AMQP 1.0 чи STOMP можуть читати те, що опублікував пристрій.[^rabbitmq-mqtt-plugin]

Звідси два висновки. По-перше, «поставити RabbitMQ на пристрій» – нонсенс: на пристрої працює клієнт, а RabbitMQ – це сервер. По-друге, пристрій не обов’язково потребує шлюзу: MQTT-клієнт може під’єднатися до RabbitMQ напряму. Але є обмеження: QoS 2 не підтримується, публікація з QoS 2 від клієнта MQTT 3.1.1 знижується до QoS 1, а клієнт MQTT 5.0 буде від’єднаний з reason code 155.[^rabbitmq-mqtt-plugin] Firmware, розраховане на «exactly once» через QoS 2, з таким брокером не працюватиме.

### Як обирати

| Сценарій | Рішення |
|---|---|
| Телеметрія з MCU, нестабільний зв’язок, обмежена RAM | MQTT поверх TLS, QoS 0 для потокових вимірювань, QoS 1 з ідемпотентною обробкою для подій |
| Мережа пропускає лише HTTPS, браузерні клієнти | MQTT over WebSocket або WebSocket із власним протоколом |
| Маршрутизація, черги задач, інтеграція сервісів | RabbitMQ або інший брокер на бекенді; пристрій говорить MQTT напряму чи через шлюз |

На співбесіді добре звучать конкретні наслідки вибору: розмір буферів клієнта під максимальне повідомлення, поведінка при перепідключенні (Session Expiry Interval, відновлення сесії, повторне надсилання непідтверджених QoS 1), Will Message для моніторингу присутності і явна відповідь на питання, де саме в ланцюжку гарантується доставка.
