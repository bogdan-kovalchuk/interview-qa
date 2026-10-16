---
id: emb-elintro-0005
title: Яка функція котушки індуктивності?
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
  - source_id: aac-inductor
    title: "All About Circuits: AC inductor circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  - source_id: aac-inductor-calculus
    title: "All About Circuits: Inductor voltage and current relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
  - source_id: aac-inductor-practical
    title: "All About Circuits: Practical considerations for inductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/practical-considerations-inductors/
---

## Short answer

Індуктивність запасає енергію магнітного поля й протидіє змінам струму. Для ідеальної індуктивності `v = L*di/dt`; sinusoidal reactance дорівнює `X_L = 2π*f*L` і зростає з частотою в межах придатності моделі. Реальна обмотка також має опір та parasitic ефекти. [^aac-inductor]

## Detailed explanation

Зміна струму створює напругу на індуктивності. За прикладеної напруги струм змінюється зі швидкістю, визначеною inductance; компонент загалом не блокує весь струм. За ідеального усталеного DC струм сталий, тому inductive voltage дорівнює нулю. Реальна обмотка все одно дає resistive voltage drop. [^aac-inductor] [^aac-inductor-calculus]

У розрахунковому sinusoidal прикладі 10 mH при 1 kHz мають `X_L = 2π*1000*0.01 ≈ 62.8 Ω`. Це reactance, а не опір розсіювання; при поєднанні з іншими імпедансами потрібно враховувати phase. Запасена магнітна енергія в ідеальній лінійній моделі – `E = L*I²/2`.

Індуктивності корисні у filters і switching converters, оскільки утримують енергію під час зміни струму. Розрив шляху зі струмом індуктивності може створити велику напругу, тому важливий відповідний discharge або clamp path. Не поширюйте просте правило зростання reactance за межі self-resonant region компонента: parasitic capacitance, winding loss і core saturation можуть зробити ідеальну модель непридатною. [^aac-inductor-practical] [^aac-inductor-calculus]
