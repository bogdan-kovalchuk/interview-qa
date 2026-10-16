---
id: emb-boot-0003
title: "Як відбувається завантаження програми в мікроконтролері?"
track: embedded
section: bootloaders-and-ota
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

Після подачі живлення або reset (ARM Cortex-M):[^dou-embedded-interview]

- Апаратура читає **Vector Table** з адреси `0x00000000` (Flash)
- Завантажує початкове значення SP зі слова за адресою `0x00000000`
- Завантажує адресу Reset Handler у PC з `0x00000004`
- **Startup code** (crt0 / startup.s) копіює секцію `.data` з Flash у RAM, заповнює `.bss` нулями
- Ініціалізує тактування (PLL, clock tree)
- Викликає `main()`.

Програма зберігається у **Flash (non-volatile)**. Виконання може відбуватися безпосередньо з Flash (XIP – execute-in-place) або, для швидкодіючого коду, програма копіюється в RAM.

## Detailed explanation

На ARM Cortex-M після подачі живлення або апаратного reset процесор виконує послідовність, визначену архітектурою ARMv7-M:

1. **Читання vector table.** Апаратний блок читає два перші 32-бітні слова з базової адреси Flash (зазвичай `0x00000000` або `0x08000000` з урахуванням remapping). Слово за адресою `0x00000000` – початкове значення Main Stack Pointer (MSP); слово за адресою `0x00000004` – адреса Reset Handler.

2. **Виконання Reset Handler.** Це перша інструкція, яку виконує CPU. Зазвичай це функція `Reset_Handler` у startup-файлі (`startup_stm32f4xx.s`, `startup_nrf52.s` тощо).

3. **Startup code (crt0).** Reset Handler викликає системну функцію ініціалізації (`SystemInit`), яка налаштовує базове тактування. Потім копіює секцію `.data` (ініціалізовані глобальні змінні) з Flash у RAM за адресами, визначеними у linker script. Заповнює секцію `.bss` (неініціалізовані глобальні змінні) нулями. Для C++ викликає конструктори глобальних об'єктів (`__libc_init_array`).

4. **Виклик `main()`.** Після завершення startup code передає керування у `main()`.

Програма зберігається у Flash (non-volatile пам'ять). Виконання може відбуватися безпосередньо з Flash (XIP – execute-in-place) або, для швидкодійного коду, критичних до латентності ISR, програма копіюється у RAM.

Векторна таблиця містить 240 векторів переривань (для ARMv7-M); окрім SP та Reset Handler, вона включає адреси NMI_Handler, HardFault_Handler, MemManage_Handler тощо.[^armv7m-arm]
