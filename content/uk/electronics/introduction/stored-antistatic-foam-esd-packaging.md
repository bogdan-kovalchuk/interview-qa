---
id: emb-elintro-0028
title: "Навіщо `IC` зберігають в антистатичній піні або `ESD`-упаковці?"
description: "Навіщо `IC` зберігають в антистатичній піні або `ESD`-упаковці?"
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
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 4, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-esd-packaging
    title: "Texas Instruments: Electrostatic Discharge (ESD) Protective Semiconductor Packing Materials and Configurations"
    url: https://www.ti.com/lit/an/szza027a/szza027a.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev. A"
    applicability: "Пояснює захисні властивості пакувальних матеріалів для ESDS-компонентів; не означає, що будь-яка піна є екранувальною або безпечною для зберігання."
---

## Short answer

ESD-упаковка обмежує накопичення заряду та захищає чутливі до електростатичного розряду компоненти під час зберігання й перенесення. Її матеріал і конструкція мають відповідати потрібному рівню захисту; не кожна антистатична піна екранує розряд.[^ti-esd-packaging]

## Detailed explanation

Виводи й внутрішні структури мікросхеми можуть пошкодитися від електростатичного розряду, навіть якщо компонент після цього ще частково працює. Тому захист потрібен не лише під час перевезення: поводьтеся з компонентами у відповідній ESD-зоні та використовуйте упаковку, призначену для чутливих до ESD виробів.[^ti-esd-packaging]

У пакування можуть бути різні функції. Матеріал із низьким зарядоутворенням зменшує заряд, що виникає під час тертя чи відокремлення; dissipative матеріал дає заряду контрольовано розсіюватися, а shielding-оболонка послаблює зовнішнє електричне поле або розряд. Конкретний пакет може поєднувати ці властивості, але слова «антистатичний» самі по собі не доводять, що він забезпечує повний захист від прямого розряду.[^ti-esd-packaging]

Піна для компонентів також буває різною за електричними властивостями; провідна піна може з'єднати між собою виводи, тому її застосовують лише коли це безпечно для конкретного компонента. Не торкайтеся виводів і не покладайтеся на пакувальний матеріал як на заміну заземленню робочого місця та належним процедурам ESD.[^ti-esd-packaging]

**Практичне правило:** залишайте мікросхему в упаковці, маркованій для ESD-захисту, до роботи з нею в підготовленій зоні. Не підмінюйте таку упаковку звичайною пінопластовою підкладкою чи пластиковим пакетом.[^ti-esd-packaging]

## Sources

<!-- generated from frontmatter -->
