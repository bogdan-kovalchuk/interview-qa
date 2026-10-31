---
id: emb-fund-0024
title: "Які framework-и для збірки embedded Linux або kernel ви знаєте: Buildroot, Yocto, OpenWrt, vendor BSP?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: buildroot-manual
    title: "The Buildroot user manual"
    url: https://buildroot.org/downloads/manual/manual.html
  - source_id: yocto-overview-intro
    title: "Yocto Project Overview and Concepts Manual: Introducing the Yocto Project"
    url: https://docs.yoctoproject.org/overview-manual/yp-intro.html
  - source_id: openwrt-readme
    title: "README репозиторію OpenWrt"
    url: https://github.com/openwrt/openwrt/blob/main/README.md
---

## Short answer

**Buildroot** простіший для генерації rootfs/toolchain/images з fixed configuration. **Yocto** складніший, але гнучкий для продуктів з layers, recipes, package management і довгим lifecycle. **OpenWrt** орієнтований на мережеві пристрої, а vendor BSP часто дає швидкий старт, але може мати застарілий kernel і patches.[^dou-embedded-interview]

## Detailed explanation

Усі ці інструменти розв’язують одну задачу: з вихідних кодів на host-машині крос-компілювати toolchain, bootloader, kernel і root filesystem для цільової плати й видати готові образи. Відрізняються вони моделлю конфігурації, тим, чи є на пристрої package manager, і тим, наскільки добре масштабуються на багато продуктів і роки підтримки. На співбесіді цінують не перелік назв, а вміння пояснити, чому для конкретного продукту обрано саме цей інструмент.

### Buildroot

Buildroot спрощує й автоматизує збірку повної Linux-системи для embedded через крос-компіляцію: він уміє згенерувати cross-toolchain, root filesystem, образ kernel і bootloader, причому будь-яку з цих частин можна взяти ззовні (наприклад, готовий external toolchain). Конфігурація – Kconfig (`make menuconfig`), а для сотень готових плат є defconfig-и.[^buildroot-manual] Один `make` завантажує вихідні коди, збирає або імпортує toolchain, збирає вибрані пакети, kernel і bootloader, а результат кладе в `output/images/`.[^buildroot-manual]

Важливі властивості, які варто знати:

- **Немає бінарних пакетів на target.** Розробники Buildroot прямо пишуть, що це генератор root filesystem, а не генератор дистрибутивів; надійне відстеження встановлених файлів і зворотних залежностей вони вважають надто складним і для дистрибутивного підходу радять OpenEmbedded або OpenWrt.[^buildroot-manual] Оновлення пристрою – це заміна образу цілком.
- **Немає автоматичного визначення, що треба перезібрати.** Після зміни архітектури чи toolchain потрібна повна перезбірка, і відповідальність за це лежить на користувачеві.[^buildroot-manual]
- **br2-external** дозволяє тримати власні пакети, конфігурації плат і defconfig-и поза деревом Buildroot, що спрощує оновлення самого Buildroot.[^buildroot-manual]

Звідси типовий профіль: невеликий, фіксований образ, одна-дві плати, невелика команда, швидкий старт.

### Yocto Project / OpenEmbedded

Yocto Project – відкритий проєкт для створення власних Linux-систем для embedded-продуктів незалежно від архітектури. Ядро – OpenEmbedded build system: BitBake як рушій задач з урахуванням залежностей і metadata (recipes, класи, конфігураційні файли), спільна основа яких – OpenEmbedded-Core.[^yocto-overview-intro]

Ключова ідея – **layer model**: шари є репозиторіями з інструкціями для збірки, які можна перевикористовувати й перевизначати. Окремо тримають BSP-шар, distro-конфігурацію, middleware і застосунки, а не все в одному шарі.[^yocto-overview-intro] Збірка пакує ПЗ у бінарні пакети (DEB, RPM або IPK), формує з них package feed і вже з нього – образ root filesystem, а паралельно генерує SDK для розробників застосунків.[^yocto-overview-intro]

Переваги, які Yocto декларує: часткові перезбірки через shared state cache (sstate), високий рівень binary reproducibility, license manifest для аудиту open-source ліцензій, релізи кожні шість місяців (квітень і жовтень). Недоліки визнаються там само: крутий поріг входу, багато способів зробити одне й те саме, а додавання пакета до образу вимагає зміни конфігурації та перезбірки.[^yocto-overview-intro]

Типовий профіль: лінійка продуктів на кількох SoC, кілька команд, довгий життєвий цикл, вимоги до відтворюваності й ліцензійної звітності, можливість оновлювати окремі пакети.

### OpenWrt

OpenWrt – Linux-система для embedded-пристроїв, найвідоміша як прошивка для мережевого обладнання. На відміну від «статичної» прошивки він надає записувану файлову систему з package management, тож пристрій налаштовують установленням пакетів.[^openwrt-readme] Збірка влаштована подібно до Buildroot: `./scripts/feeds update -a` і `./scripts/feeds install -a` підтягують визначення пакетів із feeds, `make menuconfig` вибирає toolchain, target і пакети, а `make` будує toolchain, kernel і застосунки.[^openwrt-readme] Вибір OpenWrt виправданий, якщо продукт – роутер, точка доступу чи шлюз на підтримуваному SoC: мережевий стек, вебінтерфейс LuCI і готові пакети дають дуже швидкий старт.

### Vendor BSP

Vendor BSP – це те, що постачає виробник SoC: зазвичай власний Yocto-шар або форк Buildroot (Buildroot прямо згадує, що сторонні проєкти будують на ньому свої BSP і SDK[^buildroot-manual]) разом із форком kernel і bootloader. Він дає найшвидший шлях до працюючої плати, бо містить драйвери, яких ще може не бути в mainline. Перед тим як будувати на ньому продукт, варто перевірити версію kernel і чи є вона LTS, скільки патчів не потрапило в mainline, як часто вендор випускає оновлення безпеки і чи можна відокремити його шар від власного коду. Найпоширеніша пастка – продукт, прив’язаний до старого вендорського ядра, яке неможливо оновити без повторного портування драйверів.

### Як відповісти на співбесіді

- Buildroot – простота, швидкість, один образ, оновлення «цілим образом».
- Yocto – масштаб, шари, пакети, SDK, відтворюваність і ліцензійний облік ціною складності та часу збірки.
- OpenWrt – готовий дистрибутив для мережевих пристроїв з package management.
- Vendor BSP – стартова точка, яку бажано інтегрувати як шар у Yocto (або як br2-external у Buildroot), а не як фундамент, у який вписують власний код.

Сильна відповідь також згадує, що від вибору залежить стратегія оновлення в полі (A/B-образи чи пакети), і що kernel та bootloader можна будувати будь-яким із цих інструментів, але патчі до них краще тримати окремо, у власному шарі чи каталозі.
