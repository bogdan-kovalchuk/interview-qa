---
id: emb-volconst-0010
title: "Що означає декларація `uint32_t * volatile p`?"
description: "p є volatile-вказівником на звичайний uint32_t."
track: embedded
section: volatile-and-const
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
---

## Short answer

**`p` є volatile-вказівником на звичайний `uint32_t`**.

Тут volatile стосується самого pointer variable, а не даних за адресою. Доступ до `p` є volatile-доступом, але `*p` позначає звичайний `uint32_t`, а не volatile hardware data.[^iso-c-n1570]

Для volatile-даних за адресою потрібен тип `volatile uint32_t *p`; для обох властивостей – `volatile uint32_t * volatile p`.[^iso-c-n1570]

## Detailed explanation

У декларації `uint32_t * volatile p` ім’я `p` позначає вказівник, а `volatile` після зірочки кваліфікує сам pointer variable. Тип об’єкта за адресою – звичайний `uint32_t`, без `volatile`. Отже, компілятор має зберігати семантику доступів до змінної-вказівника `p`, однак це не робить читання `*p` volatile-доступом до цільових даних.[^iso-c-n1570]

Це розрізнення видно, якщо `p` зберігає адресу периферійного регістра. Коли hardware змінює значення за цією адресою, некваліфіковане `*p` може бути прочитане як звичайна пам’ять, тож програма ризикує використати застаріле значення. Кваліфікатор на вказівнику стосується лише збереженої адреси. Він потрібен, коли сама адреса змінюється зовнішнім способом і таке спостереження має бути volatile-доступом, але це окремий випадок.[^iso-c-n1570]

**Приклад:**

```c
uint32_t * volatile p = first_address;
uint32_t value = *p; // ordinary read of pointed-to data
p = second_address;  // volatile access to the pointer object
```

Тут `value` читається через некваліфікований lvalue, а перепризначення `p` змінює volatile pointer variable. Для звичайного memory-mapped register частіше потрібен інший тип:

```c
volatile uint32_t *p = register_address;
uint32_t value = *p; // volatile access to pointed-to data
```

Якщо і вказівник, і дані мають бути volatile, пишуть `volatile uint32_t * volatile p`. C визначає семантику volatile для абстрактної машини й лишає конкретне поняття доступу реалізації; апаратний ефект треба звірити з документацією компілятора та MCU. Наявність `volatile` також не забезпечує атомарність чи взаємне виключення.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->
