---
id: emb-elee-0175
title: "Чи можна брати з випрямляча з великим конденсатором постійний струм, рівний номінальному RMS-струму вторинної обмотки?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: hammond-rectifier-guide
    title: "Hammond Manufacturing: Design Guide for Rectifier Use"
    url: https://www.hammfg.com/pdf/5c007.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Ні. Конденсаторний фільтр змушує діоди проводити лише короткими імпульсами зарядного струму біля піків, тому RMS-струм вторинної обмотки більший за середній постійний струм навантаження.[^fiore-rectification] Для мостового випрямляча з конденсатором настанова виробника трансформаторів дає орієнтир `I_DC ≈ 0.62*I_RMS` вторинної обмотки.[^hammond-rectifier-guide]

## Detailed explanation

**Що означає номінал.** Номінальний струм вторинної обмотки – це RMS-значення: воно визначає нагрівання обмотки, а номінал у VA дорівнює номінальній вторинній напрузі, помноженій на максимальний вторинний струм; у прикладі Fiore це 24 В RMS × 0,3 А = 7,2 VA.[^fiore-rectification] Постійний струм навантаження – це середнє значення. Для мостового випрямляча з резистивним навантаженням вони близькі: за таблицею Hammond `I_DC = 0.90*I_RMS`.[^hammond-rectifier-guide]

**Чому з конденсатором інакше.** Діод відкривається лише тоді, коли вхідна напруга перевищує напругу на конденсаторі приблизно на 0,7 В (у мосту – на два такі падіння), а більша ємність робить цей інтервал коротшим і піки струму вищими.[^fiore-rectification] У симуляції Fiore для однопівперіодного випрямляча зі 100 Ом і 1000 мкФ зарядний струм сягає близько 800 мА, хоча навантаження бере менш як 0,1 А.[^fiore-rectification] Заряд, який конденсатор віддав навантаженню за період, обмотка мусить повернути за малу частку періоду. У спрощеній моделі прямокутних імпульсів, що займають частку `d` періоду пульсацій, маємо `I_RMS = I_DC/sqrt(d)`: для `d = 0.4` це 1.6*I_DC, для `d = 0.1` – уже 3.2*I_DC.

**Приклад.** Трансформатор 12 В / 1 А RMS (12 VA) з мостом і великим конденсатором. За орієнтиром Hammond постійний струм становить близько `0.62*1 A = 0.62 A`, а не 1 А. І навпаки: щоб отримати 1 А постійного струму, потрібна вторинна обмотка приблизно на `1/0.62 ≈ 1.6 A` RMS, тобто ≈ 19 VA за 12 В.[^hammond-rectifier-guide] Це орієнтир, а не закон. У чисельній моделі схеми з qid:emb-elee-0179 (синусоїдне джерело 9 В RMS, 1000 мкФ, постійне навантаження 0,1 А, 0,7 В на діод) струм обмотки залежить від сумарного послідовного опору: за 0,5 Ом RMS ≈ 0,26 А (≈ 2.6*I_DC) і пік ≈ 0,86 А, за 2 Ом – RMS ≈ 0,21 А (≈ 2.1*I_DC).

**Межі й побічні ефекти.** Коефіцієнт залежить від типу випрямляча: за Hammond для однопівперіодного випрямляча з конденсатором `I_DC = 0.28*I_RMS`, тож ситуація там ще гірша.[^hammond-rectifier-guide] Імпульсний струм навантажує не лише обмотку: Hammond радить діоди з номіналом щонайменше вдвічі більшим за вихідний струм (запас на turn-on surge), а RMS ripple current конденсатора може бути 2–3 разів більшим за I_DC.[^hammond-rectifier-guide] Піковий струм діодів докладніше розібрано в qid:emb-elee-0139.

**Типові помилки:**

- Порівнювати постійний струм навантаження безпосередньо з номінальним RMS-струмом обмотки (1:1).
- Обчислювати потрібні VA як `V*I_DC`, ігноруючи імпульсність струму.
- Збільшувати ємність, щоб зменшити пульсації, не перевіривши піковий струм діодів і обмотки.
- Орієнтуватися лише на середній струм діода, а не на піковий.
