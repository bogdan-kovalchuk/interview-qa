---
id: emb-elee-0118
title: "Як побудований RL-фільтр високих частот?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Резистор увімкнено послідовно з джерелом, котушку – від вихідного вузла до спільного проводу, а вихід знімають із вузла, паралельно котушці. На DC імпеданс ідеальної котушки дорівнює нулю, а зі зростанням частоти збільшується, тож вихід наближається до входу.[^aac-high-pass-filters]

## Detailed explanation

RL-ФВЧ можна побудувати з резистора, увімкненого послідовно з джерелом, і котушки, з’єднаної від вихідного вузла до спільного проводу; вихід знімають із вузла, тобто паралельно котушці. На низькій частоті імпеданс L малий, тому котушка відводить сигнал до спільного проводу. На високій частоті її імпеданс більший, тож вихід наближається до вхідної напруги.[^aac-high-pass-filters]

Якщо навантаженням є сам вхід наступного каскаду і його впливом можна знехтувати, ідеальна передавальна функція має вигляд `H(jω) = jωL/(R + jωL)`. Модуль зростає від нуля на DC до одиниці на високих частотах; на частоті `f_c = R/(2π*L)` він дорівнює приблизно 0.707 від високочастотного рівня. Реальне навантаження паралельно котушці змінює еквівалентний опір і характеристику, тож формула з одним R не є універсальною для будь-якого підключення.[^aac-high-pass-filters]

Приклад: якщо `R = 1 kΩ` і `L = 2.2 mH`, то `f_c ≈ 72.3 kHz`. Нижче зрізу амплітуда зростає приблизно пропорційно частоті, а значно вище зрізу вихід наближається до входу. Не плутайте цю схему з RL-ФНЧ: там котушка стоїть послідовно в сигнальному шляху, а вихід беруть на резисторі. У реальній котушці опір обмотки й паразитні параметри змінюють низькочастотне передавання та верхню межу корисного діапазону.[^aac-high-pass-filters]
