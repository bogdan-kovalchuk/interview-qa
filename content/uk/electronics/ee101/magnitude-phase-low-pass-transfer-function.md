---
id: emb-elee-0091
title: "Які модуль і фаза передавальної функції RC-ФНЧ?"
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

Для пасивного RC-ФНЧ без суттєвого навантаження `H(f) = 1/(1 + j*f/f_c)`, де `f_c = 1/(2*pi*R*C)`. Тоді `|H| = 1/sqrt(1 + (f/f_c)^2)`, а фаза виходу відносно входу дорівнює `-atan(f/f_c)`: на зрізі модуль становить `1/sqrt(2)` від низькочастотного значення, а фаза дорівнює `-45°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

Передавальна функція описує, як лінійне коло змінює синусоїдальний сигнал залежно від частоти. Для звичайного RC-ФНЧ резистор стоїть послідовно з входом, конденсатор з’єднаний із вихідним вузлом на землю, а вихід знімають із конденсатора. Його імпеданс зменшується зі зростанням частоти, тому більша частина високочастотної напруги падає на резистор. За ідеальних компонентів і ненавантаженого виходу подільник дає `H(f) = 1/(1 + j*f/f_c)`, де `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-transfer]

Модуль `|H|` задає відношення амплітуд виходу й входу, а аргумент комплексного числа `H` задає фазове відставання. На низьких частотах конденсатор має великий імпеданс, тому сигнал майже проходить без зміни амплітуди й фази. Зі зростанням частоти модуль плавно спадає, а фаза переходить від приблизно нуля до `-90°`. На `f_c` модуль дорівнює `1/sqrt(2)` від смугового рівня, що відповідає приблизно `-3 dB`, а фаза становить `-45°`.[^aac-rc-low-pass-transfer]

Наприклад, якщо `R = 1 kΩ` і `C = 159 nF`, то частота зрізу близька до `1 kHz`. На цій частоті вихідна амплітуда буде близько 70.7% вхідної. Це не означає, що компонент «відсікає» всі частоти вище зрізу: характеристика безперервна. Під’єднане навантаження, опір джерела та паразитні параметри змінюють реальну передавальну функцію, тож прості формули застосовні, коли ці впливи малі або враховані окремо.[^aac-rc-low-pass-transfer]

**Типові помилки:**
- Плутати частоту в герцах `f` з кутовою частотою `ω = 2*pi*f`.
- Називати `f_c` межею, за якою сигнал зникає.
- Забувати, що фаза відноситься до виходу щодо входу та має від’ємний знак.
