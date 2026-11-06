---
id: emb-elee-0260
title: "Why can a motor on a shared supply rail cause a microcontroller to hang?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-motor-drive-protection
    title: "Texas Instruments Application Report SLVA636: Designing Motor Drive Circuits for High Reliability"
    url: https://www.ti.com/lit/an/slva636/slva636.pdf
  - source_id: st-mcu-noise-immunity
    title: "STMicroelectronics Application Note AN4683: Robust design for microcontroller applications"
    url: https://www.st.com/resource/en/application_note/an4683-robust-design-for-microcontroller-applications-stmicroelectronics.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

A motor is an inductive load: during rotation and commutation, it generates voltage spikes and back-EMF that kick back onto the power rail. In the course lecture, spikes on a 3.3 V rail reached 2–3 V peak-to-peak and even pulled the voltage below ground. Such transients trigger brownout resets or corrupt digital logic, which is easily mistaken for a firmware bug.[^udemy-electronics-course]

## Detailed explanation

TODO
