---
id: emb-elinteg-0012
title: "Чому не можна обмежувати струм семисегментного індикатора одним загальним резистором в аноді?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Якщо встановити один резистор у спільному аноді, сумарний струм розподілятиметься між усіма увімкненими сегментами. При відображенні цифри 1 струм ділиться між двома сегментами, а при цифрі 8 – між сімома, через що яскравість цифри 8 буде в рази меншою. Правильна схемотехніка вимагає встановлення окремого струмообмежувального резистора для кожного сегмента.[^udemy-electronics-course]

## Detailed explanation

TODO
