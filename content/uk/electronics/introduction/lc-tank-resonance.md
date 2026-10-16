---
id: emb-elintro-0144
title: "Що таке резонанс LC-контуру?"
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
---

## Short answer

На ідеальній резонансній частоті `f_0 = 1/(2*pi*sqrt(L*C))` реактивні опори індуктора й конденсатора зрівнюються. У послідовному контурі імпеданс мінімальний, а в паралельному – максимальний; реальні втрати обмежують ці екстремуми.[^aac-semiconductors]

## Detailed explanation

Резонанс LC-контуру виникає на частоті, де індуктивний і ємнісний реактивні опори однакові за модулем. У моделі ідеальних компонентів ця частота дорівнює `f_0 = 1/(2*pi*sqrt(L*C))`; енергія періодично переходить між магнітним полем індуктора та електричним полем конденсатора.[^aac-semiconductors]

Причину резонансу видно з частотної залежності: `X_L = 2*pi*f*L` зростає з частотою, тоді як `X_C = 1/(2*pi*f*C)` спадає. Є частота, де вони зрівнюються, і їхні реактивні впливи взаємно компенсуються на вході контуру. Для `L = 100 mH` та `C = 10 µF` ідеальна формула дає приблизно `159 Hz`.[^aac-semiconductors]

Те, що вимірює джерело, залежить від з’єднання. У послідовному LC-контурі загальний імпеданс ідеалізовано прямує до нуля на резонансі; у паралельному контурі вхідний імпеданс ідеалізовано прямує до нескінченності. Реальні втрати обмежують ці екстремуми, а паразитні опори та ємності можуть зсувати спостережуваний пік або провал.[^aac-semiconductors]

**Типова помилка:** називати імпеданс «мінімальним» для будь-якого LC-контуру. Це твердження стосується послідовного випадку; для паралельного tank-контуру на резонансі імпеданс максимальний. Формула ідеальної частоти є корисним стартовим розрахунком, але для реальної схеми важливі втрати, навантаження й паразитні параметри.[^aac-semiconductors]
