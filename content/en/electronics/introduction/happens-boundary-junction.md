---
id: emb-elintro-0032
title: "What happens at the boundary of a P-N junction?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-pn-junction
    title: "All About Circuits: The P-N Junction"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-2/the-p-n-junction/
---

## Short answer

Carriers diffuse across the boundary between P- and N-regions and recombine, forming a depletion region and a potential barrier. Its magnitude depends on the material; for a silicon diode, a ballpark figure of around 0.6–0.7 V is often cited rather than a universal value.[^aac-pn-junction]

## Detailed explanation

At the boundary of P- and N-doped regions, electrons and holes diffuse across the junction and recombine, leaving a region depleted of mobile charge carriers.[^aac-semiconductors]

In the N-region, fixed positive donor ions remain after electrons depart, while in the P-region near the junction, negative acceptor ions remain. This charge separation creates an internal electric field that opposes further diffusion of majority carriers. In this way, a depletion region and a potential barrier are formed.[^aac-semiconductors]

In equilibrium, the diffusion of majority carriers is balanced by drift transport in the internal electric field, so the junction cannot be described as an area where carriers simply come to a halt. Forward bias lowers the barrier and narrows the depletion region, allowing significant current to flow across the junction. Reverse bias widens the region; a real diode still exhibits a small leakage current, and a sufficiently high reverse voltage leads to breakdown.[^aac-pn-junction]

Example: for a conventional silicon rectifier diode, the value `0.7 V` can be a convenient approximation in simple calculations, but the exact forward drop must be taken from the characteristic curve or datasheet at a given current and temperature. If a diode is connected in series with a resistor to a power supply, it is the resistor that limits the current once the junction turns on; the forward voltage approximation alone does not determine a safe current.[^aac-pn-junction]
