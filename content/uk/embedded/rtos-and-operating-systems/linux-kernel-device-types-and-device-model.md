---
id: emb-fund-0022
title: "Які типи пристроїв існують у Linux kernel і як вони представлені через device model?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: ldd3-ch01-device-classes
    title: "Linux Device Drivers, 3rd Edition, розділ 1: An Introduction to Device Drivers"
    url: https://static.lwn.net/images/pdf/LDD3/ch01.pdf
  - source_id: linux-allocated-devices
    title: "The Linux Kernel: Linux allocated devices"
    url: https://docs.kernel.org/admin-guide/devices.html
  - source_id: linux-driver-infrastructure
    title: "The Linux Kernel: Device drivers infrastructure"
    url: https://docs.kernel.org/driver-api/infrastructure.html
  - source_id: linux-driver-binding
    title: "The Linux Kernel: Driver Binding"
    url: https://docs.kernel.org/driver-api/driver-model/binding.html
  - source_id: linux-sysfs
    title: "The Linux Kernel: sysfs – файлова система для експорту kernel objects"
    url: https://docs.kernel.org/filesystems/sysfs.html
  - source_id: linux-platform-devices
    title: "The Linux Kernel: Platform Devices and Drivers"
    url: https://docs.kernel.org/driver-api/driver-model/platform.html
  - source_id: linux-devicetree-usage-model
    title: "The Linux Kernel: Linux and the Devicetree"
    url: https://docs.kernel.org/devicetree/usage-model.html
---

## Short answer

У Linux є **character**, **block**, **network**, platform, bus-specific devices тощо. Device model представляє їх через `struct device`, bus, driver, class і sysfs nodes. Для embedded важливі platform devices, devicetree/ACPI опис hardware і binding driver до compatible/resource data.[^dou-embedded-interview]

## Detailed explanation

На це питання є дві різні відповіді, і їх варто розділяти: як пристрій виглядає для user space (клас інтерфейсу) і як ядро внутрішньо описує пристрої, шини та драйвери (device model).

### Три класичні класи пристроїв

Linux традиційно розрізняє три фундаментальні типи пристроїв, і драйвер зазвичай реалізує один із них:[^ldd3-ch01-device-classes]

- **Character device** – потік байтів, до якого звертаються як до файлу через вузол у `/dev` (`/dev/ttyS0`, `/dev/console`). Драйвер реалізує щонайменше `open`, `release`, `read`, `write`, а часто ще `ioctl`, `poll`, `mmap`. Більшість char devices – послідовні канали даних, хоча деякі (наприклад, frame grabber) дозволяють `lseek` або `mmap`.
- **Block device** – пристрій, на якому може жити файлова система (диск, eMMC, SD). Він теж має вузол у `/dev`, і Linux дозволяє user space читати з нього довільну кількість байтів, тож для користувача різниця з char device майже непомітна. Різниця – у тому, як ядро керує даними: block driver має зовсім інший інтерфейс до ядра, ніж char driver.
- **Network interface** – пристрій, що надсилає й приймає пакети під керуванням мережевої підсистеми. Він не прив’язаний до вузла файлової системи: інтерфейс має ім’я (`eth0`, `wlan0`), але відповідного файлу в `/dev` немає, а ядро викликає функції передавання пакетів замість `read`/`write`.

Char і block пристрої ідентифікуються парою major/minor. Ядро веде офіційний реєстр статично виділених номерів, але прямо застерігає: нині Linux підтримує динамічне виділення номерів, а іменування бере на себе sysfs разом з udev, тож новому драйверу фіксований major зазвичай не потрібен.[^linux-allocated-devices]

Важливо, що класифікація за шиною ортогональна до цих трьох типів. USB-пристрій обслуговується через USB-підсистему, але в системі він з’являється як char device (USB serial), block device (кардрідер) або мережевий інтерфейс (USB Ethernet).[^ldd3-ch01-device-classes] Тому відповідь «є ще platform devices, I2C devices, SPI devices» говорить не про тип інтерфейсу, а про те, через яку шину ядро знайшло пристрій і прив’язало драйвер.

### Device model: device, bus, driver, class

На найнижчому рівні кожен пристрій у Linux – це екземпляр `struct device`. Він рідко існує сам по собі: зазвичай його вбудовано в структуру конкретної шини чи підсистеми (`struct pci_dev`, `struct platform_device`, `struct i2c_client`), яка додає власні поля.[^linux-driver-infrastructure]

