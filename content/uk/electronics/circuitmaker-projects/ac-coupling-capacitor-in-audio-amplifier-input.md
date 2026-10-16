---
id: emb-elcmproj-0041
title: "Навіщо між виходом таймера 555 і базою транзистора підсилювача ставлять розділовий конденсатор?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Вихідний сигнал таймера 555 містить велику постійну складову на рівні половини живильної напруги. Розділовий конденсатор ізолює постійний струм, пропускаючи на підсилювач виключно змінний акустичний сигнал звукової частоти. Це захищає підсилювальний транзистор від потрапляння в режим насичення або теплового пробою.[^udemy-electronics-course]

## Detailed explanation

TODO
