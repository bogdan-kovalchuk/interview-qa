---
id: emb-elee-0231
title: "Як налагоджувати зібраний транзисторний аудіопідсилювач?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

Без сигналу виміряти `V_B`, `V_E`, `V_C` і переконатися в активному режимі: у кремнієвому NPN `V_BE` близько 0,7 В, а колектор вищий за базу.[^fiore-bjt-basics] Подати малий синус близько 1 кГц і порівняти амплітуду та фазу: каскад зі спільним емітером інвертує сигнал.[^fiore-common-emitter-amplifier] Збільшувати вхід, доки вихід не почне обрізатися, потім повернутися до лінійної області. Змінювати частоту, щоб побачити вплив розділових конденсаторів.

## Detailed explanation

Налагодження починають без сигналу, бо підсилювач працює правильно лише тоді, коли кожен транзистор стоїть в активному режимі: емітерний перехід прямо зміщений, колекторний зворотно. У кремнієвому NPN напруга база–емітер у цьому режимі близько 0,7 В, а колектор має бути вищим за базу.[^fiore-bjt-basics] Якщо `V_BE` близько нуля, транзистор закритий; якщо `V_CE` опускається до десятих часток вольта, він у насиченні. Межі колекторної напруги задають `V_CE(cutoff) = V_CC` і `V_CE(sat)`.[^fiore-bjt-dc-load-line]

**Приклад:** `V_CC = 9 В`, виміряно `V_E = 1,00 В`, `V_B = 1,70 В`, `V_C = 5,0 В`. Тоді `V_BE = 1,70 - 1,00 = 0,70 В` (емітерний перехід прямий), а `V_CB = 5,0 - 1,70 = 3,3 В` означає, що колекторний перехід зворотний. Отже транзистор активний. Якщо ж `V_B` дорівнює `V_E`, то `V_BE = 0` і транзистор закритий.

Потім подають малий синус близько 1 кГц, де реактивний опір розділових конденсаторів малий і вони майже не послаблюють сигнал.[^fiore-common-emitter-amplifier] Каскад зі спільним емітером інвертує сигнал, тобто зсуває фазу на 180°; знак мінус у `A_v = -r_C/(r'_e + r_E)` і відповідає цій інверсії. Очікуване значення оцінюють через `r'_e = 26 мВ / I_C`.[^fiore-bjt-ac-model] При `I_C = 1 мА` і `r_C = 2,2 кОм` маємо `r'_e ≈ 26 Ом`, а з емітером, зашунтованим конденсатором, `|A_v| ≈ 2200/26 ≈ 85`. Без цього конденсатора з `r_E = 234 Ом` підсилення падає до `2200/(26+234) ≈ 8,5`, тобто в десять разів.

На низьких частотах розділові конденсатори дають спад. З `R = 10 кОм` і C = 100 нФ зріз близько 159 Гц, і на 100 Гц вихід нижчий приблизно на 5,5 дБ.[^fiore-ac-circuit-analysis] Тому якщо підсилювач добре працює на 1 кГц, але слабшає на низьких звукових частотах, першою перевіркою є номінали розділових конденсаторів, а не транзистор.

Амплітуду вхідного сигналу збільшують поступово, доки вихід не почне обрізатися. Обрізання з одного боку зазвичай означає, що робоча точка зсунута до однієї з меж, а з обох боків – що вхід завеликий для каскаду. Після цього амплітуду повертають до лінійної області й вимірюють підсилення там.

**Типові помилки:**

- Міряти підсилення, не перевіривши постійні напруги: у відсіканні або насиченні результат не має сенсу.
- Вважати інверсію фази несправністю: каскад зі спільним емітером інвертує сигнал.
- Робити висновок про поганий підсилювач з втрат на 100 Гц, не перевіривши розділові конденсатори.
