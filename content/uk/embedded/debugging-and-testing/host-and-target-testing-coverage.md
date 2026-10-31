---
id: emb-testemb-0002
title: "Як тестувати embedded C-код на host і на target, і що саме має покривати кожен рівень?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: zephyr-ztest
    title: "Zephyr Project documentation: Test Framework (Ztest)"
    url: https://docs.zephyrproject.org/latest/develop/test/ztest.html
  - source_id: zephyr-native-sim
    title: "Zephyr Project documentation: Native simulator - native_sim"
    url: https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html
  - source_id: zephyr-posix-arch
    title: "Zephyr Project documentation: The POSIX architecture"
    url: https://docs.zephyrproject.org/latest/boards/native/doc/arch_soc.html
  - source_id: zephyr-twister
    title: "Zephyr Project documentation: Test Runner (Twister)"
    url: https://docs.zephyrproject.org/latest/develop/twister/index.html
  - source_id: zephyr-coverage
    title: "Zephyr Project documentation: Generating coverage reports"
    url: https://docs.zephyrproject.org/latest/develop/test/coverage.html
---

## Short answer

**Host tests** покривають чисту логіку: state machines, parsers, protocol framing, boundary cases, mocks для HAL/MMIO. **Target tests** перевіряють те, що залежить від заліза: clocks, drivers, DMA, ISR latency, buses, power states і real timing. HIL або board tests мають ловити інтеграційні дефекти, які unit tests на PC не бачать.[^dou-embedded-interview]

## Detailed explanation

Тестування embedded C-коду будують як кілька рівнів, бо жоден з них окремо не бачить усіх дефектів. Чим ближче до заліза, тим тест дорожчий, повільніший і рідше запускається, але тим більше реальних ефектів він охоплює. Добра стратегія розкладає перевірки так, щоб кожен дефект ловився на найдешевшому рівні, який здатен його побачити.

### Рівень 1: unit tests на host

На host компілюють окремий модуль звичайним компілятором ПК і запускають тисячі тестів за секунди. Сюди належить усе, що не залежить від заліза: state machines, parsers, protocol framing і CRC, фільтри та арифметика з граничними значеннями (переповнення, нулі, максимальна довжина кадру), обробка помилок.

Zephyr для цього має pseudo-board `unit_testing`: це не залізо і не симулятор, а ціль з `arch: unit`, яка збирає модуль host-toolchain у звичайний виконуваний файл, причому ядро Zephyr не збирається взагалі. Залежності модуля замінюють stubs або mocks на основі FFF (Fake Function Framework), інтегрованого в Ztest.[^zephyr-ztest] Щоб це працювало, код має бути розділений: логіка окремо, доступ до регістрів і HAL – за тонким інтерфейсом (qid:emb-testemb-0006).

Обмеження рівня: інший компілятор і інша архітектура. Розміри типів на кшталт `long`, вирівнювання, порядок байтів і implementation-defined поведінка на host і на MCU можуть не збігатися, тому код, що залежить від них, на host перевірено лише частково.

### Рівень 2: симуляція та емуляція

Наступний рівень запускає весь firmware з RTOS, але без реальної плати: QEMU для емуляції конкретної архітектури або `native_sim`, який компілює застосунок разом з ядром Zephyr у звичайний Linux-виконуваний файл.[^zephyr-native-sim] Тут перевіряють взаємодію tasks, черги, таймаути, протокольні сценарії й інтеграцію модулів.

Важливо розуміти модель часу. Документація POSIX-архітектури Zephyr, на якій побудовано `native_sim`, описує код як такий, що виконується за нульовий симульований час; переривання, зокрема таймерні, не надходять, поки код виконується, а busy-wait цикли перетворюються на нескінченні. Код, що залежить від власної швидкості виконання, зазвичай не працює так, як очікується.[^zephyr-posix-arch] Отже, цей рівень не підтверджує ні timing, ні гонки з перериваннями.

### Рівень 3: тести на target

На реальній платі перевіряють те, що існує лише в залізі:

- конфігурацію clock tree і PLL, старт після reset і після brown-out;
- драйвери з реальною периферією: UART, SPI, I2C, ADC, таймери, DMA;
- латентність ISR і jitter (вимірюють осцилографом або logic analyzer за перемиканням GPIO);
- входи в low-power режими і вихід з них, wake-up sources;
- запис у flash, bootloader, спрацювання watchdog.

Zephyr Twister запускає ті самі тестові застосунки або в емульованому середовищі, або на реальних пристроях: для цього складають hardware map підключених плат і запускають з `--device-testing`. Результат зчитується harness-ом, який розбирає вивід консолі (`ztest`, `console`) або делегує виконання зовнішньому фреймворку, наприклад pytest.[^zephyr-twister]

### Рівень 4: HIL і системні тести

Hardware-in-the-loop підключає плату до стенда, що імітує датчики, навантаження і мережу. Тут перевіряють поведінку при відмовах (обрив шини, просідання живлення, шум), тривалі прогони на витоки пам’яті й накопичення помилок, повні сценарії з вимог.

### Coverage

Coverage найпростіше отримати на host і в симуляції. У Zephyr для `native_sim` gcov пише звичайні `gcda`-файли; для вбудованих цілей дані gcov збираються в RAM і виводяться через консоль, підтримка обмежена обсягом RAM і, згідно з документацією, наразі ввімкнена лише для QEMU-емуляції вбудованих цілей.[^zephyr-coverage] Тому покриття апаратно-залежного коду зазвичай підтверджують не відсотком рядків, а переліком сценаріїв на target, прив’язаних до вимог.

### Що хоче почути інтерв’юер

Чіткий розподіл: host – логіка й граничні випадки з mocks, симуляція – інтеграція без реального часу, target – залізо, timing і power, HIL – система й відмови. Плюс розуміння, що зелені host-тести не доводять коректності драйверів чи ISR, і що архітектура коду (відокремлення логіки від HAL) визначає, скільки можна перевірити дешево.
