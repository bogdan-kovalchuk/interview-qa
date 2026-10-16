---
id: emb-elintro-0112
title: "Як знайти еквівалентний опір двох паралельних резисторів?"
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
  - source_id: aac-simple-parallel-circuits
    title: "All About Circuits: Parallel Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-parallel-circuits/
---

## Short answer

Для двох резисторів, під’єднаних до тих самих двох вузлів, `R_eq = (R_1*R_2)/(R_1+R_2)`. Це значення менше за кожен із резисторів, бо паралельне з’єднання додає шлях для струму.[^aac-simple-parallel-circuits]

## Detailed explanation

Еквівалентний опір паралельної пари – це один опір, який між тими самими двома вузлами споживатиме такий самий сумарний струм за заданої напруги. У паралельному колі напруга на обох резисторах однакова, а загальний струм дорівнює сумі струмів гілок. Підставивши закон Ома для кожної гілки, отримуємо `1/R_eq = 1/R_1 + 1/R_2`; для двох резисторів це можна перетворити на добуток, поділений на суму.[^aac-simple-parallel-circuits]

Формула передбачає, що обидва компоненти є резисторами й підключені саме паралельно – кожен кінець першого з’єднаний з відповідним кінцем другого. Якщо вони мають лише один спільний вузол, їх не можна згорнути цією формулою. Для позитивних скінченних опорів результат менший за менший опір: струм має два паралельні шляхи, тому провідності додаються. Додавання самих опорів, навпаки, стосується послідовного з’єднання.[^aac-simple-parallel-circuits]

Приклад розрахунку:
```text
R_1 = 1 kΩ, R_2 = 2 kΩ
R_eq = (1000*2000)/(1000+2000) = 666.7 Ω
```
Отже, еквівалентний опір приблизно `667 Ω`, що менше за `1 kΩ`.[^aac-simple-parallel-circuits]

**Типові помилки:**
- Застосовувати формулу до резисторів, які не мають обох спільних вузлів.
- Додавати номінали, як для послідовного з’єднання.
- Забувати перевести одиниці в одну систему перед підстановкою.
