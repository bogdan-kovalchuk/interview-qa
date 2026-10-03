---
id: emb-elintro-0165
title: "Чому Шотткі-діод швидший за стандартний Si-діод?"
description: "Чому Шотткі-діод швидший за стандартний Si-діод?"
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
  - source_id: st-an4789
    title: "STMicroelectronics AN4789: Monolithic Schottky diode in ST F7 LV MOSFET technology"
    url: https://www.st.com/resource/en/application_note/an4789-monolithic-schottky-diode-in-st-f7-lv-mosfet-technology-improving-application-performance-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 1"
    applicability: "Пояснює малий накопичений заряд Schottky та швидше перемикання на прикладі конкретної технології; параметри окремих діодів і паразитні ефекти залежать від компонента та схеми."
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 16, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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

У звичайному P-N діоді під час прямої провідності накопичуються minority carriers, які треба видалити під час переходу до зворотного блокування; це спричиняє reverse recovery. Schottky має метал-напівпровідниковий бар’єр і переважно majority-carrier conduction, тому накопичений заряд і reverse recovery зазвичай менші, а перемикання швидше. Реальні втрати й перехідні процеси все одно залежать від компонента та схеми.[^st-an4789]

## Detailed explanation

Schottky-діод формує бар’єр на контакті металу з напівпровідником, тоді як стандартний кремнієвий діод зазвичай має P-N перехід. Ця різниця важлива під час вимкнення: у P-N діоді за прямої провідності інжектуються minority carriers і частина заряду зберігається в переході. Коли напругу швидко змінюють на зворотну, цей заряд має зникнути, перш ніж діод повністю блокуватиме струм; у цей час виникає reverse recovery current.[^st-an4789]

У Schottky струм переважно переносять majority carriers, тому такого самого накопичення minority-carrier заряду немає або воно значно менше. Відповідно, за перемикання з прямого режиму на зворотний Schottky зазвичай має менший `Q_rr` і швидше припиняє прямий струм. Саме тому його часто обирають у випрямлячах і перетворювачах, де діод комутує на високій частоті: менший заряд відновлення може зменшити втрати, струмові піки та перемикальні завади.[^st-an4789]

Слово «швидший» стосується насамперед reverse recovery, а не кожного можливого перехідного процесу. Ємність переходу, монтажна індуктивність, прикладена напруга, температура й конструкція конкретного компонента також впливають на хвильові форми. Datasheet може вказувати ємнісний струм навіть тоді, коли заряд відновлення носіїв малий; тому повне перемикання не означає миттєвої відсутності будь-якого струму.[^st-an4789]

У прикладі ST порівняно стандартний 60 V MOSFET із пристроєм такого ж класу з інтегрованим Schottky: таблиця показує `Q_rr` 100 nC і 90 nC відповідно за наведених умов, а пряме падіння 600 mV і 250 mV. Це конкретні результати пристроїв, а не універсальні цифри для кожного Schottky; порівнювати треба за однакових тестових умов і з даними виробника.[^st-an4789]

**Типові помилки:**
- Казати, що reverse recovery у будь-якого Schottky абсолютно нульовий, не перевіривши datasheet та паразитну ємність.
- Вважати, що швидкість автоматично означає найкращий вибір: слід також порівняти максимальну зворотну напругу, струм витоку, пряме падіння й теплові межі.
- Плутати механізм меншого накопиченого заряду з твердженням, що схема не матиме перехідних піків.[^st-an4789]

## Sources

<!-- generated from frontmatter -->
