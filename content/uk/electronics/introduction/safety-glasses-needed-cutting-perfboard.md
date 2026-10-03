---
id: emb-elintro-0296
title: "Навіщо при різанні perfboard потрібні захисні окуляри?"
description: "Навіщо при різанні perfboard потрібні захисні окуляри?"
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
    applicability: "Походження питання: лекція 26, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: osha-eye-protection
    title: "OSHA: Personal Protective Equipment (PPE) Assessment"
    url: https://www.osha.gov/training/library/personal-protective-equipment/assessment
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Вибір засобів захисту очей від уламків під час різання, обробки та шліфування; це загальні настанови, а не специфічна оцінка ризику для конкретного perfboard."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

Під час різання perfboard і підрізання виводів можуть розлітатися тверді частинки, тому надягайте захисні окуляри з бічним захистом. Після різання приберіть задирки так, щоб не спрямовувати уламки до обличчя.[^osha-eye-protection]

## Detailed explanation

Захисні окуляри потрібні через механічну небезпеку: різак може викинути відрізаний фрагмент виводу, а абразив або пилка – дрібні частинки основи плати й міді. Навіть якщо робота невелика, траєкторія уламка непередбачувана, а око особливо вразливе до удару. Для ризику від частинок OSHA наводить захисні окуляри з бічними щитками або goggles як належні засоби захисту; конкретний вибір має відповідати інструменту й оцінці ризику.[^osha-eye-protection]

Окуляри мають сидіти так, щоб не сповзати під час нахилу над платою. Звичайні коригувальні окуляри самі по собі не замінюють ударостійкого захисту, якщо вони не мають відповідного рейтингу. Face shield може доповнити окуляри при значній кількості уламків, але не замінює їх для ударного ризику.[^osha-eye-protection]

Перед різанням зафіксуйте плату, спрямуйте лінію різу від себе й людей поруч та тримайте пальці поза траєкторією інструмента. Після цього огляньте край і обережно зніміть задирки напилком або абразивом; стружку приберіть щіткою, а не пальцями. Захист потрібен і під час обрізання зайвих виводів після монтажу, бо короткий обрізок часто відлітає швидше й менш передбачувано, ніж сама плата.

## Sources

<!-- generated from frontmatter -->
