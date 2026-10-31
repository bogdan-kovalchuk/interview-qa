---
id: emb-tmplcx-0024
title: "Trap: чому `Uart<USART1>` і `Uart<USART2>` можуть роздути Flash?"
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

<span class="warn">Кожна інстанціація per-периферію може дати майже ідентичний код – різниться лише константа base address.</span>

На малих MCU (microcontroller unit) це швидко накопичується, якщо так само зробити `Uart<...>`, `Spi<...>`, `I2c<...>` для багатьох периферій.

Захист: non-template `UartImpl` з base address як параметром ctor + тонка шаблонна обгортка з `constexpr` адресою; економію підтверджуй linker map.[^embeddedinterviewlab]

## Detailed explanation

### Причина дублювання: окремі типи за стандартом C++

Згідно зі стандартом ISO/IEC 14882 ([temp.spec] у [^iso-cpp-n4861]), кожен унікальний набір шаблонних аргументів породжує окрему спеціалізацію шаблону класу. Якщо периферійний драйвер параметризований адресою або дескриптором апаратного блоку (non-type template parameter, NTTP):

```cpp
template <uintptr_t BaseAddr>
class Uart {
public:
    void send_byte(uint8_t byte) {
        auto* reg = reinterpret_cast<USART_TypeDef*>(BaseAddr);
        while (!(reg->ISR & USART_ISR_TXE_TXFNF)) {}
        reg->TDR = byte;
    }
    void init(uint32_t baudrate);
    void write_buffer(const uint8_t* data, size_t len);
};
```

Типи `Uart<USART1_BASE>` і `Uart<USART2_BASE>` є принципово різними типами для компілятора. Якщо методи `init`, `write_buffer` або обробники FIFO не заінлайнилися (наприклад, через їхній розмір чи наявність циклів), компілятор генерує два незалежних набори функцій у секціях `.text`.

### Прояв на рівні асемблера ARM Cortex-M

Згенерований машинний код обох інстанціацій практично збігається байт у байт:
- Логіка перевірки прапорців, індексація кільцевих буферів, розрахунок подільників бодрейту та обробка помилок парності повністю однакові.
- Єдина відмінність полягає в завантаженні константи базової адреси у регістр (наприклад, `0x40013800` для USART1 та `0x40004400` для USART2):

```assembly
// Uart<USART1>::send_byte
LDR     R1, =0x40013800
LDR     R2, [R1, #0x1C]    // ISR
TST     R2, #0x80
BEQ     .wait
STRB    R0, [R1, #0x28]    // TDR
BX      LR

// Uart<USART2>::send_byte
LDR     R1, =0x40004400
LDR     R2, [R1, #0x1C]    // ISR
TST     R2, #0x80
BEQ     .wait
STRB    R0, [R1, #0x28]    // TDR
BX      LR
```

Коли клас містить 10–15 методів (ініціалізація, налаштування DMA, підтримка асинхронного читання, обробка переривань), кожен екземпляр периферії дублює від сотень байтів до декількох кілобайтів Flash. На мікроконтролері з 32–64 КБ Flash розгортання чотирьох UART, трьох SPI і двох I2C призводить до критичного дефіциту постійної пам’яті (code bloat)[^embeddedinterviewlab].

### Архітектурне вирішення: ідіома Thin Template Wrapper

Щоб уникнути дублювання коду, алгоритмічно складну логіку відокремлюють від шаблонного інтерфейсу:

1. **Базовий нешаблонний клас (`UartBase`)**: містить реалізацію всіх методів у єдиному екземплярі у `.text`. Базова адреса зберігається як поле або передається вказівником на регістрову структуру (`USART_TypeDef*`).
2. **Тонкий шаблонний фасад (`Uart<BaseAddr>`)**: служить лише для статичної типізації, compile-time валідації та надання зручного API, викликаючи методи базового класу:

```cpp
class UartBase {
protected:
    USART_TypeDef* const regs_;
    explicit UartBase(USART_TypeDef* regs) : regs_(regs) {}
    void write_buffer_impl(const uint8_t* data, size_t len);
};

template <uintptr_t BaseAddr>
class Uart : public UartBase {
public:
    Uart() : UartBase(reinterpret_cast<USART_TypeDef*>(BaseAddr)) {}
    
    // Тонкий інлайн-метод не дублює логіку обробки
    void write_buffer(const uint8_t* data, size_t len) {
        write_buffer_impl(data, len);
    }
};
```

Такий підхід залишає всю важку логіку в єдиному місці у Flash, зберігаючи при цьому переваги статичної диспетчеризації без накладних витрат віртуальних функцій (`vtable`).

### Оптимізація на рівні лінкера (ICF)

Сучасні лінкери (зокрема LLVM `lld` з прапорцем `--icf=all` або GNU `gold`) підтримують Identical Code Folding. Проте стандартний `arm-none-eabi-ld` зазвичай не виконує агресивне згортання ідентичного коду, особливо коли функції відрізняються зміщенням до literal pool або завантаженням різних констант. Тому архітектурне розділення на рівні C++ залишається найнадійнішим способом контролю розміру Flash.

