---
id: emb-tmplcx-0027
title: "Як `static_assert` використовують із шаблонами?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

**Compile-time перевірка інваріантів типу/розміру зі зрозумілим повідомленням.**

Напр. у дефолтній гілці `if constexpr`: `static_assert(always_false<P>, "Unsupported platform")` ловить непідтримуваний тип ще на компіляції. Також `static_assert(N > 0, "...")` валідовує NTTP.

Правило: `static_assert` – головний інструмент, щоб перетворити невірне використання шаблону на зрозумілу помилку.[^embeddedinterviewlab]

## Detailed explanation

### Статичні твердження в системі типів C++

За стандартом ISO/IEC 14882 ([dcl.dcl] у [^iso-cpp-n4861]), конструкція `static_assert(bool_constexpr, message)` обчислюється на етапі трансляції. Якщо константний вираз дорівнює `false`, компілятор негайно перериває складання із зазначеним діагностичним повідомленням. При успішній перевірці `static_assert` повністю випаровується і не створює жодного байта машинного коду або накладних витрат у Flash чи RAM.

У шаблонному коді для вбудованих систем `static_assert` виконує роль формального контракту. Він перехоплює некоректні типи й параметри на ранньому етапі, замінюючи нечитабельні багатосторінкові ланцюжки діагностики компілятора (template instantiation backtrace) на зрозуміле інженерне повідомлення.

### Валідація нетипових параметрів (NTTP) та інваріантів буферів

Шаблони периферійних драйверів і комунікаційних структур часто параметризуються числовими значеннями: розміром FIFO, дільником тактової частоти, пріоритетом переривання або адресою регістра. За допомогою `static_assert` розробник гарантує апаратні вимоги:

```cpp
template <typename T, size_t Size>
class RingBuffer {
    static_assert(Size > 0, "RingBuffer size must be greater than zero");
    static_assert((Size & (Size - 1)) == 0, 
                  "Size must be a power of two to optimize modulo index to bitwise AND");
    static_assert(std::is_trivially_copyable_v<T>, 
                  "T must be trivially copyable for safe DMA transfers");
private:
    T buffer_[Size];
};
```

У цьому прикладі статична перевірка степеня двійки гарантує, що операція обчислення індексу `(head + 1) & (Size - 1)` замінить повільну операцію апаратного ділення `UDIV` на мікроконтролерах Cortex-M3/M4/M7, а на ядрах Cortex-M0/M0+ запобіжить виклику важкої софтової бібліотечної підпрограми ділення з Flash.

### Контроль розмірів, упаковки та бінарної сумісності

У низькорівневих протоколах (CAN, SPI, UART) структури пакетів часто відображаються безпосередньо на буфери прийому DMA або апаратні регістри. `static_assert` у поєднанні з `sizeof` та `alignof` захищає від небажаного вирівнювання і прихованого паддінгу (padding bytes):

```cpp
struct [[gnu::packed]] TelemetryPacket {
    uint32_t timestamp_ms;
    int16_t  ax, ay, az;
    uint16_t checksum;
};

static_assert(sizeof(TelemetryPacket) == 12, "TelemetryPacket must have exactly 12 bytes");
static_assert(alignof(TelemetryPacket) == 1, "TelemetryPacket alignment mismatch");
```

Якщо інженер оновить компілятор або змінить прапорці оптимізації і структура зміститься хоча б на 1 байт, білд надійно зупиниться ще до етапу лінкування.

### Пастка у гілках `if constexpr` (Dependent False Idiom)

Поширеною помилкою є спроба перехопити невідомий тип у завершальній гілці `if constexpr` прямим викликом `static_assert(false, ...)`:

```cpp
template <typename TargetMcu>
void init_pll() {
    if constexpr (std::is_same_v<TargetMcu, Stm32F4>) {
        // Конфігурація PLL для STM32F4
    } else if constexpr (std::is_same_v<TargetMcu, Stm32H7>) {
        // Конфігурація PLL для STM32H7
    } else {
        // Помилка: компілятор зупинить збирання навіть для Stm32F4!
        static_assert(false, "Unsupported MCU target");
    }
}
```

Згідно з правилами двофазного пошуку імен (two-phase lookup, [temp.res] у [^iso-cpp-n4861]), вирази, які не залежать від параметрів шаблону, перевіряються на першій фазі розбору. Оскільки константа `false` не залежить від `TargetMcu`, компілятор генерує помилку негайно при читанні визначення функції.

Щоб відкласти обчислення твердження до фази інстанціації конкретного типу, використовують залежну константу (dependent false)[^embeddedinterviewlab]:

```cpp
template <typename>
inline constexpr bool always_false_v = false;

template <typename TargetMcu>
void init_pll() {
    if constexpr (std::is_same_v<TargetMcu, Stm32F4>) {
        // ...
    } else {
        static_assert(always_false_v<TargetMcu>, "Unsupported MCU target");
    }
}
```

Тепер твердження буде перевірено лише в тому разі, якщо шаблон реально інстанціюється з непідтримуваним типом `TargetMcu`.

