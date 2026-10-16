---
id: emb-elee-0194
title: "`V_B` = 1,7 В, `R_E` = 1 кОм, β = 100, навантаження 1 кОм від +5 В до колектора. Які струм і напруги?"
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
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
  - source_id: fiore-pn-junction
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 2.2 The PN Junction"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.2:_The_PN_Junction
---

## Short answer

За `V_BE` ≈ 0.7 В[^libretexts-fiore-diode-models] виходить `I_E = (1.7 - 0.7)/1000 = 1` мА, а `I_C = β/(β+1)*I_E = 0.990` мА при β = 100.[^mit-6071-bjt-notes] `V_E` ≈ 1 В, `V_C = 5 - 0.99 = 4.01` В: запас достатній для активного режиму, бо `V_CE` ≈ 3 В, тоді як `V_CE(sat)` зазвичай лише десяті частки вольта.[^fiore-bjt-dc-load-line]

## Detailed explanation

Схема така: база отримує напругу `V_B` = 1.7 В від джерела з малим вихідним опором, емітер через `R_E` = 1 кОм з’єднано із землею, а колектор через навантаження 1 кОм підключено до +5 В. Для кремнію напругу база–емітер беруть як 0.7 В.[^libretexts-fiore-diode-models] Це поведінкове наближення: реальний `V_BE` залежить від струму й температури.[^fiore-pn-junction] Тоді `V_E = V_B - V_BE` = 1.0 В і `I_E = V_E/R_E` = 1.00 мА.

Колекторний струм знаходимо через `I_E`. Базовий струм `I_B = I_E/(β+1)` ≈ 9.90 мкА, а `I_C = β*I_B` ≈ 0.990 мА. Це те саме, що `I_C = β/(β+1)*I_E`, тобто α = 0.99 при β = 100.[^mit-6071-bjt-notes] Напруга на колекторі: `V_C = V_CC - I_C*R_C = 5 - 0.99*1 = 4.01` В.[^fiore-emitter-bias]

Перевірка режиму: `V_CE = 4.01 - 1.00 = 3.01` В, `V_CB = 4.01 - 1.70 = 2.31` В. Колекторно-базовий перехід зворотний, бо `V_C` вище `V_B`, а емітерно-базовий прямий, тож транзистор в активному режимі. Насичення настає, коли `V_CE` спадає до десятих часток вольта.[^fiore-bjt-dc-load-line]

Емітерний резистор уже зробив струм майже незалежним від β: при β = 200 `I_C` = 0.995 мА, тобто лише на 0.5 % більше.[^fiore-emitter-bias] Найбільший ризик тут не β, а `V_BE`. Похибка 0.1 В у `V_BE` змінює `V_E` на 0.1 В і тому `I_E` на 0.1 мА, тобто на 10 %. У розрахунку слід брати діапазон `V_BE`, а не одне значення.

Ідеальне джерело `V_B` – важлива умова. Якщо `V_B` дає дільник з опором 10 кОм, струм бази 9.9 мкА знижує його приблизно на 0.1 В (`I_B*R_B` ≈ 0.099 В), і `I_E` змінюється на 10 %. Тобто похибка в базі має такий самий ефект, як похибка `V_BE`.

**Типові помилки:**

- Множити `I_E` на β замість β/(β+1): `I_C = β*I_E` дає струм у 100 разів завищений.
- Вважати `V_BE` точно 0.7 В і не брати його діапазон.
- Не перевірити, що `V_C` вище `V_B`: інакше транзистор виходить з активного режиму.
