---
id: emb-elee-0221
title: "Чому для ключа не використовують типове β активного режиму і який струм двигуна важливий для вибору компонентів?"
description: "Чому для ключа не використовують типове β активного режиму і який струм двигуна важливий для вибору компонентів?"
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
    applicability: "Походження питання: лекція 73, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
    accessed: 2026-10-14
    kind: official
    version: "2026.02.17"
    applicability: "Посібник виробника ROHM: у перемиканні в насиченні ефективне підсилення помітно падає; β_forced обирають нижче мінімального h_FE з паспорта (типова відправна точка 5–10). Загальний посібник, а не паспорт конкретного транзистора."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Підручник, розділ 4.2: малосигнальні транзистори мають β типово 100–200, потужні – 25–50; I_E = I_C + I_B. Загальна картина, не для конкретного транзистора."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-14
    kind: book
    version: "Spring 2006"
    applicability: "Лекційні нотатки: у насиченні зв’язок між I_C і I_B нелінійний, в активному режимі I_C = β·I_B. Не документ виробника."
  - source_id: ti-drv8231a
    title: "Texas Instruments DRV8231A: 3.7-A Brushed DC Motor Driver datasheet"
    url: https://www.ti.com/lit/ds/symlink/drv8231a.pdf
    accessed: 2026-10-14
    kind: official
    version: "SLVSFZ8A, revised January 2026"
    applicability: "Паспорт драйвера TI: великі струми при низькій швидкості, пуску та загальмованому роторі. Цифри в таблицях стосуються тестових умов DRV8231A, а не всіх двигунів."
  - source_id: ti-tida00786
    title: "Texas Instruments TIDA-00786: Ultra Small Brushed DC Motor Current Regulation (reference design)"
    url: https://www.ti.com/lit/ug/tiduay8/tiduay8.pdf
    accessed: 2026-10-14
    kind: official
    version: "2015"
    applicability: "Довідковий дизайн TI для щіткового двигуна: ISTART = VSUPPLY / RWINDING, сталий струм (VSUPPLY – VBEMF) / RWINDING; реальний пусковий струм нижчий, бо двигун починає обертатися. Приклад для DRV8871 при 12–24 В; формули загальні, номінали – ні."
---

## Short answer

Для насичення базовий струм задають через `β_forced` (тут 10), що має бути нижчим за мінімальне `h_FE` з паспорта: ефективне підсилення у такому перемиканні помітно падає, тож типове β активного режиму не годиться.[^rohm-bjt-basics] Двигун при пуску та при загальмованому роторі споживає великий струм.[^ti-drv8231a] Тому транзистор, діод і джерело живлення вибирають за пусковим струмом, а не лише за робочим.

## Detailed explanation

Типове β активного режиму дає `I_C` = β·`I_B`, але для ключа це не той режим. У насиченні зв’язок між `I_C` і `I_B` стає нелінійним.[^mit-6071-bjt-notes] Колекторний струм у цьому режимі визначають навантаження й живлення.[^rohm-bjt-basics] Ефективне підсилення при такому перемиканні помітно падає, тому `β_forced` закладають з запасом.[^rohm-bjt-basics] Для малосигнального транзистора типове β – 100–200, для потужного – 25–50.[^fiore-bjt-basics] Якщо взяти β = 100 для ключа на 100 мА, вийде `I_B` = 100 мА/100 = 1 мА. Для `β_forced` = 10 потрібно 10 мА, тож базовий струм був би занижений у десять разів, і транзистор може не насититися.

Пусковий струм важливий саме на початку руху. Коли двигун обертається, зворотна ЕРС (back EMF) віднімається від напруги живлення, і струм дорівнює `(V-E)/R`, де `R` – опір обмотки.[^ti-tida00786] Поки ротор не обертається, зворотної ЕРС немає, і початковий струм оцінюють як `V/R`.[^ti-tida00786] Для ілюстрації припустімо обмотку 10 Ом і живлення 5 В. Робочий струм 100 мА означає зворотну ЕРС 4 В: (5-4)/10 = 0,1 А. При загальмованому роторі струм становить 5/10 = 0,5 А, тобто в п’ять разів більше за робочий.

Тому транзистор розраховують на 0,5 А, діод рециркуляції – на такий самий струм, а для насичення при `β_forced` = 10 базовий струм має бути 50 мА: `R_B` = (5-0.8)/0.05 = 84 Ом. Якщо драйвер віддає лише 10 мА, для 0,5 А бракує базового струму: потрібно 50 мА. Оцінка `V/R` є верхньою межею, а не виміряним значенням: двигун починає обертатися раніше, ніж струм досягає `V/R`, тож реальний пусковий струм з джерела нижчий.[^ti-tida00786]

**Типові помилки:**

- Вибирати транзистор, діод і джерело за робочим струмом 100 мА і не перевіряти пусковий або загальмований струм.
- Рахувати базовий струм за типовим β активного режиму: при β = 100 вийде 1 мА, і транзистор може не насититися.
- Брати `V/R` за точне значення пускового струму, хоча це верхня межа.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
