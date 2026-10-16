---
id: emb-dtypes-0051
title: "Trap: `packed struct` може спричинити HardFault на Cortex-M0 - чому?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv6m-alignment
    title: "Arm: ARMv6-M vs ARMv7-M – Unpacking the microcontrollers"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/armv6-m-vs-armv7-m---unpacking-the-microcontrollers
  - source_id: gcc-packed
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

Cortex-M0/M0+ вимагає природного вирівнювання для доступів пам’яті, але `packed` сам по собі не гарантує HardFault: компілятор може згенерувати безпечні byte-доступи. Результат залежить від згенерованої інструкції та доступної адреси пам’яті.[^armv6m-alignment]

`__attribute__((packed))` прибирає padding між полями, тому `uint32_t` може мати offset 1. Перевіряй assembler і використовуй `memcpy` у вирівняний об’єкт для переносимого читання з буфера.[^gcc-packed]

Частина інструкцій Cortex-M3/M4 підтримує невирівняні доступи, але це не універсально для кожної інструкції чи області пам’яті.[^armv6m-alignment]

## Detailed explanation

`packed struct` може розмістити багатобайтове поле за адресою, яка не відповідає природному вирівнюванню його типу. Це створює ризик на Cortex-M0/M0+, де архітектура вимагає природного вирівнювання доступів: наприклад, 32-бітове поле за адресою, що не ділиться на чотири, не можна вважати звичайним вирівняним word-доступом.[^armv6m-alignment]

Однак помилково казати, що кожне звернення до такого поля неодмінно породжує HardFault. `packed` – розширення компілятора, і компілятор, знаючи про зменшене вирівнювання члена, може побудувати кілька byte-доступів або інший код. Якщо ж програма обходить цю інформацію, наприклад бере адресу packed-поля та трактує її як звичайний `uint32_t *`, виникає окрема проблема невирівняного вказівника; C описує перетворення на неправильно вирівняний вказівник як undefined behavior. Фактична помилка на MCU залежить від інструкції, адреси та поведінки системи пам’яті.[^gcc-packed] [^iso-c-n1570]

Для протоколу на дроті packed-layout може бути корисним, але він не замінює серіалізацію: треба також визначити endian порядок, розмір полів і правила доступу. Безпечний загальний підхід – копіювати байти до локальної вирівняної змінної, а потім окремо приводити byte order та перевіряти довжину буфера. Навіть `memcpy` не виправляє некоректний offset або недостатню кількість вхідних байтів.[^gcc-packed]

**Типова помилка:** переносити висновок з одного ядра чи одного build на весь Cortex-M. У конкретному випадку перевіряй disassembly саме свого target та compiler flags; не вважай, що саме оголошення `packed` гарантує або відсутність, або наявність fault. Також май на увазі, що packed-поле, вкладена структура або pointer cast можуть створити інші вимоги до вирівнювання; виправлення лише одного поля не усуває всі ризики такого layout.[^gcc-packed] У тесті перевіряй саме код доступу до проблемного поля: суміжне byte-поле може працювати нормально й приховати дефект звичайним функціональним тестом.[^armv6m-alignment]
