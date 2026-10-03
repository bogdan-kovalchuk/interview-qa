---
id: emb-volconst-0044
title: "Trap: чи гарантує `volatile sig_atomic_t` ті самі властивості, що hardware atomic?"
description: "`volatile sig_atomic_t` має вузьку гарантію C для signal handling, а не є універсальним atomic primitive для MCU ISR."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">Ні. `volatile sig_atomic_t` має вузьку гарантію C для signal handling, а не є універсальним atomic primitive для MCU ISR.</span>[^iso-c-n1570]

У стандарті C `sig_atomic_t` призначений для атомарного доступу в контексті signal handling. Це не робить довільний `volatile` тип на MCU атомарним і не задає memory ordering між ISR та основним кодом.

Для MCU перевіряй ширину атомарного доступу за документацією CPU та ABI; складніший обмін захищай підтримуваними atomic operations або critical sections.[^iso-c-n1570]

## Detailed explanation

`sig_atomic_t` – тип із `<signal.h>`, призначений для вузької гарантії C щодо обміну з асинхронним signal handler. Його наявність не означає, що `volatile uint32_t`, довільний лічильник чи будь-який object на MCU є атомарним для interrupt service routine (ISR). Треба розрізняти гарантію мови для signal handling і властивості конкретного процесора та ABI.[^iso-c-n1570]

`volatile` повідомляє компілятору, що object може змінитися поза звичайним потоком виконання, і доступи до нього мають відповідати правилам abstract machine. Сам кваліфікатор не обіцяє атомарність багатобайтового читання чи запису, не створює взаємного виключення і не встановлює memory ordering для інших даних. Такі властивості залежать від atomic operations, архітектури та реалізації; стандарт C також залишає визначення самого volatile access implementation-defined.[^iso-c-n1570]

**Приклад:**

```c
volatile uint32_t ticks;

void timer_isr(void) {
    ++ticks;
}

uint32_t snapshot = ticks; // volatile access, але не автоматична гарантія atomicity
```

У цьому прикладі не можна оголосити `snapshot` узгодженим лише через `volatile`. Якщо CPU читає `uint32_t` однією неподільною інструкцією і переривання не може перервати доступ посередині, це може бути достатньо для простого читання на цій цілі; але це треба підтвердити документацією процесора, ABI та правилами компілятора. Для ширшого за native access значення можливе torn read, коли ISR оновлює частину байтів між операціями читання. Також окремо перевіряй, чи `++ticks` сам є неподільною операцією: читання, збільшення та запис можуть бути кількома інструкціями.[^iso-c-n1570]

Типова пастка проявляється як рідкісне пошкоджене значення або втрачена подія під навантаженням. Не перенось ім’я `sig_atomic_t` на платформний ISR-код як універсальний рецепт. Визнач, які саме дані спільні, звір атомарну ширину з reference manual та compiler ABI, а коли гарантії немає – захисти коротку критичну ділянку чи застосуй atomic API, який підтримує ця платформа.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
