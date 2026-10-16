---
id: emb-elcirc-0009
title: "Як вибрати потужність резистора після розрахунку розсіювання?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-resistor-power
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
  - source_id: vishay-resistor-derating
    title: "Vishay Sfernice: Power Dissipation Considerations in High Precision Thin Film Chips Resistors and Arrays"
    url: https://www.vishay.com/doc/?53047=
---

## Short answer

Розсіювану потужність резистора обчислюють як `P = V*I`, або через `I` чи `V` та опір; вибрана номінальна потужність має бути не нижчою за розрахункову й відповідати умовам охолодження та температурі.[^aac-resistor-power] Універсального правила про запас саме `2×` немає – перевіряйте derating у datasheet конкретної деталі.[^vishay-resistor-derating]

## Detailed explanation

Номінальна потужність резистора описує, скільки тепла він може розсіювати за визначених виробником умов, не перегріваючись. Електрична потужність на резисторі дорівнює `P = V*I`; для омічного резистора з закону Ома також випливають `P = I^2*R` та `P = V^2/R`. У формулах `V` і `I` мають стосуватися саме напруги на резисторі та струму через нього.[^aac-resistor-power]

Після обчислення робочої потужності обирають доступний номінал, який її витримує з урахуванням реальної температури довкілля, монтажу, повітряного потоку та умов, за яких виробник задав рейтинг. Datasheet часто вимагає зменшувати допустиме навантаження зі зростанням температури; тому назва «резистор на 0.25 W» сама по собі не гарантує можливість постійно розсіювати `0.25 W` у будь-якому корпусі чи середовищі.[^vishay-resistor-derating]

Приклад: резистор `100 Ω` із напругою `5 V` на ньому розсіює `P = V^2/R = 25/100 = 0.25 W`. Номінал `0.25 W` не має запасу на підвищену температуру або відхилення режиму; вибір більшого стандартного рейтингу може бути доречним, але конкретний запас визначають за datasheet і вимогами надійності. Для імпульсного режиму треба також перевірити імпульсну енергетичну здатність, а для високої напруги – допустиму робочу напругу, адже обмеження за напругою може спрацювати раніше за потужність.[^aac-resistor-power] [^vishay-resistor-derating]

**Типові помилки:**
- Вважати правило «взяти рівно вдвічі більший рейтинг» обов’язковим для всіх резисторів.
- Порівнювати з номіналом потужність, обчислену не для напруги й струму саме цього компонента.
- Ігнорувати temperature derating, імпульсний режим або допустиму робочу напругу.[^vishay-resistor-derating]
