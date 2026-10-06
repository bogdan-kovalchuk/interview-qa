---
id: emb-raii-0005
title: "Які пари HAL-функцій варто загортати в scoped handle?"
description: "Будь-яку пару acquire/release (init/deinit), де звільнення має відбутися на кожному шляху виходу."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: обгортати ресурс із парними acquire/release в об’єкт, що захоплює в конструкторі й звільняє в деструкторі; приклади – файли, mutex, пам’ять, не апаратна периферія."
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує __disable_irq і __enable_irq (встановлюють і очищають PRIMASK; лише privileged mode), __get_PRIMASK і __set_PRIMASK (читання й запис PRIMASK); PRIMASK, коли встановлений, блокує всі винятки з конфігурованим пріоритетом. Сторінка позначає __get_PRIMASK як доступний лише для Armv8-M, тож доступність для конкретного ядра треба перевіряти в його документації."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує mutex API CMSIS-RTOS2: osMutexAcquire і osMutexRelease; ці виклики недоступні з ISR. Конкретна RTOS-реалізація поза специфікацією може поводитися інакше."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: при кожній передачі керування в межах функції (зокрема при поверненні з неї) automatic-змінні блоку, активні в точці відправлення й неактивні в точці призначення, знищуються у зворотному порядку конструювання. Не охоплює завершення програми через exit чи abort і не описує винятки."
---

## Short answer

**Будь-яку пару acquire/release (init/deinit), де звільнення має відбутися на кожному шляху виходу.**

HAL означає hardware abstraction layer. Приклади: interrupt disable/restore, SPI (serial peripheral interface) bus lock, CS (chip select) low -> CS high, GPIO (general-purpose input/output) claim, канал DMA (direct memory access) із пулу. Якщо ресурс живе довше за один блок, handle має бути не локальним guard-ом, а move-only власником.

Правило: парні acquire/release-виклики C API (application programming interface) обгортай в RAII-об’єкт.[^cppcg-r1-raii]

## Detailed explanation

Пару варто загортати, коли виконуються три умови: звільнення обов’язкове, між acquire і release є кілька шляхів виходу (таймаут, помилка передачі, early `return`), а час життя ресурсу збігається зі scope або має чітко визначеного власника. Core Guidelines формулюють це загально: усюди, де ресурс потребує парних викликів acquire/release, його інкапсулюють в об’єкт, що захоплює ресурс у конструкторі й віддає в деструкторі.[^cppcg-r1-raii] Приклади там – файли, mutex і пам’ять, тож перенесення на апаратну периферію – це застосування принципу, а не цитата з настанови.

Як типові пари HAL відображаються на ctor/dtor. Interrupt disable/restore: конструктор зберігає поточний PRIMASK (`__get_PRIMASK()`) і викликає `__disable_irq()`, деструктор повертає збережене значення через `__set_PRIMASK()`.[^cmsis-core-register] Саме відновлення, а не безумовний `__enable_irq()`, який очищає PRIMASK, дозволяє вкладені критичні секції (див. qid:emb-raii-0006). Bus lock для SPI зазвичай реалізують як mutex, і це guard із qid:emb-raii-0003; він працює лише в thread context, бо mutex API CMSIS-RTOS2 з ISR недоступний.[^cmsis-rtos2-mutex] Chip select: конструктор опускає лінію, деструктор піднімає. GPIO claim і канал DMA: конструктор бере ресурс із пулу, деструктор повертає.

Кілька таких об’єктів у одному блоці утворюють стек: локальні змінні знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-dcl] Це видно в ілюстративному прикладі (функції `gpio_write` і `spi_xfer` вигадані, `LockGuard` – з qid:emb-raii-0003, а `ChipSelect` має такі самі `= delete` на copy):

```cpp
class ChipSelect {
    int pin_;
public:
    explicit ChipSelect(int pin) : pin_(pin) { gpio_write(pin_, 0); }  // CS low
    ~ChipSelect() { gpio_write(pin_, 1); }                              // CS high
    ChipSelect(const ChipSelect&) = delete;
    ChipSelect& operator=(const ChipSelect&) = delete;
};

int read_reg(osMutexId_t bus, int cs_pin, std::uint8_t reg, std::uint8_t* out) {
    LockGuard lock(bus);                    // 1) take the bus
    if (!lock.owns()) return -1;
    ChipSelect cs(cs_pin);                  // 2) select the device
    if (spi_xfer(reg, out) != 0) return -2; // CS goes high first, then the bus is unlocked
    return 0;
}
```

Порядок важливий: `cs` створено після `lock`, тож знищується раніше – лінію CS піднято до того, як шину віддано. Якби першою звільнялася шина, інший потік міг би почати транзакцію, поки цей пристрій іще вибраний.

Не кожна пара вкладається в локальний guard. Якщо acquire і release розділені контекстами (наприклад, DMA запускають у функції, а завершують у callback чи ISR), handle має бути полем або move-only об’єктом, який передають власнику (qid:emb-raii-0009), а не змінною блоку; для HAL-ресурсу зручний `unique_ptr` із custom deleter (qid:emb-raii-0007). Деструктор не може повернути помилку, тому якщо deinit може бути довгим чи завершитися помилкою, це треба вирішити окремо, а деструктор у контексті ISR має свої обмеження (qid:emb-raii-0018).

**Типові помилки:**

- Загортати пару, яка за своєю природою не прив’язана до scope, у локальний guard: ресурс звільниться раніше, ніж завершиться операція.
- Створити guard-и в неправильному порядку: лінія CS чи інший «вужчий» ресурс має створюватися після «ширшого» (шини) і тому знищуватися перед ним.
- Дозволити копіювання handle: дві копії виконають release двічі (qid:emb-raii-0004).
- Викликати в деструкторі те, що не можна виконувати в поточному контексті (mutex API в ISR).[^cmsis-rtos2-mutex]

## Sources

<!-- generated from frontmatter -->
