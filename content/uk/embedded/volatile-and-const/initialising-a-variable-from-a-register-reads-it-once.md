---
id: emb-volconst-0055
title: "Trap: що не так із таким оголошенням register address?"
description: "Це створює окремий об’єкт і один раз ініціалізує його значенням, прочитаним із register-а."
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
volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;
```

## Short answer

<span class="warn">Це створює окремий об’єкт і один раз ініціалізує його значенням, прочитаним із register-а; об’єкт не є alias register address.</span>[^iso-c-n1570]

Після ініціалізації `GPIOA_ODR` – окремий об’єкт. Запис у нього не запише hardware register.

Для доступу до register використовуй lvalue через pointer або macro, відповідно до memory map та правил компілятора цільового MCU.[^iso-c-n1570]

## Detailed explanation

У декларації `volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;` ліворуч оголошено об’єкт із типом `volatile uint32_t`. Вираз ініціалізації справа обчислюється під час ініціалізації: він один раз читає значення за адресою, на яку вказує перетворений pointer, і копіює його в новий об’єкт. Декларація не пов’язує ім’я `GPIOA_ODR` з адресою register-а і не робить його посиланням на той самий об’єкт.[^iso-c-n1570]

Це різниця між значенням і місцем зберігання. Після ініціалізації читання `GPIOA_ODR` читає створений об’єкт, а присвоєння йому змінює цей об’єкт. Таке присвоєння не виконує запис за адресою `0x40020014`. Те, де саме linker розмістить об’єкт, залежить від storage duration, секцій і linker script; для суті помилки достатньо, що це окреме оголошення об’єкта, а не alias register-а.[^iso-c-n1570]

Для memory-mapped I/O типовий підхід – сформувати lvalue через volatile pointer, використовуючи адресу з документації та передбачений компілятором спосіб її подання. Вираз `*(volatile uint32_t *)address` позначає lvalue для цільового об’єкта; читання чи запис через нього підпадають під правила volatile access реалізації. Саме перетворення цілого числа на pointer та доступ до peripheral memory залежать від реалізації й MCU, тож числову адресу не можна вважати переносимою C-конструкцією.[^iso-c-n1570]

**Приклад:** якщо потрібно багаторазово читати й записувати output data register, макрос може розгортатися в lvalue `(*(volatile uint32_t *)0x40020014u)`. Тоді `GPIOA_ODR = value;` записує через lvalue, а не в локальну копію. На реальному проєкті адресу, ширину доступу, вирівнювання та side effects перевіряють за reference manual конкретного MCU; деякі регістри мають особливі правила запису, для яких звичайний read-modify-write заборонений.[^iso-c-n1570]

**Типова помилка:** додати `volatile` до змінної та очікувати, що це перетворить її на hardware register. Кваліфікатор описує доступ до оголошеного об’єкта, а не його фізичну адресу. Переконайся, що вираз зліва від присвоєння справді утворений з адреси register-а, і звір його з документацією платформи.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
