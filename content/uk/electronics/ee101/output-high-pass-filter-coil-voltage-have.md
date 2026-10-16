---
id: emb-elee-0120
title: "Чому вихід RL-ФВЧ (напруга на котушці) має додатну фазу відносно джерела?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
---

## Short answer

Струм у RL-колі відстає від напруги джерела на кут `arctan(2*pi*f*L/R)`, а напруга на L випереджає сам струм на 90°. Тому фаза виходу `φ = 90° - arctan(2*pi*f*L/R)` завжди додатна: близько +90° на низьких частотах, +45° на `f_c` і прямує до 0° на високих.[^fiore-ac-circuit-analysis]

## Detailed explanation

**Схема й два зсуви.** У RL-ФВЧ джерело з’єднане послідовно з резистором `R` і котушкою `L`, а вихід знімають із котушки.[^kuphaldt-high-pass-filters] Через обидва елементи тече один і той самий струм `I`, тому фазу виходу зручно рахувати в два кроки. Для ідеальної котушки `v = L*di/dt`, отже напруга на ній випереджає власний струм на 90°.[^fiore-ac-circuit-analysis] Сам струм задає повний імпеданс `R + j*2*pi*f*L`, чия реактивна частина додатна, тому `I` відстає від напруги джерела на кут від 0° до 90°.

**Сумарна фаза.** Складаємо ці два зсуви: `φ = 90° - arctan(X_L/R)`, де `X_L = 2*pi*f*L`.[^fiore-ac-circuit-analysis] Модуль дає той самий дільник: `|V_out/V_in| = X_L/sqrt(R^2 + X_L^2)`. На частоті `f_c = R/(2*pi*L)` реактивний опір дорівнює `R`, тож амплітуда становить `1/sqrt(2) ≈ 0.707` (`-3.01 dB`), а фаза рівно +45°. Вихід завжди випереджає вхід, але ніколи не більш ніж на 90°. Таку саму форму має RC-ФВЧ, де вихід знімають із резистора: +90° на низьких частотах, +45° на критичній і майже 0° на дуже високих.[^fiore-ac-circuit-analysis]

**Приклад.** Нехай `R = 1 kΩ`, `L = 10 mH`; тоді `f_c = 1000/(2*pi*0.01) ≈ 15.9 kHz`. На `0.1*f_c ≈ 1.59 kHz` відношення `X_L/R = 0.1`, тож фаза `90° - 5.71° = +84.29°`, а `|V_out/V_in| ≈ 0.0995` (`-20.04 dB`). На `f_c` маємо +45° і 0.707. На `10*f_c ≈ 159 kHz` фаза `+5.71°`, а амплітуда `≈ 0.995` (`-0.04 dB`).

**Межі моделі.** Усе вище – для ідеальної котушки без навантаження. Реальна котушка має опір обмотки й паразитну ємність.[^fontys-passive-hf] Через опір обмотки напруга на клемах котушки на низьких частотах уже не наближається до +90°: на постійному струмі вона не нуль, а фаза прямує до 0° (див. qid:emb-elee-0121). Якщо ж вихід узяти з резистора, а не з котушки, фаза стане від’ємною (`-arctan(X_L/R)`), і це вже RL-ФНЧ.

**Типові помилки:**

- Міркувати «струм відстає, отже й вихід відстає»: вихід – це напруга на L, вона випереджає струм на 90° і лише частково компенсується відставанням самого струму.
- Вважати, що на котушці завжди рівно +90° відносно джерела: це лише межа для `f` значно менших за `f_c` і для ідеальної котушки.
- Брати вихід на `R` замість `L`: тоді виходить RL-ФНЧ із фазою від 0° до -90°.
