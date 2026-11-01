---
id: emb-elintro-0153
title: "Why should a square wave not be fed to a transformer carelessly?"
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
  - source_id: ti-magnetics-design-2
    title: "Texas Instruments: Magnetics Design 2 – Magnetic Core Characteristics"
    url: https://www.ti.com/lit/ml/slup124/slup124.pdf
---

## Short answer

A transformer can operate with rectangular pulses if its core, frequency, amplitude, duty cycle, and volt-seconds balance match the design. If volt-seconds per cycle are not balanced, magnetic flux walks toward saturation, causing magnetizing current and heating to rise. Therefore, a transformer for a sinusoidal 50/60 Hz mains cannot be connected to an arbitrary square wave without verification.[^ti-magnetics-design-2]

## Detailed explanation

A transformer can transmit rectangular pulses, but only when its magnetic core and control circuitry are designed for the appropriate voltage, frequency, pulse duration, and flux-reset regime. By Faraday's law, flux change depends on the time integral of voltage, that is, on the volt-seconds per turn. The flux must return to its operating level; if positive and negative volt-seconds do not balance, flux walking occurs and the core can saturate.[^ti-magnetics-design-2]

Upon saturation, magnetizing inductance drops sharply, so primary current can rise rapidly. This overheats the winding or stresses the converter switches. In symmetrical push-pull or bridge circuits, even a small difference in pulse durations or switch forward drops can create cumulative imbalance; this is why duty cycle limits and proper core reset are necessary.[^ti-magnetics-design-2]

Frequency is also critical. For the same voltage, a longer pulse produces a larger flux change, and a transformer designed for 50/60 Hz mains generally cannot be powered without calculation by a signal of different waveform or frequency. At the same time, a rectangular waveform is not prohibited in itself: SMPS designs use transformers with pulse excitation, limiting volt-seconds and providing a flux-reset path.[^ti-magnetics-design-2]

Example: in a push-pull converter, positive and negative pulses must produce approximately equal volt-second magnitudes. If one pulse is longer, residual flux grows cycle by cycle and can drive the core into saturation.[^ti-magnetics-design-2]

**Common mistakes:**
- assuming that a transformer cannot operate with a rectangular waveform;
- checking only amplitude while ignoring frequency and pulse duration;
- forgetting about volt-seconds balance and core demagnetization.
