---
id: emb-align-0011
title: "Що таке little-endian і big-endian для значення `0x12345678`?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: posix-byte-order
    title: "General Concepts: Data Types"
    url: https://pubs.opengroup.org/onlinepubs/009696699/basedefs/xbd_chap04.html
  - source_id: learncpp-object-sizes
    title: "Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**Порядок байтів багатобайтового значення в пам’яті.**

```text
Address: 00   01   02   03
LE:      78   56   34   12  (least-significant byte first)
BE:      12   34   56   78  (most-significant byte first)
```

LSB (least significant byte) – найменш значущі вісім бітів, а MSB (most significant byte) – найбільш значущі вісім бітів. Little-endian зберігає LSB за найнижчою адресою, а big-endian зберігає там MSB. Конкретний порядок байтів є властивістю цільової платформи або формату даних, а не самого цілого числа.

Правило: endianness впливає лише на багатобайтові типи; масив `uint8_t` однаковий усюди.[^embeddedinterviewlab]

## Detailed explanation

Ціле число `0x12345678` має однакове математичне значення в обох випадках. Endianness стає видимою, коли його багатобайтове object representation зберігають, переглядають як байти або передають у формат із визначеним порядком байтів. Чотири складові байти – `0x12`, `0x34`, `0x56` і `0x78`; змінюється лише порядок їхніх адрес.

У C кожен об’єкт має послідовність байтів, яку називають object representation. Типи символів можуть переглядати ці байти, тому дослідження цілого числа через `unsigned char *` коректно показує представлення цільової платформи.[^iso-c-n1570] Стандарт мови не зобов’язує звичайні цілі числа мати little-endian або big-endian порядок, тому переносний код не повинен цього припускати.

Endianness не розвертає масив байтів. Якщо buffer містить послідовність `{ 0x12, 0x34, 0x56, 0x78 }`, його індекси зберігають цей порядок на кожній відповідній стандарту платформі. Питання полягає в тому, яке числове значення код утворить, інтерпретуючи ці байти як одне багатобайтове ціле.

Зовнішні інтерфейси усувають неоднозначність, визначаючи порядок. POSIX network byte order ставить найстарший octet першим і надає функції перетворення для 16- та 32-бітних значень.[^posix-byte-order] Для форматів файлів, регістрів пристроїв і протоколів поза IP дотримуйся їхньої власної специфікації.

Матеріал LearnCpp про розміри об’єктів дає корисний вступ до того, як об’єкти займають байти,[^learncpp-object-sizes] а дорожня карта aCode є додатковим шляхом подальшого системного вивчення C і C++.[^acode-cpp-next]
