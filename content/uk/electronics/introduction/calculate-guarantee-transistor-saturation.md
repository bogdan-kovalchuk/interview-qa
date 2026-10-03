---
id: emb-elintro-0213
title: "Як вибрати `R_B`, щоб забезпечити насичення біполярного транзистора?"
description: "Як вибрати `R_B`, щоб забезпечити насичення біполярного транзистора?"
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

**Потрібний базовий струм визначають із навантаження, а не лише з типового beta.** Оцініть граничний `I_C` з колекторного кола, виберіть консервативний forced beta за документацією транзистора та знайдіть `I_B >= I_C/β_forced`. Потім обчисліть `R_B = (V_in - V_BE)/I_B` з урахуванням допусків живлення й виходу драйвера; стандартне значення округлюйте вниз лише після перевірки струму й потужності.[^aac-bjt-saturation] Універсальне множення на п’ять не гарантує насичення для будь-якого транзистора або температури.[^aac-bjt-beta-terms]
## Detailed explanation

Щоб забезпечити насичення, розраховують базовий струм для максимального струму навантаження й вибраного forced beta, а потім із цього струму визначають `R_B`.

Спочатку встановіть струм колектора, який потребує схема. Для резистивного навантаження це оцінка за різницею між живленням і прийнятим `V_CE(sat)`, поділеною на `R_C`. Далі не використовуйте довільний типовий beta: виробник наводить умови, за яких гарантовано конкретні `V_CE(sat)` та струми. Відношення `I_C/I_B`, задане цими умовами для ключового режиму, можна використати як практичний forced beta.[^aac-bjt-saturation]

Мінімальний струм бази оцінюють як `I_B >= I_C/β_forced`; потрібний резистор дорівнює різниці між напругою керування та падінням база–емітер, поділеній на базовий струм. Для надійності беруть до уваги мінімальну напругу керування, граничні `V_BE`, допуски резисторів і здатність виходу контролера віддавати струм. Надмірний базовий струм теж небажаний: він навантажує драйвер, а надто глибоке насичення може збільшити час вимкнення.

**Приклад розрахунку:** для ілюстрації, нехай `I_C` = 10 mA, вибраний forced beta дорівнює 10, `V_in` = 5 V і прийнято `V_BE` = 0.7 V. Тоді `I_B` має бути не меншим за 1 mA, а `R_B` – не більшим приблизно за 4.3 kΩ. Ці припущення треба замінити умовами datasheet конкретної деталі.

**Типові помилки:**

- Підставляти типовий активний beta, який може змінюватися з умовами й не гарантує насичення.[^aac-bjt-beta-terms]
- Автоматично множити мінімальний базовий струм на п’ять без перевірки компонента й драйвера.
- Забувати, що резистор вибирають з урахуванням мінімального доступного `V_in` та граничних напруг переходу.
## Sources

<!-- generated from frontmatter -->
