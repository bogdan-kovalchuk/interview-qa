---
id: emb-raii-0030
title: "Який найбезпечніший RAII-патерн для використання в ISR?"
description: "Interrupt-disable/restore scope guard – лише register-level операції."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: ti-tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (Texas Instruments)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-13
    kind: official
    version: "June 12, 2014"
    applicability: "Розділ регістрів PRIMASK і BASEPRI для Cortex-M4 у даташиті TI: PRIMASK маскує exception з програмованим пріоритетом, Reset, NMI і hard fault мають фіксований пріоритет; BASEPRI задає мінімальний пріоритет обробки. Не описує RTOS і не є стандартом C++."
  - source_id: freertos-reference-manual
    title: "The FreeRTOS Reference Manual, V10.0.0"
    url: https://www.freertos.org/media/2018/FreeRTOS_Reference_Manual_V10.0.0.pdf
    accessed: 2026-10-13
    kind: official
    version: "V10.0.0"
    applicability: "Розділи про використання API в ISR і про taskENTER_CRITICAL_FROM_ISR()/taskEXIT_CRITICAL_FROM_ISR(): API без суфікса FromISR не викликаються в ISR; на портах з вкладеністю critical section від ISR маскує переривання на рівні configMAX_SYSCALL_INTERRUPT_PRIORITY і нижче; секції мають бути короткими. Не описує поведінку конкретного порту чи апаратної платформи."
---

## Short answer

**Interrupt-disable/restore scope guard, що чіпає лише регістри.**

Він зберігає PRIMASK (або BASEPRI), вимикає переривання в ctor і відновлює збережене значення в dtor.[^ti-tm4c123-datasheet] Блокуючих чи heap-операцій у ньому немає, тож його можна використовувати в ISR.

Правило: у ISR RTOS-коду обгортка має або чіпати лише регістри, або викликати лише API з суфіксом FromISR; блокуючі виклики – поза перериванням.[^freertos-reference-manual]

## Detailed explanation

В ISR з FreeRTOS API без суфікса FromISR викликати не можна, а деякі порти забороняють навіть FromISR-виклики в перериваннях з пріоритетом вище configMAX_SYSCALL_INTERRUPT_PRIORITY.[^freertos-reference-manual] Тому guard в обробнику має або чіпати лише регістри, як нижче, або викликати лише FromISR-функції.

```cpp
#include <cstdint>

// Illustrative Cortex-M code; the intrinsics come from the CMSIS core header.
uint32_t __get_PRIMASK(void);
void __set_PRIMASK(uint32_t);
void __disable_irq(void);

class IrqGuard {
public:
    IrqGuard() noexcept : saved_(__get_PRIMASK()) {
        __disable_irq();
    }
    ~IrqGuard() noexcept {
        __set_PRIMASK(saved_);   // restore the saved state, not "enable"
    }
    IrqGuard(const IrqGuard&) = delete;
    IrqGuard& operator=(const IrqGuard&) = delete;
private:
    uint32_t saved_;
};
```

Guard зберігає попередній стан PRIMASK і відновлює його, а не завжди викликає «увімкнути». Якщо зовнішній код уже замаскував переривання, внутрішній guard при виході не повинен їх розмаскувати. PRIMASK – один біт, що блокує всі exception з програмованим пріоритетом; Reset, NMI і hard fault мають фіксований пріоритет і ним не маскуються. Регістр доступний лише в привілейованому режимі, читається і записується інструкціями MRS та MSR, а змінювати його можна також інструкцією CPS.[^ti-tm4c123-datasheet]

Вибір між PRIMASK і BASEPRI залежить від системи. PRIMASK маскує все з програмованим пріоритетом, включно з обробниками, які не викликають RTOS. BASEPRI задає мінімальний пріоритет обробки: ненульове значення блокує exception з рівним або нижчим пріоритетом і не чіпає вищих.[^ti-tm4c123-datasheet] FreeRTOS на портах з вкладеністю робить аналогічно: taskENTER_CRITICAL_FROM_ISR() вимикає переривання з пріоритетом на рівні configMAX_SYSCALL_INTERRUPT_PRIORITY і нижчим, а решту переривань лишає увімкненими.[^freertos-reference-manual] Секція в RTOS-коді має бути короткою, а API FreeRTOS всередині неї не викликаються.[^freertos-reference-manual]

**Типові помилки:**

- Безумовно викликати `__enable_irq()` у dtor: у вкладеному коді це розмаскує переривання, які зовнішній код свідомо вимкнув.
- Викликати звичайний (не FromISR) API RTOS в ISR або всередині guard.
- Вважати, що PRIMASK маскує NMI і HardFault: вони мають фіксований пріоритет.

## Sources

<!-- generated from frontmatter -->
