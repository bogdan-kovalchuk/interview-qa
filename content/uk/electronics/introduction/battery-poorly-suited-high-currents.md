---
id: emb-elintro-0075
title: "Чому 9V крона погано підходить для великих струмів?"
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
  - source_id: energizer-522-datasheet
    title: "Energizer 522 9V Alkaline Battery Product Datasheet"
    url: https://data.energizer.com/pdfs/522_ap.pdf
---

## Short answer

У крони мала ємність і відносно великий внутрішній опір. Без навантаження вона може показувати `9 В`, але при струмі двигуна або потужного LED напруга швидко просідає.[^energizer-522-datasheet]

## Detailed explanation

Напис `9 V` позначає номінальну напругу, а не здатність віддавати будь-який струм, зберігаючи цю напругу. Реальна батарея має внутрішній опір і хімічні процеси з обмеженою швидкістю. Коли навантаження бере струм, внутрішній опір створює спад напруги, а поляризація елементів може додатково зменшити клемну напругу. Високий струм також швидше витрачає доступну ємність і збільшує нагрівання.[^aac-direct-current]

Порівнювати треба конкретні режими розряду з документації, а не лише напругу на етикетці. Наприклад, datasheet лужної Energizer 522 наводить криві для навантажень із резисторами `270 Ω` та `620 Ω` і вимірює розряд до кінцевої напруги `4.8 V` за `21 °C`; він не встановлює універсальної характеристики для всіх 9 V батарей чи всіх навантажень.[^energizer-522-datasheet]

Приклад: навантаження `100 Ω`, підключене до ідеального джерела `9 V`, споживало б `90 mA` за законом Ома. У реальній батареї напруга на навантаженні буде нижчою, отже струм і потужність також відрізнятимуться; точний результат потребує її розрядної кривої або вимірювання. Для двигуна важливий також пусковий струм, який може бути значно вищий за усталений.

**Типова помилка:** судити про придатність за напругою без навантаження. Треба перевірити розрядну криву для потрібного струму, а також допустиму температуру, час роботи й вимоги самого пристрою.[^aac-direct-current]
