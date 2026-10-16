---
id: emb-elintro-0012
title: Що таке ferrite bead і де він застосовується?
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
  - source_id: adi-bead
    title: "Analog Devices AN-1368: Ferrite bead demystified"
    url: https://www.analog.com/en/resources/app-notes/an-1368.html
---

## Short answer

Ferrite bead додає frequency-dependent impedance для ослаблення небажаного high-frequency current чи noise. Зазвичай він має низький DC resistance та resistive high-frequency region, де енергія шуму розсіюється як тепло, але поведінка залежить від frequency, bias current і навколишнього кола. [^adi-bead]

## Detailed explanation

Bead не є просто ідеальною індуктивністю. Його імпеданс має resistive та reactive компоненти: на нижчих частотах він може поводитися inductively, у корисній suppression band – dissipatively, а вище resonance – capacitively. Обирайте його за impedance-versus-frequency curves, а не за одним указаним імпедансом. [^adi-bead]

Наприклад, specification на 100 MHz не визначає імпеданс на 100 kHz. DC bias може суттєво зменшити effective inductance та filtering performance, тому перевіряйте operating current разом із thermal current rating. DC resistance також створює voltage drop і power loss під навантаженням. [^adi-bead]

Bead разом із shunt capacitor може утворити supply filter, але мережа здатна резонувати й підсилювати noise у частині spectrum. AN-1368 показує важливість damping і навколишніх source/load impedances. Тому bead – компонент спроєктованого filter, а не гарантований засіб усунення шуму незалежно від placement і loading. [^adi-bead]
