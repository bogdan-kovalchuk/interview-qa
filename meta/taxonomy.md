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
  functions-and-scope/          аргументи, замикання, LEGB
  oop-and-data-model/           dunder, MRO, descriptors, dataclasses, slots
  decorators/
  iterators-and-generators/
  context-managers/
  exceptions/
  modules-and-imports/          import system, packages, циклічні імпорти
  files-and-io/
  comprehensions-and-functional/
  cpython-internals/            refcount, GC, memory arenas, інтернування
  concurrency-and-gil/          threads, processes, GIL, free-threaded build
  asyncio/
  standard-library/
  testing/                      pytest, fixtures, mocks, parametrize
  performance/                  профілювання, оптимізація, C-розширення
  practical-coding/             задачі «напиши код» на інтерв'ю
```

## `embedded/`

```
embedded/
  # Від простого до складного: основи, 12 тем C/C++ з Embedded Interview Lab у його
  # порядку (спершу Foundational, далі Intermediate), система, далі складніші теми.
  fundamentals/                      MCU vs MPU vs SoC, bare-metal vs RTOS vs Linux, архітектура
  data-types-and-memory-layout/      типи, класи пам'яті, stack і heap, де живе змінна
  pointers-and-arrays/               вказівники, масиви, адресна арифметика
  volatile-and-const/                volatile, const, регістри, змінні спільні з ISR
  cpp-classes-and-oop/               класи, віртуальність, ціна ООП на MCU
  structs-unions-and-bitfields/      агрегати, packed, бітові поля
  cpp-embedded-constraints-and-stl/  exceptions/RTTI, STL і статична алокація
  common-code-patterns/              state machines, ring buffers, бітові операції
  function-pointers-and-callbacks/   вказівники на функції, таблиці, callbacks
  memory-alignment-and-endianness/   вирівнювання, padding, порядок байтів
  raii-and-smart-pointers/           RAII, unique_ptr, володіння без heap
  templates-and-constexpr/           шаблони, constexpr, обчислення на етапі компіляції
  inline-and-macros/                 препроцесор, inline, макроси проти функцій
  toolchain-and-build/               компілятор, лінкер, ELF, ABI
  interrupts-and-timing/             ISR, латентність, пріоритети, критичні секції
  peripherals-and-buses/             GPIO, UART, SPI, I2C, CAN, DMA, ADC
  hardware-and-power/                рівні, підтяжки, режими сну, енергоспоживання
  rtos-and-operating-systems/        планування, синхронізація, процеси й потоки, Linux
  connectivity/                      мережеві протоколи, BLE, Wi-Fi
  debugging-and-testing/             JTAG/SWD, gdb, тестування, git і CI
  safety-security-and-reliability/   MISRA, watchdog, завантажувачі, OTA
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
