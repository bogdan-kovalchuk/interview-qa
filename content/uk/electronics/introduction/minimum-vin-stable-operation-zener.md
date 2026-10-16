---
id: emb-elintro-0189
title: "Яка мінімальна `V_in` потрібна для стабілізації 5.1 В стабілітроном?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

Мінімальна `V_in` залежить від `R_s`, найбільшого `I_load` і мінімального струму регулювання конкретного стабілітрона: приблизно `V_in ≥ V_Z + R_s*(I_load + I_Z(min))`.[^aac-zener-regulator] Тому 8 V для номіналу 5.1 V є лише припущенням про 3 V запас, а не універсальною межею; при нестачі струму стабілізація втрачається й `V_out` просідає.[^aac-zener-regulator]

## Detailed explanation

У простому Зенерівському стабілізаторі мінімальна вхідна напруга – це найменше значення, за якого через `R_s` ще проходить достатньо струму і для навантаження, і для стабілітрона. Номінал `V_Z = 5.1 V` сам по собі не задає цю межу: потрібні значення резистора, максимального струму навантаження та мінімального струму, за якого обраний діод забезпечує прийнятне регулювання.[^aac-zener-regulator]

Коли вихід тримається біля `V_Z`, резистор має падіння приблизно `V_in - V_Z`; отже його струм оцінюють як `I_R = (V_in - V_Z)/R_s`. За законом струмів вузла `I_R = I_load + I_Z`. Щоб залишити стабілітрон у робочій області при найбільшому навантаженні, потрібно `I_Z ≥ I_Z(min)`. Звідси випливає оцінка `V_in(min) ≈ V_Z + R_s*(I_load(max) + I_Z(min))`. У практичному проєкті також враховують найгірші допуски джерела й резистора та вимоги до точності, а не обирають межу лише за типовим номіналом діода.[^aac-zener-regulator]

Приклад розрахунку: нехай `V_Z = 5.1 V`, `R_s = 330 Ω`, найбільший струм навантаження дорівнює `10 mA`, а для розрахунку прийнято `I_Z(min) = 5 mA`. Тоді `V_in(min) ≈ 5.1 V + 330 Ω*(15 mA) = 10.05 V`. Значення `5 mA` тут є заданим припущенням прикладу, а не універсальним параметром будь-якого стабілітрона. Отже, правило «додати 3 V» не гарантує стабілізації: за інших `R_s` або струму навантаження потрібна інша вхідна напруга.

**Типові помилки:**

- Називати `8 V` мінімумом для кожного кола з діодом `5.1 V`, не знаючи резистора та навантаження.
- Перевіряти лише наявність напруги вище `V_Z` і забувати про струм коліна, який мусить лишитися після відгалуження струму навантаження.[^aac-zener-regulator]
