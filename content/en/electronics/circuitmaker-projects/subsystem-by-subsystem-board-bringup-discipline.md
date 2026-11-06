---
id: emb-elcmproj-0072
title: "Why is a freshly fabricated prototype board assembled and powered up subsystem by subsystem?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: horowitz-hill-art-electronics
    title: "Horowitz, P., & Hill, W. (2015). The Art of Electronics (3rd ed.). Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ipc-7711-7721
    title: "IPC-7711/7721: Rework, Modification and Repair of Electronic Assemblies"
    url: https://www.ipc.org/
---

## Short answer

Assembly begins strictly with the power supply section to verify regulated rail voltages before exposing sensitive ICs to potential overvoltage damage. Next, the microcontroller and clock circuitry are populated, followed by peripheral components only after clocking and firmware communications are confirmed. Staged bring-up isolates solder bridges and assembly faults without risking widespread circuit burnout.[^udemy-electronics-course]

## Detailed explanation

TODO
