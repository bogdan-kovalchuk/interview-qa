---
id: emb-elee-0135
title: "Які два крайні режими треба перевірити для стабілітронного стабілізатора?"
description: "Які два крайні режими треба перевірити для стабілітронного стабілізатора?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 56, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Поведінка стабілітрона в прямому й зворотному напрямках, ефект Зенера до ≈ 5 В і лавинний пробій вище, зміна знака температурного коефіцієнта S_Z біля 6 В, диференційний опір r_dif, струм вимірювання V_Z, вибір R за формулою R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max)) і розсіювані потужності в простому стабілізаторі; дані наведено для серій Nexperia, інші виробники можуть мати інші числа."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Конденсаторний фільтр і пульсації (розряд між піками, зростання пульсацій зі струмом навантаження, зарядні піки струму), мостовий випрямляч (у кожному півперіоді провідні два діоди, два падіння V_F), простий стабілітронний стабілізатор і втрата регуляції при надто великому струмі навантаження; книга не наводить формули ΔV = I/(f*C) і не задає V_F конкретного діода."
---

## Short answer

Перевіряють два крайні випадки. Мінімальна вхідна напруга з максимальним струмом навантаження: стабілітрон може лишитися без струму, і стабілізація зникне.[^fiore-rectification] Максимальна вхідна напруга без навантаження: весь струм резистора йде через стабілітрон, тож його нагрівання найбільше.[^nexperia-an90031] Без послідовного резистора струм через стабілітрон нічим не обмежений.[^fiore-rectification]

## Detailed explanation

У простому стабілізаторі послідовний резистор `R` з’єднує вхід із виходом, а стабілітрон у зворотному пробої стоїть паралельно навантаженню. Різниця `V_in - V_Z` падає на `R`, тож струм через нього `I_R = (V_in - V_Z)/R` ділиться між навантаженням і стабілітроном: `I_R = I_load + I_Z`.[^fiore-rectification] Стабілітрон забирає все, що не споживає навантаження, а резистор задає верхню межу струму, який схема взагалі може віддати. Струм `I_R` росте разом з `V_in`, а `I_load` визначає, скільки з нього лишається стабілітрону, тому крайні точки цих двох величин дають два різні способи зламати схему.

**Випадок 1: мінімальне `V_in`, максимальне `I_load`.** Тут `I_R` найменший, а потрібен найбільший. Якщо `I_load` майже дорівнює `I_R`, то на стабілітрон нічого не лишається, він виходить із пробою, регуляція зникає, а `R` і навантаження працюють як звичайний дільник.[^fiore-rectification] Щоб цього не сталося, у Nexperia радять вибирати `R` так, щоб через стабілітрон ішов залишковий струм навіть за найбільшого навантаження: `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`.[^nexperia-an90031] Мінімальним струмом `I_Z(min)` радять брати струм вимірювання `V_Z` з datasheet, приблизно 5 мА для `V_Z` до 17 В.[^nexperia-an90031] Для найгіршого випадку в цю формулу підставляють найменшу `V_in`. Якщо вхід живиться від випрямляча з конденсатором, під `V_in` слід розуміти мінімум пульсацій на повному навантаженні.[^fiore-rectification]

**Випадок 2: максимальне `V_in`, нульове `I_load`.** Тепер `I_R` найбільший і весь іде крізь стабілітрон: `I_Z = (V_in,max - V_Z)/R`, а потужність `P_Z = V_Z*I_Z`. Nexperia прямо зазначає, що стабілітрон розсіює максимум без навантаження.[^nexperia-an90031] Цю потужність порівнюють із `P_tot` з datasheet, яке задають для певних умов монтажу.[^nexperia-an90031] Без резистора ніщо не обмежує струм, і стабілітрон може вийти з ладу.[^fiore-rectification]

**Приклад (власний розрахунок).** `V_in` змінюється від 9 до 12 В, `V_Z = 5.1 V`, навантаження 0…10 мА, `I_Z(min) = 5 mA`. Верхня межа `R ≤ (9 - 5.1)/(0.005 + 0.010) = 3.9/0.015 = 260 Ω`; беремо 240 Ом (ряд E24). На 9 В при 10 мА: `I_R = 3.9/240 = 16.25 mA`, стабілітрону лишається 6,25 мА – регуляція є. На 12 В без навантаження: `I_R = 6.9/240 = 28.75 mA`, звідси `P_Z = 5.1*0.02875 ≈ 0.147 W` і `P_R = 6.9²/240 ≈ 0.198 W`. На практиці додатково враховують допуски `V_Z` і `R`.

**Типові помилки:**

- Перевіряти лише номінальну `V_in` і не брати мінімум із запасом на мережу й пульсації.
- Забути режим без навантаження (відімкнене або несправне навантаження) і потужність стабілітрона саме в ньому.
- Вибирати `R` так, що `I_Z(min)` стає нульовим або недостатнім для пробою.
- Ставити стабілітрон без `R`, навіть якщо «джерело слабке».

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
