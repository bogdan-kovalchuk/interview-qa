---
id: emb-testemb-0008
title: "Які dynamic analysis підходи можливі для embedded C/C++: sanitizers на host, Valgrind, trace, fault injection?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
  - source_id: clang-asan
    title: "Clang documentation: AddressSanitizer"
    url: https://clang.llvm.org/docs/AddressSanitizer.html
  - source_id: clang-ubsan
    title: "Clang documentation: UndefinedBehaviorSanitizer"
    url: https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html
  - source_id: clang-tsan
    title: "Clang documentation: ThreadSanitizer"
    url: https://clang.llvm.org/docs/ThreadSanitizer.html
  - source_id: zephyr-native-sim
    title: "Zephyr Project documentation: Native simulator - native_sim"
    url: https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html
  - source_id: valgrind-memcheck
    title: "Valgrind User Manual: Memcheck, a memory error detector"
    url: https://valgrind.org/docs/manual/mc-manual.html
  - source_id: gcc-instrumentation-options
    title: "GCC manual: Program Instrumentation Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
  - source_id: zephyr-thread-analyzer
    title: "Zephyr Project documentation: Thread analyzer"
    url: https://docs.zephyrproject.org/latest/services/debugging/thread-analyzer.html
  - source_id: gdb-set-watchpoints
    title: "Debugging with GDB: Setting Watchpoints"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Set-Watchpoints.html
  - source_id: zephyr-coverage
    title: "Zephyr Project documentation: Generating coverage reports"
    url: https://docs.zephyrproject.org/latest/develop/test/coverage.html
  - source_id: zephyr-kconfig-init-stacks
    title: "Zephyr Project documentation: Kconfig CONFIG_INIT_STACKS"
    url: https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INIT_STACKS
---

## Short answer

На host можна запускати **ASan/UBSan/TSan** для логіки без hardware dependency, а `Valgrind` корисний для Linux-target або host-сценаріїв. На target частіше використовують trace, coverage, watchpoints, stack watermarking, fault injection, bus/error simulation і HIL tests. <span class="warn">Sanitizer на PC не доводить коректність ISR, DMA cache coherency або реального timing.</span>[^dou-embedded-interview]

## Detailed explanation

Dynamic analysis перевіряє програму під час виконання, тому вона бачить те, що static analysis може лише запідозрити: реальний вихід за межі буфера, використання звільненої пам’яті, гонку між потоками. Для embedded головне обмеження в тому, що найпотужніші інструменти потребують ОС, багато пам’яті й запасу швидкодії, яких на MCU немає. Тому підходи ділять на дві групи: що запускають на host, і що працює на самій цілі.

### На host: sanitizers

Логіку, відокремлену від заліза, збирають для ПК (unit-тести або симуляція на кшталт `native_sim`) і запускають з інструментуванням компілятора:

- **AddressSanitizer (ASan)** ловить вихід за межі heap, stack і глобальних об’єктів, use-after-free, use-after-return, use-after-scope, double free і (експериментально) витоки. Типове сповільнення – близько 2x, а використання stack може зрости до 3x.[^clang-asan]
- **UndefinedBehaviorSanitizer (UBSan)** виявляє undefined behavior під час виконання: переповнення знакових цілих, некоректні зсуви, невирівняні та нульові вказівники.[^clang-ubsan]
- **ThreadSanitizer (TSan)** шукає data races; сповільнення близько 5–15x, пам’ять зростає в 5–10x, а 32-бітні платформи не підтримуються й не плануються.[^clang-tsan]

Zephyr дозволяє ввімкнути ASan (`CONFIG_ASAN`) і UBSan (`CONFIG_UBSAN`) для `native_sim`, а оскільки збірка є звичайним Linux-застосунком, її можна налагоджувати й інструментувати як будь-яку нативну програму, наприклад через gdb або Valgrind.[^zephyr-native-sim]

### Valgrind

Memcheck з Valgrind виявляє доступ до пам’яті поза межами блоків, використання неініціалізованих значень, некоректне звільнення heap, перекриття буферів у `memcpy` і витоки.[^valgrind-memcheck] Valgrind виконує процес під своїм контролем в ОС, тому його поле – host-збірки та embedded Linux, а не bare-metal MCU.

### На target: що реально доступно

- **UBSan у trap-режимі.** GCC з `-fsanitize-trap` замість виклику runtime-бібліотеки вставляє `__builtin_trap`; `libubsan` тоді не потрібна і не лінкується, тож режим придатний навіть для freestanding-середовищ.[^gcc-instrumentation-options] Clang має для подібних випадків trap mode і мінімальний runtime.[^clang-ubsan]
- **Stack protector.** `-fstack-protector` додає guard-змінну в функції з вразливими об’єктами і перевіряє її при виході.[^gcc-instrumentation-options] Це ловить частину переповнень буферів на stack, але не переповнення всього stack task-а.
- **Stack watermarking.** Stack заздалегідь заповнюють відомим значенням і згодом шукають межу, до якої його перезаписано. У Zephyr опція `CONFIG_INIT_STACKS` заповнює stacks потоків і stack переривань значенням `0xaa` саме для визначення high water mark,[^zephyr-kconfig-init-stacks] а thread analyzer виводить для кожного потоку використаний і вільний обсяг stack.[^zephyr-thread-analyzer]
- **Hardware watchpoints.** Debug-блок ядра зупиняє виконання при записі в конкретну адресу, наприклад у межу stack або в змінну, яку хтось псує. GDB пояснює, що hardware watchpoints працюють швидко, тоді як software watchpoints, що виконують програму покроково, у сотні разів повільніші, а кількість апаратних обмежена.[^gdb-set-watchpoints]
- **Coverage на цілі.** `-fprofile-info-section` розміщує інформацію профілю в окремій секції замість constructors і destructors і, за документацією GCC, призначена саме для freestanding-середовищ на кшталт embedded систем.[^gcc-instrumentation-options] У Zephyr дані gcov збираються в RAM, тож підтримка обмежена її обсягом.[^zephyr-coverage]
- **Trace.** `-finstrument-functions` викликає hooks на вході й виході кожної функції,[^gcc-instrumentation-options] а апаратний trace (ITM/SWO, ETM на ядрах, що його мають) та RTOS-trace показують послідовність подій без зупинки ядра.

### Fault injection

Окремий клас – свідоме введення відмов: fake HAL повертає timeout або NACK, тест псує CRC пакета, переповнює чергу, імітує відмову `malloc`. На стенді HIL додають апаратні відмови: просідання живлення, обрив шини, шум. Мета – переконатися, що кожна гілка помилки досяжна і веде до передбаченого стану, а не лише до того, що код компілюється.

### Межі підходу

Sanitizer на ПК перевіряє логіку на іншій архітектурі з іншим компілятором і без справжнього заліза. Він не бачить гонок між ISR і task, бо на host немає апаратних переривань; не бачить проблем когерентності cache з DMA; не перевіряє реального timing. TSan моделює потоки ОС, а не переривання MCU. Тому інтерв’юер очікує комбінації: sanitizers і Valgrind для логіки на host, легкі механізми (trap, watermark, watchpoints, trace) на target і fault injection з HIL для поведінки при відмовах.
