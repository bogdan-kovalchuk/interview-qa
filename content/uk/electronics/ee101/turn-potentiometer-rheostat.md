---
id: emb-elee-0015
title: "Як перетворити потенціометр на реостат?"
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
  - source_id: aac-potentiometer-rheostat
    title: "All About Circuits: DC Lab - Potentiometer as a Rheostat"
    url: https://www.allaboutcircuits.com/TEXTBOOK/experiments/chpt-3/potentiometer-rheostat/
---

## Short answer

З’єднайте wiper з одним із крайніх виводів, а зовнішнє коло підключіть до цієї пари: так потенціометр працює як двовивідний змінний резистор. Його опір змінюється приблизно від нуля до `R_total`, а в послідовному колі ним можна регулювати струм; фактичні межі залежать від контактного опору й конструкції компонента.[^aac-potentiometer-rheostat]

## Detailed explanation

Потенціометр має резистивну доріжку між двома крайніми виводами та рухомий контакт – wiper. Коли зовнішнє коло під’єднане між wiper і одним краєм доріжки, струм проходить лише через частину доріжки. Переміщення wiper змінює довжину цієї частини, а отже й опір; вивід на протилежному краї можна не використовувати. Інший край дає протилежний напрямок зміни опору при тому самому обертанні ручки.[^aac-potentiometer-rheostat]

В ідеалізованій моделі опір дорівнює майже нулю біля вибраного краю й наближається до повного опору доріжки на протилежному краї. Це не означає, що компонент може безпечно керувати будь-яким струмом: важливі його номінальна потужність, граничний струм, охолодження та допустима напруга. Для навантаження з великим струмом малий опір доріжки може розсіювати значну потужність; розрахуйте `P = I²*R` і звірте результат із паспортом конкретної деталі.[^aac-potentiometer-rheostat]

Приклад: якщо доріжка має 10 kΩ, а положення wiper залишає приблизно 25 % її довжини до вибраного краю, опір між цими контактами становить близько 2.5 kΩ для рівномірної доріжки. Це оцінка положення, а не точний калібрований закон: допуски й форма доріжки можуть бути лінійними або логарифмічними. Реостат зазвичай вмикають послідовно, щоб змінити струм або падіння напруги на навантаженні; він сам по собі не стабілізує струм.[^aac-potentiometer-rheostat]

**Типова помилка:** використовувати два крайні виводи без wiper і очікувати змінного опору. Між ними опір доріжки сталий, незалежно від положення ручки. У схемах, де короткий обрив контакту wiper є небезпечним, можна з’єднати невикористаний край з wiper: якщо рухомий контакт тимчасово втратить доріжку, лишиться шлях через усю доріжку. Це захист від одного режиму відмови, а не заміна перевірки надійності компонента.[^aac-potentiometer-rheostat]
