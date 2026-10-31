---
id: emb-cppstl-0020
title: "Що робить `-fno-threadsafe-statics`?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: gcc-cxx-dialect
    title: "GCC: C++ Dialect Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI: Once-only Construction API"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html#once-ctor
---

## Short answer

**Прибирає mutex-захист навколо ініціалізації function-local static.**

За замовчуванням компілятор додає guard (можливо з pthread), щоб два потоки не ініціалізували static одночасно. На bare-metal без потоків це зайвий код і залежність.

Правило: `-fno-threadsafe-statics` доречний, коли немає конкурентного доступу до lazy-init static (single-threaded bare-metal).[^embeddedinterviewlab]

## Detailed explanation

### Стандарт C++ та потокобезпечна ініціалізація локальних статичних змінних

Починаючи зі стандарту C++11 (правило «Magic Statics», [stmt.dcl])[^iso-cpp-n4861], ініціалізація локальних статичних об’єктів у функціях гарантовано є потокобезпечною. Якщо кілька потоків одночасно викликають функцію:
```cpp
UartDriver& get_driver() {
    static UartDriver instance(USART1);
    return instance;
}
```
стандарт гарантує, що конструктор `UartDriver` виконається рівно один раз одним потоком, а решта потоків чекатимуть завершення ініціалізації.

Згідно зі специфікацією Itanium C++ ABI[^itanium-cxx-abi], для реалізації цієї гарантії компілятор створює 64-бітну службову змінну-сторож (`guard variable`) та огортає виклик конструктора викликами функцій підтримки середовища виконання:
```cpp
if (__cxa_guard_acquire(&guard) != 0) {
    try {
        instance.UartDriver(USART1);
        __cxa_guard_release(&guard);
    } catch (...) {
        __cxa_guard_abort(&guard);
        throw;
    }
}
```

### Проблема на bare-metal мікроконтролерах

У стандартних бібліотеках C++ реалізація `__cxa_guard_acquire` та `__cxa_guard_release` спирається на блокування операційної системи (наприклад, POSIX mutex або системні виклики `futex`).

У вбудованій системі без повноцінної ОС виникають дві проблеми:
1. **Помилки компонування (Linker errors)**: з’являються невизначені посилання `undefined reference to '__cxa_guard_acquire'` та `undefined reference to '__cxa_guard_release'`, якщо стандартна бібліотека не містить спрощених заглушок.
2. **Роздування коду (Code bloat)**: якщо заглушки або реалізація на базі примітивів присутні, вони тягнуть додаткові сотні байтів коду та непотрібні атомарні інструкції на одноядерному чи однопотоковому процесорі.

### Що змінює прапорець `-fno-threadsafe-statics`

Прапорець компілятора `-fno-threadsafe-statics` наказує компілятору ігнорувати вимогу багатопоточної безпеки для локальних статичних змінних[^gcc-cxx-dialect].

Замість важких функцій ABI компілятор генерує найпростішу перевірку байтового прапорця:
```assembly
LDRB  r1, [guard_byte]   ; читання прапорця ініціалізації
CMP   r1, #0             ; якщо вже ініціалізовано,
BNE   already_init       ; пропускаємо конструювання
BL    UartDriver_ctor    ; викликаємо конструктор
MOVS  r1, #1
STRB  r1, [guard_byte]   ; позначаємо як ініціалізовано
already_init:
```
Це зменшує обсяг машинного коду до кількох асемблерних інструкцій і повністю позбавляє проект залежностей від потокових бібліотек runtime.

### Безпека застосування у прошивках

- **Коли прапорець повністю безпечний**:
  - У класичних однопотокових системах із суперциклом (bare-metal `super-loop`).
  - У системах з RTOS, якщо всі локальні статичні екземпляри ініціалізуються під час послідовного стартапу до запуску планувальника задач (`vTaskStartScheduler()`).
  - Коли конструктор об’єкта оголошено як `constexpr` або `constinit` – такі об’єкти взагалі ініціалізуються статично під час компіляції і не генерують runtime guard-змінних.
- **Коли виникає небезпека (Race Condition)**:
  - Якщо функція з локальним статичним об’єктом викликається паралельно з кількох завдань RTOS або зсередини обробника переривання (ISR) до того, як об’єкт було гарантовано сконструйовано. У такому разі можливе подвійне виконання конструктора або використання наполовину сконструйованого об’єкта іншим потоком.
