---
id: emb-align-0008
title: "Як поводиться misaligned access на Cortex-M3/M4 і що таке `UNALIGN_TRP`?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m3-unaligned
    title: "Arm Cortex-M3 Devices Generic User Guide: Configurable Fault Status Register"
    url: https://developer.arm.com/documentation/dui0552/a/cortex-m3-peripherals/system-control-block/configurable-fault-status-register
  - source_id: arm-cortex-m4-datasheet
    title: "Arm Cortex-M4 Processor Datasheet"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Processor%20Datasheets/Arm%20Cortex-M4%20Processor%20Datasheet.pdf
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Розміри об’єктів і оператор sizeof"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**Cortex-M3/M4 підтримують частину unaligned halfword і word accesses, але ця підтримка не універсальна.** Значення мають memory type та instruction; `LDM`, `STM`, `LDRD` і `STRD` вимагають вирівнювання.

`SCB->CCR.UNALIGN_TRP` змушує інакше підтримувані unaligned accesses піднімати UsageFault, що допомагає виявляти помилки під час розробки.

Це не скасовує вирівнювання typed pointer у C; порушення alignment requirement типу залишається undefined behavior.[^embeddedinterviewlab]

## Detailed explanation

Cortex-M3 і Cortex-M4 заявляють підтримку unaligned access, тому звичайний load/store із Normal memory може завершитися замість fault. Ядру все одно можуть знадобитися додаткові transfer, але точна ціна в тактах залежить від конкретного MCU, memory region, cache і bus fabric, а не від універсального множника.[^arm-cortex-m4-datasheet]

`UNALIGN_TRP` – діагностичний control у System Control Block. Коли він установлений, unaligned access, який інакше був би підтриманий, піднімає UsageFault і встановлює status bit `UNALIGNED`. Якщо UsageFault вимкнений, exception може ескалувати до HardFault.

```c
SCB->CCR |= SCB_CCR_UNALIGN_TRP_Msk;
```

Перемикач не є абсолютним. Arm документує, що невирівняні `LDM`, `STM`, `LDRD` і `STRD` дають fault незалежно від `UNALIGN_TRP`.[^arm-cortex-m3-unaligned] Device або Strongly-ordered memory і bus конкретного пристрою можуть мати додаткові обмеження.

На рівні C перетворення довільної byte address на `uint32_t *` може порушити alignment цільового типу й дати undefined behavior.[^iso-c-n1570] Compiler може оптимізувати code на основі цієї обіцянки, навіть коли processor здатний виконати unaligned instruction.

Використовуй `UNALIGN_TRP` у debug builds як ранній detector, а потім виправляй доступ через aligned object, `memcpy` або явне декодування байтів. Не вимикай trap лише для маскування хибного припущення про data layout.
