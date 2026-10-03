---
id: emb-volconst-0015
title: "Trap: чи можна записати в такий регістр?"
description: "Ні. Це має бути помилка компіляції, бо STATUS має const-qualified type."
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
volatile const uint32_t * const STATUS =
    (volatile const uint32_t *)0x40020008;

*STATUS = 0;
```

## Short answer

<span class="warn">Ні. Це порушення обмежень мови C, і реалізація має видати діагностику</span>, бо `*STATUS` має const-qualified type.[^iso-c-n1570]

`volatile` не скасовує `const`: воно кваліфікує доступ до об’єкта, а `const` не дозволяє модифікувати його через цей lvalue.[^iso-c-n1570]

Захист: read-only регістри описуй як `volatile const`, якщо це відповідає документації MCU. Діагностика обов’язкова за стандартом, але компілятор може продовжити трансляцію після її видачі.[^iso-c-n1570]

## Detailed explanation

Запис `*STATUS = 0` намагається змінити об’єкт, на який указує `STATUS`. Після розіменування тип `*STATUS` є `volatile const uint32_t`: `const` лишається на цільовому об’єкті, тож результат не є modifiable lvalue. Оператор присвоєння в C вимагає modifiable lvalue зліва, а порушення цього обмеження вимагає діагностики під час трансляції. Стандарт не вимагає від компілятора припинити трансляцію після діагностики, тому точніше казати «constraint violation, що потребує діагностики», а не гарантувати конкретне повідомлення чи зупинку компіляції.[^iso-c-n1570]

`volatile` не змінює це правило. Він кваліфікує цільовий об’єкт і впливає на те, як реалізація обробляє доступи до нього; він не знімає `const` і не перетворює read-only lvalue на записуваний. Так само const pointer і pointer to const data – різні речі: у наведеному коді сам `STATUS` незмінний, а його ціль окремо const-qualified. Тому і перепризначення pointer, і запис через нього мають різні причини бути забороненими.[^iso-c-n1570]

На практиці це має зупинити помилковий запис у регістр, який програмний контракт визначає як read-only. Але сам тип не захищає апаратну пам’ять від усіх можливих записів: інший pointer, cast або помилкове оголошення можуть обійти статичну перевірку, а поведінка запису в конкретний MMIO регістр визначається MCU. Тому перевіряй доступи в reference manual і користуйся vendor header, коли він точно описує регістр. Не прибирай `const` лише для придушення діагностики – це приховує помилку типу, а не робить апаратний запис безпечним.[^iso-c-n1570]

Приклад коректного читання такого статусу:

```c
uint32_t status_bits = *STATUS;
```

Якщо ж регістр справді призначений для запису, його оголошення має відображати це апаратне право: прибрати `const` із типу даних, лишивши volatile там, де цього вимагає платформа. Для питань із `const` не покладайся тільки на назву `STATUS`; перевір декларацію, а потім властивості периферії.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
