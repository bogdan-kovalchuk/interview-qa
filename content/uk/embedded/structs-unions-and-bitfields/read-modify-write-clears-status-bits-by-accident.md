---
id: emb-structs-0026
title: "Trap: що не так із read-modify-write для status register?"
description: "Компілятор може згенерувати read-modify-write усього register-а."
track: embedded
section: structs-unions-and-bitfields
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
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0483 Rev 6"
    applicability: "Приклад визначення W1C у документації виробника; фактичну семантику треба перевіряти в manual конкретного пристрою."
---

## Question code

```c
STATUS.bits.error = 0;
```

## Short answer

<span class="warn">Компілятор може згенерувати read-modify-write усього register-а.</span>

Якщо STATUS має read-to-clear bits або write-one-to-clear bits, простий запис одного bit-field може ненавмисно очистити або змінити інші flags. Для hardware registers semantics важливіша за C-level зручність.

Захист: використовуй documented clear register або записуй точну mask, наприклад `STATUS = ERROR_Msk;` для W1C, якщо manual вимагає саме так.[^stm32-w1c-manual]

## Detailed explanation

Read-modify-write для status register може підтвердити подію, яку код не збирався скидати, адже register може надавати окреме значення прочитаним і записаним бітам.

Вираз C `STATUS.bits.error = 0` описує присвоєння полю, але не задає обов’язкову транзакцію шини. Компілятор може реалізувати його читанням одиниці зберігання, зміною вибраного біта в CPU register і записом одиниці назад. Чи буде згенеровано саме таку послідовність, залежить від compiler і target, тому важливо перевірити assembly. Hardware застосовує власні правила доступу до читання й запису; для кожного register вони наведені в документації пристрою.[^iso-c-n1570]

Для status register з семантикою write-one-to-clear (W1C) запис одиниці скидає flag, а запис нуля залишає його без змін. Якщо початкове читання побачило інший активний flag як одиницю, read-modify-write може записати цю одиницю назад і також скинути другий flag. У read-to-clear register небезпека інша: саме читання може спожити подію до запланованої зміни. Ця поведінка залежить від пристрою, її треба перевірити в описі register.[^stm32-w1c-manual]

Припустімо, що ERROR і TIMEOUT очікують обробки, а код має скинути лише ERROR. Read-modify-write може прочитати обидва flags як одиниці, скинути ERROR у значенні CPU, а одиницю TIMEOUT записати назад, ненавмисно підтвердивши обидві події. Для W1C register документація може вимагати прямий запис `STATUS = ERROR_Msk;`, але це правильно лише тоді, коли datasheet саме так наказує і зарезервовані біти оброблено згідно з описом.[^stm32-w1c-manual]

**Типові помилки:**

- Застосовувати `|=` або C bit-field assignment до W1C status register.
- Вважати `volatile` гарантією одного апаратного доступу.
- Копіювати правило W1C на інший register без перевірки його семантики.

Щоб уникнути втрати подій, знайди опис read/write поведінки кожного біта, використовуй рекомендований clear/set регістр і перевір фактичний код для потрібної цілі. Якщо апаратного способу уникнути гонки немає, врахуй синхронізацію з ISR та зміни стану, описані виробником.[^stm32-w1c-manual]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
