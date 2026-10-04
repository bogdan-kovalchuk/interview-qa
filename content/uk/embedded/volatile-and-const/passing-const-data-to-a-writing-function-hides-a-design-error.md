---
id: emb-volconst-0050
title: "Trap: чи можна передати `const uint8_t *` у функцію, яка очікує `uint8_t *`?"
description: "Без cast не можна; з cast можна приховати помилку дизайну."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
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

<span class="warn">Без діагностики компілятора так передати не можна; cast не робить запис законним для справді const-об’єкта.</span>

У C передача `const uint8_t *` туди, де потрібен `uint8_t *`, порушує обмеження сумісності типів і вимагає діагностики. Якщо прибрати qualifier cast-ом, запис є undefined behavior, коли початковий об’єкт справді був оголошений `const`; інакше запис може бути допустимим, але API все одно приховує намір.[^iso-c-n1570]

Розділяй API: input buffer як `const uint8_t *`, output buffer як `uint8_t *`. Не прибирай qualifier без перевірки того, чи початковий об’єкт змінюваний.[^iso-c-n1570]

## Detailed explanation

Параметр `uint8_t *` обіцяє, що функція може змінювати байти через цей вказівник. А `const uint8_t *` такого дозволу не дає. У C ці типи не є сумісними для звичайного присвоєння аргументу параметру: виклик функції, яка очікує змінюваний вказівник, з const-вказівником порушує constraint і компілятор має видати діагностику.[^iso-c-n1570]

Cast може прибрати кваліфікацію в типі виразу, але не змінює властивостей самого об’єкта. Якщо початковий об’єкт був визначений з `const`, спроба модифікувати його через перетворений вказівник має undefined behavior. Якщо об’єкт насправді змінюваний, запис через alias без `const` може бути дозволений мовою, але такий cast усе одно приховує контракт API та ускладнює рев’ю.[^iso-c-n1570]

**Приклад:** функція обробки пакета, якій потрібні лише вхідні дані, має приймати `const uint8_t *input`; функція заповнення результату має отримувати `uint8_t *output`. Якщо одна функція робить обидві речі, її параметри варто розділити або явно описати змінюваний буфер. Це також дає компілятору й читачеві точний контракт.[^iso-c-n1570]

**Типова помилка:** додати cast, щоб прибрати compiler warning, а потім дозволити функції записувати у пам’ять. Симптомом може стати fault під час спроби запису у Flash чи read-only region; якщо об’єкт C оголошений `const`, така модифікація також порушує правила мови. Спершу виправ тип параметра або передай окремий змінюваний буфер.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
