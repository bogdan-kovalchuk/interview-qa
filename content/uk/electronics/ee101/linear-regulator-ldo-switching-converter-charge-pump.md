---
id: emb-elee-0153
title: "Чим відрізняються лінійний стабілізатор, LDO, імпульсний перетворювач і зарядова помпа?"
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-slyt527
    title: "Texas Instruments SLYT527: Linear versus switching regulators in industrial applications with a 24-V bus (Analog Applications Journal, 3Q 2013)"
    url: https://www.ti.com/lit/an/slyt527/slyt527.pdf
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
  - source_id: ti-charge-pump-basics
    title: "Texas Instruments SSZTBO1: Pump It up with Charge Pumps – Part 1 (technical article)"
    url: https://www.ti.com/lit/ta/ssztbo1/ssztbo1.pdf
---

## Short answer

Лінійний стабілізатор регулює опір прохідного елемента, тож різниця `V_in - V_out` розсіюється теплом: схема проста й малошумна, але за великого перепаду напруг неефективна.[^ti-slva118a][^ti-slyt527] LDO – лінійний стабілізатор з малим мінімальним падінням (dropout), але зі специфічними вимогами datasheet до вихідного конденсатора.[^ti-slva118a][^ti-slva079] Імпульсний перетворювач перемикає ключ і індуктивність: ККД зазвичай значно вищий, проте є пульсації, завади й складніший розрахунок.[^ti-slyt527][^ti-switching-regulator-fundamentals] Зарядова помпа перемикає конденсатори без індуктивності: для невеликих струмів і кратних співвідношень, як ≈ `2*V_in` чи `-V_in`.[^ti-charge-pump-basics]

## Detailed explanation

Лінійний стабілізатор має прохідний елемент, яким контролер за зворотним зв’язком керує так, щоб вихід лишався сталим; його зручно уявляти як потенціометр між входом і виходом. Вхідний струм приблизно дорівнює вихідному, тож різниця напруг цілком перетворюється на тепло: `P_D ≈ (V_in - V_out)*I_out`, а ККД ≈ `V_out/V_in`.[^ti-slva118a] Звідси ж видно обмеження: лінійний стабілізатор лише знижує напругу, а на великому перепаді мало ефективний. Натомість схема проста (кілька компонентів) і дає дуже малі пульсації, тому лінійні стабілізатори ставлять навіть після імпульсних, щоб очистити вихід.[^ti-slyt527]

LDO – та сама архітектура, але з малим dropout, тобто з малою мінімальною різницею `V_in - V_out`, за якої стабілізатор ще працює в межах специфікації. Це виграє, коли вхід близький до виходу або живиться від акумулятора.[^ti-slva118a] У режимі dropout прохідний PMOS-елемент – просто резистор, `V_dropout = I_o*R_on`.[^ti-slva079] Платити доводиться вимогами до стабільності: виробник задає допустимий діапазон послідовного опору вихідного конденсатора (для TPS763xx у записці – 0,2–9 Ом), тож випадкова заміна конденсатора на інший ризикує нестабільністю.[^ti-slva079] Малий dropout не скасовує фізики: за великого перепаду LDO розсіює `(V_in - V_out)*I_out` так само, як звичайний лінійний.[^ti-slva118a]

Імпульсний перетворювач працює інакше: ключ по черзі підключає вхід до індуктивності, струм індуктивності не може змінитися миттєво і після вимкнення ключа тече далі через діод, а вихід регулюють шириною імпульсу (PWM).[^ti-switching-regulator-fundamentals] Різниця напруг не гасне в прохідному елементі, тому ККД, як правило, вищий, а топології дозволяють отримати і нижчу, і вищу, і протилежну за знаком напругу.[^ti-switching-regulator-fundamentals] Ціна – пульсації, EMI від швидкого перемикання й складніший розрахунок та розводка.[^ti-switching-regulator-fundamentals] У прикладі TI для входу 24 В, виходу 5 В і 100 мА лінійний стабілізатор має `P_D ≈ (24 - 5)*0,1 = 1,9 Вт` і ККД `5/24 ≈ 21%`; виміряні значення цієї плати – близько 20% і 2 Вт проти 84,5% і 0,093 Вт у buck, а пульсації – менше 10 мВ проти 75 мВ.[^ti-slyt527]

Зарядова помпа замість індуктивності використовує «літаючий» конденсатор: його заряджають до `V_in`, а потім перемикають послідовно з входом, і вихід дорівнює приблизно `2*V_in` (подвоювач) або `-V_in` (інвертор), наприклад ≈ 10 В і ≈ –5 В зі входу 5 В.[^ti-charge-pump-basics] Проста помпа не стабілізує вихід, а регульований подвоювач стабілізує лише між `V_in` і `2*V_in`. За оцінкою TI, помпи добрі для десятків міліампер і гірше – понад 250 мА, і менш ефективні за індуктивні перетворювачі, якщо не працюють нерегульовано.[^ti-charge-pump-basics]

**Типові помилки:**

- Вважати LDO «ефективним» за будь-якої напруги: втрати `(V_in - V_out)*I_out` лишаються, просто мінімальний перепад менший.
- Ставити на вихід LDO довільний конденсатор без перевірки допустимого ESR у datasheet.
- Ставити імпульсний перетворювач перед чутливим аналоговим вузлом без фільтра чи лінійного post-регулятора.
- Брати зарядову помпу для великих струмів: вона розрахована на невеликі навантаження.
