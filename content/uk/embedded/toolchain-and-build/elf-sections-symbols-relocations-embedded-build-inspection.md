---
id: emb-build-0014
title: "Що таке ELF-файл і яку інформацію в ньому корисно дивитися для embedded build?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: linux-man-elf
    title: "Linux manual page: elf(5)"
    url: https://man7.org/linux/man-pages/man5/elf.5.html
---

## Short answer

**ELF** – object/executable формат із headers, sections, symbols, relocations і debug info. В embedded дивляться entry point, section sizes/addresses, symbol table, vector table placement і чи `.data/.bss` потрапили в правильну RAM. Корисні команди: `readelf -S`, `readelf -s`, `objdump -d`, `size`.[^dou-embedded-interview]

## Detailed explanation

### Структура формату ELF (Executable and Linkable Format)

Формат **ELF** є стандартним двійковим форматом для об’єктних модулів, виконуваних файлів прошивок та динамічних бібліотек у сучасних вбудованих системах[^linux-man-elf].
У структурі ELF виділяють дві різні перспективи представлення (linking view та execution view):
1. **ELF Header**: фіксована за розміром структура на початку файлу, що містить магічні байти (`0x7F 'E' 'L' 'F'`), архітектуру процесора (`e_machine`), розрядність (32 чи 64 біти), порядок байтів (endianness), адресу точки входу програми (`e_entry`), а також зміщення до таблиць Program Header Table та Section Header Table.
2. **Program Header Table (PHT)**: описує сегменти (segments) для завантажувача або прошивальника. Кожен сегмент типу `PT_LOAD` визначає блок пам’яті, його зміщення у файлі, віртуальну адресу в пам’яті (VMA), адресу фізичного завантаження (LMA), розміри та права доступу (читання, запис, виконання).
3. **Section Header Table (SHT)**: описує секції (sections) для компонувальника та налагоджувача. Містить імена секцій, їхні типи (`SHT_PROGBITS`, `SHT_NOBITS`), атрибути (`SHF_ALLOC`, `SHF_WRITE`, `SHF_EXECINSTR`), адреси прив’язки та розміри[^linux-man-elf].

### Ключові секції в Embedded-розробці та їхнє розміщення

Під час аналізу скомпільованої прошивки мікроконтролера ключову роль відіграють такі секції:
- **`.text`**: машинний код інструкцій процесора та таблиця векторів переривань (`.isr_vector`). Зазвичай розміщується в енергонезалежній Flash-пам’яті з атрибутами читання та виконання (RX).
- **`.rodata`**: константи, рядкові літерали, таблиці коефіцієнтів і калібрувань. Зберігається у Flash без прав запису (R).
- **`.data`**: статичні та глобальні змінні з явними ненульовими початковими значеннями. Має початковий образ завантаження (LMA) у Flash-пам’яті та адресу виконання (VMA) в оперативній пам’яті RAM (RW).
- **`.bss`**: неініціалізовані або ініціалізовані нулями глобальні змінні. У самому файлі ELF не займає місця для даних (тип `SHT_NOBITS`), але резервує адресний простір у RAM.
- **`.ARM.exidx` / `.ARM.extab`**: таблиці для розгортання стека (stack unwinding) при обробці виключень у C++. Якщо в проекті C++ виключення заборонені прапорцем `-fno-exceptions`, ці секції можна відкинути в linker script для економії Flash.
- **Налагоджувальні секції (`.debug_*`)**: метадані формату DWARF (назви змінних, прив’язка рядків C-коду до адрес). Вони необхідні налагоджувачу (GDB), проте ніколи не завантажуються в пам’ять мікроконтролера.

### Яку інформацію перевіряти в ELF для Embedded Build

При побудові та перевірці вбудованого ПЗ перевіряють такі критичні параметри:
1. **Точка входу (`Entry point address`) та таблиця векторів**:
   Для ядер ARM Cortex-M точка входу має вказувати на функцію `Reset_Handler`. Адреса повинна знаходитися у діапазоні пам’яті виконання (наприклад `0x08000000` для STM32 або відповідний offset для bootloader), а молодший біт адреси обов’язково має дорівнювати 1, що сигналізує про виконання в режимі Thumb.
2. **Розподіл і баланс пам’яті (Footprint)**:
   Перевірка сумарного використання пам’яті: Flash = `.text` + `.rodata` + `.data`; RAM = `.data` + `.bss` + резерв під стек і купу. Необхідно переконатися, що дані не виходять за фізичні межі внутрішньої SRAM чіпа.
3. **Таблиця символів (`Symbol Table`, `.symtab`)**:
   Пошук несподіваних глобальних змінних величезного розміру, які роздувають оперативну пам’ять, або функцій стандартної бібліотеки (наприклад, важкого `sprintf` з підтримкою чисел з плаваючою комою), що випадково потрапили в збірку.
4. **Перевірка релокацій (`Relocations`)**:
   У проміжних об’єктних файлах (`.o`) інспекція секцій `.rel.*` дозволяє зрозуміти, які функції чи змінні ще не зв’язані та очікують дозволу від компонувальника.

### Практичний інструментарій інспекції

Для аналізу ELF-файлів використовують утиліти GNU Binutils:
- `arm-none-eabi-size -B firmware.elf`: показує класичний компактний підсумок Berkeley (розміри `text`, `data`, `bss`, `dec`, `hex`).
- `arm-none-eabi-readelf -l firmware.elf`: інспектує заголовки сегментів (Program Headers), зіставляючи фізичні адреси (PhysAddr / LMA) та віртуальні адреси (VirtAddr / VMA).
- `arm-none-eabi-readelf -S firmware.elf`: повна таблиця секцій із прапорцями пам’яті.
- `arm-none-eabi-nm --size-sort -S -C firmware.elf`: виводить перелік усіх функцій і змінних, відсортованих за їхнім розміром у байтах, що є головним інструментом пошуку "витоків" розміру прошивки[^dou-embedded-interview].
