---
id: emb-elee-0065
title: "Що означає від’ємний кут імпедансу кола?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-rc-phase
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
  - source_id: aac-power-factor-angle
    title: "All About Circuits: Calculating Power Factor"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/calculating-power-factor/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Від’ємний кут імпедансу означає, що в усталеному синусоїдальному режимі коло має сумарно ємнісний характер. Струм випереджає напругу на величину цього кута за модулем; для ідеального конденсатора випередження становить 90°.[^aac-power-factor-angle] [^aac-rc-phase]

## Detailed explanation

В усталеному синусоїдальному режимі на одній частоті імпеданс є комплексним відношенням фазорів напруги та струму, `Z = V/I`; його кут показує фазовий зсув напруги відносно струму. Від’ємний кут тому означає, що напруга відстає від струму, або рівнозначно – струм випереджає напругу.[^aac-rc-phase]

Для пасивних ідеальних елементів резистор має нульовий кут, котушка – додатний, а конденсатор – від’ємний. У комбінації R, L і C знак кута описує сумарну реакцію на заданій частоті: індуктивна та ємнісна складові можуть частково компенсувати одна одну. Це не означає, що в колі обов’язково є лише конденсатор, і не означає від’ємний опір; від’ємний кут лише показує, що коло загалом ємнісніше, ніж індуктивне.[^aac-power-factor-angle]

Наприклад, для послідовного RC-кола `Z = R - j*X_C`. Якщо `R = 3 Ω` і `X_C = 4 Ω`, то `Z = 3 - j4 Ω`, його модуль дорівнює `5 Ω`, а кут приблизно `-53.13°`. Отже, для напруги джерела з фазою `0°` струм має фазу приблизно `+53.13°`. У реальному колі паразитні параметри та зміна частоти можуть змінити знак або величину кута, тому висновок стосується виміряного чи розрахованого імпедансу саме в заданих умовах.[^aac-rc-phase]

**Типові помилки:**

- Вважати від’ємний кут негативним опором, хоча він указує на фазове співвідношення.
- Міняти місцями фазу струму й напруги: `angle(I) = angle(V) - angle(Z)`.
- Називати будь-яке коло з конденсатором ємнісним, не врахувавши індуктивність і частоту.[^aac-rc-phase]
