---
id: emb-elintro-0176
title: "Що таке wired-OR схема і навіщо там Шотткі-діоди?"
description: "Що таке wired-OR схема і навіщо там Шотткі-діоди?"
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
    applicability: "Походження питання: лекція 17, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: ti-diode-oring
    title: "TI: PowerPath Management Solution for ASH"
    url: https://www.ti.com/lit/pdf/SLVAF21
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює diode ORing, блокування зворотного струму та втрати на прямому падінні; не задає універсального падіння напруги для діода."
  - source_id: aac-schottky-diodes
    title: "All About Circuits textbook: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Описує конструкцію Шотткі та типове, але не універсальне низьке пряме падіння напруги."
  - source_id: ti-schottky-selection
    title: "TI: Schottky Diode Selection in Asynchronous Boost Converters"
    url: https://www.ti.com/tw/lit/pdf/snva762
    accessed: 2026-10-04
    kind: official
    version: "SNVA762, September 2016"
    applicability: "Підтверджує залежність зворотного витоку Шотткі від температури та конкретної моделі діода."
---

## Short answer

У схемі diode ORing кожне джерело під’єднують до спільного виходу через діод, який дає струму йти до навантаження та ізолює гілки від зворотного струму. Шотткі часто обирають через відносно мале пряме падіння напруги, але точне значення залежить від конкретного діода, струму й температури.[^ti-diode-oring][^aac-schottky-diodes]

## Detailed explanation

Diode ORing об’єднує кілька джерел живлення так, щоб навантаження могло отримувати енергію від доступної гілки, а струм не повертався з виходу в інше джерело. Для цього кожну гілку під’єднують через діод: анод спрямований до джерела, катод – до спільного вузла. Коли напруга джерела достатня, його діод проводить; якщо напруга іншої гілки нижча, її діод закривається і перешкоджає зворотному струму. Це не гарантує ідеального резервування: напруги джерел, їхні характеристики та умови перемикання визначають, яка гілка фактично несе навантаження.[^ti-diode-oring]

У прикладі з USB та адаптером таке з’єднання зменшує ризик подачі напруги з одного входу назад в інший. Два джерела не варто просто з’єднувати паралельно, якщо їхні виробники не дозволяють режим current sharing: навіть невелика різниця вихідних напруг може змусити одне джерело приймати струм від іншого. Діод створює ізоляцію, але його падіння зменшує напругу на навантаженні.[^ti-diode-oring]

Шотткі часто використовують, бо його пряме падіння зазвичай нижче, ніж у звичайного кремнієвого випрямного діода, що може зменшити втрати `P = V_f*I`. Значення на кшталт `0.3 V` не є сталою властивістю всіх Шотткі: перевіряють графік або специфікацію конкретної деталі при робочому струмі й температурі. Також важливі максимальна зворотна напруга, допустимий струм і reverse leakage, який у Шотткі може помітно зростати з температурою.[^aac-schottky-diodes][^ti-schottky-selection]

**Типові помилки:**
- вважати, що обидва джерела автоматично ділять струм порівну;
- приймати `0.3 V` за гарантоване падіння для кожного діода;
- не враховувати нагрівання від прямого струму та зворотний витік.[^ti-diode-oring][^ti-schottky-selection]

## Sources

<!-- generated from frontmatter -->
