---
id: emb-elintro-0004
title: Яка функція конденсатора?
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
  - source_id: aac-capacitor
    title: "All About Circuits: Capacitors and calculus"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/capacitors-and-calculus/
  - source_id: nichicon-polarity
    title: "Nichicon: Technical notes for aluminum electrolytic capacitors"
    url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
---

## Short answer

Конденсатор запасає енергію електричного поля та утримує протилежні заряди на електродах. В ідеальній моделі `i = C*dv/dt`: струм протікає під час зміни напруги, але не за сталої DC напруги. Його використовують для filtering, decoupling і coupling змінних сигналів. [^aac-capacitor]

## Detailed explanation

Capacitance пов’язує заряд і напругу через `Q = C*V`; запасена енергія – `E = C*V²/2`. Заряд міститься на електродах, а енергія пов’язана з електричним полем у dielectric. За розрахунком конденсатор 100 nF при 5 V має заряд за модулем 0.5 µC на кожному електроді та запасає 1.25 µJ. [^nichicon-polarity]

«Блокує DC» описує ідеальний усталений стан після заряджання, а не момент підключення DC живлення. Під час заряджання напруга змінюється і протікає струм. Для ідеального конденсатора й sinusoidal signal модуль імпедансу зменшується з частотою; це допомагає coupling та filtering, але не робить будь-який конденсатор коротким замиканням на будь-якій AC частоті. [^aac-capacitor]

Supply decoupling capacitor біля IC локально забезпечує transient current і обмежує зміни напруги живлення. Реальні конденсатори мають leakage, ESR та parasitic inductance, тому важливі розміщення і характеристики компонента. Для polarized capacitor додатково потрібно дотримуватися polarity та voltage limits. [^nichicon-polarity]
