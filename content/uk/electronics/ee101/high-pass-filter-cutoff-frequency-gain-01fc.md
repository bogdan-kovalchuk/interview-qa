---
id: emb-elee-0119
title: "RL-ФВЧ: R = 1 kΩ, L = 2.2 mH. Які частота зрізу та коефіцієнт передавання на 0.1 f_c, f_c і 10 f_c?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Для ідеального RL-ФВЧ із виходом на котушці `f_c = R/(2π*L) ≈ 72.3 kHz` за R = 1 kΩ і L = 2.2 mH. На `0.1 f_c`, `f_c` і `10 f_c` модуль передавання становить відповідно 0.0995, 0.707 і 0.995; фаза дорівнює приблизно +84.3°, +45° і +5.7°.[^aac-high-pass-filters]

## Detailed explanation

Для ідеального RL-ФВЧ із послідовним R та котушкою від виходу до спільного проводу частота зрізу дорівнює `f_c = R/(2π*L)`. На цій частоті модуль напруги на котушці становить приблизно 70.7 % від високочастотного рівня. Передавальна функція `H(jω) = jωL/(R + jωL)` показує, чому схема пропускає високі частоти: реактивний опір котушки зростає з частотою, тому дедалі менша частка сигналу губиться на послідовному R.[^aac-high-pass-filters]

Приклад розрахунку для заданих компонентів:

```text
R = 1000 Ω
L = 2.2 mH = 0.0022 H
f_c = R/(2π*L) ≈ 72.3 kHz
```

Позначимо відношення частоти до зрізу як `x = f/f_c`. Тоді модуль передавання дорівнює `|H| = x/sqrt(1 + x²)`, а фаза – `atan(1/x)`. Для `x = 0.1` маємо близько 0.0995 та +84.3°: котушка майже замикає вихід на спільний провід. При `x = 1` отримуємо 0.707 та +45°. Для `x = 10` маємо близько 0.995 та +5.7°, тобто сигнал майже проходить без ослаблення й фазового зсуву. Коефіцієнт тут задано як відношення вихідної напруги до вхідної; це не потужність.[^aac-high-pass-filters]

Ці числа передбачають ідеальні R та L, малий опір джерела й відсутність навантаження, яке змінює еквівалентний опір. У практичному колі наступний каскад може шунтувати котушку; опір обмотки також змінює низькочастотний рівень. Перевірте схему й точку вимірювання перед підстановкою номіналів. Поширена помилка – використати цю ж формулу для ФНЧ: для ФНЧ вихід знімають на резисторі, а не на котушці.[^aac-high-pass-filters]
