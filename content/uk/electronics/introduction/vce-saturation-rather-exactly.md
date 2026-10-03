---
id: emb-elintro-0211
title: "Чому `V_CE` насиченого транзистора не дорівнює нулю?"
description: "Чому `V_CE` насиченого транзистора не дорівнює нулю?"
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

**Насичення не означає нульовий спад напруги.** Реальний BJT має ненульове `V_CE(sat)`, значення якого залежить від компонента, `I_C` і базового струму; діапазон 0.1–0.2 V не є універсальною гарантією. Більший базовий струм зазвичай зменшує спад у межах режиму й безпечних значень з документації.[^aac-bjt-saturation]
## Detailed explanation

Насичений біполярний транзистор проводить струм із ненульовим падінням напруги між колектором і емітером.

Модель ідеального ключа замикає контакти без опору, але BJT є напівпровідниковим приладом із внутрішніми переходами. Тому навіть коли транзистор відкритий настільки, що навантаження обмежує колекторний струм, `V_CE` залишається додатним. У документації його подають як `V_CE(sat)` для вказаних струмів колектора й бази; число залежить від типу транзистора та умов вимірювання.[^aac-bjt-saturation]

Значення 0.1–0.2 V часто використовують як приблизну модель для нескладних розрахунків, але це не універсальний фізичний поріг. Для іншого компонента, струму або температури падіння може бути іншим. Збільшення базового струму часто зменшує `V_CE(sat)`, проте обмежене допустимими струмами бази та розсіюваною потужністю.[^aac-bjt-saturation]

**Приклад:** якщо в розрахунку прийнято `V_CC` = 5 V, `R_C` = 1 kΩ та `V_CE(sat)` = 0.2 V, то струм колектора оцінюють як `I_C = (V_CC - V_CE(sat))/R_C = 4.8 mA`. Це значення є наслідком прийнятої моделі, а не характеристикою кожного транзистора.

**Типова помилка:** вважати «насичений» синонімом «ідеально замкнений». У практичному ключі треба врахувати спад на транзисторі, його потужність і відповідний рядок datasheet.[^aac-bjt-saturation]
## Sources

<!-- generated from frontmatter -->
