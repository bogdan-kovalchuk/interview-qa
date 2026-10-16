---
id: emb-elintro-0262
title: "Чому P-channel MOSFET зазвичай має більший `R_DS(on)`, ніж N-channel?"
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
  - source_id: infineon-mosfet-overview
    title: "Infineon: What Is a MOSFET?"
    url: https://www.infineon.com/technology/mosfets
---

## Short answer

У P-channel основні носії заряду – дірки, рухливість яких нижча за рухливість електронів у N-channel. За однакової площі кристала це зазвичай дає P-channel більший `R_DS(on)`, хоча фактичне значення залежить від конструкції транзистора та умов вимірювання.[^infineon-mosfet-overview]

## Detailed explanation

У MOSFET струм каналу переноситься носіями заряду, які формує напруга gate-source. У N-channel основними носіями є електрони, а в P-channel – дірки. У кремнієвих пристроях електрони мають вищу рухливість, тому за порівнюваної геометрії їм легше забезпечити той самий струм каналу з меншими втратами.[^infineon-mosfet-overview]

Цей фізичний чинник пояснює тенденцію, а не гарантує співвідношення для кожної пари деталей. За однакової площі кристала P-channel зазвичай має більший `R_DS(on)`. Щоб отримати близький опір, виробнику доводиться збільшувати активну площу кристала; це може збільшити розмір, ємності або вартість корпусованого компонента. У конкретному застосуванні порівнюйте datasheet за однаковими `V_GS`, температурою переходу й струмом, бо опір увімкненого каналу змінюється з умовами керування і нагріванням.[^infineon-mosfet-overview]

Приклад: якщо два компоненти мають однакові корпус і напругу gate, але один має `R_DS(on)` 40 мОм, а інший 80 мОм, при 2 A втрати провідності за формулою `P = I²*R` становитимуть відповідно 0.16 W і 0.32 W. Це ілюстрація впливу опору, а не універсальна пара значень для N-channel та P-channel. Вища ефективність N-channel часто робить його привабливим для силових ключів, але P-channel може спростити high-side керування без окремого драйвера, коли його source під’єднаний до позитивної шини.[^infineon-mosfet-overview]

Типова помилка – вважати, що тип каналу сам по собі визначає кращий вибір. Спершу визначте топологію та доступний рівень керування, далі перевірте `R_DS(on)` саме при вашому `V_GS`, допустимі напругу й струм, тепловий режим і заряд gate. Порогова напруга `V_GS(th)` лише позначає початок провідності за тестових умов datasheet; вона не обов’язково означає, що транзистор повністю відкритий для розрахункового навантаження.[^infineon-mosfet-overview]
