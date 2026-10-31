---
id: emb-build-0022
title: "Як налаштувати CI для збірки firmware під кілька target-платформ і toolchains?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: github-actions-matrix
    title: "GitHub Docs: Running variations of jobs in a workflow"
    url: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations
  - source_id: cmake-toolchains
    title: "CMake documentation: cmake-toolchains(7)"
    url: https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html
  - source_id: reproducible-builds-sde
    title: "Reproducible Builds: SOURCE_DATE_EPOCH"
    url: https://reproducible-builds.org/docs/source-date-epoch/
  - source_id: zephyr-twister
    title: "Zephyr Project documentation: Test Runner (Twister)"
    url: https://docs.zephyrproject.org/latest/develop/twister/index.html
---

## Short answer

CI має матрицю **target x toolchain x config**: наприклад GCC/Clang, debug/release, board variants. Кожна job ставить pinned toolchain, запускає configure/build, static analysis, unit tests і збирає artifacts: ELF, HEX/BIN, map, logs. Для target-only перевірок окремо підключають HIL runners або nightly hardware jobs.[^dou-embedded-interview]

## Detailed explanation

### Осі матриці

Firmware рідко збирається в одному варіанті. Типові осі:

- **target** – плата, модель MCU, ревізія hardware;
- **toolchain** – GCC певної версії, Clang, іноді комерційний компілятор виробника;
- **configuration** – Debug/Release, набори feature flags, варіант bootloader чи застосунку;
- **host** – окремі job-и з unit-тестами на host-і, яким target не потрібен.

Повний декартів добуток швидко вибухає, тому матрицю обрізають: непотрібні комбінації виключають, а повний набір запускають рідше (nightly), залишаючи на pull request критичний мінімум.

### Матриця в CI-системі

У GitHub Actions `strategy.matrix` створює окремий запуск job для кожної комбінації змінних; `exclude` прибирає комбінації, причому достатньо часткового збігу, а `include` додає або доповнює їх. `fail-fast: true` скасовує job-и, що виконуються або стоять у черзі, якщо одна з них впала, а `continue-on-error` дозволяє позначити експериментальні комбінації, падіння яких не зупиняє решту.[^github-actions-matrix]

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container: ghcr.io/example/fw-toolchain:gcc-13.3-cmake-3.28
    strategy:
      fail-fast: false
      matrix:
        board: [nucleo_f411re, custom_rev_b]
        toolchain: [gcc, clang]
        build_type: [Debug, Release]
        exclude:
          - board: custom_rev_b
            toolchain: clang
    steps:
      - uses: actions/checkout@v4
      - run: arm-none-eabi-gcc --version
      - run: >
          cmake -S . -B build
          -DCMAKE_TOOLCHAIN_FILE=cmake/${{ matrix.toolchain }}-arm.cmake
          -DBOARD=${{ matrix.board }}
          -DCMAKE_BUILD_TYPE=${{ matrix.build_type }}
      - run: cmake --build build
      - uses: actions/upload-artifact@v4
        with:
          name: fw-${{ matrix.board }}-${{ matrix.toolchain }}-${{ matrix.build_type }}
          path: |
            build/*.elf
            build/*.hex
            build/*.map
```

Тут 2 × 2 × 2 = 8 комбінацій, а `exclude` за частковим збігом прибирає обидві збірки `custom_rev_b` з Clang, тож запускається 6 job-ів. `fail-fast: false` вибрано свідомо: для firmware корисно бачити всі зламані комбінації одразу, а не лише першу.

### Закріплений toolchain

Збірка має бути відтворюваною, тому toolchain не встановлюють "останньої версії" з пакетного менеджера, а беруть із контейнерного образу або архіву з точною версією. Версію варто друкувати в лог кожної job: `--version` виводить версію GCC, а `-v` – ще й команди, які драйвер запускає на кожній стадії компіляції.[^gcc-overall-options]

Для CMake перемикання компілятора робиться toolchain file: його передають через `-DCMAKE_TOOLCHAIN_FILE=...` (або `--toolchain`), він завантажується рано і задає компілятори та утиліти; коли CMake виконує крос-компіляцію, змінна `CMAKE_CROSSCOMPILING` стає істинною.[^cmake-toolchains] Для bare-metal target у такому файлі зазвичай задають `CMAKE_SYSTEM_NAME` зі значенням `Generic`, як це показано, наприклад, для компіляторів Renesas.[^cmake-toolchains]

Окремий аспект відтворюваності – дати й час, які потрапляють у бінарник. `SOURCE_DATE_EPOCH` – стандартизована змінна середовища з часом останньої зміни вихідного коду в секундах від Unix epoch, яку інструменти збірки використовують замість поточного часу.[^reproducible-builds-sde] Якщо дві збірки одного commit дають різні хеші, CI має це помітити: це або недетермінований крок, або різне середовище.

### Що робить кожна job

1. Configure і build з тими самими прапорцями, що й у локальній збірці розробника.
2. Перевірка розміру: заповнення flash і RAM із map-файлу, з порогом, щоб помітити регресію ще до того, як образ перестане влазити.
3. Статичний аналіз і попередження компілятора; Clang у матриці корисний навіть без релізу під нього, бо дає іншу діагностику.
4. Host unit-тести – один раз, а не для кожного target.
5. Артефакти: ELF із debug-символами (для налагодження і розбору crash dump), HEX/BIN для прошивання, map-файл, журнал збірки, версія toolchain і commit hash.

### Приклад інструменту: Zephyr Twister

Twister за замовчуванням збирає тестові застосунки для плат, позначених як default, і запускає їх в емуляторі (QEMU, `native_sim`), якщо він доступний; інакше тест лише збирається. Опція `--platform` обмежує набір плат, а `build_toolchains` у конфігурації платформи створює окремий екземпляр тесту для кожного toolchain, наприклад GCC і Clang для `native_sim`.[^zephyr-twister] Той самий інструмент вміє запускати тести на реальних платах (`--device-testing`, hardware map, fixtures для спеціальної обв’язки)[^zephyr-twister], що вже наближає CI до hardware-in-the-loop (qid:emb-build-0025).

### Що очікують почути на співбесіді

Матриця з обґрунтованими осями і обрізанням, закріплені версії toolchain у контейнері, toolchain files замість хардкоду компілятора, повний набір артефактів із ELF і map, розділення швидкого PR-контуру і повного nightly-прогону, а також окремий шар тестів на реальному hardware, який не блокує збірку, коли стенд недоступний.
