---
id: emb-build-0025
title: "Як забезпечити Continuous Delivery для MCU, якщо пристрій має фізичний target, bootloader і hardware-in-the-loop тести?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: mcuboot-design
    title: "MCUboot documentation: Bootloader design"
    url: https://docs.mcuboot.com/design.html
  - source_id: mcuboot-imgtool
    title: "MCUboot documentation: Image tool"
    url: https://docs.mcuboot.com/imgtool.html
  - source_id: zephyr-twister
    title: "Zephyr Project documentation: Test Runner (Twister)"
    url: https://docs.zephyrproject.org/latest/develop/twister/index.html
---

## Short answer

CD pipeline має збирати signed artifacts, прошивати device через bootloader/debug probe, запускати smoke/HIL tests і збирати logs/trace. Потрібні керовані test rigs: power cycling, serial logs, reset control, version readback і failure recovery. **Release gate** має перевіряти не лише build, а й update path, rollback і базову роботу hardware.[^dou-embedded-interview]

## Detailed explanation

### Чим CD для MCU відрізняється від серверного

Для серверного ПЗ "доставити" означає розгорнути контейнер і за потреби відкотити його за хвилину. Для MCU артефакт має дійти до фізичного пристрою через bootloader, а сам шлях оновлення – найризикованіша частина системи: невдале оновлення в полі може перетворити пристрій на "цеглу", і відкотити його віддалено вже нічим. Тому Continuous Delivery для firmware – це не лише автоматична збірка, а автоматична перевірка того самого шляху оновлення, яким пройде реліз, на реальному hardware.

### Етапи pipeline

1. **Збірка** у CI-матриці (qid:emb-build-0022) дає незмінний артефакт: ELF із символами, образ для прошивання, map-файл і маніфест із версією та commit hash. Далі по конвеєру рухається саме цей артефакт, а не перезібраний.
2. **Підпис.** Для MCUboot образ підписує `imgtool sign`; обов’язкові параметри – версія, розмір заголовка і розмір слота, ключ задається `--key`. Підтримуються ключі RSA-2048, RSA-3072, ECDSA P-256 і Ed25519. Приватний ключ має бути захищеним; development-ключ, що поставляється з MCUboot, широко поширений і ніколи не повинен використовуватися в production. `imgtool getpub` експортує публічний ключ у C-структуру, тож збірці bootloader не потрібен приватний ключ – він може бути лише в release-команди.[^mcuboot-imgtool] У CI підпис релізу виконують в окремій захищеній job.
3. **Доставка на стенд** – тим самим транспортом, що і в полі (UART, USB DFU, BLE, мережа), а не лише через debug probe. Probe лишається для початкового прошивання і відновлення стенда.
4. **Тести** – smoke, функціональні HIL-тести, перевірка версії, яку повідомляє сам пристрій.
5. **Просування** – поетапне розгортання: спершу внутрішні пристрої, потім невелика частка парку, потім усі.

```sh
imgtool sign --key release.pem --version 1.4.0 --header-size 0x200 \
    --pad-header --slot-size 0x60000 build/app.bin build/app.signed.bin
west twister --device-testing --hardware-map map.yml -T tests/smoke
```

### Bootloader, rollback і що саме перевіряти

MCUboot при swap-оновленні може виконати "test" swap: новий образ переноситься в primary slot і запускається, а потім мусить сам позначити себе "OK". Якщо цього не сталося, на наступному завантаженні bootloader робить "revert" swap і повертає старий образ. Документація прямо пояснює мету: якщо пристрій падає одразу після запуску поганого образу, після reset він повернеться до робочої версії, а прошивка може зробити swap постійним лише після self-test. Bootloader також має коректно працювати, якщо reset стався посеред swap.[^mcuboot-design] Захист від downgrade буває програмним (порівняння версій, лише зі стратегією overwrite-only) або апаратним: security counter у захищеній TLV-області образу порівнюється зі значенням у довіреній енергонезалежній пам’яті.[^mcuboot-design]

Отже, release gate перевіряє не "чи зібралося", а сценарії оновлення:

| Сценарій | Очікуваний результат |
|---|---|
| оновлення N-1 до N штатним транспортом | пристрій працює на N, версія підтверджена |
| новий образ навмисно не підтверджує себе | після reset повертається N-1 |
| вимкнення живлення в випадковий момент swap | пристрій завантажується в N-1 або N, без "цегли" |
| образ, підписаний чужим ключем | bootloader відмовляється його запускати |
| спроба downgrade (якщо ввімкнено захист) | оновлення відхилене |

Підтвердження образу не слід ставити першим рядком `main()`: воно має відбуватися після self-test, наприклад коли пристрій ініціалізував периферію і підключився до сервера. Інакше rollback не захищає від образу, який стартує, але не виконує основної функції.

### Стенд hardware-in-the-loop

Типовий стенд: пристрій під тестом; debug probe для відновлення і crash dump; USB-UART для логів; кероване живлення (реле або програмоване джерело) для power cycling і вимірювання струму; керування reset і boot-виводами з GPIO; обв’язка для стимуляції входів (loopback, імітатори сенсорів); host із self-hosted runner CI.

Zephyr Twister показує, як це формалізують. Hardware map – файл зі списком підключених пристроїв, їхніх послідовних портів і ідентифікаторів; fixtures описують спеціальну обв’язку, яку вимагає тест (наприклад, `gpio_loopback`), і тест запускається лише на платі, що її має. Опція `flash_before` прошиває пристрій до відкриття послідовного порту, щоб уникнути від’єднання порту під час прошивання на платах із USB CDC.[^zephyr-twister]

Стенд сам по собі ненадійний: зависає USB-хаб, злітає probe. Тому pipeline має відрізняти збій інфраструктури від збою тесту: health-check стенда перед прогоном, автоматичне відновлення через probe (повне стирання і заводський образ), карантин несправного стенда замість червоного релізу.

### Що очікують почути на співбесіді

Кандидат має пояснити: один незмінний артефакт від збірки до релізу; підпис із захищеним ключем; тести того самого шляху оновлення, що в полі, включно з rollback, обривом живлення і чужим підписом; HIL-стенд із керованими живленням, reset і логами; відокремлення збоїв стенда від збоїв firmware; поетапне розгортання.
