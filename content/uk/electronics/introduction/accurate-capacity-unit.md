---
id: emb-elintro-0056
title: "Чому Вт·год краще за мА·год для порівняння запасу енергії батарей?"
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
  - source_id: iata-lithium-guidance-2023
    title: "IATA Lithium Battery Guidance Document 2023"
    url: https://data.energizer.com/wp-content/uploads/2023/04/IATA-Lithium-Guidance-2023.pdf
---

## Short answer

мА·год показує заряд, але не енергію без урахування напруги: номінальна оцінка енергії дорівнює `Ah*V`. Тому батарея 2400 мА·год при 1.2 В має близько 2.88 Вт·год, а 2000 мА·год при 3.7 В – близько 7.4 Вт·год; точна доступна енергія залежить від умов розряду.[^iata-lithium-guidance-2023]

## Detailed explanation

Вт·год точніше описує запас електричної енергії, ніж мА·год, коли порівнюють батареї з різною напругою. Ампер-година є інтегралом струму за часом і вимірює електричний заряд; сама по собі вона не задає роботу, яку може виконати джерело. Для оцінки номінальної енергії заряд множать на номінальну напругу: `E(Wh) = C(Ah)*V(V)`. Щоб перейти від мА·год до А·год, значення ділять на 1000.[^iata-lithium-guidance-2023]

Наприклад, 2400 мА·год – це 2.4 А·год. За номінальної напруги 1.2 В отримуємо `2.4*1.2 = 2.88 Wh`. Елемент на 2000 мА·год при 3.7 В має `2.0*3.7 = 7.4 Wh`: його ємність у мА·год менша, але номінальний запас енергії більший. Такий розрахунок є наближенням: напруга під час розряду змінюється, а паспортна ємність визначається за заданих виробником навантаження, температури й порогової напруги.[^iata-lithium-guidance-2023]

Не слід трактувати Вт·год як гарантію однакового часу роботи в будь-якому пристрої. Перетворювач живлення має втрати, навантаження споживає потужність нерівномірно, а доступний заряд залежить від режиму розряду й граничної напруги. Однак Вт·год краще за мА·год нормалізує порівняння батарей різної номінальної напруги. Для однакової хімії, напруги й умов тесту порівняння мА·год може бути достатнім.

**Типова помилка:** порівнювати лише число мА·год і вважати більшу цифру доказом більшого запасу енергії. Спершу перевірте номінальну напругу й умови, за яких виробник визначив ємність.[^iata-lithium-guidance-2023]
