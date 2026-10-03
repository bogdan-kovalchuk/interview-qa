---
id: emb-elintro-0172
title: "Які параметри діода першими перевіряти в datasheet?"
description: "Які параметри діода першими перевіряти в datasheet?"
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
  - source_id: onsemi-nsr0630p2-datasheet
    title: "onsemi NSR0630P2 Schottky Barrier Diode datasheet"
    url: https://www.onsemi.com/download/data-sheet/pdf/nsr0630p2-d.pdf
    accessed: 2026-10-04
    kind: official
    version: "Issue E, 2024-02-08"
    applicability: "Приклад того, як datasheet прив’язує V_F, I_R і теплові межі до умов; наведені значення лише для NSR0630P2."
---

## Short answer

Почніть із повторюваної зворотної напруги `V_RRM`, потрібного прямого струму `I_F` та падіння `V_F` саме за цього струму. Перевірте також зворотний витік, теплові межі, імпульсний струм і умови вимірювання: рейтинги залежать від температури та монтажу.[^onsemi-nsr0630p2-datasheet]

## Detailed explanation

Параметри діода читають як набір обмежень для конкретного кола, а не як одну універсальну цифру. Спершу перевірте, чи витримує `V_RRM` найбільшу повторювану зворотну напругу разом із перехідними процесами та запасом. `I_F` має відповідати середньому й піковому струму схеми; допустимий струм часто обмежує не сам кристал, а нагрівання за заданої площі міді чи температури середовища.[^onsemi-nsr0630p2-datasheet]

Далі знайдіть `V_F` при вашому струмі: значення при 10 mA не прогнозує падіння при 1 A. Для втрат у прямому напрямку корисна оцінка `P = V_F*I_F`; далі треба перевірити тепловий опір, допустиму потужність та максимальну температуру переходу. У випрямлячі важливий також імпульсний струм `I_FSM`, але короткий surge rating не дозволяє постійно працювати на цьому струмі.[^onsemi-nsr0630p2-datasheet]

Зворотний витік `I_R` може мати значення у батарейному пристрої або за високої температури. Перевірте умову тесту – зворотну напругу й температуру – та графіки, якщо режим лежить між табличними точками. Наприклад, datasheet NSR0630P2 наводить `V_F` для кількох заданих струмів і `I_R` за конкретних `V_R`; ці цифри стосуються саме цього виробу, а не всіх діодів.[^onsemi-nsr0630p2-datasheet]

**Типова помилка:** порівнювати два діоди лише за максимальним струмом або типовим `V_F`, ігноруючи умови вимірювання, охолодження та зворотний витік. Перевіряйте графи й примітки таблиці, а не тільки заголовок параметра.

## Sources

<!-- generated from frontmatter -->
