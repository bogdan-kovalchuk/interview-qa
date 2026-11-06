---
id: emb-elpcb-0005
title: "Why are the inner layers in a 4-layer PCB dedicated to ground and power planes?"
track: electronics
section: pcb-design
sources:
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose. Printed Circuit Board Design Techniques for EMC Compliance: A Handbook for Designers (2nd Edition)"
    url: https://www.wiley.com/en-us/Printed+Circuit+Board+Design+Techniques+for+EMC+Compliance%3A+A+Handbook+for+Designers%2C+2nd+Edition-p-9780780353763
  - source_id: bogatin-signal-integrity
    title: "Eric Bogatin. Signal and Power Integrity - Simplified (3rd Edition)"
    url: https://www.pearson.com/en-us/subject-catalog/p/signal-and-power-integrity-simplified/P200000003233
  - source_id: horowitz-hill
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics (3rd Edition)"
    url: https://artofelectronics.net/
---

## Short answer

Signals are typically routed on outer layers, dropping vias into solid inner ground and power planes from anywhere on the board. A continuous ground plane minimizes loop area for high-frequency return currents, provides controlled transmission line impedance, and shields against EMI. Closely spaced power and ground planes also form an intrinsic low-inductance distributed decoupling capacitance.[^montrose-emc-pcb]

## Detailed explanation

TODO
