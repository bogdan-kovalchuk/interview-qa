---
id: emb-elinteg-0047
title: "Як оцінити граничну тактову частоту обчислювального блоку за затримкою поширення суматора?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Період тактового сигналу системи повинен перевищувати сумарний найгірший час поширення сигналу через суматор плюс час встановлення наступного регістра. Наприклад, якщо затримка додавання двох 8-бітних слів становить 20 нс, період такту має бути не меншим за 20–25 нс. Це обмежує граничну частоту роботи однотактового арифметичного тракту величиною близько 40–50 МГц.[^udemy-electronics-course]

## Detailed explanation

TODO
