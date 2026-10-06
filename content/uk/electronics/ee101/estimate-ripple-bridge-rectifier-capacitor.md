---
id: emb-elee-0130
title: "Як оцінити пульсації після мостового випрямляча з конденсатором?"
description: "Як оцінити пульсації після мостового випрямляча з конденсатором?"
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
    applicability: "Походження питання: лекція 55, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Конденсаторний фільтр і пульсації (розряд між піками, зростання пульсацій зі струмом навантаження, зарядні піки струму), мостовий випрямляч (у кожному півперіоді провідні два діоди, два падіння V_F), простий стабілітронний стабілізатор і втрата регуляції при надто великому струмі навантаження; книга не наводить формули ΔV = I/(f*C) і не задає V_F конкретного діода."
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Співвідношення i = C*dv/dt: сталий струм через конденсатор дає лінійну зміну напруги, тобто ΔV = I*Δt/C; розділ не розглядає випрямлячі, ESR і реальні форми струму навантаження."
---

## Short answer

Для невеликих пульсацій `ΔV_pp ≈ I_load/(f_ripple*C)`: між піками конденсатор віддає струм навантаження приблизно протягом одного періоду пульсацій.[^fiore-capacitors] Після мостового випрямляча `f_ripple = 2*f_mains`, тобто 100 Гц для мережі 50 Гц, тому при 20 мА і 1000 мкФ `ΔV_pp ≈ 0.02/(100*0.001) = 0.2 V`. Оцінка наближена: вона припускає сталий струм і ігнорує ESR конденсатора. Щоб зменшити пульсації при тому самому струмі, збільшують C, але діоди тоді проводять коротшими й більшими імпульсами струму.[^fiore-rectification]

## Detailed explanation

Між піками випрямленої напруги діоди закриті, бо напруга на вході нижча за напругу на конденсаторі, і навантаження живиться лише від конденсатора. Струм конденсатора пов’язаний з напругою як `i = C*dv/dt`, тому при приблизно сталому струмі навантаження напруга на ньому падає лінійно: `ΔV = I*Δt/C`.[^fiore-capacitors] Найдовший час розряду – проміжок між сусідніми піками, `Δt = 1/f_ripple`, звідки й береться формула `ΔV_pp ≈ I_load/(f_ripple*C)`. Чим більший струм навантаження, тим більші пульсації, а на легкому навантаженні вихід лишається близько піка вторинної напруги з дуже малими пульсаціями.[^fiore-rectification]

**Чому `f_ripple = 2*f_mains`.** У мостовому випрямлячі струм тече через навантаження в одному напрямку в обох півперіодах мережі, тому піків за період мережі два: 100 Гц для 50 Гц і 120 Гц для 60 Гц.[^fiore-rectification] В однопівперіодному випрямлячі `f_ripple = f_mains`, тож для тих самих пульсацій потрібна вдвічі більша ємність; саме тому двопівперіодні схеми дозволяють брати менший фільтрувальний конденсатор.[^fiore-rectification]

**Межі наближення.** Формула працює, коли пульсації малі порівняно з постійною складовою, тобто стала часу `R_load*C` набагато більша за період пульсацій. Для 12 В і 20 мА маємо `R_load = 12/0.02 = 600 Ом` і `τ = 600*0.001 = 0.6 s` проти 10 мс між піками; експоненційний розрахунок `12*(1 - e^(-0.01/0.6))` дає ≈ 0,20 В, тобто той самий результат. Насправді конденсатор розряджається трохи менше за 10 мс, бо діоди відкриваються ще до піка, а ESR конденсатора додає ступінчасту складову `I*ESR`, тому реальне значення відрізняється від оцінки. Якщо пульсації великі або `R_load*C` порівнянне з періодом, розряд уже не лінійний і потрібен розрахунок з експонентою.

**Приклад.** Для мережі 60 Гц із тими самими 20 мА й 1000 мкФ: `f_ripple = 120 Гц` і `ΔV_pp ≈ 0.02/(120*0.001) ≈ 0.17 V`. Щоб при 50 Гц отримати не більше 0,1 В, потрібно `C ≥ 0.02/(100*0.1) = 0.002 F = 2000 μF`. Більша ємність не безкоштовна: діод відкривається лише тоді, коли вхідна напруга перевищує напругу конденсатора, тож зі зростанням C інтервал провідності скорочується, а піки зарядного струму зростають.[^fiore-rectification] Діоди й трансформатор перевіряють за піковим, а не середнім струмом.

**Типові помилки:**

- Брати `f_ripple = 50 Гц` для мосту замість 100 Гц і отримувати вдвічі завищені пульсації.
- Підставляти мікрофаради як фаради: 1000 μF – це 0.001 F, а не 1000.
- Вважати формулу точною при великих пульсаціях (`R_load*C` порівнянне з періодом) і забувати про ESR.
- Збільшувати C без перевірки пікового струму діодів і трансформатора.

## Sources

<!-- generated from frontmatter -->
