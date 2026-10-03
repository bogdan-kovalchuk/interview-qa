---
id: emb-elintro-0305
title: "Що таке cold solder joint і як його розпізнати?"
description: "Що таке cold solder joint і як його розпізнати?"
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
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ipc-cold-solder-definition
    title: "IPC: Acceptance Testing Of Low-Ag Reflow Solder Alloys"
    url: "https://www.ipc.org/system/files/technical_resource/E38%26S14-01%20-%20KrisTroxel.pdf"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Наводить визначення IPC-A-610 для cold solder як поганого wetting із сіруватим пористим виглядом і можливими причинами; це технічний матеріал про reflow, а не повна інструкція для всіх процесів пайки."
  - source_id: fluke-continuity-test
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-test-for-continuity
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтримує перевірку continuity на знеструмленому колі; пороги приладу й вимірювання в схемі залежать від мультиметра та інших шляхів кола."
---

## Short answer

Cold solder joint – це з’єднання з поганим wetting, яке часто має сірувату, пористу поверхню; недостатнє нагрівання чи забруднення можуть цьому сприяти. Зовнішній вигляд є підказкою, а не остаточним тестом, тому підозріле з’єднання перевіряють знеструмленим вимірюванням і за потреби перепаюють.[^ipc-cold-solder-definition]

## Detailed explanation

Cold solder joint – це паяне з’єднання, у якому припій погано змочив поверхні металу й не утворив надійного контакту. IPC описує його як з’єднання з поганим wetting і сіруватим пористим виглядом; серед можливих причин названі недостатнє нагрівання, забруднення та домішки в припої.[^ipc-cold-solder-definition]

Під час огляду зверніть увагу на тьмяну сіру поверхню, пористість, нерівну форму або межу, де припій ніби лежить краплею на виводі замість того, щоб розтікатися по виводу й площадці. Але лише блиск не є надійним критерієм: різні сплави та флюси можуть давати різний вигляд, а частина дефектів прихована під корпусом компонента. Ознаки треба оцінювати разом із формою змочування та механічною цілісністю з’єднання.[^ipc-cold-solder-definition]

Електрично дефект може проявлятися як обрив або переривчастий контакт: плата працює лише коли її торкнутися чи трохи зігнути, LED мерехтить або покази мультиметра змінюються. Для перевірки від’єднайте живлення й використайте continuity або вимірювання опору; нульовий чи змінний показ треба інтерпретувати з урахуванням решти паралельних шляхів на платі. Не вимірюйте опір на ввімкненій схемі.[^fluke-continuity-test]

Щоб уникнути дефекту, забезпечте чисті поверхні, придатний флюс і достатнє нагрівання саме виводу та площадки, а не лише плавлення припою на жалі. Не рухайте деталь під час застигання з’єднання. Підозрілу пайку слід очистити за потреби й перепаяти належним тепловим контактом; додавання припою поверх погано змоченої поверхні не усуває причину. Для серійного виробництва конкретні критерії приймання визначають застосовним класом і редакцією стандарту.[^ipc-cold-solder-definition]

## Sources

<!-- generated from frontmatter -->
