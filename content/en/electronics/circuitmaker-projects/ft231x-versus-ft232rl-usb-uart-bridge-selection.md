---
id: emb-elcmproj-0058
title: "Why is the FT231X USB-UART bridge a superior engineering choice over the legacy FT232RL?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ftdi-ft231x-datasheet
    title: "FTDI Chip: FT231X USB to Full Handshake UART IC Datasheet"
    url: https://ftdichip.com/wp-content/uploads/2020/08/DS_FT231X.pdf
  - source_id: ftdi-ft232r-datasheet
    title: "FTDI Chip: FT232R USB UART IC Datasheet"
    url: https://ftdichip.com/wp-content/uploads/2020/07/DS_FT232R.pdf
---

## Short answer

The FT231X bridge comes in modern SSOP-20 and QFN packages at significantly lower cost than the legacy FT232RL. It features lower power consumption, full USB 2.0 Full Speed compliance, and a dedicated `VCCIO` pin. This enables seamless logic-level shifting to 3.3 V or 5 V without requiring external level translators.[^udemy-electronics-course][^ftdi-ft231x-datasheet]

## Detailed explanation

TODO
