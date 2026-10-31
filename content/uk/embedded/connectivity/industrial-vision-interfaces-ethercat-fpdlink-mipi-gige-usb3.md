---
id: emb-conn-0013
title: "Які industrial або vision interfaces можуть бути embedded-relevant, але нішевими: EtherCAT, FPD-Link III, MIPI CSI, GigE Vision, USB3 Vision?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: ethercat-technology
    title: "EtherCAT Technology Group: EtherCAT Technology"
    url: https://www.ethercat.org/en/technology.html
  - source_id: ti-ds90ub954-q1
    title: "TI DS90UB954-Q1 Dual 4.16 Gbps FPD-Link III Deserializer Hub With MIPI CSI-2 Outputs"
    url: https://www.ti.com/lit/ds/symlink/ds90ub954-q1.pdf
  - source_id: linux-v4l2-tx-rx
    title: "Linux kernel documentation: Pixel data transmitter and receiver drivers"
    url: https://docs.kernel.org/driver-api/media/tx-rx.html
  - source_id: a3-gige-vision
    title: "A3: GigE Vision Standard"
    url: https://www.automate.org/vision/vision-standards/vision-standards-gige-vision
  - source_id: a3-usb3-vision
    title: "A3: What Is USB3 Vision?"
    url: https://www.automate.org/vision/vision-standards/usb3-vision
  - source_id: aravis-ethernet-performance
    title: "Aravis documentation: Ethernet Devices"
    url: https://aravisproject.github.io/aravis/aravis-stable/ethernet.html
---

## Short answer

**EtherCAT** - deterministic industrial Ethernet для motion/control, часто з dedicated slave controller. **FPD-Link III** і **MIPI CSI** часто зустрічаються у camera/display pipelines на embedded SoC. **GigE Vision** і **USB3 Vision** - machine-vision transports, де важливі bandwidth, latency, drivers і buffer handling.[^dou-embedded-interview]

## Detailed explanation

Ці інтерфейси нішеві не тому, що рідкісні, а тому, що кожен вимагає спеціалізованого заліза і власного програмного стеку. На співбесіді не чекають знання специфікацій напам’ять; чекають розуміння, яку задачу розв’язує інтерфейс, де проходить межа між hardware і firmware і що ламається на практиці.

### EtherCAT: детермінований обмін для motion control

EtherCAT розроблявся під короткі цикли (до 100 мкс), низький jitter синхронізації (до 1 мкс) і дешеве залізо. Ключова ідея – обробка "на льоту": MainDevice (раніше master) надсилає один кадр, що проходить через усі вузли; кожен SubDevice (раніше slave) читає адресовані йому дані й вставляє свої, поки кадр рухається далі, а останній вузол повертає кадр назад. Надсилати кадри у сегменті має право лише MainDevice, тому колізій і непередбачуваних затримок немає.[^ethercat-technology]

Що це означає для embedded-розробника:

- **MainDevice** використовує звичайний Ethernet MAC без окремого комунікаційного процесора і реалізується програмно на Linux, Windows, QNX, VxWorks тощо. Payload іде у стандартному Ethernet-кадрі з EtherType `0x88A4`, без TCP/IP.[^ethercat-technology]
- **SubDevice** потребує EtherCAT SubDevice Controller (ESC) – ASIC, FPGA або блок усередині MCU, – який обробляє кадри апаратно. Прикладний MCU спілкується з ESC через Process Data Interface: SPI для невеликих обсягів даних, паралельну шину для великих; найпростіші вузли взагалі обходяться без MCU.[^ethercat-technology]
- **Конфігурація** описується XML-файлом ESI; базові параметри пристрою зберігаються в EEPROM (SII), щоб MainDevice міг працювати з пристроєм навіть без ESI.[^ethercat-technology]
- **Синхронізація** – Distributed Clocks: час першого вузла з DC розсилається іншим, затримка поширення вимірюється й компенсується, і дії (наприклад, захоплення позиції енкодера) запускаються локальним годинником, а не моментом приходу кадру.[^ethercat-technology]
- **Діагностика**: кожен адресований вузол інкрементує Working Counter; якщо його значення не збігається з очікуваним, MainDevice не передає дані цього datagram у прикладну програму.[^ethercat-technology]

