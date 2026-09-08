---
id: emb-align-0002
title: "Чому CPU взагалі вимагає вирівнювання даних?"
description: "Шина читає/пише пам'ять word-aligned шматками фіксованого розміру."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
  - source_id: arm-cortex-m3-unaligned
    title: "Arm Cortex-M3 Devices Generic User Guide: Configurable Fault Status Register"
    url: https://developer.arm.com/documentation/dui0552/a/cortex-m3-peripherals/system-control-block/configurable-fault-status-register
    accessed: 2026-09-08
    kind: official
    version: "1.0"
    applicability: "Trapping невирівняного доступу в Cortex-M3 та інструкції, які завжди дають fault за невирівняної адреси."
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Розміри об'єктів і оператор sizeof"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додаткове пояснення byte-addressed об'єктів і залежних від реалізації розмірів об'єктів."
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Додатковий український маршрут вивчення C++; не є нормативним джерелом поведінки processor."
---

## Short answer

**Вирівняний доступ відповідає межам, яких очікують тип і memory system.**

Вирівняне значення може вміститися у природну одиницю transfer. Невирівняне значення може перетнути її межу, тому апаратура або розкладає операцію на кілька вирівняних transfer, або відхиляє її з fault.

Не зводь це до правила про покоління Cortex-M: результат залежить від instruction, memory attributes і налаштування trapping.[^embeddedinterviewlab]

## Detailed explanation

Правило C і правило processor – різні речі. C вимагає належного вирівнювання типізованого об'єкта; порушення цієї вимоги дає undefined behavior ще до розгляду processor-specific поведінки.[^iso-c-n1570]

На рівні processor реалізація може перетворити одну невирівняну instruction на кілька вирівняних bus transfer. Для умовного 32-бітного transfer перетин межі виглядає так:

**Вирівняний доступ:**

Якщо `uint32_t` знаходиться за адресою 0x2000_0000 (кратна 4), CPU читає його за одну транзакцію:
```
Address: 0x2000_0000  0x2000_0004
Data:    [4 bytes]    [4 bytes]
         ^^^^
         one transaction
```

**Невирівняний доступ:**

Якщо `uint32_t` знаходиться за адресою 0x2000_0001 (не кратна 4), значення перетинає межу слова:
```
Address: 0x2000_0000  0x2000_0004  0x2000_0008
Data:    [4 bytes]    [4 bytes]    [4 bytes]
          ^^^^         ^^^^
          1 byte       3 bytes
```
Реалізація може прочитати обидва вирівняні слова та об'єднати потрібні байти. Це модель, а не гарантія, що кожен 32-бітний MCU має чотирибайтову bus transaction.

**Конкретний приклад Cortex-M3**

Cortex-M3 може виконувати частину невирівняних load і store. Software може ввімкнути trapping через `UNALIGN_TRP`, а невирівняні `LDM`, `STM`, `LDRD` і `STRD` дають fault незалежно від цього налаштування.[^arm-cortex-m3-unaligned]

Інші ядра та memory region мають інші правила. Device memory, exclusive або multiple-register instructions, peripheral registers і bus fabric конкретного виробника можуть вимагати суворішого вирівнювання, ніж звичайний доступ до RAM.

**Практичні наслідки**

- Дозволь compiler розміщувати звичайні об'єкти та структури відповідно до target ABI.
- Для packet або serial bytes використовуй `memcpy` у вирівняне ціле число, а потім декодуй endianness. Не перетворюй довільний byte pointer на `uint32_t *`.
- Для DMA buffers і memory-mapped registers перевір reference manual MCU: alignment може бути потрібним для correctness, atomicity або performance.
- Вимірюй саме target, перш ніж називати фіксований множник затримки.

## Sources

<!-- generated from frontmatter -->
