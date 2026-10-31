---
id: emb-linemb-0001
title: "У чому різниця між kernel-модулем та user-space драйвером в embedded Linux?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: linux-kernel-docs
    title: "The Linux Kernel Documentation: Driver Implementation"
    url: https://www.kernel.org/doc/html/latest/driver-api/index.html
  - source_id: linux-uio-howto
    title: "The Userspace I/O HOWTO"
    url: https://www.kernel.org/doc/html/latest/driver-api/uio-howto.html
  - source_id: linux-vfio
    title: "VFIO - Virtual Function I/O"
    url: https://docs.kernel.org/driver-api/vfio.html
  - source_id: linux-kernel-hacking-guide
    title: "The Linux Kernel: Unreliable Guide To Hacking The Linux Kernel"
    url: https://docs.kernel.org/kernel-hacking/hacking.html
  - source_id: linux-spidev
    title: "The Linux Kernel: SPI userspace API"
    url: https://docs.kernel.org/spi/spidev.html
  - source_id: linux-i2c-dev
    title: "The Linux Kernel: реалізація драйверів I2C-пристроїв у userspace"
    url: https://docs.kernel.org/i2c/dev-interface.html
  - source_id: linux-gpio-chardev
    title: "The Linux Kernel: GPIO Character Device Userspace API"
    url: https://docs.kernel.org/userspace-api/gpio/chardev.html
  - source_id: linux-stable-api-nonsense
    title: "The Linux Kernel Driver Interface (stable API nonsense)"
    url: https://docs.kernel.org/process/stable-api-nonsense.html
  - source_id: linux-tuntap
    title: "The Linux Kernel: Universal TUN/TAP device driver"
    url: https://docs.kernel.org/networking/tuntap.html
  - source_id: linux-uinput
    title: "The Linux Kernel: uinput module"
    url: https://docs.kernel.org/input/uinput.html
---

## Short answer

**Kernel-драйвер, вбудований у ядро або завантажений як модуль, виконується в kernel context і може використовувати механізми ядра для переривань, DMA, power management та стандартних підсистем пристроїв; його дефект здатен пошкодити або впустити систему.**[^linux-kernel-docs] User-space драйвер лишає основну логіку в ізольованому процесі, але потребує kernel-інтерфейсу для доступу до пристрою. UIO придатний для простих memory-mapped пристроїв поза стандартними підсистемами, а VFIO підтримує захищений прямий доступ, зокрема DMA, якщо платформа забезпечує потрібну ізоляцію.[^linux-uio-howto][^linux-vfio] Вибір залежить від інтеграції, latency, DMA, security, відновлення та супроводу.

## Detailed explanation

Спершу варто розвести терміни. «Kernel-модуль» – це спосіб пакування коду ядра: драйвер, вбудований в образ ядра, і той самий драйвер, завантажений через `modprobe`, виконуються однаково, у kernel context з повними привілеями. Справжня межа проходить між кодом, що працює в ядрі, і кодом, що працює у звичайному процесі та звертається до пристрою через інтерфейс, який надає ядро.

### Kernel-драйвер: повна інтеграція і повна відповідальність

Драйвер у ядрі має прямий доступ до обробників переривань, DMA API, power management і, головне, може зареєструватися в стандартній підсистемі: мережевий драйвер стає інтерфейсом `eth0`, драйвер датчика – пристроєм Industrial I/O, контролер – I2C- або SPI-адаптером, а також користуватися DMAEngine, clock- і regulator-фреймворками. Застосунки працюють з ним через звичні API (сокети, sysfs, `/dev`), не знаючи про регістри.[^linux-kernel-docs]

Ціна – правила ядра. У ядрі немає захисту пам’яті: пошкодження пам’яті валить усю машину, а не один процес. Стек ядра малий (приблизно 3–6 КБ на більшості 32-бітних архітектур, близько 14 КБ на 64-бітних), FPU-контекст не зберігається, а сон дозволено лише в process context.[^linux-kernel-hacking-guide] Ще одна ціна – супровід: внутрішні інтерфейси ядра свідомо не стабільні. Функції перейменовують, структури змінюють, і всі користувачі в mainline виправляються одночасно, тоді як out-of-tree модуль доводиться адаптувати до кожної нової версії самостійно. Стабільним гарантовано лише інтерфейс між ядром і user space – системні виклики.[^linux-stable-api-nonsense]

