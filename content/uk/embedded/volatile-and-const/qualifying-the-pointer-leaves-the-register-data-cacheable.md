---
id: emb-volconst-0011
title: "Trap: чому `uint32_t * volatile reg` не є правильним типом для hardware register data?"
description: "volatile застосований до pointer variable, а не до даних за адресою."
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

<span class="warn">`volatile` застосований до pointer variable, а не до даних за адресою.</span>

`volatile` стосується доступу до самої змінної-вказівника, а тип `*reg` лишається звичайним `uint32_t`. Отже, доступ до register data не має volatile-кваліфікатора й не отримує властивих йому правил обчислення.[^iso-c-n1570]

Захист: використовуй `volatile uint32_t *reg` для pointer to volatile data або `volatile uint32_t * const reg`, якщо адреса фіксована.[^iso-c-n1570]

## Detailed explanation

У `uint32_t * volatile reg` кваліфікатор `volatile` стоїть праворуч від `*`, отже він належить самому об’єкту-вказівнику `reg`. Тип даних, на які вказує `reg`, – звичайний `uint32_t`. Це важливо, бо компілятор застосовує кваліфікатори до конкретного типу, а не до всього виразу декларації: volatile pointer і pointer to volatile – різні типи.[^iso-c-n1570]

Для апаратної адреси змінюваною зазвичай є величина в регістрі, а не адреса, яку треба завантажувати з `reg`. Тому тип часто записують як `volatile uint32_t * const reg`: `const` фіксує адресу вказівника, а `volatile` кваліфікує об’єкт, доступний через розіменування. Саме розміщення кваліфікаторів визначає, до якого об’єкта застосовуються правила мови C.[^iso-c-n1570]

Наприклад, цикл, що чекає на апаратний прапорець, повинен читати volatile-об’єкт щоразу відповідно до правил конкретної реалізації C. Якщо кваліфікувати лише pointer variable, читання `*reg` залишається звичайним читанням, і компілятор не зобов’язаний трактувати його як доступ до volatile-об’єкта. Стандарт уточнює, що таке доступ до volatile-об’єкта, визначає реалізація, тому потрібно звірятися також із документацією компілятора та MCU.[^iso-c-n1570]

Приклад правильного розрізнення типів:

```c
volatile uint32_t * const reg = (volatile uint32_t *)address;
uint32_t value = *reg;  // volatile data, fixed pointer
```

**Типова помилка:** читати декларацію зліва направо й вважати, що будь-яке `volatile` робить volatile весь вираз. Щоб уникнути цього, визнач спершу об’єкт, який має змінюватися апаратурою, а тоді перевір, що саме його тип кваліфікований. `volatile` не гарантує атомарності, синхронізації між потоками чи апаратного memory barrier; для таких гарантій потрібні відповідні засоби платформи.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
