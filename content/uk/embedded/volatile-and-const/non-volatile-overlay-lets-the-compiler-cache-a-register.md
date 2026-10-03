---
id: emb-volconst-0046
title: "Trap: що не так із таким struct overlay?"
description: "Поля register overlay не volatile-qualified."
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
typedef struct {
    uint32_t MODER;
    uint32_t IDR;
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
```

## Short answer

<span class="warn">Поля register overlay не мають qualifier `volatile`.</span>

`GPIOA->IDR` має тип звичайного `uint32_t`, тому C abstract machine не вимагає окремого volatile-доступу при кожному читанні. Для register, який змінює hardware, це може дати застаріле значення.[^iso-c-n1570]

Захист: оголоси поля як `volatile uint32_t MODER;`, `volatile uint32_t IDR;` або використовуй vendor CMSIS headers, де qualifiers уже задані.[^iso-c-n1570]

## Detailed explanation

`volatile` у типі register overlay позначає доступи, значущі поза звичайним потоком виконання C, наприклад через peripheral hardware. C стандарт не задає конкретну адресу GPIO чи поведінку шини: коректність адреси, ширини доступу та qualifier залежить від memory map і документації MCU.[^iso-c-n1570]

У наведеному прикладі `GPIOA->IDR` читається через lvalue типу `uint32_t`, який не є volatile-qualified. Якщо цикл очікує, що периферія змінить IDR, компілятор не зобов’язаний трактувати повторне читання як окрему подію пристрою; оптимізований код може не перечитувати адресу так, як задумано програмістом. Це не гарантує, що кожен компілятор неодмінно кешуватиме register, але код не виражає потрібної властивості.[^iso-c-n1570]

Типова помилка – вважати, що сама адреса peripheral memory автоматично повідомляє компілятору про hardware. Для C це лише вказівник на об’єкт заданого типу; спеціальна семантика має бути відображена у типі й підтримана ABI та компілятором платформи. `volatile` також не робить операцію atomic і не замінює memory barrier чи синхронізацію між потоками.[^iso-c-n1570]

Приклад виправленого оголошення:

```c
typedef struct {
    volatile uint32_t MODER;
    volatile uint32_t IDR;
} GPIO_TypeDef;
```

**Типова помилка:** додати `volatile` до локальної копії значення, а не до доступу за memory-mapped адресою. Перевіряй оголошення самого register pointer та точне формулювання в reference manual MCU; використовуй vendor header, якщо він відповідає цій ревізії пристрою.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
