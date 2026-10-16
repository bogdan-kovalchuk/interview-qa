---
id: emb-elintro-0113
title: "Чим `LED` відрізняється від резистора: що відбувається з напругою на ньому при зміні струму?"
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
  - source_id: digikey-rgb-led-forward-voltage
    title: "DigiKey: RGB LEDs Provide Multicolor Display Solutions"
    url: https://www.digikey.com/en/articles/how-to-drive-multicolor-leds
---

## Short answer

На резисторі напруга зростає пропорційно струму, тоді як у `LED` після коліна характеристики струм різко зростає за невеликої зміни прямої напруги `V_f`. Тому `V_f` не є сталою: її беруть із datasheet для потрібного струму й умов, а для початкового розрахунку використовують типове значення.[^digikey-rgb-led-forward-voltage]

## Detailed explanation

Резистор і `LED` мають різні вольт-амперні характеристики. Для ідеального резистора закон Ома дає лінійну залежність `V = I*R`: якщо опір сталий, збільшення струму вдвічі подвоює падіння напруги. `LED` є напівпровідниковим діодом, і після досягнення прямого «коліна» його струм швидко змінюється навіть за невеликої зміни прикладеної напруги.[^digikey-rgb-led-forward-voltage]

Це не означає, що напруга на `LED` абсолютно стала. `V_f` залежить від струму, температури, кольору та конкретної моделі; datasheet зазвичай наводить типове або граничне значення за визначених умов. Для вибору послідовного резистора типове `V_f` допомагає оцінити режим, але перевірка максимального струму має враховувати допуски джерела, розкид параметрів компонента та нагрівання. Значення струму доцільно обмежити резистором або спеціальним драйвером.[^digikey-rgb-led-forward-voltage]

Наприклад, у конкретному RGB-модулі Adafruit 2739 у статті наведено типові значення при `20 mA`: близько `2.0 V` для червоного каналу й `3.2 V` для зеленого та синього. При `15 mA` наведені вже `1.9 V` і `3.1 V`. Це показує, що число змінюється зі струмом і належить певному виробу, а не є універсальним порогом для всіх світлодіодів.[^digikey-rgb-led-forward-voltage]

**Типові помилки:**
- Називати `V_f` фіксованою незалежно від струму.
- Використовувати формулу резистора як доказ того, що `LED` поводиться лінійно.
- Переносити типове `V_f` одного кольору або моделі на будь-який інший `LED`.
