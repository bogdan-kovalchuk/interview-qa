---
id: emb-elintro-0212
title: "Знайдіть `I_B`, `I_C` та `I_E` для насиченого NPN-транзистора: `V_in` = 5 V, `R_B` = 3.3 kΩ, `R_C` = 1 kΩ, `V_CC` = 5 V."
description: "Знайдіть `I_B`, `I_C` та `I_E` для насиченого NPN-транзистора: `V_in` = 5 V, `R_B` = 3.3 kΩ, `R_C` = 1 kΩ, `V_CC` = 5 V."
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: aac-bjt-saturation
    title: "All About Circuits: Transistor Ratings and Packages (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-ratings-packages-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: Пояснює V_CE(sat), залежність від транзистора й базового струму; не задає параметрів невказаної моделі.
  - source_id: aac-bjt-active-mode
    title: "All About Circuits: Active-mode Operation (BJT)"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: Описує активний режим, насичення та межу струму навантаження; приклади навчальні.
  - source_id: aac-bjt-beta-terms
    title: "All About Circuits: What Is BJT Beta? Understanding the Current Gain of a Bipolar Junction Transistor"
    url: https://www.allaboutcircuits.com/technical-articles/all-about-bjt-beta-understanding-terminology/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: Розрізняє beta активного режиму та forced beta зовнішнього кола; універсального значення не задає.
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 20, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

**За заданою моделлю** вважаємо `V_BE` = 0.7 V та `V_CE(sat)` = 0.2 V. Тоді `I_B = (5 - 0.7)/3.3 kΩ ≈ 1.30 mA`, `I_C ≈ (5 - 0.2)/1 kΩ = 4.8 mA`, а `I_E = I_B + I_C ≈ 6.1 mA`. Це оцінка; фактичні напруги залежать від транзистора й робочого струму.[^aac-bjt-saturation] Навантаження обмежує `I_C`, тож не можна продовжувати множити `I_B` на активний beta після насичення.[^aac-bjt-active-mode]
## Detailed explanation

У заданій схемі оцінні струми становлять `I_B ≈ 1.30 mA`, `I_C ≈ 4.8 mA` та `I_E ≈ 6.1 mA`, якщо прийняти `V_BE` = 0.7 V і `V_CE(sat)` = 0.2 V.

Припускаємо NPN-транзистор із емітером на землі, резистором `R_B` між `V_in` і базою та `R_C` між `V_CC` і колектором. Також вважаємо, що джерела ідеальні, переходи описуються прийнятими наближеними напругами, а транзистор справді здатен досягти насичення. Напруга на `R_B` дорівнює `V_in - V_BE`; закон Ома тоді дає приблизно 1.30 mA базового струму.

Струм колектора в насиченні обмежує резистор колектора й живлення, а не активний beta: на `R_C` залишається приблизно `5 - 0.2 = 4.8 V`, отже `I_C ≈ 4.8 mA`. Для NPN з емітерним струмом, спрямованим назовні, закон Кірхгофа дає `I_E = I_C + I_B`, тобто приблизно 6.1 mA.[^aac-bjt-saturation]

**Приклад розрахунку:**

```text
I_B = (5 - 0.7) / 3300 = 1.30 mA
I_C = (5 - 0.2) / 1000 = 4.80 mA
I_E = I_B + I_C = 6.10 mA
```

Це навчальне наближення, а не точний прогноз: реальні `V_BE` і `V_CE(sat)` визначаються datasheet при заданих умовах. Перевірка насичення потребує порівняння доступного `I_B` з потрібним для компонента forced beta; самі номінали не доводять, що будь-який транзистор насититься.[^aac-bjt-active-mode]

**Типова помилка:** обчислити `β*I_B` і прийняти результат за фактичний `I_C`, хоча навантаження може не забезпечити такий струм.[^aac-bjt-active-mode]
## Sources

<!-- generated from frontmatter -->
