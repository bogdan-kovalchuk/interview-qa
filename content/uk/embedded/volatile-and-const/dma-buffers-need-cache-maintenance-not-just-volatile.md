---
id: emb-volconst-0039
title: "Trap: чи достатньо `volatile` для DMA buffer?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
---

## Short answer

<span class="warn">Не завжди.</span>

`volatile` може змусити compiler виконувати доступи до descriptor або flag, які змінює DMA. Але воно не вирішує cache coherency, alignment, ownership, memory barriers і race conditions. На Cortex-M7 з D-cache DMA може записати RAM, а CPU все ще читатиме старі cache lines.[^gcc-volatile] [^arm-cortex-m7]

Захист: використовуй non-cacheable memory або cache clean/invalidate у правильних напрямках, barriers за вимогами платформи та чіткий ownership protocol між CPU та DMA.[^arm-cortex-m7]

## Detailed explanation

`volatile` і cache coherency вирішують різні проблеми. Кваліфікатор впливає на те, як compiler обробляє доступи до позначених об’єктів; DMA при цьому є окремим bus master і читає чи записує фізичну пам’ять. Якщо CPU має D-cache, дані в RAM та cache line можуть тимчасово відрізнятися. volatile не записує брудну cache line в RAM і не викидає застарілу копію з cache.[^gcc-volatile] [^arm-cortex-m7]

Для DMA, який читає дані, підготовлені CPU, перед передачею ownership треба забезпечити, щоб актуальні байти дійшли до пам’яті, видимої DMA; на кешованій ділянці це зазвичай означає clean операції згідно з SoC документацією. Для DMA, який записує дані, до старту DMA треба врахувати можливі dirty cache lines, щоб CPU не записав їх поверх результату DMA; після завершення DMA CPU не повинен споживати стару cache line, тож потрібна відповідна invalidate процедура. Якщо ділянка може містити сусідні дані CPU у тій самій cache line, бездумне invalidate може відкинути ці зміни; потрібні alignment, розмір ділянки й протокол володіння, узгоджені з розміром cache line та CMSIS API.[^arm-cortex-m7]

Точна послідовність залежить від напрямку передачі, наявності cache, правил DMA engine і memory attributes конкретного SoC. Non-cacheable region може спростити coherency, але має обмеження продуктивності й налаштування MPU. Barriers упорядковують accesses за правилами архітектури, але самі по собі не замінюють clean/invalidate. Перевір приклади з документації MCU та функції cache maintenance, які постачає його CMSIS/device SDK.[^arm-cortex-m7]

**Типові помилки:**

- Позначати весь buffer volatile і вважати проблему coherency вирішеною.
- Забувати передати ownership buffer між CPU та DMA лише після потрібних операцій.
- Викликати invalidate на довільній адресі чи довжині без урахування cache-line alignment.

Найпростіший надійний дизайн задає однозначний стан buffer: хто ним володіє, коли CPU може його читати або змінювати, і які cache операції потрібні на кожній межі передачі.[^arm-cortex-m7]
