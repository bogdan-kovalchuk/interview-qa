---
id: emb-raii-0006
title: "Як виглядає interrupt-disable RAII guard і чому він безпечний у ISR?"
description: "Ctor зберігає поточний стан переривань і вимикає їх; dtor відновлює попередній стан."
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
  - source_id: cmsis-core-register-access
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує функції `__get_PRIMASK()`, `__set_PRIMASK()` і `__disable_irq()`: остання вимикає переривання й configurable fault handlers установленням PRIMASK інструкцією `CPSID i`, виконується лише в privileged mode, а вимкнене переривання все одно може стати pending. Не описує, як ці функції реалізовано в конкретному компіляторі, і не стосується ядер поза Cortex-M."
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPMS376E"
    applicability: "Для ядра Cortex-M4F: PRIMASK = 1 забороняє активацію всіх exceptions з configurable priority, а Reset, NMI і hard fault мають фіксований пріоритет; регістр доступний лише в privileged mode, а в Handler mode виконання завжди privileged. Для інших ядер і чипів деталі можуть відрізнятися."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Нотатка каже, що при виході зі scope будь-яким способом об’єкти з automatic storage duration, які там створено, знищуються в зворотному порядку; виняток – завершення програми через `exit()` чи `abort()`. Про переривання нічого не каже."
  - source_id: gcc-extended-asm
    title: "GCC: Extended Asm"
    url: https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Каже, що clobber `\"memory\"` повідомляє компілятору, що asm читає чи пише пам’ять поза операндами, і діє як бар’єр для компілятора, але не перешкоджає процесору виконувати speculative reads. Не описує конкретну інструкцію `cpsid`."
---

## Short answer

**Ctor зберігає поточний стан переривань і вимикає їх; dtor відновлює збережений стан, а не вмикає переривання безумовно.** На Cortex-M це читання PRIMASK і `cpsid i` без блокування й heap,[^cmsis-core-register-access] а PRIMASK доступний у privileged mode, тож в ISR (Handler mode) guard працює.[^tm4c123-datasheet] Відновлення збереженого значення дозволяє вкладені секції; поки PRIMASK = 1, маскуються всі exceptions з configurable priority, тож секцію тримай короткою.[^tm4c123-datasheet]

## Detailed explanation

Guard робить критичну секцію властивістю області видимості. Коли керування покидає scope будь-яким шляхом (`return`, `break`, `goto`), об’єкти з automatic storage duration знищуються, тож dtor повертає стан переривань незалежно від того, яким шляхом вийшли з функції.[^cpp-draft-stmt-jump] Dtor не відпрацює, якщо програма завершиться через `exit()` чи `abort()` або зависне, впаде у fault чи перезапуститься посеред секції, тож стан PRIMASK тоді не відновиться.

На Cortex-M «вимкнути переривання» означає встановити PRIMASK = 1. CMSIS-функція `__disable_irq()` робить це інструкцією `CPSID i`, а `__get_PRIMASK()` і `__set_PRIMASK()` читають і пишуть регістр; вимкнений interrupt усе одно може стати pending, його просто не обробляють, доки секція не закінчиться.[^cmsis-core-register-access] PRIMASK = 1 забороняє активацію всіх exceptions з configurable priority, але Reset, NMI і hard fault мають фіксований пріоритет, тож guard від них не захищає.[^tm4c123-datasheet]

Зберігати стан потрібно тому, що guard може створюватися, коли переривання вже вимкнено: у вкладеному виклику, у функції, яку викликають і з main-контексту, і з ISR, або в секції, яку відкрив зовнішній guard. Якби dtor викликав `__enable_irq()`, внутрішній guard вмикав би переривання посеред зовнішньої секції. Збережене значення повертає саме той PRIMASK, що був на вході: 1 для внутрішнього guard і 0 для зовнішнього. В ISR це працює, бо в Handler mode виконання завжди privileged, а доступ до PRIMASK можливий саме в privileged mode.[^tm4c123-datasheet]

```cpp
// Ілюстративний приклад; потребує CMSIS device header.
class InterruptGuard {
 public:
  InterruptGuard() : saved_(__get_PRIMASK()) { __disable_irq(); }
  ~InterruptGuard() { __set_PRIMASK(saved_); }
  InterruptGuard(const InterruptGuard&) = delete;
  InterruptGuard& operator=(const InterruptGuard&) = delete;

 private:
  uint32_t saved_;
};

void outer() {
  InterruptGuard a;     // PRIMASK 0 -> 1, збережено 0
  inner();              // всередині свій guard: збережено 1, після нього знову 1
}                       // PRIMASK повертається до 0
```

Якщо писати обгортки на `asm` самостійно, потрібен clobber `"memory"`: він змушує компілятор не вважати, що значення з пам’яті не змінилися через asm, і діє як бар’єр лише для компілятора, а не для процесора.[^gcc-extended-asm]

**Типові помилки:**

- Безумовний `__enable_irq()` у dtor: вкладені секції передчасно вмикають переривання.
- Довга секція або повільні й блокуючі виклики всередині (мьютекс, `malloc`, затримка): усі masked exceptions чекають, а latency зростає.
- Використання з unprivileged-коду: PRIMASK доступний лише в privileged mode.[^tm4c123-datasheet]
- Припущення, що guard маскує NMI чи hard fault: вони мають фіксований пріоритет.[^tm4c123-datasheet]

## Sources

<!-- generated from frontmatter -->
