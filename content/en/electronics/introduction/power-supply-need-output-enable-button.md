---
id: emb-elintro-0264
title: "Why does a power supply need an `Output Enable` button?"
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
  - source_id: keysight-e364xa-user-guide
    title: "Keysight: E364xA Dual Output DC Power Supplies User's Guide"
    url: https://www.keysight.com/us/en/assets/9018-01166/user-manuals/9018-01166.pdf
---

## Short answer

The `Output Enable` button turns off the power terminals while keeping the instrument powered on. This allows the user to safely configure voltage and current limits and wire the load before energizing the circuit, preventing accidental exposure to unverified settings, though it does not eliminate all output transients on its own.[^keysight-e364xa-user-guide]

## Detailed explanation

The `Output Enable` button controls the delivery of power to the output terminals independently of powering the instrument's own control circuitry. When the output is disabled, the operator can configure supply parameters or adjust wiring without applying live power to the device under test. The Keysight E364xA user guide describes configuring current limits and output voltage while `OUTPUT OFF` is displayed, followed by enabling the output as a distinct action.[^keysight-e364xa-user-guide]

This is far more convenient and controlled than power-cycling the entire instrument: configuration settings and display readings remain active, and energizing the output becomes a deliberate step. For example, before powering a prototype board, one can configure its nominal supply voltage, set the current limit, verify lead polarity, and only then enable the output. This workflow reduces the risk of accidentally applying incorrect voltage during bench setup, though it does not eliminate setup mistakes, reverse wiring, or transient overshoot; turn-on transient behavior depends on the power supply design and load impedance.[^keysight-e364xa-user-guide]

Do not assume that `Output Enable` automatically makes any wiring setup completely safe. Before enabling the output, always recheck voltage, polarity, current limits, load power ratings, and sensitive component connections. On some instruments, this button is labeled `Output On/Off`, and its disabled-state behavior varies: the output may open an internal relay, electronically regulate to zero, or retain settings for subsequent reactivation.[^keysight-e364xa-user-guide]

Example operational sequence: disable the output, connect the leads to the board, program the target parameters, verify them on the display, and press enable. If the supply enters CC mode instead of the expected CV immediately after enabling, this is a clear indication to inspect the current limit and troubleshoot the load for faults rather than blindly raising the current limit.[^keysight-e364xa-user-guide]
