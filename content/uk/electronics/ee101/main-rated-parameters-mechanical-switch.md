---
id: emb-elee-0010
title: "Які основні паспортні параметри механічного перемикача?"
description: "Які основні паспортні параметри механічного перемикача?"
track: electronics
section: ee101
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
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 33, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: omron-basic-switch-terms
    title: "OMRON: Basic Switches, Explanation of Terms"
    url: https://www.ia.omron.com/support/guide/29/explanation_of_terms.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення рейтингів, опорів контактів та ізоляції; параметри залежать від конкретного перемикача й умов випробування."
  - source_id: omron-basic-switch-spec
    title: "OMRON: X General-purpose Basic Switch, Specifications"
    url: https://www.ia.omron.com/products/family/291/specification.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Числовий приклад конкретного базового перемикача: опори, ratings і довговічність; не узагальнюється на інші моделі."
---

## Short answer

Основні параметри перемикача – номінальні напруга й струм для визначеного типу навантаження, початковий contact resistance, insulation resistance, dielectric strength, а також механічна й електрична довговічність. Значення залежать від конкретної моделі та умов випробування; універсальних меж на кшталт «менше 50 мОм» або фіксованого ресурсу немає.[^omron-basic-switch-terms]

## Detailed explanation

Паспортні параметри перемикача описують, яке коло він може комутувати та як його ізоляція й контакти поводяться за визначених умов. Номінальні напруга і струм завжди слід читати разом: виробник задає їх для конкретного типу навантаження, наприклад резистивного, та може вказувати окремі рейтинги для AC і DC. Індуктивне або лампове навантаження має інший пусковий струм і дугу під час розмикання, тому сам збіг робочих напруги й струму з цифрами на корпусі ще не гарантує придатності.[^omron-basic-switch-terms]

Contact resistance характеризує замкнений контакт і впливає на падіння напруги та нагрівання; його значення зазвичай наведене як початкове та за умов тесту. Insulation resistance стосується розімкнених або ізольованих провідних частин, а dielectric strength – напруги й тривалості випробування, за яких ізоляція не повинна пробитися. Це різні характеристики: висока insulation resistance не замінює перевірку dielectric strength.[^omron-basic-switch-terms]

Механічна довговічність рахує спрацювання механізму, а електрична – комутації під заданим електричним навантаженням; остання часто нижча. У каталозі Omron для конкретного basic switch наведено 1 000 000 механічних і 100 000 електричних операцій, 15 мОм початкового contact resistance та мінімум 100 МОм insulation resistance при 500 VDC. Це приклад однієї моделі, а не типовий норматив для всіх перемикачів.[^omron-basic-switch-spec]

Приклад вибору: для перемикання двигуна перевіряють номінал саме для індуктивного навантаження, допустимий пусковий струм, електричну довговічність і спосіб гасіння дуги. Перевищення рейтингу може спричинити зварювання контактів або прискорене зношення, навіть якщо механічно кнопка продовжує клацати.

**Типова помилка:** порівнювати лише максимальні ампери й вольти та переносити опір чи ресурс з одного каталожного прикладу на всі перемикачі. Потрібно звірити даташит конкретної моделі, тип навантаження, частоту комутації та умови, для яких вказані результати.[^omron-basic-switch-spec]

## Sources

<!-- generated from frontmatter -->
