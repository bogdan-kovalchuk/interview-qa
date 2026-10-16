---
id: emb-elintro-0014
title: Як правильно підключити мультиметр для вимірювання струму?
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
  - source_id: fluke-meter
    title: "Fluke 3000 FC Users Manual"
    url: https://media.fluke.com/437e18a0-de4d-4090-ab8a-b0df016de4fd_original%20file.pdf
---

## Short answer

Вимкніть живлення кола, виберіть правильні current function, rated input jack і range, потім розімкніть гілку та ввімкніть meter послідовно. Відновлюйте живлення лише після підключення; перед від’єднанням знову його вимкніть. Ніколи не підключайте meter у current mode безпосередньо паралельно voltage source. [^fluke-meter]

## Detailed explanation

Current measurement пропускає струм гілки через внутрішній current-measurement path мультиметра. Тому meter потрібно ввімкнути послідовно саме в гілку, яку вимірюють. Натомість voltage measurement підключає high-impedance input між двома вузлами. Плутанина цих підключень може замкнути source через current input. [^fluke-meter]

Процедура Fluke явно вимагає вимкнути живлення, розімкнути коло, підключити послідовно й потім відновити живлення. Оберіть AC чи DC за потребою та function, terminal і range з rating для очікуваного струму. Не припускайте, що кожен meter має input 10 A: згаданий 3000 FC має specified mA measurement ranges. Межі визначає manual фактичного meter. [^fluke-meter]

Вставлений meter може змінити коло через burden voltage; виміряний струм не обов’язково точно дорівнює початковому струму без приладу. Після вимірювання вимкніть живлення перед відновленням кола та поверніть lead у voltage/resistance jack для цих функцій. Перед наступним вимірюванням перевірте wiring та input rating.
