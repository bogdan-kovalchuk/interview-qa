---
id: emb-elintro-0171
title: "Який компроміс у Шотткі-діода порівняно зі звичайним кремнієвим діодом?"
description: "Який компроміс у Шотткі-діода порівняно зі звичайним кремнієвим діодом?"
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
  - source_id: diodes-schottky-tradeoff
    title: "Diodes Incorporated AN1192: Understanding the Different Approaches to Input Reverse Voltage Protection"
    url: https://www.diodes.com/assets/App-Note-Files/AN1192_App-Note_Automotive-RVP.pdf
    accessed: 2026-10-04
    kind: official
    version: "Rev 1, February 2025"
    applicability: "Пояснює низьке падіння напруги та підвищений зворотний витік Schottky, особливо за високої температури; порівняння стосується розглянутих виробником компонентів і застосувань."
---

## Short answer

**Перевага Schottky** – низьке пряме падіння напруги та мала затримка перемикання, що зменшує втрати у відповідних випрямлячах. Компромісом часто є більший зворотний витік, який помітно зростає з температурою; допустиму зворотну напругу треба звіряти для конкретної деталі.[^diodes-schottky-tradeoff]

## Detailed explanation

Діод Schottky утворює бар’єр на межі металу й напівпровідника, тоді як звичайний кремнієвий випрямний діод має p-n-перехід. У Schottky немає накопичення й подальшого видалення значного заряду неосновних носіїв, тому перемикання може бути швидким; конкретна швидкодія залежить від конструкції та режиму, тож її перевіряють у datasheet. Низьке `V_F` також зменшує провідникові втрати `P = V_F*I`, що корисно, наприклад, у низьковольтному перетворювачі.[^diodes-schottky-tradeoff]

Ця перевага не означає, що Schottky завжди кращий. Його зворотний витік часто більший і може різко зростати при нагріванні; у силовому колі це збільшує втрати та нагрів, а в батарейному пристрої може скоротити час роботи. Тому порівнюйте витік за найгіршої очікуваної температури, а не лише типове значення за кімнатної температури. Межі `V_R` теж не можна узагальнювати на весь клас: різні технології й моделі мають різні рейтинги.[^diodes-schottky-tradeoff]

Приклад: якщо конкретна схема пропускає `2 A`, а вибраний datasheet задає `V_F = 0.4 V` за цього струму, оцінка втрат на діоді становить `P = 0.4*2 = 0.8 W`. Це оцінка провідникової потужності в зазначеній робочій точці, не повний тепловий розрахунок; потрібні також температурна залежність, монтаж і тепловий опір.[^diodes-schottky-tradeoff]

**Типова помилка:** вибирати Schottky лише за низьким `V_F` і не перевіряти зворотну напругу, витік і тепловий режим. Зіставте вимоги схеми з максимальними значеннями та умовами тестування конкретної деталі.

## Sources

<!-- generated from frontmatter -->
