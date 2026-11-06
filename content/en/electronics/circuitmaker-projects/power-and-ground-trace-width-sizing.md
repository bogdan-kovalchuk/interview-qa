---
id: emb-elcmproj-0033
title: "Why are main power and ground traces routed significantly wider than signal traces?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ipc-2152
    title: "IPC-2152: Standard for Determining Additional Current-Carrying Capacity in Printed Board Design"
    url: https://www.ipc.org/
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose: Printed Circuit Board Design Techniques for EMC Compliance (2nd Edition), IEEE Press / Wiley"
    url: https://www.wiley.com/en-us/Printed+Circuit+Board+Design+Techniques+for+EMC+Compliance%3A+A+Handbook+for+Designers%2C+2nd+Edition-p-9780780353763
---

## Short answer

Main power and ground buses carry the aggregated return and supply currents of all circuit loads. Increasing trace width lowers ohmic DC resistance and parasitic loop inductance. This minimizes static voltage drops across power rails and shields logic ICs from switching transients.[^udemy-electronics-course]

## Detailed explanation

TODO
