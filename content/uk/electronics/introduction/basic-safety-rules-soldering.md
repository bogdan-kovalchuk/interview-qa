---
id: emb-elintro-0285
title: "Які базові правила безпеки при паянні?"
description: "Які базові правила безпеки при паянні?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: hse-solder-fume-indg248
    title: "Health and Safety Executive: Solder fume and you (INDG248)"
    url: https://www.hse.gov.uk/pubns/indg248.pdf
    accessed: 2026-10-04
    kind: official
    version: "INDG248(rev2) 09/15"
    applicability: "Пояснює ризики диму від каніфольного флюсу та рекомендує витяжку й уникнення потоку диму; рекомендації щодо перегрівання звіряти з іншими джерелами."
  - source_id: hse-soldering-controls
    title: "Health and Safety Executive: OCE4 Soldering Engineering Control"
    url: https://www.hse.gov.uk/pubns/guidance/oce4.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Надає рекомендації щодо мінімально достатньої температури, обслуговування витяжки, очищення робочої зони та миття рук перед перервами."
  - source_id: hakko-fx888d-safety
    title: "HAKKO FX-888D Instruction Manual"
    url: https://www.hakko.com/english/support/doc/result.php?mode=download&seq=5500
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Інструкція конкретної моделі застерігає не торкатися жала, ставити інструмент у підставку, вимикати його без нагляду та провітрювати робочу зону."
  - source_id: osha-eye-protection
    title: "OSHA 29 CFR 1910.133: Eye and Face Protection"
    url: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.133/
    accessed: 2026-10-04
    kind: official
    version: "29 CFR 1910.133"
    applicability: "Вимагає захисту очей для працівників за наявності небезпеки від частинок, розплавленого металу чи хімікатів; застосовність залежить від конкретного ризику й юрисдикції."
---

## Short answer

Тримайте гаряче жало в підставці, не торкайтеся його і працюйте з витяжкою, що відводить флюсовий дим від обличчя. Використовуйте захист очей, коли є ризик частинок або бризок розплавленого металу. Не перегрівайте паяльник; якщо використовували свинцевий припій, мийте руки перед їжею чи перервою та не переносьте залишки зі столу на їжу.[^hakko-fx888d-safety] [^osha-eye-protection] [^hse-solder-fume-indg248] [^hse-soldering-controls]

## Detailed explanation

Безпечне робоче місце для паяння зменшує ризик опіків і вдихання диму від флюсу. Жало нагрівається до високої температури, тому паяльник кладуть у підставку, коли ним не працюють. Не залишайте його ввімкненим без нагляду й розміщуйте кабель так, щоб рука не могла зачепити його та стягнути інструмент зі столу.[^hakko-fx888d-safety]

Під час ручного паяння дим флюсу піднімається від місця нагрівання і може потрапити в зону дихання. Дим каніфольного флюсу пов’язаний із серйозним ризиком для здоров’я, зокрема професійною астмою. Використовуйте належну витяжку біля джерела, тримайте голову осторонь від потоку диму та не перегрівайте паяльник. Звичайний вентилятор, що лише розносить дим по кімнаті, не рівнозначний його видаленню з робочої зони.[^hse-solder-fume-indg248]

Захист очей потрібен, коли операція створює небезпеку від частинок, бризок металу чи хімікатів; наприклад, обрізання виводів може відкинути обрізок у бік обличчя. Дотримуйтеся інструкцій до флюсу й припою: залишки та ризики відрізняються залежно від їх складу. За свинцевого припою уникайте їжі й напоїв на робочому місці, прибирайте пил і залишки належним способом та мийте руки перед перервами.[^osha-eye-protection] [^hse-soldering-controls]

Приклад: перед паянням перевірте, що станція стоїть рівно, жало має місце у підставці, а витяжка захоплює дим біля з’єднання. Після роботи вимкніть живлення, дочекайтеся охолодження згідно з інструкцією виробника і приберіть робочу поверхню.[^hakko-fx888d-safety] [^hse-solder-fume-indg248]

**Типові помилки:**
- Спрямовувати дим через обличчя або вважати, що коротка робота не потребує контролю флюсового диму.
- Залишати ввімкнений паяльник на столі без підставки.
- Після роботи зі свинцевим припоєм торкатися їжі до миття рук.

## Sources

<!-- generated from frontmatter -->
