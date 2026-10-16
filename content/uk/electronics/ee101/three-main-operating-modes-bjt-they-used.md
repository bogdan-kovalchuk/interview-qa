---
id: emb-elee-0188
title: "Які три основні режими роботи BJT і де їх використовують?"
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
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

Відсічення – B–E не проводить (немає достатнього прямого зміщення), струму колектора практично немає, вимкнений ключ. Активний – B–E прямо, B–C зворотно зміщені, лінійне підсилення. Насичення – обидва переходи прямо зміщені, увімкнений ключ.[^mit-6071-bjt-notes] Активний режим використовують у підсилювачах, насичення – у ключах.[^fiore-bjt-collector-curves]

## Detailed explanation

Режим задає стан двох переходів: база–емітер (B–E) і база–колектор (B–C). Для NPN у звичайній роботі важливі три режими, і кожен має свою зону на колекторних характеристиках. Ліворуч лежить насичення, праворуч – пробій, якого не можна допускати. Посередині є майже горизонтальна ділянка, де струм колектора слабо залежить від напруги колектор–емітер; це і є активна зона.[^fiore-bjt-collector-curves][^mit-6071-bjt-notes]

В активному режимі B–E прямо зміщений, тому електрони з емітера входять у базу, і більшість із них доходить до колектора. Колекторний струм задає базовий: I_C = β·I_B. Це і дає підсилення, бо невелика зміна I_B викликає β разів більшу зміну I_C. Співвідношення тримається, поки B–C залишається зворотно зміщеним, тобто поки V_BE < V_CE < V_CC.[^mit-6071-bjt-notes]

У відсіченні B–E не проводить, базового струму немає, а отже немає й колекторного. Ключ розімкнений, і напруга колектор–емітер дорівнює напрузі живлення, бо падіння на колекторному резисторі нульове.[^fiore-bjt-dc-load-line] У насиченні обидва переходи прямо зміщені, I_C визначає зовнішнє коло, а його максимум дорівнює (V_CC − V_CE(sat))/R_C. Напруга V_CE(sat) при цьому мала, близько 0,2 В, тож ключ замкнений, а β на струм уже не впливає.[^mit-6071-bjt-notes]

Тому активний режим використовують у лінійних підсилювачах, де вихідний струм має повторювати вхідний. Відсічення й насичення використовують у ключах: транзистор або не проводить, або проводить повний струм, який визначає навантаження.[^fiore-bjt-collector-curves]

**Типові помилки:**
- Вважати, що активний режим зберігається при будь-якому R_C: великий R_C або малий V_CC зменшують I_C(sat), і I_C не може досягти β·I_B, тож транзистор насичується.[^fiore-bjt-dc-load-line]
- Плутати відсічення з насиченням: у відсіченні V_CE ≈ V_CC і I_C ≈ 0, у насиченні V_CE ≈ 0,2 В, а струм задає R_C.[^mit-6071-bjt-notes]
