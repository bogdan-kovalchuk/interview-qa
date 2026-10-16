---
id: emb-elee-0106
title: "Як зміниться частота зрізу RC-ФНЧ, якщо замінити 100 nF на 1 µF при R = 1 kΩ?"
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
  - source_id: aac-rc-low-pass-cutoff
    title: "All About Circuits: Introduction to Analog Filters"
    url: https://www.allaboutcircuits.com/TEXTBOOK/designing-analog-chips/filters/introduction-to-analog-filters/
---

## Short answer

За незмінного ефективного R частота зрізу зменшиться вдесятеро, приблизно з 1.59 kHz до 159 Hz, оскільки `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-cutoff] Це ідеальний розрахунок без додаткового навантаження.

## Detailed explanation

Частота зрізу однополюсного RC-ФНЧ – це частота, на якій амплітуда виходу дорівнює приблизно 0.707 амплітуди входу, або на 3 dB менша за рівень у смузі пропускання. Для ідеального ненавантаженого каскаду її обчислюють як `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-cutoff]

Якщо R залишається сталим, збільшення C у десять разів збільшує добуток `R*C` у десять разів, тож частота зрізу зменшується в десять разів. Це не означає, що фільтр просто «стає повільнішим» у всіх сенсах: форма нормованої характеристики першого порядку не змінюється, але вся частотна шкала зміщується вниз.

Для заданих `R = 1 kΩ` і `C = 100 nF` маємо приблизно `1591.5 Hz`; для `C = 1 µF` – приблизно `159.2 Hz`. Ці значення округлені, а не є точними частотами для реальних компонентів із допуском. Припускається, що резистор має саме вказаний номінал, конденсатор – номінальну ємність, а опір джерела та навантаження не змінюють ефективний R.

**Типові помилки:**
- Множити частоту на десять разом із ємністю, хоча частота обернено пропорційна `C`.
- Застосовувати формулу до навантаженої схеми, не перевіривши ефективний опір, який бачить конденсатор.

Якщо до виходу під’єднано наступний каскад із скінченним вхідним опором або генератор має помітний вихідний опір, потрібно спершу знайти еквівалентну мережу опорів. Тоді простий розрахунок із заданими номіналами може не передбачити виміряну частоту зрізу.
