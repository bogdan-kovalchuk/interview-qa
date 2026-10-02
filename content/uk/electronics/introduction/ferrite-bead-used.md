---
id: emb-elintro-0012
title: Що таке ferrite bead і де він застосовується?
description: Що таке ferrite bead і де він застосовується?
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
- source_id: adi-bead
  title: 'Analog Devices AN-1368: Ferrite bead demystified'
  url: https://www.analog.com/en/resources/app-notes/an-1368.html
  accessed: 2026-10-04
  kind: official
  version: AN-1368
  applicability: Impedance regions, heat dissipation, bias dependence and LC resonance.
---

## Short answer

Ferrite bead додає frequency-dependent impedance для ослаблення небажаного high-frequency current чи noise. Зазвичай він має низький DC resistance та resistive high-frequency region, де енергія шуму розсіюється як тепло, але поведінка залежить від frequency, bias current і навколишнього кола. [^adi-bead]

## Detailed explanation

Bead не є просто ідеальною індуктивністю. Його імпеданс має resistive та reactive компоненти: на нижчих частотах він може поводитися inductively, у корисній suppression band – dissipatively, а вище resonance – capacitively. Обирайте його за impedance-versus-frequency curves, а не за одним указаним імпедансом. [^adi-bead]

Наприклад, specification на 100 MHz не визначає імпеданс на 100 kHz. DC bias може суттєво зменшити effective inductance та filtering performance, тому перевіряйте operating current разом із thermal current rating. DC resistance також створює voltage drop і power loss під навантаженням. [^adi-bead]

Bead разом із shunt capacitor може утворити supply filter, але мережа здатна резонувати й підсилювати noise у частині spectrum. AN-1368 показує важливість damping і навколишніх source/load impedances. Тому bead – компонент спроєктованого filter, а не гарантований засіб усунення шуму незалежно від placement і loading. [^adi-bead]

## Sources

<!-- generated from frontmatter -->
