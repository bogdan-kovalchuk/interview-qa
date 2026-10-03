---
id: emb-volconst-0004
title: "Trap: чи робить `volatile` операцію атомарною?"
description: "Ні. volatile не гарантує atomicity."
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Поведінка volatile-доступів і відсутність гарантії memory barrier у GCC; інші компілятори можуть відрізнятися."
---

## Short answer

<span class="warn">Ні. `volatile` не гарантує atomicity.</span> Наприклад, `volatile uint32_t` на 8-bit MCU може читатися кількома інструкціями, і ISR може спрацювати між ними; навіть якщо окреме читання `counter` атомарне на певному Cortex-M, `counter++` складається з читання, обчислення й запису.

Захист: для shared state використовуй atomic operations, critical section або платформні primitives, підібрані до потрібної гарантії.[^iso-c-n1570]

## Detailed explanation

`volatile` і atomicity відповідають на різні запитання. `volatile` стосується спостережуваності доступу для реалізації C; atomicity означає, що інша сторона не може побачити проміжний стан операції. З кваліфікатора не випливає, що CPU виконає доступ однією інструкцією або що читання та запис утворять неподільну транзакцію.[^iso-c-n1570]

Розмір і властивості шини мають значення. На 8-bit MCU читання 32-bit об’єкта може потребувати кількох byte access; якщо ISR змінить його посеред послідовності, код може зібрати суміш старих і нових байтів. На іншому MCU одиночне вирівняне читання 32-bit значення може бути атомарним за документацією CPU, але це не робить атомарним `counter++`: це read-modify-write із окремим читанням і записом. Не поширюй гарантію окремого load/store на складений вираз.[^iso-c-n1570]

У багатопотоковому коді C використовуй `_Atomic` типи та операції стандартної бібліотеки, якщо вони підтримуються й відповідають задачі. У взаємодії main code з ISR або DMA рішення залежить від toolchain та MCU: коротка critical section може захистити спільний доступ від ISR, а DMA може вимагати окремих кешових та memory barrier дій. Перевіряй, чи дозволена конкретна операція в ISR і чи справді вона lock-free; atomic API не обіцяє цього для кожного типу й платформи.[^iso-c-n1570] [^gcc-volatile]

Приклад: якщо main code збільшує лічильник, а ISR теж його змінює, два `counter++` можуть перезаписати один одного навіть за volatile-декларації. Потрібна одна узгоджена стратегія синхронізації, яка охоплює всю read-modify-write операцію.

**Типова помилка:** перевірити лише, що змінна оголошена `volatile`, і зробити висновок про атомарність. Визнач ширину доступу, можливість переривання та межі критичної операції.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
