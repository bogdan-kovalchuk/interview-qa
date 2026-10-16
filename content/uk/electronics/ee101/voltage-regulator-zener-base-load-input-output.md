---
id: emb-elee-0226
title: "Стабілізатор напруги зі стабілітроном 5,6 В на базі, навантаження 50 мА, β ≈ 100, вхід 9 В. Які вихід, струм бази і потужність транзистора?"
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
  - source_id: vishay-silicon-zener-diodes
    title: "Vishay: Silicon Zener Diodes (application document)"
    url: https://www.vishay.com/docs/84117/84117.pdf
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

Вихід `V_out ≈ 5.6 - 0.7 = 4.9` В: стабілітрон тримає базу близько 5,6 В, а емітер лежить на падіння `V_BE ≈ 0.7` В нижче.[^vishay-silicon-zener-diodes][^fiore-bjt-basics] Базовий струм `I_B ≈ 0.5` мА (`I_E/(β+1)`) проходить від 9 В через резистор, який також живить стабілітрон. Потужність транзистора `P ≈ 4.1*0.05 ≈ 0.2` Вт при `V_CE ≈ 4.1` В.

## Detailed explanation

Це емітерний повторювач: колектор підключено до 9 V, навантаження стоїть в емітері, а база тримається стабілітроном. Стабілітрон у режимі пробою підтримує майже сталу напругу, тому його можна змоделювати джерелом `V_Z0` із малим диференційним опором.[^vishay-silicon-zener-diodes] Оскільки `V_BE = V_B - V_E`, емітер лежить на `V_E = V_B - V_BE`. Для кремнію `V_BE` приблизно 0,7 В, тож `V_out = 5.6 - 0.7 = 4.9 V`.[^fiore-bjt-basics]

Для навантаження 50 mA і β = 100 емітерний струм `I_E = 50 mA`. З `I_E = I_C + I_B` і `I_C = β*I_B` випливає `I_B = I_E/(β+1) = 50/101 ≈ 0.495 mA ≈ 0,5 mA`, а `I_C ≈ 49.5 mA`.[^fiore-bjt-basics] Колектор на 9 V, тож `V_CE = 9 - 4.9 = 4.1 V`, а потужність транзистора `P = V_CE*I_C = 4.1*0.0495 ≈ 0.203 W`. Якщо взяти `I_C = 50 mA`, отримаємо 0.205 W; різниця близько 1%.

Схема тримає вихід лише в межах. По-перше, стабілітрон має працювати в області стабілізації: за малих струмів його динамічний опір різко зростає, і стабілізація погіршується, тож резистор має забезпечити не лише `I_B`, а й достатній струм стабілітрона.[^vishay-silicon-zener-diodes] По-друге, вхід має лишатися вищим за `V_out + V_CE(sat) ≈ 4.9 + 0.1 = 5.0 V`. Нижче цього транзистор насичується.[^fiore-bjt-dc-load-line] Тоді, за розрахунком, вихід слідує за входом мінус `V_CE(sat)` і перестає бути стабілізованим. По-третє, `V_Z` має температурний коефіцієнт `α_VZ`, тож вихід залежить від температури.[^vishay-silicon-zener-diodes]

**Типові помилки:**

- Вважати вихід рівним `V_Z` (5,6 В) і не віднімати `V_BE`.
- Плутати `I_B` із `I_E`: базовий струм лише близько `1/(β+1)` від струму навантаження.
- Не перевіряти потужність транзистора: при `V_CE = 4.1 V` і 50 mA вона близько 0,2 W.
