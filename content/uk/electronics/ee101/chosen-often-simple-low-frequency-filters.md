---
id: emb-elee-0116
title: "Чому для простих низькочастотних фільтрів частіше обирають RC, а не RL?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Для ідеального RL-ФНЧ зі зрізом 1 kHz і R = 1 kΩ потрібна L ≈ 159 mH. У багатьох малопотужних сигнальних колах RC-фільтр простіший і компактніший, бо котушка такої індуктивності може мати значні габарити, ціну та опір обмотки. Це практична перевага, а не заборона RL-фільтрів: вони доречні, коли важливі малий послідовний опір і робота зі значним струмом.[^aac-low-pass-filters]

## Detailed explanation

Для ідеального RL-ФНЧ `f_c = R/(2π*L)`, тому за фіксованих опору та бажаної частоти зрізу потрібна індуктивність зростає обернено до частоти. При низьких частотах це може означати котушку з великою кількістю витків або більшим осердям. Мідний дріт має опір, осердя має втрати, а взаємне магнітне поле може зв’язувати котушку із сусідніми вузлами; ці ефекти додають розсіювання та ускладнюють передбачення поведінки. Для багатьох простих сигнальних фільтрів резистор і конденсатор тому дешевші та компактніші.[^aac-low-pass-filters]

Приклад розрахунку:

```text
f_c = 1000 Hz
R = 1000 Ω
L = R/(2π*f_c) = 1000/(2π*1000) ≈ 0.159 H = 159 mH
```

Це не означає, що RL завжди гірший. У джерелі живлення чи силовому тракті серійний опір створює небажане падіння напруги та нагрівання, тому дросель може бути кращим за резистивний елемент. Вибір залежить від струму, допустимих втрат, розміру, вартості, частотного діапазону й вимог до джерела; також треба врахувати опір навантаження, який впливає на фактичний зріз. Зручне правило для первинного вибору: RC – для недорогого малопотужного фільтра, RL – коли індуктивність уже потрібна або критично не додавати послідовний опір. Остаточне рішення перевіряють на очікуваних номіналах і навантаженні.[^aac-low-pass-filters]
