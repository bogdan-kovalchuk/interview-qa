---
id: emb-elee-0058
title: "Який імпеданс мають ідеальні індуктор і конденсатор?"
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
  - source_id: aac-ideal-lc-impedance
    title: "All About Circuits: Series R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-r-l-and-c/
---

## Short answer

Для ідеального індуктора `Z_L = j*ω*L = j*X_L`, де `X_L = ω*L` додатна; для ідеального конденсатора `Z_C = 1/(j*ω*C) = -j/(ω*C) = -j*X_C`, де `X_C = 1/(ω*C)` додатна. Тут `ω = 2π*f`, тому індуктивний імпеданс має кут `+90°`, а ємнісний – `-90°` за частоти `f > 0`.[^aac-ideal-lc-impedance]

## Detailed explanation

Для синусоїдального усталеного режиму ідеальні індуктор і конденсатор мають суто уявний імпеданс, але з протилежними знаками. Якщо `ω = 2π*f`, то `Z_L = j*ω*L`, тоді як `Z_C = 1/(j*ω*C) = -j/(ω*C)`. Реактивності `X_L = ω*L` і `X_C = 1/(ω*C)` є додатними скалярними величинами; знак з’являється у комплексному записі імпедансу.[^aac-ideal-lc-impedance]

Знак пов’язаний з фазою: для ідеального індуктора напруга випереджає струм на `90°`, а для конденсатора струм випереджає напругу на `90°`. Залежність від частоти теж різна. За незмінної індуктивності `X_L` зростає пропорційно `f`, а `X_C` зменшується обернено пропорційно `f`. Ці співвідношення припускають лінійні ідеальні елементи без втрат і паразитних параметрів.[^aac-ideal-lc-impedance]

Приклад: для ідеального індуктора `L = 10 mH` на `f = 1 kHz`, `ω = 2π*1000 rad/s`, тому `X_L ≈ 62.8 Ω` і `Z_L ≈ j*62.8 Ω`. Для конденсатора `C = 10 µF` на тій самій частоті `X_C ≈ 15.9 Ω`, отже `Z_C ≈ -j*15.9 Ω`. Це не два звичайні резистори: знак і фаза впливають на суму в колі. Обчислення використовують точні номінали ідеальних елементів та округлення до трьох значущих цифр.[^aac-ideal-lc-impedance]

У реальних деталях обмотка індуктора має опір і паразитну ємність, а конденсатор – втрати та паразитний опір виводів. Тому ідеальні формули є наближенням у робочому діапазоні, а поблизу власного резонансу поведінка компонента може відрізнятися. Для `f = 0` формула конденсатора як синусоїдального фазора має граничний характер: його імпеданс прямує до нескінченності, тоді як індуктивний імпеданс прямує до нуля.[^aac-ideal-lc-impedance]

**Типові помилки:**

- Забувати мінус у `Z_C` і приписувати конденсатору індуктивний фазовий знак.
- Плутати реактивність `X_C` як додатну величину з уявною частиною імпедансу `-j*X_C`.
- Вважати ідеальні формули точною моделлю реальної деталі на будь-якій частоті.[^aac-ideal-lc-impedance]
