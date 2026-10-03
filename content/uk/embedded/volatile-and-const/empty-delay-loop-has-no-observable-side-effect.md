---
id: emb-volconst-0034
title: "Trap: що не так із таким delay loop?"
description: "Компілятор може повністю прибрати порожній loop, бо він не має observable side effects."
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

## Question code

```c
for (uint32_t i = 0; i < 100000; ++i) {
}
```

## Short answer

<span class="warn">Компілятор може повністю прибрати порожній loop</span>, бо він не має observable side effects.[^iso-c-n1570]

Додавання `volatile` до лічильника іноді змушує виконати інкременти, але це погана основа для точного timing: оптимізація, частота CPU, wait states і pipeline змінюють реальну затримку.

Захист: для затримок використовуй hardware timer, SysTick, DWT cycle counter або RTOS delay. `volatile` не є timing API.[^iso-c-n1570]

## Detailed explanation

Порожній цикл у прикладі не змінює стан, який програма спостерігає, і не виконує volatile access. Компілятор може зберегти лише потрібну поведінку програми й вилучити цикл разом із лічильником: час, витрачений на обчислення, не є спостережуваним результатом за правилами абстрактної машини C. Тут умова циклу скінченна, бо `i` доходить до 100000 і зупиняється; отже цикл не є нескінченним.[^iso-c-n1570]

На рівні оптимізації без змін цикл може виглядати як очікувана затримка, а з оптимізацією виконуваний код може не містити очікування зовсім. Інший варіант – позначити лічильник як `volatile`, що створює volatile access під час читань і записів, але точна семантика доступу залежить від реалізації. Навіть тоді кількість циклів процесора не задає сталу тривалість у часі: частота ядра, wait states, кеші, переривання та параметри компіляції впливають на результат.[^iso-c-n1570]

Для затримки потрібного часу використовуйте засіб, визначений платформою: hardware timer, SysTick, DWT cycle counter або RTOS delay. Вони прив’язують очікування до лічильника часу чи scheduler і дають змогу врахувати тактування MCU. Для короткого busy-wait теж потрібен контракт конкретного MCU та перевірка зібраного коду; `volatile` не є переносним timing API.[^iso-c-n1570]

Приклад проблеми:

```c
for (uint32_t i = 0; i < 100000; ++i) {
    // порожнє тіло не створює спостережуваного ефекту
}
```

**Як уникнути пастки:** не оцінюйте затримку за кількістю ітерацій у вихідному тексті. Вимірюйте потрібний інтервал периферійним таймером або використовуйте перевірений платформний API затримки.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
