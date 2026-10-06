---
id: emb-patterns-0036
title: "Яке значення матиме `next` і чому?"
description: "next == 0 – wraparound на початок буфера."
track: embedded
section: common-code-patterns
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Підтверджує integer promotions (6.3.1.1), побітове AND (6.5.10) і арифметику unsigned за модулем (6.2.5, пункт 9); не описує конкретних пристроїв і тулчейнів."
  - source_id: linux-circular-buffers
    title: "Circular Buffers (The Linux Kernel documentation)"
    url: https://www.kernel.org/doc/html/latest/core-api/circular-buffers.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Підтверджує, що для кільцевого буфера розміру степеня двійки замість модуля (ділення) використовують побітове AND, а індекс загортається виразом `(head + 1) & (size - 1)`; буфер вважають повним, коли `head` на одиницю менший за `tail`. Це документація ядра Linux, не специфікація для MCU."
---

## Question code

```c
#define RB_SIZE 8
#define RB_MASK (RB_SIZE - 1)
uint16_t head = 7;
uint16_t next = (head + 1) & RB_MASK;
```

## Short answer

**`next == 0`** – wraparound на початок буфера.

`(7 + 1) & 7 = 8 & 0b0111 = 0`: маска `SIZE-1` = `0b0111` залишає лише молодші три біти, тож біт `0b1000` відкидається і індекс «загортається» без `%` чи `if`.[^linux-circular-buffers][^iso-c-n1570]

Правило: цей трюк працює тільки якщо `SIZE` – степінь двійки.

## Detailed explanation

Розберімо вираз крок за кроком. `head` має тип `uint16_t`, але в арифметиці він спершу проходить integer promotions і стає `int`, тож `head + 1` дорівнює `8` типу `int`.[^iso-c-n1570] `RB_MASK` розкривається в `(8 - 1)`, тобто `7` = `0b0111`. Побітове AND залишає біт у результаті лише там, де він встановлений в обох операндах: `0b1000 & 0b0111 = 0b0000`, і в `next` потрапляє `0`.[^iso-c-n1570] Питання в коді нічого не «повертає», тому коректне формулювання – яке значення отримає `next`.

Чому це працює: якщо розмір `N = 2^k`, маска `N - 1` складається з `k` одиниць, і `x & (N - 1)` залишає саме `k` молодших бітів числа – для беззнакових чисел це те саме, що остача `x % N`. Для індексу від `0` до `N - 1` додавання одиниці або дає наступне число, або дає рівно `N` (єдиний встановлений біт `k`), який маска відкидає, – і виходить `0`. Ядро Linux використовує саме цей вираз і пояснює вибір тим, що обчислення модуля потребує повільної інструкції ділення, а для буфера розміру степеня двійки досить побітового AND.[^linux-circular-buffers]

Коли умова порушена, трюк тихо ламається. Нехай `RB_SIZE = 6`, тоді `RB_MASK = 5 = 0b101`. Для `head = 5` маємо `(5 + 1) & 5 = 0b110 & 0b101 = 0b100 = 4`, а не `0`; з `0` отримуємо `1`, а `(1 + 1) & 5 = 0b010 & 0b101 = 0`. Індекс ходить лише по парах `{0, 1}` і `{4, 5}`, а слоти `2` і `3` ніколи не використовуються. Тому розмір варто перевіряти на етапі компіляції, а не покладатися на коментар:

```c
#define RB_SIZE 8u
#define RB_MASK (RB_SIZE - 1u)
_Static_assert(RB_SIZE != 0u && (RB_SIZE & RB_MASK) == 0u,
               "RB_SIZE must be a power of two");
```

Окремо зауважте: якщо кільцевий буфер визначає повноту як `next == tail`, використовуваних елементів буде `N - 1`, бо один слот лишається порожнім – так описує схему й документація ядра.[^linux-circular-buffers] Для free-running індексів (маску застосовують лише під час доступу до масиву) повноту визначають як `head - tail == N`, тож доступні всі `N` елементів; беззнаковий лічильник переповнюється безпечно, бо результат беззнакової арифметики зводиться за модулем, але `N` має ділити `2^16` для `uint16_t`, тобто знову бути степенем двійки.[^iso-c-n1570]

**Типові помилки:**

- Брати `RB_SIZE`, який не є степенем двійки (6, 10, 100), і все одно маскувати `SIZE - 1`.
- Плутати маску з розміром: писати `& RB_SIZE` замість `& (RB_SIZE - 1)`.
- Забувати, що повний буфер за схемою `next == tail` вміщує `N - 1` елементів.

## Sources

<!-- generated from frontmatter -->
