---
id: emb-elee-0242
title: "Чому підключення наступного вентиля або LED може змінити високий рівень виходу транзисторного вентиля?"
description: "Чому підключення наступного вентиля або LED може змінити високий рівень виходу транзисторного вентиля?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 77, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-slaa067
    title: "TI: Understanding Basic Analog – Circuit Equations (SLAA067)"
    url: https://www.ti.com/lit/pdf/slaa067
    accessed: 2026-10-14
    kind: official
    version: SLAA067
    applicability: "Закон Ома: напруга на ділянці кола дорівнює струму, помноженому на опір, для резистора в будь-якій схемі; не містить даних про логічні сімейства."
  - source_id: fiore-bjt-switching
    title: "Fiore: Semiconductor Devices, 4.7 BJT Switching and Driver Applications (LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04%3A_Bipolar_Junction_Transistors_(BJTs)/4.7%3A_BJT_Switching_and_Driver_Applications
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Приклад LED-драйвера: логічний вихід може віддати обмежений струм (приклад 5 мА), а для потрібної яскравості LED може знадобитися понад 10 мА; це ілюстрація, а не дані конкретного логічного сімейства."
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-14
    kind: official
    version: SCLS181H
    applicability: "Рекомендовані умови й електричні характеристики NAND серії HC: VIH і VIL при VCC 4,5 В, VOH при малому навантаженні; інші сімейства логіки мають інші пороги."
---

## Short answer

Якщо від виходу з резистором підтягування береться струм, високий рівень падає на `I*R` і дорівнює `V_CC - I*R`.[^ti-slaa067] Струм LED зі своїм резистором і базовий струм входу наступного каскаду проходять через резистор підтягування, тож яскравість LED не є точною перевіркою логічного порога.

## Detailed explanation

Вентиль з резистором підтягування (pull-up) має простий вихід: коли нижній транзистор закритий, вихід через резистор `R` з’єднаний з `V_CC`. Без навантаження струму через `R` немає, і напруга на виході дорівнює `V_CC`. Коли від виходу береться струм `I`, на резисторі з’являється падіння `I*R`, тому високий рівень зменшується до `V_CC - I*R`.[^ti-slaa067]

Є два типи навантаження. Перший – вхід наступного каскаду: якщо це база BJT, вона бере базовий струм, який теж іде через `R`. Другий – LED зі своїм резистором, який бере струм прямо з виходу. Логічний вихід може віддавати лише обмежений струм: у прикладі з книги Fiore він може віддати, скажімо, 5 мА, тоді як для потрібної яскравості LED може знадобитися понад 10 мА.[^fiore-bjt-switching]

**Приклад:** `V_CC = 4,5 В`, `R = 1 кОм`, LED з резистором 330 Ом і прямою напругою 2 В (припущення для прикладу). Без навантаження вихід дає 4,5 В. З LED напруга `V` задовольняє `V = 4,5 - 1000*(V - 2)/330`, звідки `V` ≈ 2,62 В, а струм LED `(2,62 - 2)/330` ≈ 1,88 мА. Для SN74HC00 при 4,5 В вхід гарантовано високий лише від 3,15 В (VIH min), тож 2,62 В уже не гарантує логічної одиниці.[^ti-hc00]

Висновок для налагодження: вимірювати треба напругу на вході наступного вентиля з підключеним LED і без нього, а не судити за яскравістю. LED, що світиться, не доводить, що високий рівень достатній.

**Типові помилки:**

- вважати, що LED, який горить, означає правильний високий рівень;
- рахувати високий рівень як `V_CC` без урахування струму навантаження;
- не враховувати базовий струм входу, підключеного до виходу.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
