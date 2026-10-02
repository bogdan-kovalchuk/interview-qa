---
id: emb-elintro-0099
title: "Чому реактивне навантаження може збільшувати струм у мережі без корисної роботи?"
description: "Чому реактивне навантаження може збільшувати струм у мережі без корисної роботи?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-ac-power
    title: "True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Реактивний обмін енергією, фазовий зсув, RMS-струм і втрати у резистивних елементах кола."
---

## Short answer

Ідеальні котушка й конденсатор періодично запасають енергію поля та повертають її джерелу, тож їхня середня активна потужність за період дорівнює нулю, хоча RMS-струм не обов’язково нульовий. Цей струм усе одно спричиняє втрати `I_rms^2*R` у проводах та внутрішньому опорі джерела; реальні реактивні компоненти теж мають втрати.[^aac-ac-power]

## Detailed explanation

У реактивному колі струм і напруга зсунуті за фазою. В ідеальній котушці енергія переходить у магнітне поле, а в ідеальному конденсаторі – в електричне; протягом іншої частини циклу поле повертає енергію джерелу. За цілий період чистий перенос енергії в ідеальний реактивний елемент дорівнює нулю, але миттєвий струм і обмін енергією тривають.[^aac-ac-power]

Мережу й генератор навантажує не лише активна потужність, а й RMS-струм. Реактивний струм збільшує повну потужність у `VA`; через опір кабелів і внутрішній опір джерела цей струм розсіює тепло за законом `P_loss = I_rms^2*R`. Тому фраза «без корисної роботи» стосується ідеальної реактивної частини навантаження, а не всього реального кола: провідники гріються, а котушки мають опір обмотки й інші втрати.[^aac-ac-power]

Для синусоїдального однофазного кола `P = V_rms*I_rms*cos(φ)`. Якщо при незмінних напрузі й активній потужності коефіцієнт потужності падає, джерелу потрібен більший RMS-струм. Наприклад, для `120 W` при `120 V` та `cos(φ) = 0.5` потрібно `I_rms = 2 A`; за коефіцієнта `1` для тієї самої активної потужності потрібно `1 A`. Цей приклад передбачає синусоїдальний режим і сталу напругу.[^aac-ac-power]

**Типова помилка:** стверджувати, що реактивне навантаження споживає струм, але «нічого не робить», отже провідники не гріються. Воно може не споживати середньої активної потужності в ідеальній моделі, однак струм створює втрати в усіх ненульових опорах реальної мережі.

## Sources

<!-- generated from frontmatter -->
