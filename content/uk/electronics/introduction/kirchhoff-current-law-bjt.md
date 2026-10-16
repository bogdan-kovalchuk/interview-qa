---
id: emb-elintro-0199
title: "Закон Кірхгофа для струмів `BJT`?"
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
---

## Short answer

За законом Кірхгофа в кожному вузлі сума струмів, що входять, дорівнює сумі струмів, що виходять. Для звичайного режиму BJT за узгоджених напрямків струмів це дає `I_E = I_C + I_B`; наближення `I_E ≈ I_C` допустиме лише коли `I_B` справді малий порівняно з `I_C`.[^aac-semiconductors]

## Detailed explanation

Закон Кірхгофа для струмів (KCL) є наслідком збереження електричного заряду: заряд не накопичується нескінченно у вузлі, тому алгебрична сума струмів у ньому дорівнює нулю. Для трьох виводів транзистора це співвідношення пов’язує струм емітера, колектора та бази.[^aac-semiconductors]

Якщо умовно вважати струм емітера таким, що входить у транзистор, а струми бази й колектора такими, що виходять, отримаємо `I_E = I_B + I_C`. Для NPN і PNP фізичні напрямки струмів різні; рівняння лишається коректним за послідовно вибраних знаків і напрямків. Не слід механічно підставляти модулі струмів, якщо обрана система знаків передбачає інші напрями.[^aac-semiconductors]

Оскільки в багатьох режимах `I_B` набагато менший за `I_C`, для грубої оцінки можна прийняти `I_E ≈ I_C`. Але ця апроксимація має похибку приблизно на величину частки базового струму. Для точного балансу потужності, вимірювання чи розрахунку зміщення базовий струм треба включити.[^aac-semiconductors]

Приклад: якщо `I_B = 0.02 mA`, а `I_C = 2.00 mA`, то за законом вузла `I_E = 2.02 mA`. Наближення дало б 2.00 mA, тобто похибка близько 1% від точного значення емітерного струму. Це припущення, а не інший закон.[^aac-semiconductors]

**Типові помилки:** записувати `I_E = I_C - I_B` при несумісних напрямках; вважати `I_E` рівним `I_C` без застереження; забувати про базовий струм у точному розрахунку.[^aac-semiconductors]
