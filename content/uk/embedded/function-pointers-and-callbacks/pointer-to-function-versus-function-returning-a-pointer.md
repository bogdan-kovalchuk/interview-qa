---
id: emb-fnptr-0003
title: "Trap: чим відрізняються `void (*f)(void)` і `void *f(void)`?"
description: "Це повністю різні типи."
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

<span class="warn">Це повністю різні типи.</span>

`void (*f)(void)` – змінна `f`, яка є pointer to function returning void. `void *f(void)` – функція `f`, яка приймає nothing і повертає `void *`.

Щоб розрізнити їх, починай читати декларацію з імені й рухайся назовні за дужками.[^iso-c-n1570]

## Detailed explanation

`void (*f)(void)` оголошує `f` як вказівник на функцію без параметрів, що повертає `void`, тоді як `void *f(void)` оголошує `f` як функцію без параметрів, що повертає вказівник на `void`. Різницю визначають дужки навколо `*f`: у першій декларації вони групують зірочку з ім’ям і змінюють зв’язування наступного списку параметрів.[^iso-c-n1570]

Прочитай першу декларацію, починаючи з `f`: `*f` означає, що це вказівник; `(void)` після закриття групувальних дужок означає функціональний тип без параметрів; `void` на початку є типом повернення цієї функції. Отже, `f` зберігає посилання на функцію, яку можна вибрати або замінити під час виконання та викликати як `f()`. Сам вказівник може бути null, тому перед викликом його значення має бути задане коректною функцією.[^iso-c-n1570]

У другому випадку `f(void)` безпосередньо оголошує функцію, а початкове `void *` задає її результат. Виклик `f()` виконує тіло функції й повертає вказівник на об’єкт або null; це не callback-змінна. Для C `void` у списку параметрів позначає відсутність параметрів, на відміну від старої декларації з порожніми дужками, яка не задає прототип із перевіреним списком параметрів.[^iso-c-n1570]

Приклад:

```c
void on_tick(void);
void (*callback)(void) = on_tick;
void *get_context(void);
callback();
void *context = get_context();
```

Тут `callback()` запускає `on_tick`, а `get_context()` виконується як звичайна функція і повертає значення. Типова помилка – дивитися лише на `void` на початку й пропускати, що саме оголошує ідентифікатор. Щоб уникнути її, починай розбір із `f` та йди за дужками назовні; для повторно вживаних callback-сигнатур оголошуй зрозумілий `typedef`.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
