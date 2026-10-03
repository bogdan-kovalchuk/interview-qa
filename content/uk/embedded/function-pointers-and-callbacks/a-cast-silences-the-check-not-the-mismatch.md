---
id: emb-fnptr-0017
title: "Чому cast function pointer-а часто приховує реальний баг?"
description: "Cast вимикає перевірку типів, але не змінює реальну сигнатуру функції."
track: embedded
section: function-pointers-and-callbacks
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

<span class="warn">Cast вимикає перевірку типів, але не змінює реальну сигнатуру функції.</span>

Якщо API очікує `void (*)(void *)`, а ти передаєш `void (*)(int)` через cast, caller усе одно викличе функцію за контрактом API. Аргументи будуть передані не так, як очікує callee. Це не portable і може бути UB.

Захист: пиши thin wrapper: `static void wrapper(void *ctx) { real_handler((int)(intptr_t)ctx); }`, якщо така модель справді потрібна.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

Cast function pointer змінює тип виразу, яким програма бачить адресу, але не переписує визначення функції і не створює код адаптації. Стандарт C допускає перетворення між типами вказівників на функції та вимагає, щоб перетворений вказівник можна було повернути до початкового типу; виклик через тип, несумісний із типом функції, залишається undefined behavior. [^iso-c-n1570]

Припустімо, API приймає `void (*)(void *)`, а функція має тип `void (*)(int)`. Після cast компілятор може перестати попереджати про невідповідність у місці передавання, але API викликає callback за власним контрактом і подає `void *`. Функція ж очікує `int`. На конкретному ABI це може призвести до помилкового читання аргументу чи іншого результату, але точний прояв не визначає мова C. [^iso-c-n1570]

**Типові помилки:**

- Сприймати успішну компіляцію як доказ сумісності типів.
- Використовувати cast як «перекладач» між різними calling convention або типами аргументів.
- Перетворювати `void *` на `int` без перевірки ширини й контракту платформи.

Якщо callback має отримати стан, використовуйте передбачений API `void *ctx` і передавайте в ньому адресу об’єкта правильного типу. Статичний wrapper із сигнатурою API може привести контекст назад до узгодженого типу, перевірити його та викликати справжній handler. Якщо ж значення зберігається в pointer, перетворення на ціле число залежить від реалізації та потребує окремо задокументованої гарантії платформи. [^iso-c-n1570]

Приклад: `static void wrapper(void *ctx) { struct state *s = ctx; real_handler(s->value); }` має тип callback API; функція `real_handler` викликається звичайним типобезпечним викликом. Тож wrapper усуває розбіжність структурно, тоді як cast лише приховав би її від діагностики. [^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
