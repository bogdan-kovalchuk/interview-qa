---
id: emb-elintro-0090
title: "Формула потужності – три форми?"
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
  - source_id: aac-power
    title: "All About Circuits: Calculating Electric Power"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/calculating-electric-power/
---

## Short answer

Для резистивного навантаження потужність можна обчислити трьома еквівалентними способами: `P = V*I`, `P = I²*R` або `P = V²/R`. Виберіть форму за відомими величинами; останні дві отримують із `P = V*I` та закону Ома.[^aac-power]

## Detailed explanation

Електрична потужність показує, з якою швидкістю передається або перетворюється енергія. Для миттєвих величин основне співвідношення має вигляд `p = v*i`; у простому резистивному колі на постійному струмі ним користуються як `P = V*I`. Одиниця потужності – ват, причому `1 W = 1 J/s`.[^aac-power]

Якщо навантаження є резистором, закон Ома дає змогу замінити струм або напругу у формулі потужності. Підстановка `I = V/R` приводить до `P = V²/R`, а підстановка `V = I*R` – до `P = I²*R`. Це не три різні закони, а три форми, застосовні за однакової резистивної моделі. Для змінного струму в загальному випадку не можна перемножити довільні RMS напругу та струм: у формулі активної потужності також важливі фазовий зсув і форма хвилі.[^aac-power]

**Приклад розрахунку:** резистор `1 kΩ` під’єднаний до `5 V DC`. Струм становить `5 mA`, тому потужність `P = 5 V*5 mA = 25 mW`; той самий результат дає `P = 5²/1000 = 0.025 W`. Оцінюючи нагрівання, порівнюйте розрахунок із номінальною потужністю резистора та враховуйте умови охолодження.[^aac-power]

**Типова помилка:** піднести опір до квадрата або переплутати форми. Квадрат струму множать на опір, а квадрат напруги ділять на опір; перевірка одиниць допомагає виявити помилку до вибору компонента.[^aac-power]
