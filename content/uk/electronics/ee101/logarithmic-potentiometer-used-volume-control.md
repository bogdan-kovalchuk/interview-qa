---
id: emb-elee-0014
title: "Чому для регулювання гучності використовують логарифмічний потенціометр?"
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
  - source_id: analog-devices-taper
    title: "Analog Devices: Taper"
    url: https://www.analog.com/en/resources/glossary/logarithmic_linear_taper.html
---

## Short answer

Сприйняття гучності приблизно логарифмічне, тому audio taper змінює рівень сигналу повільніше на нижніх налаштуваннях і швидше на верхніх. Це зазвичай дає плавніше суб’єктивне регулювання, хоча точний результат залежить від кривої потенціометра та аудіосхеми.[^analog-devices-taper]

## Detailed explanation

Логарифмічний потенціометр застосовують для гучності, щоб зміна положення ручки краще відповідала тому, як людина сприймає зміну рівня звуку. Сприйняття не є лінійним: однакова абсолютна зміна амплітуди не відчувається однаково на тихому й гучному рівні. Audio taper формує нелінійну залежність опору від кута, а отже й нелінійну зміну сигналу на виході дільника.[^analog-devices-taper]

У типового audio taper зміна рівня на нижній частині ходу повільніша, що дає точніше налаштування тихого звуку; вище рівень змінюється швидше. Це робить ручку зручнішою для користувача, але не означає, що її механічний кут прямо задає сприйману гучність: на результат впливають навантаження потенціометра, вхідний опір підсилювача, схема включення та акустичні умови.[^analog-devices-taper]

Логарифмічна крива в реальному компоненті є наближенням і може складатися з кількох лінійних ділянок. Тому центральне положення ручки не означає ані половини вихідної напруги, ані половини суб’єктивної гучності. Якщо потрібно точне керування в децибелах або узгоджений stereo tracking, варто перевірити криву конкретної моделі або застосувати активний чи цифровий регулятор.[^analog-devices-taper]

Приклад: у voltage divider потенціометр з лінійним taper дає приблизно пропорційну зміну напруги від кута, тоді як audio taper навмисно змінює це співвідношення, щоб ручка працювала природніше на слух. У реальному аудіоканалі форма кривої буде змінена навантаженням, тому очікувану характеристику перевіряють у схемі.[^analog-devices-taper]

**Типова помилка:** стверджувати, що людське вухо ідеально логарифмічне або що логарифмічний потенціометр гарантує лінійне відчуття гучності. Це практичне наближення, а не точний психоакустичний закон.[^analog-devices-taper]