### User-space драйвер: які інтерфейси для цього є

User-space драйвер усе одно потребує kernel-частини, яка дає доступ до заліза. Для embedded типові варіанти такі:

- **UIO.** Невеликий kernel-модуль (або загальний `uio_pdrv_genirq` для platform-пристроїв з виділеною лінією IRQ) реєструє пристрій, а логіка живе в процесі. Регістри відображаються через `mmap()` на `/dev/uioX`, а блокувальний `read()` чи `select()` повертається, коли стається переривання; прочитане число – загальний лічильник переривань, за яким видно пропуски.[^linux-uio-howto] UIO розрахований на пристрої, які мають пам’ять для відображення, повністю керуються записами в неї, зазвичай генерують переривання і не вписуються в стандартні підсистеми. Пристрої, які добре обслуговують мережева, serial чи USB-підсистеми, кандидатами для UIO не є.[^linux-uio-howto]
- **VFIO.** Фреймворк для прямого доступу до пристрою з user space під захистом IOMMU, тобто з безпечним DMA і можливістю працювати без root. Документація прямо порівнює його з UIO, який не має уявлення про IOMMU, має обмежену підтримку переривань і вимагає root-прав. Без апаратного IOMMU є лише режим no-IOMMU, який документація називає небезпечним для DMA.[^linux-vfio]
- **Інтерфейси шин.** `spidev` дає `read()`/`write()` для half-duplex та `ioctl()` для full-duplex обміну зі SPI-пристроєм; документація радить його для прототипування в середовищі, де хибний вказівник не покладе систему, і прямо зазначає, що драйвери, яким потрібні IRQ-обробники чи інші шари ядра, у user space не напишеш.[^linux-spidev] `i2c-dev` надає символьний пристрій на кожен I2C-адаптер.[^linux-i2c-dev] Для GPIO актуальний символьний пристрій `/dev/gpiochipX` (API v2 з Linux 5.10), причому документація застерігає не керувати з user space залізом, для якого є нормальний kernel-драйвер.[^linux-gpio-chardev]

### Порівняння за критеріями

- **Надійність і відновлення.** Помилка в user-space драйвері зазвичай вбиває процес, який supervisor перезапускає; помилка в kernel-драйвері може означати oops, panic і перезавантаження.
- **Latency переривань.** У kernel-драйвері обробник викликається безпосередньо. У UIO ядро лише підтверджує або маскує переривання, а процес дізнається про нього після пробудження й планування, тож до затримки додається scheduling latency цього процесу.
- **DMA і безпека.** Програмування DMA-контролера з user space без IOMMU дає процесу змогу писати в довільну фізичну пам’ять. Безпечний DMA з user space – це VFIO з IOMMU.[^linux-vfio]
- **Інтеграція.** Повноцінну інтеграцію в мережеву, block, framebuffer чи input-підсистему зазвичай дає kernel-драйвер; user-space драйвер видимий тільки власному застосунку або через власний IPC. Винятки теж спираються на kernel-модулі-посередники: TUN/TAP передає пакети віртуального мережевого інтерфейсу процесу, а `uinput` дозволяє процесу емулювати вхідний пристрій.[^linux-tuntap][^linux-uinput]
- **Ліцензія й супровід.** Kernel-код пов’язаний з ліцензією ядра та нестабільним внутрішнім API; user-space код живе на стабільному ABI системних викликів і оновлюється незалежно від ядра.[^linux-stable-api-nonsense]

### Як відповісти на співбесіді

Kernel-драйвер обирають, коли пристрій має стати частиною стандартної підсистеми, коли потрібні жорсткі вимоги до latency переривань або DMA без IOMMU, або коли пристроєм користуються кілька незалежних застосунків. User-space драйвер доречний для простого memory-mapped пристрою з одним споживачем, для швидкого прототипування через `spidev`/`i2c-dev`, для пропрієтарної логіки або коли важлива ізоляція збоїв. Сильна відповідь додає, що часто найкраще рішення – гібрид: мінімальний kernel-драйвер на стандартному API, а вся бізнес-логіка – у процесі.
