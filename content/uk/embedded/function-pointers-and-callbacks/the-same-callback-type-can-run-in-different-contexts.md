---
id: emb-fnptr-0050
title: "Чому callback API має документувати execution context?"
description: "Бо той самий callback type може викликатися з ISR, task, main loop або driver lock context."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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
  - source_id: freertos-isr-api
    title: "Mastering the FreeRTOS Real Time Kernel: Using the FreeRTOS API from an ISR"
    url: https://www.freertos.org/media/2018/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf
    accessed: 2026-10-04
    kind: official
    version: "V10.0.0 tutorial"
    applicability: "Пояснює, що ISR не може блокувати task і потребує спеціально дозволених ISR-safe API; конкретні обмеження залежать від платформи."
---

## Short answer

**Бо той самий callback type може викликатися з ISR, task, main loop або driver lock context.**[^freertos-isr-api]

Від цього залежить, чи можна блокуватися або викликати API, що може чекати на task чи scheduler. Наприклад, FreeRTOS має окремі ISR-safe варіанти API, бо звичайний виклик може спробувати перевести task у Blocked state, чого ISR зробити не може.[^freertos-isr-api]

Тому callback contract має описувати execution context та дозволені операції; також корисно вказати reentrancy, lifetime і ownership.

## Detailed explanation

Execution context – це середовище, з якого виконується callback: звичайний код у task або main loop, ISR чи ділянка driver-а з утримуваним lock. Однакова сигнатура функції не означає однакові умови виконання: тип вказівника описує параметри й результат, але не повідомляє, чи дозволено чекати, брати mutex або викликати конкретне API.

Різниця особливо помітна в interrupt context. ISR має завершитися швидко і не може приспати поточний task, бо переривання не виконується як task. У FreeRTOS для частини операцій є окремі варіанти з суфіксом `FromISR`; звичайні API, що можуть блокувати task, у цьому контексті не підходять. Це правило стосується FreeRTOS, а не кожного RTOS, тому контракт конкретного callback має називати платформу та її правила.[^freertos-isr-api]

Виклик під lock створює інший ризик: якщо callback повторно зайде у той самий driver або чекатиме на ресурс, який утримує caller, виникне deadlock. Якщо ж один callback використовується з task і ISR, треба окремо перевірити синхронізацію спільного стану та безпечність функцій, які він викликає. «Коротка функція» сама по собі не є доказом безпеки.

Приклад: драйвер UART може передавати подію приймання байта двома способами. У першому він викликає callback безпосередньо з ISR, тож callback лише зберігає байт у кільцевому буфері й сигналізує task дозволеним ISR-safe механізмом. У другому ISR ставить подію в чергу, а callback викликається вже з task; тоді допустимий набір операцій може бути ширшим. Контракт має точно вказати, який із цих варіантів реалізовано.[^freertos-isr-api]

**Типові помилки:**

- Вважати, що callback можна блокувати лише тому, що він має звичайну C-функційну сигнатуру.
- Брати mutex або викликати довгу операцію з ISR, не перевіривши контракт RTOS.
- Не врахувати, що driver може викликати callback під власним lock.

Документація має назвати контекст, допустимі API, можливість повторного входу, час життя переданих вказівників і відповідального за їхнє володіння. Це перетворює приховані припущення на перевірюваний контракт.

## Sources

<!-- generated from frontmatter -->
