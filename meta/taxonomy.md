# Таксономія: треки й секції

Єдине оголошення того, які треки й секції існують і в якому порядку їх читати. Кожен рядок у
блоках нижче – це і назва теки в `content/{en,uk}/`, і сегмент URL. Порядок рядків – це порядок
у навігації сайту й у номерах колод Anki (`tools/iqa/taxonomy.py`), тож сортувати їх за
алфавітом не можна. Правила іменування – у `meta/questions.md`.

Секція може бути порожньою: на сайті й у колоді вона з'являється разом із першим питанням.
Новий трек додається новим блоком тут, мітками й префіксами в `meta/vocabulary.yml` і префіксом
ID у `tools/iqa/model.py`.

Треки: `python`, `embedded`, `electronics` – у порядку їхніх блоків нижче.

## `python/`

```
python/
  fundamentals/                 модель виконання, bytecode, CPython vs інші рантайми
  syntax-and-control-flow/
  objects-and-types/            id, type, mutability, truthiness
  collections/                  list, tuple, dict, set, deque, namedtuple
  strings-and-text/             encoding, str vs bytes, f-strings, normalization
  functions-and-scope/          аргументи, замикання, LEGB
  oop-and-data-model/           dunder, MRO, descriptors, dataclasses, slots
  typing-and-annotations/       typing, Protocol, Generic, mypy/pyright
  decorators/
  iterators-and-generators/
  context-managers/
  exceptions/
  modules-and-imports/          import system, packages, циклічні імпорти
  packaging-and-environments/   venv, pip, uv, pyproject, wheels, версіонування
  files-and-io/
  comprehensions-and-functional/
  cpython-internals/            refcount, GC, memory arenas, інтернування
  concurrency-and-gil/          threads, processes, GIL, free-threaded build
  asyncio/
  standard-library/
  testing/                      pytest, fixtures, mocks, parametrize
  performance/                  профілювання, оптимізація, C-розширення
  practical-coding/             задачі «напиши код» на інтерв'ю
  frameworks/                   Python-специфічні бібліотеки (pydantic тощо)
```

## `embedded/`

```
embedded/
  # Phase 1: C/C++ Foundations - структура джерела Embedded Interview Lab,
  # збережена один в один. Порядок тут - порядок навчання.
  data-types-and-memory-layout/     типи, представлення, layout структур у пам'яті
  pointers-and-arrays/              вказівники, масиви, адресна арифметика
  structs-unions-and-bitfields/     агрегати, packed, бітові поля
  volatile-and-const/               volatile, const, їхня взаємодія й типові помилки
  function-pointers-and-callbacks/  вказівники на функції, таблиці, callbacks
  inline-and-macros/                препроцесор, inline, макроси проти функцій
  memory-alignment-and-endianness/  вирівнювання, padding, порядок байтів
  common-code-patterns/             типові прийоми C у прошивках
  cpp-classes-and-oop/              класи, віртуальність, ціна ООП на MCU
  raii-and-smart-pointers/          RAII, unique_ptr, володіння без heap
  templates-and-constexpr/          шаблони, constexpr, обчислення на етапі компіляції
  cpp-embedded-constraints-and-stl/ exceptions/RTTI, STL і статична алокація
  fundamentals/                 MCU vs MPU vs SoC, bare-metal vs RTOS vs Linux, крос-компіляція
  toolchain-and-build/          GCC/Clang для ARM, лінкер, флаги, розмір бінаря
  c-in-embedded/                volatile, const, бітові поля, фіксована точка, freestanding
  cpp-in-embedded/              чому вимикають exceptions/RTTI, constexpr, статична алокація
  memory-and-linker/            linker script, секції .text/.data/.bss, startup code, стек vs купа
  interrupts-and-timing/        ISR, латентність, пріоритети, критичні секції, WCET
  peripherals-and-buses/        GPIO, UART, SPI, I2C, CAN, USB, DMA, ADC
  rtos/                         планування, пріоритетна інверсія, черги, семафори
    freertos/
    zephyr/
  power-management/             режими сну, wake-up, бюджет енергії
  bootloaders-and-ota/          завантажники, оновлення прошивки, відкат, підпис
  debugging-and-tracing/        JTAG/SWD, gdb, логічний аналізатор, трасування
  testing-embedded/             HIL, симуляція, mock-и периферії, unit-тести без заліза
  safety-and-standards/         MISRA C/C++, IEC 61508, ISO 26262, DO-178C, AUTOSAR
  connectivity/                 BLE, Wi-Fi, LoRa, MQTT, Modbus
  hardware-basics/              для прошивників: рівні, підтяжки, живлення, осцилограма
  linux-embedded/               P2: Yocto, buildroot, device tree, драйвери
```

## `electronics/`

```
electronics/
  introduction/                 розділ 2: компоненти, закон Ома, джерела, діоди, BJT, MOSFET, інструменти
  circuit-analysis/             розділ 3: KCL/KVL, змішані кола, подільники напруги, SPICE
  ee101/                        розділ 4: перемикачі, RC/RL, фазори, фільтри, живлення, каскади, логіка, 555
  digital-logic/                розділ 5: булева алгебра, системи числення, часові діаграми, TTL
  digital-integration/          розділ 6: SSI/MSI/LSI, комбінаційні й послідовні мікросхеми 74xx
  pcb-design/                   розділ 7: основи PCB, CircuitMaker, розбір плат
  circuitmaker-projects/        розділ 8: схеми, розводка й Gerber у CircuitMaker
```
