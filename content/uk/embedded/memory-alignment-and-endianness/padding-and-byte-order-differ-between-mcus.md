---
id: emb-align-0020
title: "Trap: чому не можна передавати raw-структуру через `memcpy` між різними MCU?"
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
  - source_id: learncpp-struct-miscellany
    title: "Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

<span class="warn">In-memory representation структури C є деталлю ABI, а не переносним wire-форматом.</span>

Два endpoints можуть випадково збігтися, але різні ABI здатні вибрати інші member offsets, tail padding, type widths, alignment і byte order. Raw `memcpy` передає всі ці implementation choices разом із padding bytes.

Захист: завжди визначай явний wire-формат і серіалізуй поле за полем з явним byte order.[^embeddedinterviewlab]

## Detailed explanation

Для структури C зберігає порядок оголошення членів, але дозволяє безіменний padding між ними та після останнього члена. Його обсяг є implementation-defined, і навіть representation скалярних членів не утворює переносний serialization contract.[^iso-c-n1570] Додаткові ризики:

- `int`, `long`, enums, pointers і floating-point types можуть мати різні розміри або representations;
- integer byte order може відрізнятися;
- bit-field allocation order і packing є implementation-defined;
- padding bytes можуть містити unspecified data й під час передавання розкрити старі дані з пам'яті;
- compiler options на кшталт packing змінюють ABI, але не визначають протокол.

Сам `memcpy` точно виконує запитане копіювання байтів. Помилка полягає в його застосуванні до об'єкта, байти якого ніколи не визначали як interoperable message. Packing може скоротити padding, але не нормалізує endianness, scalar representation або versioning.

Визначай wire format незалежно: точні widths полів, byte offsets, signedness, byte order, reserved bytes і правила версій. Кодуй кожне поле в byte buffer і декодуй його у вирівняні native objects. POSIX network order – один із прикладів такого явного контракту для певних integer widths.[^posix-byte-order] Тестуй за golden byte vectors, а не лише round trip між однаковими збірками.

Raw-копіювання структури прийнятне лише всередині свідомо обмеженої ABI boundary, де обом сторонам гарантовано однакові визначення типу, compiler ABI, options, alignment, representation і version. Зафіксуй та перевір цю умову; не роби такого висновку лише тому, що обидва пристрої називаються MCU.

Матеріал LearnCpp про структури показує, як padding з'являється в layout,[^learncpp-struct-miscellany] а дорожня карта aCode є додатковим орієнтиром для подальшого вивчення C і C++.[^acode-cpp-next]
