---
id: emb-elee-0152
title: "Чим фільтрація відрізняється від стабілізації напруги?"
description: "Чим фільтрація відрізняється від стабілізації напруги?"
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
    applicability: "Походження питання: лекція 60, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
    applicability: "Конденсатор згладжує випрямлену напругу, віддаючи заряд у навантаження між піками; зміна напруги від розряду конденсатора названа пульсаціями; зі зростанням струму навантаження пульсації збільшуються, а середній рівень виходу знижується, тоді як за легкого навантаження вихід тримається біля піка вторинної напруги. Книга не наводить параметрів лінійних стабілізаторів."
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Співвідношення i = C*dv/dt: сталий струм через конденсатор дає лінійну зміну напруги, тобто ΔV = I*Δt/C; розділ не розглядає випрямлячі, ESR і реальні форми струму навантаження."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Line regulation як зміна виходу від зміни входу, load regulation як зміна виходу від зміни струму навантаження (обидві усталені); PSRR як відношення пульсацій виходу до пульсацій входу на всіх частотах; dropout як різниця вхід-вихід, за якої схема перестає стабілізувати. Записка про LDO; значення PSRR залежать від частоти й конкретної мікросхеми, а числа прикладу нижче ілюстративні."
---

## Short answer

Фільтрація згладжує випрямлену напругу, зменшуючи змінну складову (пульсації), але рівень виходу все одно знижується зі зростанням струму навантаження.[^fiore-rectification] Стабілізація утримує задану вихідну напругу при зміні вхідної напруги та струму навантаження, а також послаблює пульсації на вході (PSRR).[^ti-slva079]

## Detailed explanation

Фільтр і стабілізатор розв’язують різні задачі, хоча обидва «роблять напругу рівнішою». Після випрямляча напруга пульсує, бо конденсатор між піками віддає заряд у навантаження, а потім дозаряджається; ця змінна складова на постійному рівні – і є пульсації.[^fiore-rectification] Фільтр (найчастіше конденсатор, паралельний навантаженню) зменшує саме її. Але він не фіксує рівень: за легкого навантаження вихід тримається біля піка вторинної напруги, а зі зростанням струму пульсації збільшуються й середній рівень виходу знижується.[^fiore-rectification] Піки вторинної обмотки пропорційні її напрузі, тож рівень після фільтра слідує і за мережею.

Оцінка пульсацій для моста: `ΔV_pp ≈ I/(f_ripple*C)`, що випливає з `ΔV = I*Δt/C`.[^fiore-capacitors] Для `C = 1000 мкФ` і `f_ripple = 100 Гц` струм 20 мА дає `0,02/(100*0,001) = 0,2 В`, а 100 мА – `0,1/(100*0,001) = 1,0 В`. Тобто лише навантаження змінило пульсації в п’ять разів, і ця ж зміна струму зсуває середній рівень виходу вниз.

Стабілізатор працює за іншим принципом: він порівнює вихід з опорою й коригує прохідний елемент, тому вихід майже не залежить від входу й навантаження. Цю якість описують двома усталеними параметрами: line regulation `ΔV_out/ΔV_in` (реакція виходу на зміну входу) і load regulation `ΔV_out/ΔI_out` (реакція на зміну струму).[^ti-slva079] Побічно стабілізатор послаблює й пульсації: PSRR – це відношення пульсацій виходу до пульсацій входу, і воно залежить від частоти.[^ti-slva079] Якщо, наприклад, PSRR становить –60 дБ на частоті пульсацій (число ілюстративне), то `10^(-60/20) = 0,001`, і 1 В пульсацій на вході перетворюється приблизно на 1 мВ на виході.

Звідси порядок і взаємна залежність блоків. Стабілізатор не скасовує потреби у фільтрі: найнижча точка пульсацій на його вході має лишатися вищою за `V_out` плюс dropout, бо dropout – це різниця вхід-вихід, за якої схема перестає стабілізувати.[^ti-slva079] Фільтр без стабілізатора не дає сталого рівня: вихід зсувається з мережею й навантаженням. Тому в типовому блоці живлення спершу йдуть випрямляч і фільтрувальний конденсатор, а потім стабілізатор.

**Типові помилки:**

- Вважати, що великий конденсатор «стабілізує» напругу: він зменшує пульсації, але не фіксує середній рівень.
- Змішувати пульсації з line regulation: перші – швидка змінна складова за частотою мережі, друга – усталений зсув виходу при зміні входу.
- Очікувати від стабілізатора ідеального згладжування, не перевіривши PSRR на частоті пульсацій і запас за dropout.

## Sources

<!-- generated from frontmatter -->
