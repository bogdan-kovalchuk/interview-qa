---
id: emb-elintro-0004
title: Яка функція конденсатора?
description: Яка функція конденсатора?
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
- source_id: aac-capacitor
  title: 'All About Circuits: Capacitors and calculus'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/capacitors-and-calculus/
  accessed: 2026-10-04
  kind: book
  version: null
  applicability: Capacitor current depends on voltage change; ideal steady-state DC behavior.
- source_id: nichicon-polarity
  title: 'Nichicon: Technical notes for aluminum electrolytic capacitors'
  url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Polarized oxide dielectric, charge/energy relations and reverse-voltage damage, section 2-3-2.
---

## Short answer

Конденсатор запасає енергію електричного поля та утримує протилежні заряди на електродах. В ідеальній моделі `i = C*dv/dt`: струм протікає під час зміни напруги, але не за сталої DC напруги. Його використовують для filtering, decoupling і coupling змінних сигналів. [^aac-capacitor]

## Detailed explanation

Capacitance пов’язує заряд і напругу через `Q = C*V`; запасена енергія – `E = C*V²/2`. Заряд міститься на електродах, а енергія пов’язана з електричним полем у dielectric. За розрахунком конденсатор 100 nF при 5 V має заряд за модулем 0.5 µC на кожному електроді та запасає 1.25 µJ. [^nichicon-polarity]

«Блокує DC» описує ідеальний усталений стан після заряджання, а не момент підключення DC живлення. Під час заряджання напруга змінюється і протікає струм. Для ідеального конденсатора й sinusoidal signal модуль імпедансу зменшується з частотою; це допомагає coupling та filtering, але не робить будь-який конденсатор коротким замиканням на будь-якій AC частоті. [^aac-capacitor]

Supply decoupling capacitor біля IC локально забезпечує transient current і обмежує зміни напруги живлення. Реальні конденсатори мають leakage, ESR та parasitic inductance, тому важливі розміщення і характеристики компонента. Для polarized capacitor додатково потрібно дотримуватися polarity та voltage limits. [^nichicon-polarity]

## Sources

<!-- generated from frontmatter -->
