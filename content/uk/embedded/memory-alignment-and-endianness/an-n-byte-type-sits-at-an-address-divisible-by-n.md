---
id: emb-align-0001
title: "Що таке natural alignment?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Розміри об’єктів і оператор sizeof"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-next-cpp
    title: "aCode: Кінець? Що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**Об’єкт має лежати за адресою, яка задовольняє вимогу вирівнювання його типу.**

У типовому ABI для MCU природне вирівнювання `uint32_t`, `uint16_t` і `uint64_t` дорівнює відповідно 4, 2 і 8 байтам, але сам розмір не задає переносне правило. Допустима адреса кратна `_Alignof(T)` у C або `alignof(T)` у C++.

Доступ через невирівняний типізований pointer має undefined behavior у C, навіть якщо апаратура вміє виконати відповідну інструкцію.[^embeddedinterviewlab]

## Detailed explanation

**Вимога вирівнювання** – це визначена реалізацією кількість байтів між допустимими початковими адресами об’єктів певного типу. У C її повертає `_Alignof(T)`, у C++ – `alignof(T)`. Точне правило спирається на це значення, а не на `sizeof(T)`.[^iso-c-n1570]

Наприклад, в ABI, де `_Alignof(uint32_t) == 4`, допустимі початкові адреси кратні 4. Це твердження про ABI: сама мова не гарантує чотирибайтового вирівнювання 32-бітного типу, а для розширених типів alignment може бути меншим за розмір. `sizeof` більшості фундаментальних типів також залежить від реалізації.[^learncpp-object-sizes]

Вирівнювання має два різні рівні:

- Object model мови C вимагає, щоб об’єкт зберігався за належно вирівняною адресою. Перетворення адреси byte buffer на `T *` не робить її вирівняною; розіменування невирівняного pointer має undefined behavior.
- Апаратура може виконати unaligned instruction, розкласти її на кілька transfer або згенерувати fault. Поведінка залежить від інструкції, memory region, налаштувань ядра та реалізації шини.

Для звичайних змінних, елементів масиву та виділених об’єктів compiler забезпечує потрібне вирівнювання. Він також додає padding у структури, щоб кожне поле та кожен елемент масиву структур починалися за допустимою адресою.

Коли байти надходять із packet, file, packed structure або peripheral buffer, скопіюй їх через `memcpy` у вирівняний об’єкт і явно декодуй byte order. Сам cast не виправляє ані вирівнювання, ані representation.

Використовуй `_Alignas` у C або `alignas` у C++, коли storage потребує суворішого вирівнювання, ніж дає його звичайне оголошення. Вимоги protocol, DMA, cache line і peripheral перевіряй окремо, бо вони можуть бути суворішими за natural alignment типу.
