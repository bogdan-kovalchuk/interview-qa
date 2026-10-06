---
id: emb-elee-0142
title: "Стабілітронний стабілізатор 9 В / 5,1 В / 390 Ом: скільки струму лишається стабілітрону при навантаженні 10 кОм і 1 кОм?"
description: "Стабілітронний стабілізатор 9 В / 5,1 В / 390 Ом: скільки струму лишається стабілітрону при навантаженні 10 кОм і 1 кОм?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Походження питання: лекція 58, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
    applicability: "Вибір R1 так, щоб при найбільшому струмі навантаження через стабілітрон лишався струм не менший за мінімальний (для стабілітронів до 17 В – приблизно 5 мА, струм вимірювання V_Z з datasheet), щоб діод працював на крутій ділянці зворотної провідності; дані наведено для серій Nexperia, інші виробники можуть мати інші числа."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Параметри BZX84-C5V1: V_Z = 4,8–5,4 В при 5 мА, максимум r_dif 480 Ом при 1 мА і 60 Ом при 5 мА; значення для цієї серії, а не для всіх стабілітронів на 5,1 В."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Простий стабілітронний стабілізатор: струм послідовного резистора I = (V_cap - V_Z)/R_limit ділиться між навантаженням і стабілітроном, при легкому навантаженні більша частина тече через стабілітрон, а при надто великому струмі навантаження стабілітрон перестає проводити й регуляція зникає. Книга не розглядає допуск V_Z."
---

## Short answer

Якщо стабілітрон у пробої й `V_out ≈ V_Z = 5.1 V`, то струм через резистор `I_R = (9 - 5.1)/390 = 10 mA` і він ділиться між навантаженням та стабілітроном.[^fiore-rectification] При 10 кОм навантаження бере `5.1/10000 = 0.51 mA`, тож стабілітрону лишається ≈ 9,49 мА. При 1 кОм навантаження бере 5,1 мА, і лишається ≈ 4,9 мА. Це номінальні значення: для BZX84-C5V1 `V_Z` має допуск 4,8–5,4 В при 5 мА, тож при 1 кОм лишок може бути приблизно від 3,8 до 6,0 мА.[^nexperia-bzx84]

## Detailed explanation

**Модель.** Поки стабілітрон у зворотному пробої, він тримає на виході майже `V_Z`, а решту напруги джерела бере на себе резистор: `I_R = (V_in - V_Z)/R`. Цей струм ділиться між навантаженням і стабілітроном, тож `I_Z = I_R - I_load`.[^fiore-rectification] Для `V_in = 9 V`, `V_Z = 5.1 V`, `R = 390 Ом` маємо `I_R = 3.9/390 = 10 mA`, і він майже не залежить від навантаження.

**Два навантаження.** При `R_L = 10 kΩ` навантаження бере `5.1/10000 = 0.51 mA`, тож `I_Z = 10 - 0.51 = 9.49 mA`, а стабілітрон розсіює `5.1*9.49 ≈ 48 mW`. При `R_L = 1 kΩ` навантаження бере `5.1/1000 = 5.1 mA`, `I_Z = 10 - 5.1 = 4.9 mA` і `P_Z = 5.1*4.9 ≈ 25 mW`. Тобто що важче навантаження, то менше струму лишається стабілітрону; сума `I_Z + I_load` стала й дорівнює `I_R`.[^fiore-rectification]

**Допуск і запас.** «5,1 В» – номінал. Для BZX84-C5V1 `V_Z` лежить у межах 4,8–5,4 В при 5 мА.[^nexperia-bzx84] Для `V_Z = 5.4 V` маємо `I_R = 3.6/390 ≈ 9.23 mA`, а для `V_Z = 4.8 V` – `I_R = 4.2/390 ≈ 10.77 mA`. Тому при 1 кОм: `I_Z = 9.23 - 5.4 = 3.83 mA` або `10.77 - 4.8 = 5.97 mA`; при 10 кОм – від `9.23 - 0.54 ≈ 8.7 mA` до `10.77 - 0.48 ≈ 10.3 mA`. Це розкид через допуск, а не похибка арифметики.

**Чи достатньо 4,9 мА.** Nexperia радить вибирати R1 так, щоб при найбільшому струмі навантаження через стабілітрон ішов не менший за мінімальний струм, для діодів до 17 В – приблизно 5 мА, струм вимірювання `V_Z`.[^nexperia-an90031] Для цього навантаження не повинно брати більше за `10 - 5 = 5 mA`, тобто `R_L ≳ 5.1/0.005 ≈ 1.02 kΩ`. Отже, 1 кОм уже на межі: стабілітрон ще проводить, але в гіршому випадку допуску лишок менший за 5 мА, а максимальний динамічний опір цієї серії при 1 мА становить 480 Ом проти 60 Ом при 5 мА, тож вихід гірше тримається.[^nexperia-bzx84] Для 10 кОм запас великий.

**Межа застосовності.** Розрахунок `I_Z = I_R - I_load` має сенс, лише поки `I_Z > 0`. Якщо навантаження захоче забрати більше за `I_R`, стабілітрон перестане проводити, регуляція зникне, а резистор із навантаженням утворять дільник напруги.[^fiore-rectification] Теоретична межа тут `R_L = 5.1/0.01 = 510 Ом`; випадок 100 Ом розібрано в `qid:emb-elee-0143`.

**Типові помилки:**

- Рахувати `I_R = V_in/R = 9/390 ≈ 23 mA`, забувши відняти `V_Z`.
- Рахувати струм навантаження як `V_in/R_L` замість `V_out/R_L`.
- Вважати 5,1 В точним значенням і ігнорувати допуск `V_Z`.
- Застосовувати `I_Z = I_R - I_load` і тоді, коли результат вийшов від’ємним.

## Sources

<!-- generated from frontmatter -->
