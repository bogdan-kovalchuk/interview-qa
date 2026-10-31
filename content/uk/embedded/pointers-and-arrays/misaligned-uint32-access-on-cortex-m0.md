---
id: emb-cppfound-0056
title: "Trap на Cortex-M0 – ризик?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: arm-cortex-m0-alignment
    title: "Arm Cortex-M0 Devices Generic User Guide: Address alignment"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
uint8_t *p=(uint8_t*)0x40020000;
uint32_t val=*(uint32_t*)p;
```

## Short answer

`p` – `uint8_t*`: гарантій вирівнювання нема. Cast до `uint32_t*` і розіменування:

Якщо адреса `0x40020000` вирівняна на 4 -> ОК. Але якщо `p` вказує на `0x40020001` (misaligned) -> Cortex-M0: <span class="warn">HardFault</span>. Cortex-M3/M4: повільно але без fault.

Безпечно: `uint32_t val; memcpy(&val, p, sizeof(val));` – компілятор оптимізує до одного LDR якщо вирівняно.[^embeddedinterviewlab]

## Detailed explanation

Пряме приведення покажчика `uint8_t *` до `uint32_t *` із наступним розіменуванням є однією з найпоширеніших пасток низькорівневого програмування для мікроконтролерів. Цей вираз несе критичні апаратні ризики та порушує вимоги стандарту ISO/IEC 9899 (§6.3.2.3 Pointers).[^iso-c-n1570]

### Апаратні обмеження архітектури ARMv6-M (Cortex-M0)

Ядро ARM Cortex-M0 реалізує архітектуру ARMv6-M. На відміну від старших ядер (Cortex-M3/M4/M7 на архітектурі ARMv7-M), Cortex-M0 **не підтримує невирівняний доступ до пам’яті (unaligned memory access) на апаратному рівні**.[^arm-cortex-m0-alignment]

Згідно з інструкцією користувача ARM Cortex-M0 Generic User Guide:
- Інструкція `LDR` (Load Register), яка завантажує 32-бітне слово у регістр, вимагає, щоб адреса пам’яті була строго кратна 4 байтам (біти адреси `[1:0]` мають дорівнювати `00`).[^arm-cortex-m0-alignment]
- Якщо процесор виконує інструкцію `LDR` за адресою, не вирівняною на 4 байти (наприклад, `0x20000001`, `0x20000002` чи `0x20000003`), ядро негайно переходить в апаратний виняток `HardFault`.[^arm-cortex-m0-alignment]
- Оскільки ядро Cortex-M0 має спрощену систему винятків і позбавлене окремого обробника помилок `UsageFault`, помилка вирівнювання невідворотно призводить до блокування системи у векторі `HardFault_Handler`.[^arm-cortex-m0-alignment]

### Стандарт C та undefined behavior

Стандарт ISO/IEC 9899 (§6.3.2.3 p7) встановлює:[^iso-c-n1570]
> «A pointer to an object type may be converted to a pointer to a different object type. If the resulting pointer is not correctly aligned for the referenced type, the behavior is undefined».

Тип `uint8_t *` має вимогу вирівнювання в 1 байт (вирівняний за будь-якою адресою). Тип `uint32_t *` має вимогу вирівнювання в 4 байти. Приведення покажчика байтового буфера до `uint32_t *` є законним лише тоді, коли адреса гарантовано кратна 4. Якщо ж вона не вирівняна, розіменування є `undefined behavior` ще на рівні мови C, до виконання асемблерного коду процесором.[^iso-c-n1570]

### Відмінності між Cortex-M0 та Cortex-M3/M4/M7

Між різними поколіннями ядер ARM Cortex-M існує принципова різниця:
1. **Cortex-M0 / Cortex-M0+ (ARMv6-M):** апаратний модуль контролера пам’яті не вміє розділяти 32-бітний доступ на два послідовні зчитування шини AHB-Lite. Будь-який невирівняний доступ породжує `HardFault`.[^arm-cortex-m0-alignment]
2. **Cortex-M3 / Cortex-M4 / Cortex-M7 (ARMv7-M):** підтримують невирівняний доступ до нормальної пам’яті (SRAM та Flash) через апаратну декомпозицію на кілька шинних циклів. Інструкція `LDR` виконається без збою, але з певною втратою продуктивності (займає 2–3 такти замість 1 такту).
3. **Регістр конфігурації CCR (Configuration and Control Register):** навіть на Cortex-M3/M4 у регістрі `SCB->CCR` є біт `UNALIGN_TRP`. Якщо цей біт активовано, процесор згенерує `UsageFault` при будь-якому невирівняному зверненні.

### Доступ до регістрів периферії (Device Memory)

У наведеному питанні вказано адресу `0x40020000`. В мікроконтролерах сімейства STM32 це діапазон адрес периферійних модулів (наприклад, шина AHB1/APB):
- Сама адреса `0x40020000` вирівняна на 4 байти, тому одиничне зчитування за фіксованою адресою виконається успішно.
- Проте область `0x40000000`–`0x5FFFFFFF` у карті пам’яті ARM визначена як `Device Memory` або `Strongly-Ordered Memory`.
- **Критичне правило:** на **жодному** ядрі ARM (включно з Cortex-M3, M4 та M7) невирівняний доступ до пам’яті периферії (Device Memory) не підтримується! Навіть на Cortex-M4 спроба виконати `*(uint32_t *)0x40020001` миттєво викличе виняток `BusFault` або `HardFault`.[^arm-cortex-m0-alignment]

### Безпечні інженерні практики у прошивках

Щоб надійно зчитати 32-бітне ціле з потенційно невирівняного буфера байтів (наприклад, пакету UART чи кадру радіомодуля), слід використовувати безпечні патерни:

1. **Використання `memcpy`:**
   ```c
   uint32_t val;
   memcpy(&val, p, sizeof(val));
   ```
   Компілятор автоматично враховує архітектуру цільового процесора. Для Cortex-M0 компілятор згенерує 4 інструкції `LDRB` зі зсувами або зчитування через маніпуляцію регістрами. Для Cortex-M4 він підставить швидку інструкцію `LDR`.
2. **Побітове складання байтів (Little-Endian / Big-Endian незалежне):**
   ```c
   uint32_t val = (uint32_t)p[0] |
                  ((uint32_t)p[1] << 8) |
                  ((uint32_t)p[2] << 16) |
                  ((uint32_t)p[3] << 24);
   ```
   Цей код є 100% переносним, не залежить від вирівнювання шини та гарантує передбачуваний порядок байтів у пам’яті.
