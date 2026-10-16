---
id: emb-dtypes-0004
title: "Що таке секція `.bss` і чим вона відрізняється від `.data`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

У типовому embedded образі `.bss` описує глобальні або `static` об'єкти, які мають початкове нульове значення, а `.data` – об'єкти з ненульовим початковим значенням. Startup code зазвичай обнуляє діапазон `.bss` у RAM і копіює початкові байти `.data` з ROM/Flash до RAM; точне компонування задає linker script.[^embedded-ld-layout]

## Detailed explanation

У C об'єкти з static storage duration, які не мають явного ініціалізатора, гарантовано отримують нульове початкове значення; це правило мови не вимагає секції з назвою `.bss`.[^iso-c-n1570]

У поширеному embedded компонуванні linker відводить таким об'єктам діапазон RAM у `.bss`, а об'єктам з ненульовими початковими значеннями – RAM у `.data`. Значення `.data` зберігаються в ROM/Flash як load image, тоді як виконувана адреса вказує на RAM. На старті runtime копіює `.data` і зануляє `.bss` до виклику `main`.[^embedded-ld-layout]

Нульове значення не означає, що об’єкт «не існує» або не займає RAM: у `.bss` усе одно резервується потрібний обсяг RAM. Економія стосується образу Flash, де зазвичай не треба зберігати послідовність нульових байтів. Формат object file, linker script і boot/runtime середовище можуть змінити представлення, тому для конкретного MCU перевіряйте map-файл та startup code.[^embedded-ld-layout]

Той самий принцип стосується і локального об’єкта з `static`: його тривалість зберігання є статичною, хоча ім’я доступне лише в межах блока, де його оголошено; розміщення визначає реалізація та компонувальник.[^iso-c-n1570]

**Приклад:**

```c
static int retries;       // початкове значення 0, зазвичай .bss
static int limit = 3;     // початкове значення 3, зазвичай .data
```

Обидва об'єкти мають static storage duration і займають RAM під час виконання; лише для `limit` потрібні ненульові початкові байти в образі завантаження.
