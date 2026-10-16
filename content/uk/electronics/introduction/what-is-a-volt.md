---
id: emb-elintro-0023
title: "Що таке вольт?"
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
  - source_id: nist-sp330-section2
    title: "NIST Special Publication 330: The International System of Units, Section 2"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-2
---

## Short answer

Вольт (V) – одиниця різниці електричних потенціалів; `1 V = 1 J/C`. Він показує, скільки енергії припадає на одиницю перенесеного заряду між двома точками.[^nist-sp330-section2]

## Detailed explanation

Напруга між двома точками описує зміну електричної потенціальної енергії на одиницю заряду. Один вольт дорівнює одному джоулю на кулон: `V = E/Q`.[^nist-sp330-section2]

Напруга завжди задається між двома точками, а не «в одній точці». Її полярність залежить від того, у якому порядку вибрано точки вимірювання. Джерело створює різницю потенціалів, а замкнений шлях і властивості компонентів визначають струм; сама напруга не гарантує певного струму.[^aac-direct-current]

Аналогія з тиском іноді допомагає уявити роль напруги в колі, але не є визначенням і не замінює закони кола. Зокрема, струм залежить також від навантаження та його режиму, наприклад від опору в простому резистивному колі.[^aac-direct-current]

Знак напруги залежить від обраного порядку точок: якщо поміняти щупи вольтметра місцями, знак показу зміниться, хоча фізична різниця потенціалів між тими самими точками не зникне. Тому в схемі варто позначати опорний вузол і полярність вимірювання. Це особливо важливо, коли порівнюють кілька напруг або перевіряють падіння напруги на компоненті.[^aac-direct-current]

**Приклад:** якщо заряд `2 C` отримує `6 J` енергії під час переміщення між точками, різниця потенціалів дорівнює `V = E/Q = 6 J/2 C = 3 V`.
