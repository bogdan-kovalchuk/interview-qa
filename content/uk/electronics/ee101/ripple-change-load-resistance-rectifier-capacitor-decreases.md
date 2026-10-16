---
id: emb-elee-0138
title: "Як змінюються пульсації при зменшенні опору навантаження випрямляча з конденсатором?"
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
---

## Short answer

Пульсації збільшуються: при меншому опорі навантаження струм більший, тож конденсатор між піками розряджається швидше.[^fiore-rectification] Для невеликих пульсацій `ΔV_pp ≈ I_load/(f_ripple*C)`, тобто вони ростуть приблизно пропорційно до струму навантаження,[^fiore-capacitors] а середня вихідна напруга при цьому знижується.[^fiore-rectification] Спостереження роблять поетапно: без конденсатора, з конденсатором (з правильною полярністю), потім із меншим опором навантаження.

## Detailed explanation

Між піками діоди закриті, і навантаження живиться лише від конденсатора. Його напруга падає за законом `i = C*dv/dt`: при приблизно сталому струмі спад лінійний, `ΔV = I*Δt/C`, де `Δt` – проміжок між піками.[^fiore-capacitors] Струм навантаження `I = V/R_load`, тому зі зменшенням `R_load` він зростає, а разом із ним росте й спад напруги за той самий час. Підручник формулює це так: пульсації зростають зі струмом навантаження, а за легкого навантаження вихід лишається біля піка вторинної напруги з дуже малими пульсаціями; при великому струмі пульсації збільшуються й середня напруга на виході падає.[^fiore-rectification]

Інакше це видно через сталу часу `τ = R_load*C`: розряд відбувається за експонентою, і чим менший `R_load`, тим менша `τ` порівняно з проміжком між піками, тобто фільтр гірше «тримає» напругу.[^fiore-rectification] Лінійна формула `ΔV ≈ I/(f*C)` – це наближення для випадку, коли `τ` набагато більша за період пульсацій; для великих пульсацій вона недостатньо точна.

**Приклад (власний розрахунок).** Мостовий випрямляч від мережі 50 Гц, `f_ripple = 100 Hz`, `C = 1000 μF`, напруга близько 12 В:

- `R_load = 600 Ω`: `I = 12/600 = 20 mA`, `ΔV ≈ 0.02/(100*0.001) = 0.2 V`;
- `R_load = 120 Ω`: `I = 100 mA`, `ΔV ≈ 0.1/(100*0.001) = 1.0 V`; експоненційний розрахунок `12*(1 - e^(-0.01/0.12)) ≈ 0.96 V` майже збігається;
- `R_load = 12 Ω`: `I = 1 A`, лінійна формула дає 10 В, що безглуздо; експонента `12*(1 - e^(-0.01/0.012)) ≈ 6.8 V` показує, що за 10 мс конденсатор втрачає понад половину напруги, і фільтр фактично не працює.

Опір зменшили в 5 разів – пульсації зросли приблизно в 5 разів, поки `τ` лишається набагато більшою за 10 мс. Для 600 Ом `τ = 0.6 s`, для 120 Ом `τ = 0.12 s`, для 12 Ом `τ = 12 ms` – тут уже порівнянна з періодом, і лінійна оцінка перестає працювати.

Є й побічний ефект: що більший струм навантаження, то більші короткі імпульси струму діодів (у симуляції підручника піки сягають сотень мА).[^fiore-rectification] Тому зменшення `R_load` перевіряють і за піковим струмом діодів і трансформатора.

**Типові помилки:**

- Думати, що більший струм «згладжує» вихід: фільтр, навпаки, гірше працює при меншому `R_load`.
- Користуватися лінійною формулою для великих пульсацій, коли `R_load*C` порівнянне з періодом.
- Забувати, що в мосту `f_ripple = 2*f_mains`, а в однопівперіодній схемі `f_ripple = f_mains`.
