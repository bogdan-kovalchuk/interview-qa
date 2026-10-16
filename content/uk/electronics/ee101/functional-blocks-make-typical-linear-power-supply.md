---
id: emb-elee-0151
title: "З яких функціональних блоків складається типове лінійне джерело живлення від AC?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
---

## Short answer

Понижувальний трансформатор знижує мережеву змінну напругу, випрямляч (діодний міст) робить її однополярною, а накопичувальний конденсатор зменшує пульсації.[^fiore-rectification] Лінійний стабілізатор наприкінці утримує задану вихідну напругу при зміні вхідної напруги й струму навантаження.[^ti-slva118a]

## Detailed explanation

Типовий лінійний блок живлення від мережі – це ланцюжок із чотирьох ступенів, і кожен розв’язує окрему задачу. Трансформатор масштабує змінну напругу за відношенням витків: вторинна обмотка дає нижчу напругу, а її розмір обмежує добуток номінальної напруги й струму, VA-рейтинг.[^fiore-rectification] Саме трансформатор приводить мережеву напругу до рівня, з якого далі можна отримати потрібну постійну напругу.

Випрямляч, найчастіше діодний міст із чотирьох діодів, пропускає струм через навантаження в один бік в обох півперіодах: у кожному з них проводять по два діоди, тож на виході пульсуюча напруга одного знака з піком на два прямі падіння нижчим за пік вторинної.[^fiore-rectification] Це ще не постійна напруга: між піками вона падає майже до нуля. Тому наступний ступінь – накопичувальний (фільтрувальний) конденсатор: він заряджається, поки діоди проводять, і віддає заряд у навантаження між піками. Що більший струм навантаження, то більші пульсації, а що більша ємність, то вони менші, але діоди проводять коротше й із більшими піками струму.[^fiore-rectification] Оцінка для мосту: якщо між піками конденсатор віддає майже сталий струм, то `ΔV_pp ≈ I/(f_ripple*C)`, де `f_ripple = 2*f_mains`, бо піки йдуть в обох півперіодах. Сама залежність `ΔV = I*Δt/C` випливає з `i = C*dv/dt`.[^fiore-capacitors]

Останній ступінь – стабілізатор. Лінійний стабілізатор має прохідний елемент, яким керує контролер за зворотним зв’язком, і підтримує сталу вихідну напругу, поки змінюються вхідна напруга й струм навантаження.[^ti-slva118a] Ціна цього – тепло: різниця `V_in - V_out` за даного струму розсіюється в стабілізаторі, `P_D ≈ (V_in - V_out)*I_out`.[^ti-slva118a] Тому стабілізатору потрібен запас: навіть найнижча точка пульсацій на його вході має лишатися вище за `V_out` плюс dropout. Без цього ступеня блок лишається нестабілізованим: його вихід змінюється з мережею й навантаженням.

**Приклад (ілюстративний, без урахування просідання вторинної обмотки).** Вторинна обмотка 12 В RMS, міст із падінням 0,7 В на діод, мережа 50 Гц, струм 100 мА, конденсатор 1000 мкФ. Пік вторинної `12*√2 ≈ 17,0 В`, після двох діодів `17,0 - 1,4 ≈ 15,6 В`. Пульсації `ΔV_pp ≈ 0,1/(100*0,001) = 1,0 В`, тож вхід стабілізатора коливається від ≈ 14,6 до ≈ 15,6 В, у середньому ≈ 15,1 В. Для виходу 5 В розсіювання `P_D ≈ (15,1 - 5)*0,1 ≈ 1,0 Вт`, а ККД ступеня ≈ `5/15,1 ≈ 33%`.[^ti-slva118a] Якщо мережа просяде на 10% (12 В стане 10,8 В RMS), пік зменшиться до `10,8*√2 - 1,4 ≈ 13,9 В`, найнижча точка – до ≈ 12,9 В, і 5 В на виході збережеться, хоча без стабілізатора вихід упав би приблизно на 11%.

**Типові помилки:**

- Вважати конденсатор стабілізатором: він згладжує пульсації, але рівень виходу змінюється з мережею й навантаженням.
- Забувати про запас напруги: у найнижчій точці пульсацій вхід стабілізатора все одно має перевищувати вихід на dropout.
- Не враховувати нагрів: у лінійному стабілізаторі розсіюється `(V_in - V_out)*I_out`, тож висока напруга на вході за значного струму потребує тепловідведення.
