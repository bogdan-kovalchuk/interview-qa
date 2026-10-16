---
id: emb-elintro-0271
title: "Для чого потрібен логічний аналізатор?"
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
  - source_id: tek-oscilloscope-types
    title: "Tektronix: Oscilloscope Types"
    url: https://www.tek.com/en/documents/primer/oscilloscope-types
---

## Short answer

Він записує багато цифрових каналів одночасно і декодує протоколи, наприклад `I²C`, `SPI`, `UART`. Це зручно, коли важлива послідовність логічних подій, а не аналогова форма сигналу.[^tek-oscilloscope-types]

## Detailed explanation

Логічний аналізатор захоплює багато цифрових входів і показує їхні логічні рівні та переходи в часі. Він порівнює кожен відлік із заданим порогом і класифікує його як high або low, тому на екрані переважно видно стани й переходи, а не точну амплітуду чи форму фронту. Поріг потрібно налаштувати відповідно до рівнів досліджуваної логічної сім’ї: хибне значення може спричинити помилкове розпізнавання бітів.[^tek-oscilloscope-types]

Захоплення кількох ліній одночасно показує часовий порядок подій. Наприклад, можна перевірити, чи з’явився сигнал вибору пристрою до тактових імпульсів SPI, чи є підтвердження після байта I²C, або скільки триває імпульс мікроконтролера. Якщо прилад підтримує декодер потрібного протоколу, він групує біти у поля та показує їхні значення. Якість декодування залежить від частоти дискретизації, глибини пам’яті, налаштованого порога та правильного підключення пробників.[^tek-oscilloscope-types]

Для аналізу аналогової поведінки цифрової лінії – дзвону, overshoot, повільного фронту чи просідання рівня – потрібен осцилографічний вхід. Логічний аналізатор може виявити помилковий перехід, але не покаже форму напруги, яка його спричинила. Якщо декодер показує неправильний байт UART, перевіряють baud rate, полярність і поріг, а потім зіставляють цифрові стани з аналоговою формою сигналу.

**Типові помилки:**

- Вважати, що логічний аналізатор вимірює точну напругу або якість фронту.
- Покладатися на декодер без перевірки параметрів захоплення.
- Ігнорувати допустимі рівні входів і правильне підключення землі.
