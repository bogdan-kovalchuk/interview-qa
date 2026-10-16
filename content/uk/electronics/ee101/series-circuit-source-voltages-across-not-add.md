---
id: emb-elee-0064
title: "Послідовне RC-коло: R = 100 Ω, X_C = 75 Ω, джерело 10 V RMS. Чому напруги на R і C (8 V і 6 V) не дають у сумі 14 V?"
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
  - source_id: aac-series-rc
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
---

## Short answer

За заданих `R = 100 Ω` і `X_C = 75 Ω` імпеданс кола дорівнює `Z = 100 - j75 Ω`, його модуль – `125 Ω`, а кут – приблизно `-36.87°`. За джерела `10 V RMS` струм має модуль `0.08 A`; напруги `8 V` на R і `6 V` на C взаємно зсунуті на 90°, тому їхня фазорна сума має модуль `10 V`, а не `14 V`.[^aac-series-rc]

## Detailed explanation

У послідовному RC-колі миттєві напруги на резисторі й конденсаторі не досягають максимуму одночасно, тому їхні RMS-модулі не можна додавати як скаляри. Напруга на резисторі синфазна зі струмом, а напруга на ідеальному конденсаторі відстає від струму на 90°. Отже, ці два напругові фазори взаємно перпендикулярні.[^aac-series-rc]

Для наведених номіналів `Z = R - jX_C = 100 - j75 Ω`. Його модуль дорівнює `sqrt(100² + 75²) = 125 Ω`, тому струм становить `10/125 = 0.08 A RMS`. Напруга на резисторі дорівнює `I*R = 8 V RMS`, а на конденсаторі – `I*X_C = 6 V RMS`. Квадратурне додавання дає `sqrt(8² + 6²) = 10 V RMS`, що узгоджується з напругою джерела.[^aac-series-rc]

Такий результат є наслідком фазорного закону Кірхгофа: миттєві напруги за будь-якої миті алгебраїчно узгоджуються з напругою джерела, а в синусоїдальному усталеному режимі для обчислень використовують комплексні фазори. Резистивна й ємнісна складові мають різні фазові кути, тому модуль їхньої суми не дорівнює сумі модулів. Для інших реактивних елементів напрямок фазора буде іншим, але правило комплексного додавання лишається тим самим.[^aac-series-rc]

У полярній формі імпеданс має кут близько `-36.87°`, отже за напруги джерела з фазою `0°` струм має кут `+36.87°`, бо `I = V/Z`. Це дає незалежну перевірку фазового співвідношення: струм випереджає напругу в ємнісному послідовному колі.[^aac-series-rc]

**Типова помилка:** скласти `8 V + 6 V` і зробити висновок, що джерело має напругу `14 V`. Так додають тільки фазори з однаковим кутом; для компонентів із різними фазами спочатку треба подати напруги в комплексній формі, скласти їх, а вже тоді знайти модуль результату.[^aac-series-rc]
