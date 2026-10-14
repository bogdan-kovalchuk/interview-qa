---
id: emb-elee-0247
title: "Звідки на осцилограмі тактового сигналу можуть з’явитися overshoot і ringing, яких немає в схемі?"
description: "Звідки на осцилограмі тактового сигналу можуть з’явитися overshoot і ringing, яких немає в схемі?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Походження питання: лекція 78, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-14; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: keysight-probing-5988-5021
    title: "Keysight: Optimizing Oscilloscope Measurement Accuracy on High-Performance Systems with Keysight Active Probes (application note 5988-5021EN)"
    url: https://prc.keysight.com/Content/PDF_Files/5988-5021EN.pdf
    accessed: 2026-10-14
    kind: official
    version: "5988-5021EN"
    applicability: "Механізм ringing через LC-контур з ємності пробника та індуктивності заземлювального проводу, порада найкоротшого проводу землі, смуга пробника й внутрішній резонанс, до 25 нГн на дюйм у проводах, що подовжують сигнальний шлях пробника. Опис пробників Keysight; не визначає поведінку пробників інших виробників."
---

## Short answer

Overshoot і ringing можуть з’являтися через довгий заземлювальний провід пробника: його індуктивність разом з ємністю пробника утворює LC-контур.[^keysight-probing-5988-5021] Коротке заземлення зменшує індуктивність і має зсунути частоту дзвону за смугу осцилографа та пробника.[^keysight-probing-5988-5021]

## Detailed explanation

Overshoot – це вихід напруги за кінцевий рівень після фронту, а ringing – загасаючі коливання після того самого фронту. Коли такі викиди з’являються на осцилограмі, а в схемі їх немає, питання полягає в тому, чи це частина дизайну, чи спричинила вимірювальна система. Keysight прямо ставить це питання інженеру.[^keysight-probing-5988-5021]

Механізм у заземлювальному проводі такий: провід додає індуктивність L, а пробник має вхідну ємність C. Keysight описує ringing як LC-контур з ємності пробника та індуктивності заземлювального проводу й наконечника.[^keysight-probing-5988-5021] Резонансна частота такого контуру дорівнює `f = 1/(2*pi*sqrt(L*C))`. Для ілюстрації візьмемо `L = 200 nH` і `C = 16 pF`: `f = 1/(2*pi*sqrt(200e-9*16e-12)) ≈ 89 МГц`. Keysight дає до 25 нГн на дюйм для проводів, що подовжують сигнальний шлях пробника.[^keysight-probing-5988-5021] Значення 200 нГн для заземлювального проводу тут є припущенням того самого порядку, а не значенням із джерела.

Той самий розрахунок для проводу з індуктивністю порядку 25 нГн (один дюйм за Keysight) дає `f ≈ 252 МГц`. Вища частота дзвону легше виходить за смугу осцилографа та пробника, і це відповідає порадам Keysight.[^keysight-probing-5988-5021] Числа ілюстративні: 200 нГн і 16 пФ є припущеннями, а не паспортом конкретного пробника.

Смуга пробника діє і в протилежний бік. За межами смуги пробника амплітуди сигналу стають надмірно послабленими, а вимірювання – непередбачуваними.[^keysight-probing-5988-5021] Тому фронти, виміряні поза смугою, можуть виглядати м’якшими за реальні. Усередині смуги внутрішній резонанс пробника може зробити вихід відмінним від входу й показатися як overshoot і ringing.[^keysight-probing-5988-5021]

Для точних вимірювань часу фронту Keysight радить використовувати найкоротший провід землі.[^keysight-probing-5988-5021] Практична перевірка: повторити вимір із коротшим заземленням і порівняти форму. Якщо дзвін зникає або зсувається, він має походження у вимірі, а не в схемі.

**Типові помилки:**

- Шукати причину overshoot і ringing у схемі, не перевіривши заземлення пробника.[^keysight-probing-5988-5021]
- Вважати, що дзвін у смузі пробника завжди властивість схеми: внутрішній резонанс пробника може показати overshoot і ringing.[^keysight-probing-5988-5021]
- Оцінювати форму фронту за межами смуги осцилографа або пробника, де амплітуда занижена.[^keysight-probing-5988-5021]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
