---
id: emb-elintro-0074
title: "Що означає мінус у законі Фарадея `EMF = -N*dΦ/dt`?"
description: "Що означає мінус у законі Фарадея EMF = -N*dΦ/dt?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: faraday-lenz
    title: "All About Circuits: Lenz’s Law and Faraday’s Law Calculator"
    url: https://www.allaboutcircuits.com/tools/lenz-law-calculator-faradays-law-calculator
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює закон Фарадея, закон Ленца та знак індукованої ЕРС; сторінка є навчальним поясненням, не стандартом."
---

## Short answer

Мінус – це закон Ленца: індукована напруга створює струм, який протидіє зміні магнітного потоку, що спричинила індукцію. Інакше система «створювала» б енергію з нічого.[^faraday-lenz]

## Detailed explanation

Закон Фарадея пов’язує індуковану електрорушійну силу в котушці зі швидкістю зміни магнітного потоку крізь її витки. У записі `EMF = -N*dΦ/dt` число витків – `N`, а `Φ` – потік через один виток. Знак мінус виражає правило Ленца: напрям індукованої ЕРС та струму такий, що створене ними магнітне поле протидіє зміні потоку, яка спричинила індукцію.[^faraday-lenz]

Важливо точно назвати, чому саме протидіє струм. Якщо зовнішній потік у вибраному додатному напрямку зростає, індуковане поле спрямовується протилежно цьому приросту. Якщо той самий потік зменшується, індуковане поле намагається його підтримати. Тому без заданих напрямків нормалі та обходу контуру не можна прочитати знак як «струм завжди проти поля». Зміна знака цих домовленостей змінює алгебричний знак, але фізичне правило лишається тим самим.

Приклад: якщо потік у вибраному напрямку зростає, індукований струм створює поле у протилежному напрямку. Якщо потік у тому самому напрямку спадає, індуковане поле має той самий напрямок, щоб протидіяти спаданню. Це правило пояснює, чому генератор потребує механічної роботи: індукований ефект протидіє руху, що змінює потік, а енергія переходить між механічною та електричною формами.[^aac-direct-current]

**Типова помилка:** казати, що мінус означає, ніби індукована напруга завжди від’ємна або протилежна магнітному полю. Знак залежить від визначених напрямків; зміст закону Ленца – протидія зміні потоку.[^faraday-lenz]

## Sources

<!-- generated from frontmatter -->
