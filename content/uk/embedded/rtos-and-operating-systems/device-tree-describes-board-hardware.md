---
id: emb-boot-0001
title: "Що таке device tree?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
  - source_id: devicetree-spec
    title: "Devicetree Specification v0.4"
    url: https://github.com/devicetree-org/devicetree-specification/releases/tag/v0.4
---

## Short answer

**Device Tree** – структура даних, що описує апаратуру плати (CPU, пам'ять, периферія, переривання, шини) у вигляді, не залежному від коду ядра.[^dou-embedded-interview] Дозволяє одному образу ядра Linux підтримувати різні плати.

Файли: `.dts` (Device Tree Source, текст) компілюється `dtc` у `.dtb` (Device Tree Blob, бінарний файл). Bootloader (U-Boot) передає адресу DTB ядру при завантаженні.

Приклад вузла: описує UART1 – базову адресу регістрів, номер переривання, тактування; Драйвер у ядрі читає ці параметри через DT API.

## Detailed explanation

Device Tree – це ієрархічна структура даних, що описує апаратне забезпечення у вигляді вузлів і властивостей. Кожен вузол представляє пристрій або групу пристроїв; властивості містять параметри (адреси регістрів, номери переривань, частоти, рядки `compatible`). Кореневий вузол містить загальносистемну інформацію (розмір пам'яті, тип машини); дочірні вузли описують периферію (UART, SPI, I2C, GPIO контролери тощо).

Файл `.dts` (текстовий, читабельний) компілюється утилітою `dtc` (Device Tree Compiler) у бінарний `.dtb`. Bootloader (наприклад, U-Boot) завантажує `.dtb` у пам'ять і передає його адресу ядру через регістр процесора (r2 на ARM 32-bit, або через ATAGS/EFI на інших архітектурах).

Під час ініціалізації ядро парсить дерево: читає властивості кореневого вузла (`#address-cells`, `#size-cells`, `memory`) для визначення розміру пам'яті та типу машини, потім обходить вузли пристроїв. Для кожного вузла ядро зіставляє властивість `compatible` з драйверами, зареєстрованими у subsystem (platform bus, I2C bus, SPI bus тощо), і прив'язує відповідний драйвер. Драйвер читає з вузла конфігураційні дані: `reg` (адреса та розмір регістрів), `interrupts` (номер та тип переривання), `clock-frequency`, `status` ("okay" / "disabled") тощо.[^devicetree-spec]

Такий підхід відділяє опис апаратури від коду ядра: один образ ядра може працювати на різних платах, змінюється лише `.dtb`. Це усунуло потребу в board-specific `machine_desc` структурах та окремих збірках ядра для кожної плати.
