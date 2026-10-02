---
id: emb-elintro-0005
title: Яка функція котушки індуктивності?
description: Яка функція котушки індуктивності?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-inductor
  title: 'All About Circuits: AC inductor circuits'
  url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  accessed: 2026-10-04
  kind: book
  version: null
  applicability: Ideal inductive reactance and frequency dependence.
- source_id: aac-inductor-calculus
  title: 'All About Circuits: Inductor voltage and current relationship'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
  accessed: '2026-10-04'
  kind: book
  version: null
  applicability: Voltage/current derivative, steady DC and response to opening an inductive current path.
- source_id: aac-inductor-practical
  title: 'All About Circuits: Practical considerations for inductors'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/practical-considerations-inductors/
  accessed: '2026-10-04'
  kind: book
  version: null
  applicability: Winding resistance, saturation, stray capacitance and self-resonance limitations.
---

## Short answer

Індуктивність запасає енергію магнітного поля й протидіє змінам струму. Для ідеальної індуктивності `v = L*di/dt`; sinusoidal reactance дорівнює `X_L = 2π*f*L` і зростає з частотою в межах придатності моделі. Реальна обмотка також має опір та parasitic ефекти. [^aac-inductor]

## Detailed explanation

Зміна струму створює напругу на індуктивності. За прикладеної напруги струм змінюється зі швидкістю, визначеною inductance; компонент загалом не блокує весь струм. За ідеального усталеного DC струм сталий, тому inductive voltage дорівнює нулю. Реальна обмотка все одно дає resistive voltage drop. [^aac-inductor] [^aac-inductor-calculus]

У розрахунковому sinusoidal прикладі 10 mH при 1 kHz мають `X_L = 2π*1000*0.01 ≈ 62.8 Ω`. Це reactance, а не опір розсіювання; при поєднанні з іншими імпедансами потрібно враховувати phase. Запасена магнітна енергія в ідеальній лінійній моделі – `E = L*I²/2`.

Індуктивності корисні у filters і switching converters, оскільки утримують енергію під час зміни струму. Розрив шляху зі струмом індуктивності може створити велику напругу, тому важливий відповідний discharge або clamp path. Не поширюйте просте правило зростання reactance за межі self-resonant region компонента: parasitic capacitance, winding loss і core saturation можуть зробити ідеальну модель непридатною. [^aac-inductor-practical] [^aac-inductor-calculus]

## Sources

<!-- generated from frontmatter -->
