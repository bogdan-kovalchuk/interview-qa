---
id: emb-volconst-0052
title: "Що означає `volatile` для спільних даних у C: чи це заміна mutex або atomic?"
description: "Ні. volatile не замінює mutex, atomic або RTOS synchronization."
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

<span class="warn">Ні. `volatile` не замінює mutex, atomic або RTOS synchronization.</span>

У C `volatile` стосується доступів до volatile-qualified object, але саме по собі не створює synchronizes-with зв’язку між потоками. Для спільних даних між потоками C11 надає atomic operations; RTOS також може визначати власні механізми синхронізації.[^iso-c-n1570]

Правило: використовуй `volatile` лише коли цього вимагають правила реалізації для зовнішніх змін, а synchronization primitives – для синхронізації потоків.[^iso-c-n1570]

## Detailed explanation

`volatile` впливає на те, як реалізація обробляє доступи до volatile-qualified object. Воно не перетворює звичайне читання і запис на неподільну операцію та саме по собі не створює між потоками відношення синхронізації. У C11 атомарні типи й операції мають окремий контракт: вони визначають атомарність і, залежно від memory order, синхронізаційні відношення між потоками.[^iso-c-n1570]

Для embedded-коду важливо розрізняти кілька джерел спільного стану. C standard описує abstract machine, але звичайна апаратна interrupt service routine часто є розширенням компілятора або RTOS. Тому те, як ISR взаємодіє з кодом main loop, визначають документація toolchain і платформи; `volatile` може бути потрібним для спостережуваних доступів, але цього недостатньо, щоб зробити довільний спільний протокол безпечним. Для потоків, що працюють за моделлю C11, невпорядковані конфліктні доступи не стають коректними лише від додавання `volatile`.[^iso-c-n1570]

Наприклад, якщо один RTOS task записує `ready = true`, а інший читає `ready` і після цього читає payload, `volatile bool ready` не встановлює гарантії, що читач побачить попередній запис payload. Потрібні atomic release/acquire або механізм RTOS із визначеною семантикою синхронізації. Для короткої критичної ділянки підійде mutex чи critical section, якщо їхній контракт охоплює обидва контексти. Вибір залежить від того, чи це потоки, ISR, DMA або memory-mapped I/O.[^iso-c-n1570]

**Типова помилка:** вважати, що `volatile` означає «thread-safe». Воно не захищає складену операцію на кшталт перевірки, а потім оновлення, і не встановлює порядок для решти звичайної пам’яті. Спершу визнач джерело конкурентного доступу, а тоді застосуй примітив, який має потрібну семантику саме для цього середовища.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