- **Bus** (`struct bus_type`) – канал між процесором і пристроями. Для device model усі пристрої підключені через якусь шину, навіть якщо це внутрішня віртуальна шина `platform`. Шини можуть вкладатися: USB-контролер зазвичай сам є PCI-пристроєм.[^linux-driver-infrastructure]
- **Driver** (`struct device_driver`) – ядро відстежує всі відомі драйвери насамперед для того, щоб зіставляти їх з новими пристроями. Серед полів драйвера є таблиці зіставлення `of_match_table` (devicetree) і `acpi_match_table`.[^linux-driver-infrastructure]
- **Class** – високорівневе представлення пристрою за функцією, а не за способом підключення: для класу SCSI-диск і ATA-диск – просто диски. Класи дозволяють user space працювати з пристроями за тим, що вони роблять.[^linux-driver-infrastructure]

**Binding** – це процес зв’язування пристрою з драйвером. Його запускають дві події: реєстрація нового пристрою (ядро перебирає драйвери його шини) і реєстрація нового драйвера (ядро перебирає ще не прив’язані пристрої). Як порівнювати ідентифікатори, вирішує callback `match` конкретної шини; після збігу викликається `probe()` драйвера, який ініціалізує пристрій і створює per-device стан. Цей стан разом із прив’язкою можна вважати «екземпляром драйвера».[^linux-driver-binding]

### sysfs як відображення моделі

sysfs робить ці зв’язки видимими:[^linux-sysfs]

- `/sys/devices/` – ієрархія `struct device`, тобто фізичне дерево пристроїв;
- `/sys/bus/<bus>/devices/` і `/sys/bus/<bus>/drivers/` – пристрої та драйвери кожної шини;
- `/sys/class/<class>/` – symlink-и на пристрої, згруповані за функцією;
- `/sys/dev/char/` і `/sys/dev/block/` – symlink-и з іменами `<major>:<minor>`, тож від результату `stat()` на вузлі `/dev` легко перейти до його опису в sysfs.

Коли binding відбувся, ядро створює symlink-и між каталогом драйвера в `/sys/bus/<bus>/drivers/` і каталогом пристрою у фізичній ієрархії, а при відв’язуванні прибирає їх.[^linux-driver-binding] На співбесіді корисно показати шлях від вузла `/dev` через `stat()` і `/sys/dev/char/<major>:<minor>` до `struct device` у `/sys/devices/`, а звідти – до драйвера на його шині.

### Platform devices і devicetree в embedded

На SoC більшість периферії (UART, SPI- та I2C-контролери, таймери) сидить на внутрішній шині з прямою адресацією з боку CPU і не має механізму автоматичного виявлення, як PCI чи USB. Для них ядро використовує псевдошину `platform`: `platform_device` має ім’я та список ресурсів (діапазони адрес, IRQ), а `platform_driver` надає `probe()` і `remove()`, тоді як виявлення пристроїв відбувається поза драйвером.[^linux-platform-devices]

Хто ж створює ці `platform_device`? Раніше – статичні таблиці в board-файлах, по одному ядру на плату. Зараз на ARM та інших embedded-архітектурах їх створює ядро, розбираючи devicetree: вузли з властивістю `compatible` у корені дерева та дочірні вузли `simple-bus` реєструються як platform devices викликом `of_platform_populate()`. Вузли під контролером I2C або SPI натомість реєструє драйвер цього контролера під час свого `probe()`, як `i2c_client` чи `spi_device` на відповідній шині.[^linux-devicetree-usage-model] Зіставлення драйвера з вузлом іде через `compatible`-рядки з `of_match_table` (докладніше про сам devicetree – qid:emb-boot-0001).

### Що хоче почути інтерв’юер

- Три типи інтерфейсу (char, block, network) і те, що мережевий інтерфейс не має вузла в `/dev`.
- Розрізнення типу інтерфейсу і шини: «platform device» – не четвертий тип, а спосіб, у який пристрій потрапив у device model.
- Ланцюжок bus – device – driver – `match` – `probe()` і роль класу як функціонального представлення.
- Уміння знайти пристрій і його драйвер через `/sys/bus`, `/sys/class`, `/sys/dev`.
- Типова помилка – вважати, що драйвер сам «шукає» своє залізо: у сучасній моделі пристрої описує devicetree, ACPI або сама шина, а драйвер лише оголошує, з якими ідентифікаторами він сумісний.
