---
id: emb-dtypes-0019
title: "Що таке little-endian і big-endian? Як Cortex-M зберігає `0x12345678`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m0-datasheet
    title: "Arm Cortex-M0 Processor Datasheet"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Processor%20Datasheets/Arm_Cortex-M0_Processor_Datasheet.pdf?hash=4AF1DD0929A9911BDC7FFC800BC74F7D&revision=9310a7ce-480c-4491-88e7-c4392d28fb80
---

## Short answer

**Endianness** – порядок байтів багатобайтового значення в пам’яті.

**Little-endian**: LSB за нижчою адресою, тож `0x12345678` зберігається як `[78][56][34][12]`, якщо байтова адреса зростає. Endianness Cortex-M залежить від конкретної реалізації та конфігурації; перевіряйте документацію ядра/SoC, а не вважайте режим універсальним.[^arm-cortex-m0-datasheet]

**Big-endian**: MSB зберігається за нижчою адресою; порядок байтів протоколу – окреме правило формату, тож серіалізуйте байти явно або застосовуйте відповідні перетворення.[^iso-c-n1570]

## Detailed explanation

Endianness описує порядок байтів у пам’яті для значень, що займають кілька байтів; він не змінює числове значення чи порядок бітів усередині байта. У little-endian найменш значущий байт лежить за найменшою адресою. Наприклад, за такої конфігурації чотири байти `0x12345678` за адресами `p` до `p+3` матимуть значення `78`, `56`, `34`, `12`.[^iso-c-n1570]

У big-endian за найменшою адресою лежить найзначущий байт: для того самого числа послідовність буде `12`, `34`, `56`, `78`. Документація Arm для Cortex-M0 перелічує підтримку як little-endian, так і byte-invariant big-endian доступів; отже, не слід поширювати припущення про один режим на всі реалізації Cortex-M. Перевіряйте конкретний MCU та налаштування його системи.[^arm-cortex-m0-datasheet]

Порядок CPU і порядок байтів протоколу – різні речі. Протокол може вимагати big-endian незалежно від того, як процесор представляє ціле число в RAM. Під час обміну байтами формуйте або розбирайте кожен байт явно, або використовуйте API перетворення з потрібною семантикою; не передавайте сире представлення цілого як переносимий формат.

**Типова помилка:** робити висновок про порядок байтів із надрукованого hex-значення. Форматований друк показує числове значення, а не послідовність байтів у пам’яті; перевірка має дивитися на окремі адреси або документовану ABI.
