---
id: emb-hwbasic-0004
title: "How do you assess signal integrity on a long line or fast digital interface in an embedded device?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: bogatin-signal-integrity
    title: "Eric Bogatin: Signal and Power Integrity - Simplified"
    url: https://www.pearson.com/en-us/subject-catalog/p/signal-and-power-integrity---simplified/P200000003257
---

## Short answer

Assess line length relative to rise time: if propagation delay is significant, treat the line as a transmission line. Check impedance, termination, return path, ground reference, crosstalk, ringing and overshoot with an oscilloscope using proper probing. For long or noisy lines, a differential interface like RS-485/CAN/Ethernet, lower speed or galvanic isolation is often better.[^dou-embedded-interview]

## Detailed explanation

TODO
