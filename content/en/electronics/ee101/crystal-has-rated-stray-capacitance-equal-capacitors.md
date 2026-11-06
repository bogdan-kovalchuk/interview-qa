---
id: emb-elee-0250
title: "A crystal has a rated C_L = 18 pF and stray capacitance ≈ 3 pF. Which equal capacitors C_1=C_2 are needed?"
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
  - source_id: st-an2867-oscillator-design
    title: "STMicroelectronics Application Note AN2867: Oscillator design guide for STM32 microcontrollers"
    url: https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm32-microcontrollers-stmicroelectronics.pdf
  - source_id: microchip-an826-crystal-basics
    title: "Microchip Application Note AN826: Crystal Oscillator Basics and Crystal Selection for rfPIC and PICmicro Devices"
    url: https://ww1.microchip.com/downloads/en/appnotes/00826a.pdf
  - source_id: art-of-electronics
    title: "Horowitz P., Hill W. The Art of Electronics. 3rd ed. Cambridge University Press, 2015"
    url: https://artofelectronics.net/
---

## Short answer

The effective load capacitance is `C_L ≈ (C_1 * C_2) / (C_1 + C_2) + C_stray = C / 2 + 3 pF`, yielding `C ≈ 30 pF`. This provides an initial design estimate; actual PCB stray capacitance and crystal manufacturer recommendations determine the final component value.[^udemy-electronics-course]

## Detailed explanation

TODO
