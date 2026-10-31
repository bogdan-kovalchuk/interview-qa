---
id: emb-periph-0019
title: "Як працюють CAN, LIN, MOST і FlexRay, і чим вони відрізняються за arbitration, timing і automotive use-case?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: iso-11898-1
    title: "ISO 11898-1: Road vehicles – Controller area network (CAN) – Part 1: Data link layer and physical signalling"
    url: https://www.iso.org/standard/63648.html
  - source_id: ti-sloa101-can
    title: "Texas Instruments SLOA101B: Introduction to the Controller Area Network (CAN)"
    url: https://www.ti.com/lit/an/sloa101b/sloa101b.pdf
  - source_id: lin-2-2a-spec
    title: "LIN Specification Package, Revision 2.2A"
    url: https://www.cs-group.de/wp-content/uploads/2016/11/LIN_Specification_Package_2.2A.pdf
---

## Short answer

**CAN** має multi-master arbitration за message ID і добре підходить для robust control networks. **LIN** дешевший master-slave bus для простих actuators/sensors; **FlexRay** дає deterministic time-triggered communication для safety-critical systems. **MOST** історично використовувався для automotive multimedia; його роль інша, ніж у control buses.[^dou-embedded-interview]

## Detailed explanation

### Архітектурний огляд автомобільних шин
В автомобільній електроніці (Automotive Embedded) різні підсистеми висувають протилежні вимоги до пропускної здатності, надійності, детермінізму та вартості вузла. Тому в сучасних автомобілях використовується ієрархія гетерогенних мереж, з’єднаних через центральний шлюз (Gateway ECU):
- **CAN (Controller Area Network)**: основна робоча конячка для систем керування силовим агрегатом (powertrain), шасі та кузовом.
- **LIN (Local Interconnect Network)**: недорога підмережа для локальних виконавчих механізмів та датчиків.
- **FlexRay**: високошвидкісна детермінована шина для систем x-by-wire (гальмування, активне кермування, активна підвіска).
- **MOST (Media Oriented Systems Transport)**: оптоволоконна/мідна шина для передачі мультимедіа, відео та звуку.

### Порівняльний аналіз протоколів за ключовими критеріями

1. **CAN (Controller Area Network – ISO 11898)** [^iso-11898-1]:
   - **Топологія та фізичний рівень**: диференційна вита пара (`CAN_H`, `CAN_L`) із термінацією 120 Ом на кінцях лінії. Логічні рівні: домінантний (0 – різниця напруг близько 2 В) та рецесивний (1 – нульова диференційна напруга). Для high-speed CAN TI наводить типові рівні: у рецесивному стані обидві лінії близько 2.5 В, у домінантному `CAN_H` близько 3.5 В, `CAN_L` близько 1.5 В.[^ti-sloa101-can]
   - **Арбітраж**: неруйнівний побітовий арбітраж (CSMA/CD + NBA). Всі вузли можуть почати передачу одночасно; під час передачі ідентифікатора повідомлення вузол читає шину. Якщо він передає рецесивний біт '1', але виявляє домінантний '0' (від вузла з меншим числовим значенням ID), він миттєво програє арбітраж і переходить у режим прийому без спотворення чужого кадру.[^ti-sloa101-can]
   - **Timing**: подійно-орієнтований (event-driven). Гарантується найнижча затримка для кадрів із найвищим пріоритетом (найменшим ID), проте при високому завантаженні шини низькопріоритетні кадри страждають від джиттеру або затримки.
   - **Швидкість**: Classic CAN – до 1 Мбіт/с (зазвичай 500 кбіт/с); CAN FD – до 5–8 Мбіт/с у фазі даних.

2. **LIN (Local Interconnect Network – ISO 17987)**:
   - **Топологія та фізичний рівень**: однопровідна лінія напругою 12 В (рівень бортової мережі), відкритий колектор із підтяжкою. Максимальна довжина до 40 м.
   - **Арбітраж**: арбітраж відсутній, оскільки архітектура суворо Master-Slave. Тільки Master ініціює будь-яку комунікацію, надсилаючи заголовок кадру (`Sync Break`, `Sync Byte 0x55`, `Identifier`). Slave-вузли лише відповідають передачею поля даних.
   - **Timing**: детермінований розклад (Schedule Table), що циклічно виконується Master-контролером. Для звичайних (unconditional) кадрів колізій немає, бо на кожен заголовок відповідає рівно один вузол. Виняток – event triggered frame: на його заголовок можуть відповісти кілька Slave одночасно, і тоді Master розв’язує колізію окремою collision resolving schedule table.[^lin-2-2a-spec]
   - **Швидкість та застосування**: до 20 кбіт/с[^lin-2-2a-spec]. Використовується там, де вузол CAN був би надмірно дорогим (склопідйомники, регулювання сидінь, дзеркала, клімат-контроль, датчики дощу).

3. **FlexRay (ISO 17458)**:
   - **Топологія та фізичний рівень**: шина, зірка або гібридна топологія, диференційна пара. Підтримує дублювання каналів (Channel A та Channel B) зі швидкістю 10 Мбіт/с на канал для забезпечення відмовостійкості (fault tolerance).
   - **Арбітраж та Timing**: комбінація TDMA (Time Division Multiple Access) та динамічного сегмента (Mini-slotting). Кожен комунікаційний цикл ділиться на:
     - *Статичний сегмент (Static Segment)*: фіксовані часові слоти, виділені окремим ECU. Жорсткий детермінізм із нульовим джиттером.
     - *Динамічний сегмент (Dynamic Segment)*: слоти змінної довжини для подійно-орієнтованих повідомлень.
   - **Застосування**: системи безпеки з високими вимогами ASIL D, steer-by-wire, brake-by-wire.

4. **MOST (Media Oriented Systems Transport)**:
   - **Топологія та фізичний рівень**: кільцева топологія (Ring), зазвичай пластикове оптичне волокно (POF) або екранована вита пара (ePHY).
   - **Арбітраж та передача даних**: синхронна TDM-передача потокового аудіо/відео без упаковки в пакетні заголовки разом із каналами асинхронних пакетів і керування.
   - **Швидкість та застосування**: від 25 Мбіт/с (MOST25) до 150 Мбіт/с (MOST150). Використовувалася для мультимедіа та підсилювачів акустики. У нових архітектурах витісняється автомобільним Ethernet (Automotive Ethernet 100BASE-T1 / 1000BASE-T1 з протоколами TSN/AVB).

### Підсумкова таблиця порівняння характеристик

| Характеристика | LIN | CAN / CAN FD | FlexRay | MOST |
| :--- | :--- | :--- | :--- | :--- |
| **Швидкість** | До 20 кбіт/с | 1 Мбіт/с / до 8 Мбіт/с | До 10 Мбіт/с (×2 канали) | 25–150 Мбіт/с |
| **Фізичний рівень** | 1 провід (12 В) | Диференційна пара (5 В) | Диференційна пара | Оптика (POF) / мідь |
| **Керування доступом** | Master-Slave | CSMA/CD + NBA (за ID) | TDMA + Dynamic Slots | Кільце, TDM-канали |
| **Детермінізм** | Жорсткий (розклад) | Пріоритетний (за ID) | Жорсткий (Time-triggered) | Синхронні потоки |
| **Відмовостійкість** | Низька | Середня (CRC, ACK) | Висока (Dual Channel) | Обрив кільця критичний |
| **Основна роль** | Кузовна електроніка | Powertrain, Chassis | Safety-critical, x-by-wire | Інфотейнмент, аудіо |
