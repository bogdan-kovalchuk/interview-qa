---
id: emb-elintro-0057
title: "Що таке внутрішній опір батареї і як він впливає на напругу?"
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
  - source_id: libretexts-real-batteries
    title: "Physics LibreTexts: 6.5 Real Batteries"
    url: https://phys.libretexts.org/Courses/Kettering_University/Electricity_and_Magnetism_with_Applications_to_Amateur_Radio_and_Wireless_Technology/06:_Direct-Current_(DC)_Resistor_Circuits/6.05:_Real_Batteries
---

## Short answer

Внутрішній опір моделює втрати всередині батареї: під час розряду напруга на клемах приблизно дорівнює `V_term = E - I*r`. Що більший струм або внутрішній опір, то більша внутрішня втрата напруги; конкретні значення залежать від батареї та умов.[^libretexts-real-batteries]

## Detailed explanation

Внутрішній опір – це зручна модель сукупних електричних втрат усередині реального джерела. У простій схемі батарею подають як ідеальне джерело електрорушійної сили `E` послідовно з опором `r`. Коли зовнішнє коло споживає струм `I`, частина напруги витрачається всередині батареї, а на її клемах залишається приблизно `V_term = E - I*r`.[^libretexts-real-batteries]

За відсутності навантаження струм майже нульовий, тож падіння `I*r` мале і виміряна напруга наближається до напруги холостого ходу. Коли навантаження вимагає більшого струму, падіння на внутрішньому опорі зростає. Частина хімічної енергії перетворюється на тепло всередині елемента; за значного внутрішнього опору це також зменшує напругу й потужність, доступні навантаженню.[^libretexts-real-batteries]

Наприклад, якщо еквівалентне джерело має `E = 1.5 V`, а під час роботи через нього йде `I = 0.1 A`, то за `r = 2 Ω` модель передбачає внутрішнє падіння `0.1*2 = 0.2 V` і напругу на клемах близько 1.3 В. Це лише приклад моделі, а не універсальне значення для елемента AA. Реальні батареї не є незмінним резистором: їхня поведінка залежить від хімії, температури, рівня заряду, віку та тривалості навантаження.[^libretexts-real-batteries]

**Типова помилка:** вважати, що батарея з номіналом 1.5 В завжди підтримує рівно 1.5 В на клемах. Номінальна напруга не скасовує просідання під навантаженням; оцінюйте її для конкретного струму й умов.
