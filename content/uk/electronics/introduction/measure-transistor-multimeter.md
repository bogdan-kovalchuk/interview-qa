---
id: emb-elintro-0209
title: "Як виміряти β транзистора мультиметром?"
description: "Як виміряти β транзистора мультиметром?"
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
  - source_id: meter-beta
    title: "Fluke 8050A Instruction Manual"
    url: https://assets.fluke.com/manuals/8050a___imeng0200.pdf
    accessed: 2026-10-04
    kind: official
    version: "8050A manual"
    applicability: "Описує beta test для моделі Fluke 8050A та зазначає залежність beta від температури; процедура й гнізда залежать від моделі приладу."
---

## Short answer

У режимі `hFE` мультиметр оцінює gain за власних малосигнальних тестових умов; вставляйте від’єднаний транзистор у правильні гнізда `E`, `B`, `C`, звіривши інструкцію приладу та pinout компонента.[^meter-beta] Показання не є універсальною нормою для 2N2222 і не гарантує параметрів у робочому колі; нуль може мати кілька причин і сам собою не доводить несправність.[^meter-beta]

## Detailed explanation

Функція `hFE` мультиметра дає приблизне вимірювання малосигнального коефіцієнта струмового підсилення BJT за умов, заданих самим приладом, а не універсальне значення транзистора.[^meter-beta]

Якщо мультиметр має відповідне гніздо, вимкніть транзистор від схеми, визначте його тип `NPN` або `PNP` і розпіновку за datasheet, а тоді вставте в гнізда `E`, `B`, `C` згідно з маркуванням саме цього приладу. Прилад подає малий тестовий струм і оцінює відношення колекторного струму до базового. Інші моделі можуть мати інше розташування гнізд або взагалі не підтримувати такий тест, тож інструкція мультиметра є визначальною.[^meter-beta]

Показання корисне для швидкого порівняння чи пошуку явної несправності, але не є перевіркою придатності підсилювача або ключа. Datasheet задає gain для визначених `I_C`, `V_CE` і температури; тест мультиметра може використовувати зовсім іншу робочу точку. β також залежить від температури, тож нагрівання пальцями може змінити результат.[^meter-beta]

Не можна робити висновок, що показання `0` неодмінно означає зламаний транзистор: можливі неправильна орієнтація, переплутані виводи, невідповідний тип, поганий контакт або межа діапазону. Перевірте інструкцію, полярність і розпіновку, а потім, якщо потрібно, окремо перевірте два переходи режимом diode-test. Така перевірка теж не замінює вимірювання транзистора під робочим навантаженням.[^meter-beta]

**Типова помилка:** сприймати число з дисплея як гарантований `hFE` у будь-якому колі. Записуйте його лише разом із моделлю приладу та розумійте як порівняльне вимірювання.

## Sources

<!-- generated from frontmatter -->
