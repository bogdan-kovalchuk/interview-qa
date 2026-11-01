---
id: emb-elintro-0051
title: "What happens if an ammeter is connected directly across a power source?"
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
  - source_id: aac-ammeter-usage
    title: "All About Circuits: Intro Lab – How to Use an Ammeter to Measure Current"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-2/ammeter-usage/
---

## Short answer

An ammeter has low internal resistance, so placing it directly across a power source creates a path with virtually zero resistance: current can surge dramatically, blowing the meter's fuse or damaging the power source.[^aac-ammeter-usage] It is connected in series with the load so that the current being measured flows through the instrument.[^aac-ammeter-usage]

## Detailed explanation

Connected directly between the terminals of a power source, an ammeter creates a short circuit. In current measurement mode, a multimeter typically inserts a very low internal shunt resistance into the circuit; this small voltage drop allows the instrument to determine current, but does not limit it the way an ordinary resistor would.[^aac-ammeter-usage]

The magnitude of the fault current is not identical across all power sources. It is limited by the internal resistance of the power source, the resistance of the wiring and contact points, and the ammeter itself. A bench power supply with current limiting can mitigate the consequences, whereas a battery with low internal resistance can deliver a substantial current. The multimeter fuse may blow, but its presence does not make such a connection safe: the power source or test leads can also overheat or suffer damage.[^aac-ammeter-usage]

To measure current in a branch, one breaks the circuit and connects the ammeter in series so that all branch current flows through the instrument. To measure source voltage, the multimeter is configured for voltage mode and connected in parallel; operating modes and probe jacks must be verified before measurement. A common mistake is leaving a probe in the current jack and touching both terminals of the power source: this shorts the circuit through the low-resistance path of the ammeter.[^aac-ammeter-usage]

Example: if a battery and a lamp are already connected in series, to measure current one disconnects a single lead between the battery and the lamp and inserts the ammeter into the break. The reading reflects the current flowing through the lamp; connecting the test probes directly across both battery terminals measures not the lamp's operating current, but a short-circuit current through the instrument.[^aac-ammeter-usage]