### MIPI CSI-2 і FPD-Link III: камера до SoC

**MIPI CSI-2** – шина передачі зображення від камери до SoC. У Linux камеру й CSI-2 receiver обслуговують драйвери V4L2, і документація ядра дає формулу пропускної здатності:[^linux-v4l2-tx-rx]

```text
pixel_rate = link_freq * 2 * nr_of_lanes * 16 / k / bits_per_sample
k = 16 for D-PHY, 7 for C-PHY
```

Приклад: D-PHY, 2 lanes, `link_freq` = 400 МГц, формат RAW10. Тоді `400e6 * 2 * 2 * 16 / 16 / 10` = 160 Мпікс/с. Кадр 1920×1080 при 30 fps – це близько 62,2 Мпікс/с без урахування blanking, тож запас є. Типова проблема bring-up – перехід у high-speed: передавач коротко переводить лінії в стан LP-11 (або LP-111, залежно від PHY), цей інтервал може тривати лише близько 100 мкс, і деякі приймачі вимагають, щоб програма встигла це помітити; без апаратної підтримки зробити це програмно важко.[^linux-v4l2-tx-rx]

CSI-2 розрахована на короткі з’єднання на платі. Коли камеру треба винести на метри кабелю (автомобіль, робот), ставлять serializer/deserializer. TI DS90UB954-Q1 – deserializer hub, що приймає дані з одного або двох сенсорів по FPD-Link III через коаксіальний кабель або екрановану виту пару і видає їх як MIPI CSI-2 (1–4 data lanes, до 1,6 Гбіт/с на lane, чотири virtual channels). Окремий двонаправлений back channel передає I2C і GPIO, тож SoC налаштовує віддалений сенсор "крізь" кабель, а живлення камери можна подати тим самим коаксіалом (Power-over-Coax).[^ti-ds90ub954-q1] Для firmware це означає ланцюжок I2C-адрес (deserializer, serializer, сенсор), порядок увімкнення і діагностику link.

### GigE Vision і USB3 Vision: промислові камери до ПК або SoC

**GigE Vision** – стандарт інтерфейсу камер поверх Gigabit Ethernet: стандартні кабелі CAT5e/CAT6, передача до 100 м, сумісність камер і ПЗ різних виробників. Можливості камери описуються XML-файлом за синтаксисом GenApi зі стандарту GenICam.[^a3-gige-vision] **USB3 Vision** використовує той самий GenICam для опису функцій, але передає дані bulk transfers USB 3.0; A3 оцінює стійкий потік у 350–400 МБ/с.[^a3-usb3-vision]

Практичні питання тут – пропускна здатність і втрати пакетів. Приклад: Mono8 1920×1200 при 40 fps – це 1920 × 1200 × 40 = 92,16 МБ/с, або близько 737 Мбіт/с, тобто більша частина гігабітного link. Документація відкритої бібліотеки Aravis радить у такому разі підключати камеру напряму до окремого порту, збільшувати буфер сокета, підвищувати пріоритет потоку прийому і збільшувати розмір stream-пакета, що вимагає підняти MTU мережевого адаптера понад стандартні 1500 байтів (рекомендовано 8192).[^aravis-ethernet-performance]

### Що очікують почути

- EtherCAT – це про детермінізм і апаратний ESC, а не про "швидкий Ethernet"; firmware SubDevice працює з process data через PDI і синхронізується через DC.
- CSI-2 і FPD-Link – про bring-up ланцюжка сенсор–serializer–deserializer–SoC, розрахунок link frequency і lanes, драйвери V4L2.
- GigE Vision і USB3 Vision – про bandwidth budget, буфери, MTU, CPU load і GenICam як спільну модель налаштувань камери.
