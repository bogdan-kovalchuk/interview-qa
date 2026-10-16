---
id: emb-elee-0191
title: "Звідки береться енергія підсиленого сигналу в транзисторному підсилювачі?"
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
  - source_id: fiore-biasing-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
  - source_id: fiore-amplifier-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 6.2 Amplifier Model"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/06:_Amplifier_Concepts/6.2:_Amplifier_Model
---

## Short answer

Від джерела живлення, а не з вхідного сигналу: без додаткового джерела енергії підсилення неможливе.[^fiore-biasing-need] Транзистор лише керує цим потоком: малий струм бази змінює струм колектора.[^fiore-ebers-moll] Колекторний струм іде від `V_CC` через навантаження.[^fiore-emitter-bias]

## Detailed explanation

Підсилювач не створює енергію з нічого. Вхідний сигнал у базі лише визначає, як змінюється струм, який джерело живлення віддає в колекторне коло. Без додаткового джерела енергії підсилення неможливе.[^fiore-biasing-need]

У точці спокою колекторний струм постійний: він тече від `+V_CC` через навантаження `R_C` і транзистор до землі. Зміна струму бази на `ΔI_B` дає зміну колекторного струму `ΔI_C = β*ΔI_B`.[^fiore-ebers-moll] Напруга на колекторі `V_C = V_CC - I_C*R_C` тоді змінюється у протилежний бік, і ця змінна напруга є вихідним сигналом.[^fiore-emitter-bias]

Приклад: у точці спокою струм колектора 0.99 мА при +5 В і навантаженні 1 кОм. Джерело віддає в колекторне коло постійну потужність 5 В × 0.99 мА ≈ 4.95 мВт. Нехай змінна складова струму колектора має амплітуду 0.1 мА. Її діюче значення 0.1 мА / √2 ≈ 0.071 мА, тож змінна потужність у навантаженні (0.071 мА)² × 1 кОм ≈ 5 мкВт. Ця корисна потужність становить близько 0.1 % від потужності джерела. Сигнал визначає, яка частка цієї потужності йде в навантаження, але не створює її.

Коефіцієнт підсилення потужності – це відношення `P_out/P_in`, тому значення більше 1 не суперечить збереженню енергії. Приклад із підручника: 50 мВт на виході при 10 мВт на вході дає підсилення 5.[^fiore-amplifier-model] Енергія при цьому береться з джерела живлення, а не з сигналу.

**Типові помилки:**

- Вважати, що підсилювач «додає» енергію сигналу, бо вихідна потужність більша за вхідну.
- Ототожнювати `P_out/P_in` з джерелом енергії: це лише відношення двох потужностей.
- Подавати сигнал без постійного зсуву: тоді від’ємна півхвиля і додатні напруги нижче приблизно 0.7 В не відкривають перехід.[^fiore-biasing-need]
