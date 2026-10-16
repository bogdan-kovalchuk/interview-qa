---
id: emb-elee-0182
title: "Які три різні проблеми завад у живленні розглядаються і чому один великий конденсатор не вирішує всі?"
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: fiore-inductance-dc
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 9.2 Inductance and Inductors"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/09:_Inductors/9.2:_Inductance_and_Inductors
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
---

## Short answer

Повільні пульсації після випрямляча і короткі просідання при стрибках навантаження мають різне походження. Високочастотні завади походять від швидкого перемикання, наприклад ключів імпульсного регулятора.[^ti-switching-regulator-fundamentals] Провідники живлення мають опір і індуктивність.[^fiore-inductance-dc] Тому швидка зміна струму створює на них напругу `V_L = L*di/dt`.[^fiore-ac-circuit-analysis] Тому один великий конденсатор не закриває всі три: пульсації й просідання залежать від ємності, а високі частоти – від ESL і довжини доріжки.[^ti-switching-regulator-fundamentals]

## Detailed explanation

Пульсації – це зміна вихідної напруги через розряд конденсатора між піками випрямленої напруги.[^libretexts-fiore-rectification] У двопівперіодному мості навантаження отримує струм в обидва півперіоди одного напрямку, тому частота пульсацій вдвічі вища за мережеву: 100 Гц при мережі 50 Гц або 120 Гц при мережі 60 Гц.

Просідання при стрибку навантаження – інше явище. Конденсатор на виході віддає струм, поки джерело ще не відреагувало. За `i = C*dv/dt` напруга на конденсаторі змінюється зі швидкістю `i/C`,[^fiore-ac-circuit-analysis] тож більша ємність зменшує спад, але не може миттєво замінити струм, який джерело подає із затримкою.

Високочастотні завади створюють елементи, що швидко перемикаються: транзистори й діоди імпульсних перетворювачів дають значні EMI, які легко потрапляють у доріжки та провідники.[^ti-switching-regulator-fundamentals] Велика електролітична ємність тут слабка, бо її паразитна індуктивність ESL обмежує дію на високих частотах.[^ti-switching-regulator-fundamentals] Тому високочастотні завади гасять керамічні або плівкові конденсатори, поставлені поруч із навантаженням.

Тут і виявляється індуктивність провідника. Провідник протидіє зміні струму, що через нього тече,[^fiore-inductance-dc] а за `v = L*di/dt` швидка зміна струму на індуктивності дає напругу.[^fiore-ac-circuit-analysis] Для ілюстрації візьмемо ділянку з індуктивністю 10 нГн, через яку струм змінюється на 1 А за 10 нс: `V = L*di/dt = 10e-9 Гн * (1 А / 10e-9 с) = 1 В`. Така напруга з’являється на ділянці між конденсатором і мікросхемою, тому великий конденсатор, встановлений далеко, не покриває швидку зміну струму в межах цього імпульсу.

**Типові помилки:**

- Вважати, що один великий конденсатор одночасно усуває пульсації, просідання і високочастотні завади.
- Ставити bypass далеко від мікросхеми: довга доріжка має індуктивність, і `L*di/dt` на ній лишається.
- Плутати пульсації мережі з високочастотними завадами і вибирати для них один і той самий фільтр.
