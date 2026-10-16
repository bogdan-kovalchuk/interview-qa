---
id: emb-elee-0198
title: "Що таке зміщення (bias) транзистора і навіщо воно потрібне?"
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
  - source_id: fiore-bias-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

Зміщення (bias) – це постійні напруги й струми, які задають робочу точку транзистора. Завдяки ним малий змінний сигнал коливається навколо цієї точки і не вимикає транзистор у кожному півперіоді, бо база–емітер відкривається лише при напрузі близько 0,7 В.[^fiore-bias-need]

## Detailed explanation

Робоча точка, або Q-точка, – це постійні струм і напруга транзистора без сигналу: `I_CQ` і `V_CEQ`. Усі можливі Q-точки лежать на навантажувальній прямій.[^fiore-bjt-dc-load-line] Для NPN зміщення має забезпечити прямо зміщене база–емітерне з’єднання і зворотно зміщений колекторно-базовий перехід, тобто `V_C` > `V_B` > `V_E`.[^fiore-bjt-ebers-moll] Саме ці постійні напруги й струми і є зміщенням.

Навіщо це потрібно. Транзистор практично не проводить, поки `V_BE` не досягне близько 0,7 В.[^fiore-bias-need] Приклад: синусоїда з амплітудою 0,2 В, подана на базу без зміщення, дає `V_BE` не більше 0,2 В, тобто менше за 0,7 В. Транзистор не відкривається в жодній півхвилі, тож підсилення немає. Підручник пише, що сигнали мікрофонів і датчиків часто мають кілька сотень мілівольт, і без постійного зміщення такий сигнал може бути повністю проігнорований.[^fiore-bias-need] Постійне зміщення вирішує це: змінний сигнал накладається на велику постійну напругу, і навіть його негативний пік лишається додатною напругою на базі.[^fiore-bias-need]

Q-точка має бути стабільною, бо `I_C` і `V_CE` залежать від β, а β змінюється з температурою, струмом і напругою `V_CE`.[^fiore-bjt-ebers-moll] Підручник пояснює, що нестабільна Q-точка робить підсилення нестабільним, підвищує спотворення й зменшує вихідну потужність.[^fiore-bias-need] Тому робочу точку вибирають у зоні постійного струму, де `I_C` майже не залежить від `V_CE` і де працюють лінійні підсилювачі.[^fiore-bjt-collector-curves] Її кінці – це `I_C(sat)` і `V_CE(cutoff)`; Q-точка лежить між ними, а не на одному з кінців, тож сигнал має запас в обидва боки.[^fiore-bjt-dc-load-line]

**Типові помилки:**

- Вважати, що Q-точка стабільна сама собою: β змінюється від екземпляра до екземпляра і з температурою.[^fiore-bjt-ebers-moll]
- Ставити робочу точку в зону насичення або пробою замість зони постійного струму, де працюють лінійні підсилювачі.[^fiore-bjt-collector-curves]
- Розраховувати зміщення за одним значенням β з каталогу без перевірки запасу сигналу.
